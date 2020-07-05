import bs4
from googlesearch import search

user_zip_code = input("Please enter your five digit zip code: ")
while user_zip_code:
    if len(user_zip_code) == 5: 
        pass
    elif user_zip_code.isnumeric():
        pass
    else:
        print("Sorry, that input is not valid. Please try again.")

query = "COVID-19 testing locations near " + str(user_zip_code)

def zip_code_search():
    for result in search(query, tld= 'com', lang = 'en', num = 5, start = 0, stop = 5, pause = 3.0):
        print(result)

print(zip_code_search())
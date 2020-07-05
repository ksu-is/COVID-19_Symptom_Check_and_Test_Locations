import webbrowser

zip_code = input("Please enter your five digit zip code: ")
def zip_code_tester(zip_code):
    if len(zip_code) != 5:
        print("Incorrect response. Please try again.")
        zip_code = input("Please enter your five digit zip code: ")
    elif zip_code.isalpha == True:
        print("Incorrect response. Please try again.")
        zip_code = input("Please enter your five digit zip code: ")
    else:
        return zip_code

zip_code_tester(zip_code)

query = "COVID-19 testing locations near " + str(zip_code)

webbrowser.open("https://google.com/?#q=" + query)
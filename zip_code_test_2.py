import webbrowser
user_zip_code = []
print("We will now ask you for your five digit zip code. We will use this zip code to provide you with testing locations near you.")
def zip_code_tester():
    while True: 
        zip_code = input("Please enter your five digit zip code: ")
        if len(zip_code) != 5:
            print("Incorrect response. Please try again.")
            zip_code = input("Please enter your five digit zip code: ")
        elif zip_code.isalpha == True:
            print("Incorrect response. Please try again.")
            zip_code = input("Please enter your five digit zip code: ")
        else:
            user_zip_code.append(zip_code)
            return user_zip_code

zip_code_tester()

user_zip = " ".join(user_zip_code)

query = "COVID-19 testing locations near " + str(user_zip)

webbrowser.open("https://google.com/?#q=" + query)

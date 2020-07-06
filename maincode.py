#Introductory greeting #
print("Welcome to our COVID-19 Symptom Checker! We will ask you a series of questions regarding whether you are exhibiting any of the CDC's currently recognized list of COVID-19 Symptoms.")
print("If you unfortunately are exhibiting symptoms of COVID-19, we will then provide you with resources to get tested locally.")
# End Introduction #

# Symptoms Explaination #
cdc_symptoms = ["Fever and/or chills, Coughing, Breathing difficulties, Fatigue, Muscle and/or body aches, Headache, Loss of taste and/or smell, Sore throat, Congestion, Runny nose, Nausea and/or vomitting, Diarrhea"]
covid_symptoms = ", ".join(cdc_symptoms)
print("Based on current CDC data, the currently recognized symptoms of COVID-19 are:", covid_symptoms)
# End Explaination #

# Establish repository for user responses #
user_responses = []
user_symptoms = []
# End establishment #

# Symptoms Examination #
print("We are about to ask you a series of medical questions. Please type '1' for 'Yes' or  '0' for 'No' for your responses.")
## Begin symptom1. We will be using the same type of 'while True' functions to quiz users for each of the symptoms. This first one below will be used as a template for the reamining symptoms ##
symptom1 = input("Within the last two weeks have you experienced a fever or bodily chills in any capacity? ")
while True:
    if symptom1 == "1":
        user_responses += ("1")
        user_symptoms.append("Fever and/or chills")
        break
    elif symptom1 == "0":
        break
    else:
        if symptom1 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom1 = input("Within the last two weeks have you experienced a fever or bodily chills in any capacity? ")
 ## End symptom1 ##

## Begin symptom2. Notice how there is a secondary if function to determine if the user is experiencing a dry cough or just normal coughing bouts. ##
## Because of the severity of this secondary symptom, we will end up appending it as two symptoms if a user has a dry cough ##
symptom2 = input("Within the last two weeks have you had any issues with coughing, especially dry coughing? ")
while True:
    if symptom2 == "1":
        user_responses += ("1")
        user_symptoms.append("Coughing")
        drycough = input("Have you experienced a dry cough? ")
        if drycough == "1":
            user_responses += ("1")
            user_symptoms.append("Dry Cough")
            break
        else:
            break
    elif symptom2 == "0":
        break
    else:
        if symptom1 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom1 = input("Within the last two weeks have you experienced a fever or bodily chills in any capacity? ")
## End symptom2 ##
#Introductory greeting #
print("Welcome to our COVID-19 Symptom Checker! We will ask you a series of questions regarding whether you are exhibiting any of the CDC's currently recognized list of COVID-19 Symptoms.")
print("If you unfortunately are exhibiting symptoms of COVID-19, we will then provide you with resources to get tested locally.")
# End introductory greeting #

# Symptoms Explaination #
cdc_symptoms = ["Fever and/or chills, Coughing, Breathing difficulties, Fatigue, Muscle and/or body aches, Headache, Loss of taste and/or smell, Sore throat, Congestion, Runny nose, Nausea and/or vomitting, Diarrhea"]
covid_symptoms = ", ".join(cdc_symptoms)
print("Based on current CDC data, the currently recognized symptoms of COVID-19 are:", covid_symptoms)
# End symtoms explaination #

# Establish repository for user responses #
user_responses = []
user_symptoms = []
# End establishment #

# Symptoms Examination #
print("We are about to ask you a series of medical questions. Please type '1' for 'Yes' or  '0' for 'No' for your responses.")
## Begin symptom1 ##
### We will be using the same type of 'while True' functions to quiz users for each of the symptoms. This first one below will be used as a template for the reamining symptoms ###
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

## Begin symptom2 ##
### Notice how there is a secondary if function to determine if the user is experiencing a dry cough or just normal coughing bouts. ###
### Because of the severity of this secondary symptom, we will end up appending it as two symptoms if a user has a dry cough ###
symptom2 = input("Within the last two weeks have you had any issues with coughing, especially dry coughing? ")
while True:
    if symptom2 == "1":
        user_responses += ("1")
        user_symptoms.append("Coughing")
        dry_cough = input("Have you experienced a dry cough within the last two weeks? ")
        if dry_cough == "1":
            user_responses += ("1")
            user_symptoms.append("Dry cough")
            break
        elif dry_cough == "0":
            break
        else:
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            dry_cough = input("Have you experienced a dry cough within the last two weeks? ")
    elif symptom2 == "0":
        break
    else:
        if symptom2 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom2 = input("Within the last two weeks have you experienced a fever or bodily chills in any capacity? ")
## End symptom2 ##

## Begin symptom3 ##
symptom3 = input("Within the last two weeks have you had any issues with your breathing, such as lightheadedness or shallowness of breath? ")
while True:
    if symptom3 == "1":
        user_responses += ("1")
        user_symptoms.append("Breathing Difficulties")
        break
    elif symptom3 == "0":
        break
    else:
        if symptom3 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom3 = input("Within the last two weeks have you had any issues with your breathing, such as lightheadedness or shallowness of breath? ")
## End symptom3 ##

## Begin symptom4 ##
symptom4 = input("Within the last two weeks have you experienced any noticeable fatigue? ")
while True:
    if symptom4 == "1":
        user_responses += ("1")
        user_symptoms.append("Fatigue")
        break
    elif symptom4 == "0":
        break
    else:
        if symptom4 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom4 = input("Within the last two weeks have you experienced any noticeable fatigue? ")
## End symptom4 ##

## Begin symptom5 ##
symptom5 = input("Within the last two weeks have you experienced any noticeable bodily and/or muscle aches? ")
while True:
    if symptom5 == "1":
        user_responses += ("1")
        user_symptoms.append("Fatigue")
        break
    elif symptom5 == "0":
        break
    else:
        if symptom5 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom5 = input("Within the last two weeks have you experienced any noticeable fatigue? ")
## End symptom5 ##

## Begin symptom6 ##
symptom6 = input("Within the last two weeks have you experienced any irregular headaches and/or migraines? ")
while True:
    if symptom6 == "1":
        user_responses += ("1")
        user_symptoms.append("Headaches")
        break
    elif symptom6 == "0":
        break
    else:
        if symptom6 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom6 = input("Within the last two weeks have you experienced any irregular headaches and/or migraines? ")
## End symptom6 ##

## Begin symptom7 ##
symptom7 = input("Within the last two weeks have you experienced any diminishment of your sense of taste and/or smell? ")
while True:
    if symptom7 == "1":
        user_responses += ("1")
        user_symptoms.append("Loss of taste and/or smell")
        break
    elif symptom7 == "0":
        break
    else:
        if symptom7 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom7 = input("Within the last two weeks have you experienced any diminishment of your sense of taste and/or smell? ")
## End symptom7 ##

## Begin symptom8 ##
symptom8 = input("Within the last two weeks have you experienced any noticeable throat soreness? ")
while True:
    if symptom8 == "1":
        user_responses += ("1")
        user_symptoms.append("Sore throat")
        break
    elif symptom8 == "0":
        break
    else:
        if symptom8 != "1" or "0":
            print("Incorrect response. Please try again and enter '1' for 'Yes' or '0' for 'No'.")
            symptom8 = input("Within the last two weeks have you experienced any noticeable throat soreness? ")
## End symptom8 ##






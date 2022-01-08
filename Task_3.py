import random
import sys
Operator_Name = random.choice(["Janice", "Fiona", "Siri", "Cortona", "Arthur", "Jane", "John", "Gwen", "Peter", "Sam"])

def validate_email(email_id): # Function to validate the email id
    if (email_id.count("@") == 1) and (len(email_id[:email_id.index("@")]) >= 2) and (email_id[email_id.index("@")+1:] == "pop.ac.uk"):
        return True

def extract_name(email_id): # Function to extract the name from the email id
    return email_id[:email_id.index("@")].capitalize()

def check_network_error():
    if random.choice([i for i in range(10)]) == 1:
        print("*** NETWORK ERROR ***")
        raise AssertionError

def exiting(name):
    sys.exit(f"Thanks, {name}, for using PopChat. See you again soon!")

def answering(answer):
    if "library" in answer.lower():
        print("The library is closed today.")

    elif "wifi" in answer.lower():
        print("WiFi is excellent across the campus.")

    elif "deadline" in answer.lower():
        print("Your deadline has been extended by two working days")

    elif "coffee" in answer.lower():
        print("Teekee is open until 9 PM this morning.")

    elif "fee" in answer.lower():
        print("I have sent your invoice to your email. Feel free to ask.") 

    elif "class" in answer.lower():
        print("Your Class starts at sharp 10 AM.")

    elif any(char in answer.lower() for char in ["bye", "exit", "goodbye", "help"]):
        raise AssertionError

    else :
        print(random.choice(["Hmm.", "Oh, yes, I see.", "Tell me more", "Mmmm.", "Yes", "You should try woking on this system.", "That is interesting"]))





print("Welcome to our Pop Chat \nOne of our operators will be pleased to help you today.\n")

email_id = input("Please enter your Poppleton email address: ")
validate_email(email_id)

if validate_email(email_id) != True:
    sys.exit(f"{email_id} is invalid at pop.ac.uk. \nPlease Try Again! \nExiting........")

name = extract_name(email_id)
print(f"Hi, {name}! Thank you, and Welcome to PopChat! \nMy name is {Operator_Name}, and it will be my pleasure to help you.")

while True:
    try:
        check_network_error()

        answer = input("---> ")
        answering(answer)

    except AssertionError as e:
        exiting(name)
        
print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.")

# First Question :
answer_1 = input("What is your name? ")

# Checking if it is the King or not
if answer_1.capitalize() == "Arthur":
    print("My liege! You may pass!")
else :
    # Asking Second Question:
    answer_2 = input("What is your quest? ")

    #Checking the second answer(if the grail word is or not in the string)
    if "grail" in answer_2.lower():
        
        # Asking the third question
        answer_3 = input("What is your favourite colour? ")

        # Checking the third answer( if the first letter of the name and color are same)
        if answer_3[0].upper() == answer_1[0].upper():
            print("You may pass!")

        else:
            print("Incorrect! You must now face the Gorge of the Eternal Peril.")

    else :
        print("Only those who seek the Grail may pass.")

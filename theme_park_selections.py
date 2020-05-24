"""Purpose: Create a program that allows users to see if they are within age
requirements for rides provided.
Date: 5/24/2020     Authour: Jaron Pirtle"""

#information is provided to user
print("""Hello and please select a ride you want info on

1. Scenic River Crusie
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator (a super scary roller coaster)""")

#sets condition to True for loop to work
select_int = 1

while select_int:

    #Allows user to input selection
    selection = input("\nPlease enter your selection: ")
    select_int = int(selection)

    #if-statements created to act on selection from user. breaks are added to kill loop
    if select_int == 1:
        print("You have chosen Scenic River Crusie. There is no age limit")
        break

    elif select_int == 2:
        age = input("Please enter your age: ")
        age_int = int(age)
        if age_int >= 3:
            print("You meet the requirements to ride Scenic River Crusie.")
            break
        else:
            print("You do not meet the requirements to ride Scenic River Crusie.")
            break
            
    elif select_int == 3:
        age = input("Please enter your age: ")
        age_int = int(age)
        if age_int >= 6:
            print("You meet the requirements to ride Carnival Carousel.")
            break
        else:
            print("You do not meet the requirements to ride Carnival Carousel.")
            break
            
    elif select_int == 4:
        age = input("Please enter your age: ")
        age_int = int(age)
        if age_int >= 12:
            print("You meet the requirements to ride Scenic River Crusie.")
            break
        else:
            print("You do not meet the requirements to ride Scenic River Crusie.")
            break
            
    elif select_int == 5:
        age = input("Please enter your age: ")
        age_int = int(age)
        if age_int >= 12 and age_int <= 69:
            print("You meet the requirements to ride Scenic River Crusie.")
            break
        else:
            print("You do not meet the requirements to ride Scenic River Crusie.")
            break

    #else if statement to loop back selections if other numbers are choosen
    elif select_int < 1 or select_int > 5:
        print("Please choose from selections provided")
        


  

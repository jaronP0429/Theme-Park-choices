"""Purpose: Create a math quiz that a user is able to test thier knowledege on the times table of the number they input
Quiz will tell you if your answer is correct or incorrect. Also, user will be able to enter the range of where they want
to start and stop.
Date:5/28/2020  Author: Jaron Pirtle"""




#Creating function that runs quiz when called.
def mathquiz(time_value, a, b): 

    #for loop created to run quiz how many times user request based on range inputs.
    for count in range(a, b):
        
    #Quiz question
        print(f"What is",{time_value},"*",{count},": ")

    #User inputs answer here 
        quest = input("Answer: ")

    #answer is converted from string to interger
        quest_int = int(quest)

    #Calculation for answer
        result = count * time_value

    #user answer is compared to correct answer wit stipulations if correct or wrong
        if quest_int == result:
            print("Correct")
            
        else:
            print("Incorrect the correct answer is: ",result)
            
    print("Done")

#User is asked to input what number they want to test their knowledge on as far
#as thier understanding of that numbers times table.
your_value = input("What number do you wish to test your knowledge on:  ")
yourv = int(your_value)

#range user wants to start from.
#For example if user enter 5 count wil start at 5 and count up to
#But not including where user where user wants to stop.
range_start = input("Enter your start value: ")
rs_int = int(range_start)

range_end = input("Up to what number do you wish to go up to, but not including: ")
re_int = int(range_end)

#function is called
mathquiz(yourv, rs_int, re_int)    
    

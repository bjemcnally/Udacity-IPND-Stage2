# IPND Stage 2 Final Project

# for Level 1:
sample = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."
correct_answers1 = ["function","parameters","None","list"]

# for Level 2:
# I had a lot of trouble with the creative part of this project and felt just making more vocab tests was boring (haha)

level2 = "The Eiffel Tower is in ___1___, France. The difference between ___2___ (like humans and gorillas) and monkeys is that ___2___, don't have tails. The mitochondria is the powerhouse of the ___3___. Reggae, Bob Marley, and a killer bobsled team, originated in the country of ___4___. Steph Curry is a famous ___5___ player on the Golden State Warriors. The Rock refers to both the prison on the ___6___ of Alcatraz and top shelf Nicolas Cage film." 
correct_answers2 = ["Paris","apes","cell","Jamaica","basketball","island"]

# for Level 3:
level3 = "In the first Stage of the IPND, we made a webpage using ___1___ and CSS."
correct_answers3 = ["HTML"]

# for all levels:
correct_answers = [] # this is used in the get_answers function
to_be_replaced = ["___1___","___2___","___3___","___4___","___5___","___6___"]

# introduction
user_name = raw_input("Hello! What is your name? ")
print "\nWelcome " + user_name + ", I hope you enjoy my Stage 2 project for Udacity's IPND"
level = raw_input("Would you like to play Level 1, 2, or 3? ")

def get_answers(level):
# pairs answers with chosen level
    correct = []
    if level == 1:
        correct = correct_answers1
    if level == 2:
        correct = correct_answers2
    if level == 3:
        correct = correct_answers3
    return correct

def ask_and_check(blank_number, level): # blank_number = 1, 2, 3, 4
# asks user for answer and checks if it is correct, user is allowed five attempts
    attempt = 0
    correct_answers = get_answers(level)
    index = (blank_number - 1) # corrects for index vs number in list
    while attempt < 5:
        answer = raw_input("\nWhat goes in place of " + to_be_replaced[index] + "? ")
        if answer == correct_answers[index]:
            print "\nGood job!\n"
            return answer
            break
        else:
            attempt += 1
        if attempt < 4:
            print "Nope, try again!"
        if attempt == 4:
            print "Uh oh, only one more guess! \nHint: The first letter of the correct answer is " + correct_answers[index][0]
        if attempt == 5:
            print "Game over!"
            exit() # looked this up on stackoverflow via Google

def quiz(starting_string, number_of_blanks, level):
# replaces blanks, i.e. ___x___, with correct answers 
    print "In the following paragraph, fill in the blanks with appropriate keywords.\n"
    print starting_string
    blank = 1 # i.e. ___1___
    while blank <= number_of_blanks:
        replacement = ask_and_check(blank, level)
        blank_to_be_replaced = "___" + str(blank) + "___"
        starting_string = starting_string.replace(blank_to_be_replaced, replacement)
        print starting_string
        blank += 1
    if blank > number_of_blanks:
        print "\nCongratulations! You win!"

def level_selection(chosen_level):
    if chosen_level == "1":
        # start level 1
        print "\nGreat! You chose Level " + chosen_level + ". \nThis Level uses the sample paragraph provided by the course. \nLet's get started! \n***Please note that answers are case sensitive!***"
        quiz(sample, 4, 1)
    if chosen_level == "2":
        # start level 2
        print "\nGreat! You chose Level " + chosen_level + ". \nLet's get started! \n***Please note that answers are case sensitive!***"
        quiz(level2, 6, 2)
    if chosen_level == "3":
        # start level 3
        print "\nGreat! You chose Level " + chosen_level + ". \nLet's get started! \n***Please note that answers are case sensitive!***"
        quiz(level3, 1, 3)
    elif chosen_level != "1" and chosen_level != "2" and chosen_level != "3":
        print "\nWhoops! You'll need to start over. Please type in a number from 1 - 3."

level_selection(level)
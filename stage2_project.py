# IPND Stage 2 Final Project by bjemcnally

# These are the fill in the blank paragraphs and answers for each level:

# Level 1: provided by Udacity
sample = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."
correct_answers1 = ["function","parameters","None","list"]

# Level 2: General knowledge
level2 = "The Eiffel Tower is in ___1___, France. The difference between ___2___ (like humans and gorillas) and monkeys is that ___2___, don't have tails. The mitochondria is the powerhouse of the ___3___. Reggae, Bob Marley, and a killer bobsled team, originated in the country of ___4___. Steph Curry is a famous ___5___ player on the Golden State Warriors. The Rock refers to both the prison on the ___6___ of Alcatraz and a top shelf Nicolas Cage film." 
correct_answers2 = ["Paris","apes","cell","Jamaica","basketball","island"]

# Level 3: Farm animals
level3 = "Old McDonald had a farm, E-I-E-I-O. On his farm he had a ___1___ that said 'MOO', a ___2___ that said 'NEIGH', a ___3___ that said 'CLUCK CLUCK', a ___4___ that said 'OINK', a ___5___ that said 'RIBBIT', and a ___6___ that said 'QUACK'. That's a lot of animals!"
correct_answers3 = ["cow","horse","chicken","pig","frog","duck"]

# for all levels:
correct_answers = [] # this is used in the get_answers function
to_be_replaced = ["___1___","___2___","___3___","___4___","___5___","___6___"]

# introduction
user_name = raw_input("Hello! What is your name? ")
print "\nWelcome " + user_name + ", I hope you enjoy my Stage 2 project for Udacity's IPND"
level = raw_input("\nChoose a level: \nLevel 1: IPND Stage 2 Vocab Quiz \nLevel 2: General Knowledge Quiz\nLevel 3: Farm Animals Quiz \nWould you like to play Level 1, 2, or 3? ")
difficulty = raw_input("\nChoose a difficulty: \nEasy = 5 guesses \nMedium = 3 guesses \nHard = 1 guess \nWould you like to play Easy, Medium, or Hard? ")

def difficulty_value(difficulty):
# translates user's chosen diffulty to numerical value (i.e. number of allowed attempts)
    attempts = 0
    if difficulty == "Easy":
        attempts = 5
    if difficulty == "Medium":
        attempts = 3
    if difficulty == "Hard":
        attempts = 1
    if difficulty != "Easy" and difficulty != "Medium" and difficulty != "Hard":
        print "\nWhoops! You'll need to start over. Please choose a difficulty from Easy, Medium, or Hard (case sensitive!)."
        exit()
    return attempts

def get_answers(level):
# pairs answers (output) with chosen level (input) in ask_and_check function
# may not be necessary, but was the first way I came up with to do this... suggestions welcome!
    correct = []
    if level == 1:
        correct = correct_answers1
    if level == 2:
        correct = correct_answers2
    if level == 3:
        correct = correct_answers3
    return correct

def ask_and_check(blank_number, level, allowed_attempts): # blank_number = 1, 2, 3, 4, etc
# asks user for answer and checks if it is correct, user is allowed five attempts
# blank_number refers to ___1___, ___2___, etc in each level's fill in the blank string (above)
# if answer is correct, outputs correct answer, otherwise prints prompts and/or hints 
# if you exclude function and variable definitions, I think this is less than 18 lines (?)
    attempt = 0
    correct_answers = get_answers(level)
    index = (blank_number - 1) # corrects for index vs number in list
    while attempt < allowed_attempts:
        answer = raw_input("\nWhat goes in place of " + to_be_replaced[index] + "? ")
        if answer == correct_answers[index]:
            print "\nGood job! Let's keep going.\n"
            return answer
            break
        else:
            attempt += 1
        if attempt == allowed_attempts:
            print "\nWrong. Game over!"
            exit() # looked this up on stackoverflow via Google
        if attempt < 3:
            print "Nope, try again!"
        if attempt == 3:
            print "Uh oh, this isn't going well. \nHere's a hint: The first letter of the correct answer is " + correct_answers[index][0]
        if attempt == 4:
            index_last_character = len(correct_answers[index]) - 1
            print "Oh no, only one more guess. \nHere's another hint: The last letter of the correct answer is " + correct_answers[index][index_last_character]
        
def quiz(starting_string, number_of_blanks, level, allowed_attempts):
# replaces blanks, i.e. ___x___, with correct answers 
# starting_string is each level's string, other variables are (hopefully) self explanatory
# output is start_string with correct replacements
    print "In the following paragraph, fill in the blanks with appropriate keywords.\n"
    print starting_string
    blank = 1 # i.e. ___1___
    while blank <= number_of_blanks:
        replacement = ask_and_check(blank, level, allowed_attempts)
        blank_to_be_replaced = "___" + str(blank) + "___"
        starting_string = starting_string.replace(blank_to_be_replaced, replacement)
        print starting_string
        blank += 1
    if blank > number_of_blanks:
        print "\nCongratulations! You win!"

def level_selection(chosen_level, chosen_difficulty):
# takes users chosen level from introduction
# prints level's prompt
# runs 'quiz' function with correct parameters
    allowed_attempts = difficulty_value(chosen_difficulty)
    if chosen_level == "1":
        # start level 1
        print "\nGreat! You chose Level " + chosen_level + " on " + chosen_difficulty + " \nThis Level uses the sample paragraph provided by the course. \nLet's get started! \n***Please note that answers are case sensitive!***"
        quiz(sample, 4, 1, allowed_attempts)
    if chosen_level == "2":
        # start level 2
        print "\nGreat! You chose Level " + chosen_level + " on " + chosen_difficulty + ". \nLet's get started! \n***Please note that answers are case sensitive!***"
        quiz(level2, 6, 2, allowed_attempts)
    if chosen_level == "3":
        # start level 3
        print "\nGreat! You chose Level " + chosen_level + " on " + chosen_difficulty + ". \nLet's get started! \n***Please note that answers are case sensitive!***"
        quiz(level3, 6, 3, allowed_attempts)
    if chosen_level != "1" and chosen_level != "2" and chosen_level != "3":
        print "\nWhoops! Looks like you chose an invalid Level and will need to start over."

level_selection(level, difficulty)
# IPND Stage 2 Final Project by bjemcnally version 1.1

# These are the fill in the blank paragraphs and answers for each level:

# Level 1: provided by Udacity
level1_string = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."
correct_answers1 = ["function","parameters","none","list"]
level1_number_of_blanks = 4

# Level 2: General knowledge
level2_string = "The Eiffel Tower is in ___1___, France. The difference between ___2___ (like humans and gorillas) and monkeys is that ___2___, don't have tails. The mitochondria is the powerhouse of the ___3___. Reggae, Bob Marley, and a killer bobsled team, originated in the country of ___4___. Steph Curry is a famous ___5___ player on the Golden State Warriors. The Rock refers to both the prison on the ___6___ of Alcatraz and a top shelf Nicolas Cage film." 
correct_answers2 = ["paris","apes","cell","jamaica","basketball","island"]
level2_number_of_blanks = 6

# Level 3: Farm animals
level3_string = "Old McDonald had a farm, E-I-E-I-O. On his farm he had a ___1___ that said 'MOO', a ___2___ that said 'NEIGH', a ___3___ that said 'CLUCK CLUCK', a ___4___ that said 'OINK', a ___5___ that said 'RIBBIT', and a ___6___ that said 'QUACK'. That's a lot of animals!"
correct_answers3 = ["cow","horse","chicken","pig","frog","duck"]
level3_number_of_blanks = 6

# for all levels:
correct_answers = [] # this is used in the get_answers function
level_options = ["1","2","3"] # used in check_for_valid_level and initiate_quiz functions
chosen_level = 0

# introduction
user_name = raw_input("Hello! What is your name? ")
print "\nWelcome " + user_name + ", I hope you enjoy my Stage 2 project for Udacity's IPND"
level = raw_input("\nChoose a level: \nLevel 1: IPND Stage 2 Vocab Quiz \nLevel 2: General Knowledge Quiz\nLevel 3: Farm Animals Quiz \nWould you like to play Level 1, 2, or 3? ")

def check_for_valid_level(chosen_level):
# input is raw_input level (line 28)
# if user chose invalid level, asks for valid level
# output allows for change in assignment of level variable (line 44)
    while chosen_level not in level_options:
        chosen_level = raw_input("\nWhoops! Looks like you chose an invalid Level. Please type in 1, 2, or 3: ")
    return chosen_level

if level not in level_options:
    level = check_for_valid_level(level)

difficulty = raw_input("\nChoose a difficulty: \nEasy = 5 guesses \nMedium = 3 guesses \nHard = 1 guess \nWould you like to play Easy, Medium, or Hard? ")

def difficulty_value(difficulty):
# input is raw_input difficulty (line 42)
# translates diffulty to numerical value (i.e. allowed attempts, see line 42)
# output is number of allowed attempts
    attempts = 0
    difficulty_options = ['easy','medium','hard']
    while difficulty.lower() not in difficulty_options:
        difficulty = raw_input("\nWhoops! Please type in Easy, Medium, or Hard: ")
    if difficulty.lower() == difficulty_options[0]:
        attempts = 5
    if difficulty.lower() == difficulty_options[1]:
        attempts = 3
    if difficulty.lower() == difficulty_options[2]:
        attempts = 1
    return attempts

def get_answers(level):
# input is raw_input difficulty (line 42)
# pairs answers (lines 7, 12, 17) with chosen level in ask_and_check function
# output is correctly paired right answers
    correct = []
    if level == 1:
        correct = correct_answers1
    if level == 2:
        correct = correct_answers2
    if level == 3:
        correct = correct_answers3
    return correct

def ask_and_check(blank_number, level, allowed_attempts): 
# input is blank_number (1 = ___1___, etc), chosen level, and allowed attempts (based upon difficulty selection)
# asks user for answer and checks if it is correct, user is allowed five attempts
# if answer is correct, outputs correct answer, otherwise prints prompts and/or hints 
    attempt = 0
    correct_answers = get_answers(level)
    index = (blank_number - 1) # corrects for index vs number in list
    while attempt < allowed_attempts:
        answer = raw_input("\nWhat goes in place of ___" + str(blank_number) + "___? ")
        if answer.lower() == correct_answers[index]:
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
# input is level-specific string (lines 6, 11, 16), user chosen level, and allowed attempts (based upon chosen difficulty)
# replaces blanks, e.x. ___1___, in starting_string with correct answers 
# output is start_string with correct replacements
# answer formatting is maintained from user input
    print "In the following paragraph, fill in the blanks with appropriate keywords:\n"
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

def initiate_quiz(chosen_level, chosen_difficulty):
# takes users chosen level and difficulty from introduction
# runs 'quiz' function with correct parameters
# no output
    allowed_attempts = difficulty_value(chosen_difficulty)
    print "\nGreat! Let's get started!"
    if chosen_level == level_options[0]:
        # start level 1
        quiz(level1_string, level1_number_of_blanks, int(chosen_level), allowed_attempts)
    if chosen_level == level_options[1]:
        # start level 2
        quiz(level2_string, level2_number_of_blanks, int(chosen_level), allowed_attempts)
    if chosen_level == level_options[2]:
        # start level 3
        quiz(level3_string, level3_number_of_blanks, int(chosen_level), allowed_attempts)
        
initiate_quiz(level, difficulty)
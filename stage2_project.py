# IPND Stage 2 Final Project

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

user_name = raw_input("Hello! What is your name? ")
print "Welcome " + user_name + ", I hope you enjoy my Stage 2 project for Udacity's IPND"
level = raw_input("Would you like to play Level 1, 2, or 3? ")

def level_selection(chosen_level):
    if chosen_level == "1":
        # start level 1
        print "Great! You chose Level " + chosen_level + ". Let's get started!"
    if chosen_level == "2":
        # start level 2
        print "Great! You chose Level " + chosen_level + ". Let's get started!"
    if chosen_level == "3":
        # start level 3
        print "Great! You chose Level " + chosen_level + ". Let's get started!"
    else if chosen_level != "1" or chosen_level != "2" or chosen_level != "3":
        print "Whoops! You'll need to start over. Please type in a number from 1 - 3."

level_selection(level)

to_be_replaced = ["___1___","___2___","___3___","___4___"]
correct_answers = ["function","parameters","None","list"]

def level1_quiz(starting_string):
    print "In the following paragraph, fill in the blanks with appropriate keywords."
    print starting_string
    string_as_list = starting_string.split()
    # first blank

def ask_and_check(blank_number): # blank_number = 1, 2, 3, 4
# this function asks user for answer and checks if it is correct, user is allowed
# five attempts
    attempt = 0
    while attempt < 5:
        answer = raw_input("What goes in place of " + to_be_replaced[blank_number] + "? ")
        if answer == correct_answers[blank_number]:
            print "Good job!"
            print answer
            break
        else:
            attempt += 1
        if attempt < 4:
            print "Nope, try again!"
        if attempt == 4:
            print "Uh oh, only one more guess!"
        if attempt == 5:
            print "Game over!"


level1_quiz(sample)
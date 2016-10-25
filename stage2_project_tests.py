to_be_replaced = ["___1___","___2___","___3___","___4___"]
correct_answers = ["function","parameters","None","list"]

def ask_for_input(blank_number): # blank_number = 1, 2, 3, 4
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

ask_for_input(0)
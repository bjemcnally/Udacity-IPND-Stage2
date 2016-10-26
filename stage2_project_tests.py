def difficulty_value(difficulty):
# translates user's chosen diffulty to numerical value (i.e. number of allowed attempts)
    if difficulty == "Easy":
        allowed_attempts = 5
    if difficulty == "Medium":
        allowed_attempts = 3
    if difficulty == "Hard":
        allowed_attempts = 2
    if difficulty == "Easy" and difficulty == "Medium" and difficulty == "Hard":
        print "\nWhoops! You'll need to start over. Please choose a difficulty from Easy, Medium, or Hard (case sensitive!)."
    return allowed_attempts

print difficulty_value("Easy")
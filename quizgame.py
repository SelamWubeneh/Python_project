# 5. Quiz Game
# Create a basic quiz game that:
# Contains a list of 5–10 questions stored in a dictionary (or list of dicts).
# Asks the user each question and records their answers.
# At the end, displays:
# The user’s score (e.g., 7/10)
# Correct answers for any questions they got wrong
# Skills practiced: loops, dictionaries, input, comparison, counters, print formatting


print("=====Quiz Game=====")
Quiz= {
    "In Git, what command uploads your code to GitHUB? ": "push",
    "What data type uses key value pairs in python? ": "dictionary",
    "In python loops, which keyword stops the loop immediately?": "break",
    "What function do we use to get user input? ": "input",
    "What symbol you use to comment in python? ": "#"
}

score = 0
for question in Quiz:
    answer = input(question)
    if answer.lower() == Quiz[question].lower():
        print(" Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is:", Quiz[question])
print("===============")
print("You got", score, "out of", len(Quiz), "questions correct!")
print("===============")

# import questions list
from questions import questions

# Function to start the quiz
def start_quiz():
    score = 0 # variable to store score

    print("\n Welcome to the Python Quiz!")
    print("Answer the following question.")

    #Loop through each question
    for question in questions:
        print("\n ")
        
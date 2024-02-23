# Import the following
from my_quiz_qbank_pkg import quiz_question_bank   # Import the question bank
import time      # To Handle time related
import sys       # To Exit the program
import random    # To generate random number

# Environment setup

total_score = 0             # To Track User's result

# Define the function once your quiz game starts


def my_quiz_game():
    print("##----------WELCOME TO ABHISHEK'S QUIZ GAME----------##")
    print("\n")
    my_quiz_menu_display()    # Display the menu
    # Take user input to proceed
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            my_quiz_play()    # Play the quiz
            break
        elif choice == '2':
            my_quiz_exit()    # Terminate the quiz
            break
        else:
            print("You have choosen wrong choice, please use '1' or '2' ")
            continue

# Function to display the quiz menu


def my_quiz_menu_display():
    print("1. Play the quiz game")
    print("2. Exit the Game")

# Exit the quiz


def my_quiz_exit():
    print("Going to exit the game")

# Play the quiz


def my_quiz_play():
    # Take the different input from users
    user_name = input("What is your name? ")
    user_choice_num_of_q = input(
        "\nHow many question do you want?\nChoose any number between 1 to 20 : ")
    user_choice_subject = input("\nWhat subject do you want to choose ? ")
    user_choice_level = input(
        "\nWhat level you want : Easy(E) , Medium(M) , Hard(H) or Achievers(A) ? ")
    user_alloted_time = int(user_choice_num_of_q) * \
        quiz_alloted_time(user_choice_level)
    quiz_welcome(user_name, user_choice_num_of_q,
                 user_choice_subject, user_choice_level, user_alloted_time)   # Welcome the user

    quiz_play(user_choice_num_of_q)

# Function for quiz play


def quiz_play(user_choice_num_of_q,):
    global quiz_question
    for i in range(int(user_choice_num_of_q)):
        print("Q#", i+1, end=' ')
        # Display question info
        # Display question infront of user and stored the index of the question
        q_index = displayQuestion(quiz_question_bank.quiz_question)
        user_answer = input("\n Enter your Answer : ")
        checkAnswer(q_index, user_answer, quiz_question_bank.quiz_question)
        # Remove the question at given index from question bank if already answered
        quiz_question_bank.quiz_question.pop(q_index)

        print("$$$$$$$$$$$$$$$$$$$$$$")

# Check answer


def checkAnswer(q_index, user_answer, quiz_question):
    print("\nWAIT.......YOUR ANSWER IS BEING CHECKED")
    correct_answer = quiz_question[q_index]["answer"]
    global total_score
    # Check the 1st position of user's answer by captilizing it
    if user_answer == correct_answer:
        print("\nYOUR ANSWER : ",
              quiz_question[q_index]["answer"], " IS CORRECT ")
        total_score += 1
    else:
        print("\nYOUR ANSWER : ", user_answer, " IS WRONG ")

    print("\nYour Total Score is :", total_score)
    print("***************************************************")

# Display question info


""" def displayQuestion(quiz_question):
    print("+++++++++++++++++++++++++++++")
    # Total number of question on question bank
    no_of_q_in_question_bank = len(quiz_question)
    # Generate random number between 0 and Total# of questions in question bank
    random_i = random.randint(0, no_of_q_in_question_bank)
    print(quiz_question[random_i]["question"])      # Print question
    # Loop through all options
    for opt in range(len(quiz_question[random_i]["options"])):
        print(quiz_question[random_i]["options"][opt])
    return random_i    # Return the question index """


def displayQuestion(quiz_question):
    print("+++++++++++++++++++++++++++++")
    # If question bank isnot empty
    if len(quiz_question) > 0:
        # Get the list of keys of dictioanry
        q_list_key = list(quiz_question.keys())

        # Get random key_questions from question bank

        random_i = random.choice(q_list_key)

        # Print the question
        print(quiz_question[random_i]["question"])      # Print question
        # Print the options
        for opt in range(len(quiz_question[random_i]["options"])):
            print(quiz_question[random_i]["options"][opt])
        return random_i  # Return the question index """

    else:
        print("No more question")

# Calculate the quiz alloted time for user based on number of question and level of quiz


def quiz_alloted_time(user_choice_level):
    if user_choice_level == 'E':
        return 10
    elif user_choice_level == 'M':
        return 15
    elif user_choice_level == 'H':
        return 20
    elif user_choice_level == 'A':
        return 30
    else:
        return 5


# Display the welcome message and user's choice


def quiz_welcome(user_name, user_choice_num_of_q, user_choice_subject, user_choice_level, user_alloted_time):
    print("******************************************************")
    print("\nWelcome", user_name, "to this MCQ quiz game")
    print("\nYou want", user_choice_num_of_q, "Question for the quiz")
    print("\nYour Choise of subject is :", user_choice_subject)
    print("\nYou have choosen level of quiz game : ", user_choice_level)
    print("\nTotal time alloted to this quiz is :",
          user_alloted_time, " (Seconds)")
    print("******************************************************")


# Call the quiz game
my_quiz_game()

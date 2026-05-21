print("Welcome to the Python Quiz!")

answer_user = input("Wold you like to take the quiz? (S/N): ")

if answer_user.lower() != "s":
    print("Maybe next time! Goodbye!")
    quit()

print("Great! Let's get started!")
print("Welcome to the Python Quiz!")
answer_user = input("Would you like to take the quiz? (S/N): ")

if answer_user.lower() != 's':
    print("Maybe next time! Goodbye!")
    quit()

print("Great! Let's get started!")
print("What is Python? \n (A) Python is a versatile, high-level programming language known for its easy-to-read syntax and broad applications.\n (B) \n (C) \n (D) \n")

answer_1 = input("Answer: ")

if answer_1.upper() == 'A':
    print("Correct!")
else:
    print("Incorrect")
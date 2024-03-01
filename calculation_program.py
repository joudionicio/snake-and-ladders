import random

print("Welcome to this calculator!")
print("It can add, subtract, multiply and divide whole numbers from 0 to 50")
user_number = int(input("Please choose your first number: "))
sign = input("What do you want to do? +, -, /, or *: ")
guess_number = random.randint(0,50)

if sign == '+':
    correct_answer = user_number + guess_number
    user_answer = int(input(f"What is {user_number} + {guess_number}? "))
elif sign == '-':
    correct_answer = user_number - guess_number
    user_answer = int(input(f"What is {user_number} - {guess_number}? "))
elif sign == '*':
    correct_answer = user_number * guess_number
    user_answer = int(input(f"What is {user_number} * {guess_number}? "))
elif sign == '/':
    if guess_number != 0:
        correct_answer = user_number / guess_number
        user_answer = float(input(f"What is {user_number} / {guess_number}? "))
    else:
        print("Error: Division by zero is not allowed.")

if user_answer == correct_answer:
    print("Correct!")
else:
    print(f"Incorrect. The correct answer is {correct_answer}.")

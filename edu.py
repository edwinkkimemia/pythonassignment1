products = ('XBox', 499.99, "Habibi", 23)
print(products[0])

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

print(f"Hello {name}, you are {age} years old, {height} cm tall, and weigh {weight} kg.")

# Personalized Greeting App
name = input("What’s your name? ")  # Get user's name
color = input("What’s your favorite color? ")  # Get user's favorite color

# Print personalized greeting
print(f"Hello, {name}! Your favorite color, {color}, is awesome!")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

c = a + b
print(f"The sum of {a} and {b} is {c}.")

# Simple Calculator Program

# Get input from user
num1 = float(input("Enter the first number: "))  # Convert to float to handle decimals
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Error: Invalid operation! Please use +, -, *, or /")


# Random Joke Generator
import random

# List of programming-themed jokes
jokes = [
    "Why do programmers prefer dark mode? Because the light attracts bugs!",
    "What’s a Python programmer’s favorite snack? Bytes and chips!",
    "Why don’t programmers pair program? Because they don’t want to share the screen-time!",
    "How do you comfort a JavaScript developer? Tell them 'undefined' is not a problem!",
    "Why did the Python dev go broke? Too many free libraries!"
]

# Select and display a random joke
random_joke = random.choice(jokes)
print("Here’s your random joke: 🤣")
print(random_joke)
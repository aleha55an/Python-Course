import random

# Randomly select an item from a list
dice = [1, 2, 3, 4, 5, 6]
print("Rolling the dice...")
dice_roll = random.choice(dice)
print(f"You rolled a {dice_roll}!")

# Generate a random integer between 1 and 100
number = random.randint(1, 100)
print(f"Random number between 1 and 100: {number}")

# Generate a random float between 0 and 1
value = random.random()
print(f"Random float between 0 and 1: {value}")

#randomly select name from list
name = ["Ali","Aisha", "Ahmed", "Fatima"]
print(f"Random name from the list: {random.choice(name)}")

#randomly shuffle a list of numbers
numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

#randomly uniformly select a decimal number between 1 and 10
random_numbers = random.uniform(1, 10)
print(f"Random float between 1 and 10: {random_numbers}")

secret_number = random.randint(1, 10)
attempt = 0

while True:
    guess = int(input("Guess the secret number between 1 and 10: "))
    attempt += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempt} attempts.")
        break


import math

#function to calculate square root 
number = float(input("Enter a number to calculate its square root: "))
if number < 0:
    print("Cannot calculate the square root of a negative number.")
else:
    square_root = math.sqrt(number)
    print(f"The square root of {number} is: {square_root}")


#function to calculate factorial of a number
number = int(input("Enter a number to calculate its factorial: "))
if number < 0:
    print("Cannot calculate the factorial of a negative number.")
else:
    factorial = math.factorial(number)
    print(f"The factorial of {number} is: {factorial}")

#number floor and ceil(lower and upper bound)
number = float(input("Enter a number to calculate its floor l: "))
print(f"Floor of {number} is: {math.floor(number)}")

number = float(input("Enter a number to calculate its ceil: "))
print(f"Ceil of {number} is: {math.ceil(number)}")

#calculate area of a circle untill 2 decimal places by using math.pi
radious = float(input("Enter the radius of the circle: "))
area = math.pi * radious ** 2
print(f"The area of the circle with radius {radious} is: {area:.2f}")





#request to get a random cat fact from the API
import requests

response = requests.get("https://catfact.ninja/fact")

if response.status_code == 200:
    data = response.json()
    print(f"Random cat fact: {data['fact']}")
else:
    print("Failed to retrieve cat fact. Please try again later.")

import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()

print("whole dictionary:", data)          
print("only fact:", data["fact"])        
print("only length:", data["length"])    


#statistics module to calculate mean, median, mode, and standard deviation
import statistics

numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
std_dev = statistics.stdev(numbers)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}, Standard Deviation: {std_dev}")


numbers =[]

count = int(input("Enter the range of numbers: "))
for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(f"Numbers entered: {numbers}")
print(f"Mean: {statistics.mean(numbers)}")
print(f"Median: {statistics.median(numbers)}")  
print(f"Mode: {statistics.mode(numbers)}")
print(f"Standard Deviation: {statistics.stdev(numbers)}")



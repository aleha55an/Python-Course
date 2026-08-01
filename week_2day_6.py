#greeting function with default parameters

def greet_with_age(name = "Friend" , age = "teen"):
    print(f"Hello, {name}! You are {age} years old.")

greet_with_age("Ali", 25)
greet_with_age("Aisha", 30)
greet_with_age("Ahmed", 35)
greet_with_age()  # Using default values

#introduce yourself function
def introduce_yourself(name, age, city):
    print(f"My name is {name}, I am {age} years old and I live in {city}.")

name = input("Enter your name: ")
age = input("Enter your age: ") 
city = input("Enter your city: ")
introduce_yourself(name, age, city)

#function to calculate area of rectangle
def calculate_area(length, width):
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
result = calculate_area(length, width)
print(f"The area of the rectangle is: {result}")

#number check positive, negative or zero
def number_check(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

num = float(input("Enter a number: "))
result = number_check(num)
print(f"The number is: {result}")


#function to calculate area and perimeter of rectangle and return both values
def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = int(input("Length likho: "))
width = int(input("Width likho: "))

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")


#function to calculate sum of two numbers and return the result
def number(num1,num2):
    sum = num1 + num2
    return sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = number(num1,num2)
print(f"The sum of {num1} and {num2} is: {result}")

result = number(num1,num2)
multiplication = result * 2  # Example multiplication by 2
print(f"The multiplication of {result} is: {multiplication}")
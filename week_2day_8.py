
#try and except block to handle division by zero and invalid input
print("Welcome to the safe division program.")
print("You can enter two numbers to divide them, or type 'q' to quit.")

while True:
    try:
        first_input = input("Enter the first number (or 'q' to quit): ")
        if first_input.lower() == 'q':
            print("Goodbye!")
            break

        second_input = input("Enter the second number (or 'q' to quit): ")
        if second_input.lower() == 'q':
            print("Goodbye!")
            break

        number1 = int(first_input)
        number2 = int(second_input)

        result = number1 / number2
        print(f"The result of {number1} divided by {number2} is: {result}\n")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a nonzero second number.\n")
    except ValueError:
        print("Error: Please enter valid whole numbers. Try again.\n")
    except Exception as unexpected:
        print(f"An unexpected error occurred: {unexpected}\n")

print("Program ended.")


#None use case
def find_name(username):
    # Function to find a name in a predefined list
    names_list = ["Ali", "Ahmed", "Hassan", "David", "Eve"]
    if username in names_list:
        return username
    else:
        return None

result = find_name("Haider")

if result is None:
    print("Name not found.")
else:
    print(f"Name found: {result}")


#try and except block to handle invalid input
while True:
    try:
        data = input("Enter two number separated by a space: ").split()
        num1 = int(data[0])
        num2 = int(data[1])
        print(f"The sum of {num1} and {num2} is: {num1 + num2}")
        break
    except ValueError:
        print("Error: Please enter valid whole numbers. Try again.")
    except IndexError:
        print("Error: Please enter exactly two numbers separated by a space.")


#use of string methods
name = input("Enter your name: ")
if name.isalpha():
    print(f"Hello, {name.capitalize()}!")
else:
    print("Error: Name should only contain alphabetic characters.")

name_num = input("Enter your name followed by a number (e.g., John123): ")
if name_num.isalnum():
    print(f"Your input is valid: {name_num}")
else:
    print("Error: Input should only contain alphanumeric characters.")

name_space = input("Enter your name with spaces (e.g., John Doe): ")
if name_space.replace(" ", "").isalpha():
    print(f"Hello, {name_space.title()}!")
else:
    print("Error: Name should only contain alphabetic characters and spaces.")

#string formatting to align the text
name = input("Enter your name: ")
print(f"Hello,{name:^20}")
print(f"Hello,{name:>20}") 
print(f"Hello,{name:1<20}")

#old style string formatting
name = "Ali"
age = 20

print("Mera naam {} hai aur meri age {} hai".format(name, age))


#num1 and num2 input from user and perform sum, division, percentage and width calculation in a formatted way
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
division = num1 / num2
percentage = (num1 / num2) * 100
width = num1 * num2

print(f"The sum of {num1} and {num2} is: {sum:.2f}")
print(f"The division of {num1} by {num2} is:   {division:.1f}")
print(f"The percentage of {num1} with respect to {num2} is: {percentage:.3f}%")
print(f"The width (product) of {num1} and {num2} is: {width:.2f}")
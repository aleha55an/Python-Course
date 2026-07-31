#number = 10

#if number > 5:
 #   print("Number 5 se bara hai")

#if number > 100:
 #   print("Number 100 se bara hai")

#print("Check complete")

marks = int(input("Enter a marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

    
temperature = int(input("Enter the temperature: "))
if temperature > 30:
    print("It's a hot day"  )
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")

day = int(input("Enter the day number (1-7): "))
if day == 1:
    print("Monday")         
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")


age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ").lower()

if age >= 18 and has_license == "yes":
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")


temperature = int(input("Enter the temperature: "))
is_raining = input("Is it raining? (yes/no): ").lower()

if temperature > 30 or is_raining == "yes":
    print("It's a hot day or it's raining.")
elif temperature > 20 and not is_raining == "yes":
    print("It's a nice day and it's not raining.")
else:
    print("It's a cold day and it's not raining.")








#match
choose = input("choose any operator (+,-,*,/): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match choose:
    case "+":
        print("Sum:", num1 + num2)
    case "-":
        print("Difference:", num1 - num2)
    case "*":
        print("Multiplication:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Division:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Error: Invalid operator.")

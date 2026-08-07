import json

student = [
    {
        "name": "ALi",
        "age": 20,
        "courses": ["Math", "Science", "History"]
    }
]

with open("student.json", "w") as file:
    json.dump(student, file)
    print("Student data has been written to student.json")


with open("student.json", "r") as file:
    loaded_student = json.load(file)
    print("Loaded student data from student.json:")
    print(loaded_student)

new_student = {
    "name": "John",
    "age": 22,
    "courses": ["English", "Art", "Music"]
}

student.append(new_student)

with open("student.json", "w") as file:
    json.dump(student, file)
    print("Updated student data has been written to student.json")


with open("student.json", "r") as file:
    loaded_student = json.load(file)
    print("Updated Loaded student data from student.json:")
    print(loaded_student)




#regex

import re

# Test the regex pattern with different phone number formats
numbers = ["03001234567", "+923001234567"]

for num in numbers:
    result = re.search(r"(\+92)?\d{10,11}", num)
    print(f"{num} → {result.group() if result else 'No match'}")



print(re.search(r"\d+", "abc"))
print(re.search(r"\d+", "abc5"))
print(re.search(r"\d+", "abc555xyz"))
print(re.search(r"\d+", "5a5b5"))


#check if a string contains any digits
text = "hello 453 world 123"
result = re.findall(r"\d+", text)

if result:
    for number in result:
        print(number)
else:
    print("No digits found in the string.")



text = input("write any paragraph which include all numbers and words : ")

# all numbers
numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

# all words
words = re.findall(r"[a-zA-Z]+", text)
print("Words:", words)


#keep pattern & protecting email address and cnic number

input_email = input("Enter your email address(ali@gmail.com): ")
input_cnic = input("Enter your CNIC number(35201-1234567-1): ")

email_format = re.search(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", input_email)
cnic_format = re.search(r"(\d{5}-\d{7}-\d{1})", input_cnic)

if email_format and cnic_format:
    print("Protected email address:", re.sub(r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", r"*****@\2", input_email))
    print("Protected CNIC number:", re.sub(r"(\d{5})-\d{7}-\d{1}", r"\1-XXXXXXX-X", input_cnic))
else:
    print("Invalid email address or CNIC number format.")

# protecting phone number
your_number = input("write your phone number: ")

fully_hidden = re.sub(r"\d+", "XXXXXXXXXXX", your_number)
digit_by_digit = re.sub(r"\d", "*", your_number)

print("fully hidden:", fully_hidden)
print("Digit by digit:", digit_by_digit)


#date and time
import datetime

today = datetime.date.today()
print("Today's date:", today)

#difference between two dates
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 12, 31)

difference = date2 - date1
print("Difference between", date2, "and", date1, "is", difference.days, "days.")


#formatting date and time
today = datetime.date.today()
print(today.strftime("Today's date is: %B %d, %Y"))
print(today.strftime("Today's date is: %A, %B %d, %Y"))
print(today.strftime("Today's date is: %d/%m/%Y"))
print(today.strftime("%A"))  

print("Current time:", datetime.datetime.now().strftime("%H:%M:%S"))

#birthday and age calculation
try:
    birthday = input("Enter your birthday (YYYY-MM-DD): ")
    birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
    print("Your age is:", age)
except ValueError:
    print("Invalid date format. Please enter your birthday in YYYY-MM-DD format.")

try:
    event_date = input("Enter the event date (YYYY-MM-DD): ")
    days_until_event_date = datetime.datetime.strptime(event_date, "%Y-%m-%d").date()
    days_until_event = (days_until_event_date - today).days
    print("Days until the event:", days_until_event)
except ValueError:
    print("Invalid date format. Please enter the event date in YYYY-MM-DD format.")


#math module
import math

# 1. Find area of circle
radius = float(input("Enter radius of circle: "))
area = math.pi * (radius ** 2)
print(f"Area: {area:.2f}")

# 2. Find GCD of two numbers
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print(f"GCD: {math.gcd(num1, num2)}")

# 3. Find square root and square of a number
number = float(input("Enter a number: "))
print(f"Square root: {math.sqrt(number):.2f}")
print(f"Square (power 2): {math.pow(number, 2)}")

# 4. Comparing floor, ceil, and trunc of a decimal number
decimal_num = float(input("enter any decimal number: "))
print(f"Floor: {math.floor(decimal_num)}")
print(f"Ceil: {math.ceil(decimal_num)}")
print(f"Trunc: {math.trunc(decimal_num)}")

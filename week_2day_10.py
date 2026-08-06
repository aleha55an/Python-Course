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



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

# Saare words nikalo (letters wale)
words = re.findall(r"[a-zA-Z]+", text)
print("Words:", words)


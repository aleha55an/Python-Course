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
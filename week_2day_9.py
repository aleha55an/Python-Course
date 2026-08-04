# This is a simple note-taking application that demonstrates file operations in Python.
file = open("mynote.txt", "w")
file.write("This is my note.\n")
file.write("I am learning Python.\n")
file.close()

# Reading the content of the file
with open("mynote.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)

# Appending additional content to the file
with open("mynote.txt", "a") as file:
    file.write("This is an additional line.\n")

# Reading the updated content of the file
with open("mynote.txt", "r") as file:
    content = file.read()
    print("Updated content of the file:")
    print(content)



import os

# Simple note-taking application with file operations

def add_sample_entries():
    sample_entries = [
        "This is my sample entry.",
        "I am learning Python.",
        "This is an additional line."
    ]
    with open("mynote.txt", "a") as file:
        for entry in sample_entries:
            file.write(entry + "\n")
    print("Sample entries added successfully.")

while True:
    print("\n1. Add New Entry")
    print("2. View Entries")
    print("3. Delete File")
    print("4. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        entry = input("Enter your note: ")
        with open("mynote.txt", "a") as file:
            file.write(entry + "\n")
        print("Note added successfully.")
    elif choice == '2':
        try:
            with open("mynote.txt", "r") as file:
                print("Your notes:")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No notes found. Please add a note first.")
    elif choice == '3':
        file_path = "mynote.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} has been deleted.")
        else:
            print(f"{file_path} does not exist.")
    elif choice == '4':
        add_sample_entries()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


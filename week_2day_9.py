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
    print("4. Add Sample Entries")
    print("5. Quit")

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


    
# Function to delete a specific line from the file based on user input
def delete_line_by_number(filename, line_number_to_delete):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    # Validation: check if the line number is valid
    if line_number_to_delete < 1 or line_number_to_delete > len(lines):
        print(f"Error: Line number {line_number_to_delete} is out of range. The file has {len(lines)} lines.")
        return   
    
    with open(filename, "w") as file:
        for i, line in enumerate(lines):
            if i != line_number_to_delete - 1:
                file.write(line)

    with open(filename, "r") as file:
        print("Updated content of the file after deletion:")
        for line in file:
            print(line.strip())

print("Enter the line number you want to delete from 'mynote.txt':")
line_number = int(input())
delete_line_by_number("mynote.txt", line_number)


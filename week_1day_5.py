num = 1

while num <= 10:
    print(num)
    num += 1    
print("Loop complete")


#while loop to check if marks are pass or fail
while True:
    marks_input = input("Enter your marks (or type 'exit' to quit): ")
    
    if marks_input.lower() == "exit":
        print("Program end Good Bye--!")
        break   
    
    marks = int(marks_input)
    
    if marks < 0 or marks > 100:
        print("Invalid marks entered. Please try again.")
        continue
    
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")


#loop through a string

name = input("Enter your name: ")
for key in name:
    print(key)

#range loop

i = 1
for i in range(1, 6):
    print(i)
for i in range(1, 6,2):
    print(i)


#table of a number

num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")  

     
#for and while loop to print a triangle of stars
for i in range(1, 6):
    stars = ""
    j = 1
    while j <= i:
        stars += "*"
        j += 1
    print(stars)
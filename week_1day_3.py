#operators in python
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

# Arithmetic
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Remainder:", num1 % num2)

# Comparison
print("is num1 greater than num2?", num1 > num2)
print("Are both numbers equal?", num1 == num2)
print("is num1 less than or equal to num2?", num1 <= num2)
print("is num1 greater than or equal to num2?", num1 >= num2)

# Logical
print("Are both numbers positive?", num1 > 0 and num2 > 0)
print("Is at least one number positive?", num1 > 0 or num2 > 0)
print("Is num1 positive and num2 negative?", num1 > 0 and num2 < 0)
print("Is num1 negative or num2 positive?", num1 < 0 or num2 > 0)
print("Are both numbers negative?", num1 < 0 and num2 < 0)

#list in python
fruits = ["apple", "banana", "cherry", "date"]
random_numbers = [5, 2, 9, 1, 7]
print("Fruits list:", fruits)   
print("Random numbers list:", random_numbers)

#accessing list elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("First random number:", random_numbers[0])
print("Last random number:", random_numbers[-1])

#length of list
print("Number of fruits:", len(fruits))
print("Number of random numbers:", len(random_numbers))

#adding elements to list
fruits.append("mango")
print("Fruits list after adding mango:", fruits)

#removing elements from list
fruits.remove("banana") 
print("Fruits list after removing banana:", fruits)

#inserting elements at specific index
fruits.insert(1, "kiwi")
print("Fruits list after inserting kiwi:", fruits)

#remove an element by index
fruits.pop(2)
print("Fruits list after removing element at index 2:", fruits)

#change value of an element
fruits[0] = "grape"
print("Fruits list after changing first element to grape:", fruits)

#finding index of an element
index_of_cherry = fruits.index("cherry") if "cherry" in fruits else -1
print("Index of cherry:", index_of_cherry)

#finding maximum and minimum values in a list
max_number = max(random_numbers)    
print("Maximum number in random_numbers:", max_number)
min_number = min(random_numbers)
print("Minimum number in random_numbers:", min_number)

#find item in list
print("Is 'date' in fruits list?", "date" in fruits)
print("Is 'banana' in fruits list?", "banana" in fruits)

#looping through a list
for fruit in fruits:
    print("Fruit:", fruit)

#sort a list
random_numbers.sort()
print("Sorted random numbers:", random_numbers)



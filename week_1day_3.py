#operators in python
import email
from webbrowser import get


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


#tuple in python
colors = ("red", "green", "blue")
print("Colors tuple:", colors)

#indexing in tuple

print("First color:", colors[0])
print("Last color:", colors[-1])

#length of tuple

print (len(colors))

#looping through a tuple
for color in colors:
    print("Color:", color)

#checking if an item exists in a tuple
print("Is 'green' in colors tuple?", "green" in colors)



#set in python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)

print ("Union of set1 and set2:", set1 | set2)
print ("Intersection of set1 and set2:", set1 & set2)
print ("Difference of set1 and set2:", set1 - set2)
print ("Difference of set2 and set1:", set2 - set1)
print ("Symmetric difference of set1 and set2:", set1 ^ set2)
print ("Is set1 a subset of set2?", set1 <= set2)


set1.add(6)
print("Set 1 after adding 6:", set1)
set2.remove(4)
print("Set 2 after removing 4:", set2)

#removing duplicates from a list using set
set3 = {1, 2, 3,3,4,4,5,5,6,6,6,6,7,7,8,8,9,9}
print("Set 3:", set3)



#dictionary in python
my_info = {
    "name": "Ali",
    "age": 25,
    "city": "Lalian"
}
print("My Info Dictionary:", my_info)

print("Name:", my_info["name"])
print("Age:", my_info["age"])   
print("City:", my_info["city"])


print("Country:", my_info.get("country", "Not specified"))
print("Email:", my_info.get("email", "Not specified"))

my_info["email"] = "ali@example.com"
print("Updated My Info Dictionary:", my_info)
my_info["age"] = 26
print("Updated My Info Dictionary after changing age:", my_info)

my_info.pop("city")
print("Updated My Info Dictionary after removing city:", my_info)

print("Length of my_info:", len(my_info))

print("Keys in my_info:", my_info.keys())
print("Values in my_info:", my_info.values())
print("Items in my_info:", my_info.items())

for key in my_info:
    print (f"{key}: {my_info[key]}") 
for key, value in my_info.items():
    print(f"{key}: {value}")

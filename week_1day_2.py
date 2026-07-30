# variables 
dob = input("Enter your date of birth: ")

my_name = "Ali"
my_age = 25
my_height = 5.8
am_i_student = False
favorite_subject = "Math"

# Print 
print(dob)
print(my_name)
print(my_age)
print(my_height)
print(am_i_student)
print(favorite_subject)

# Type 
print(type(my_name))
print(type(my_age))
print(type(my_height))
print(type(am_i_student))
print(type(favorite_subject))

#numbers
num1 = 15
num2 = 4
num3= 2+3j

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)
print(type(num1))

#casting

# 1. String 
num = "50"
num = int(num)
print(num + 10)

# 2. Float 
price = 99.99
print(int(price))

# 3. Int ko string 
age = 20
age_text = str(age)
print("Meri age " + age_text + " saal hai")

# 4. Check 
print(type(num))
print(type(age_text))

# string
name = "Ali Hassan"
message ="Hello, my name is " + name
print(message)

print(len(name))

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])
print(name[-8])
print(name[-9])

print(name[0:3])
print(name[:4])
print(name[4:])

country = " my  country  Pakistan "
print(country.strip())

print(country.upper())
print(country.lower())

changed_country = country.replace("Pakistan", "dubai")
print(changed_country)

print(country.find("my"))

print("ahmed" in country)

print("pakistan" * 3)

name = "Ali Hassan"
age = 25
message = f"Hello, my name is {name} and I am {age} years old."
print(message)

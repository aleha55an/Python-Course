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
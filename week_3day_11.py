class student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Courses: {self.courses}")


student1 = student("Ali", 20, ["Math", "Science", "History"])
student2 = student("John", 22, ["English", "Art", "Music"])
student1.display_info()
student2.display_info()


class bank_account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient funds")

bank_account1 = bank_account("123456789", 1000)
bank_account1.deposit(int(input("Enter amount to deposit: ")))
bank_account1.withdraw(int(input("Enter amount to withdraw: ")))


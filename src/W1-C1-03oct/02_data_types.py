from decimal import Decimal

name = "Shripathi Raman"
age = 41
is_student = True
height = 5.10
weight = 98
BMI = weight / (height ** 2)
address = None
money = Decimal("100.50")

print(f"Name: {name}, Age: {age}, Student: {is_student}, Height: {height}, Weight: {weight}, BMI: {BMI:.2f}, Address: {address}, Money: {money} ")
print(f"Type of name: {type(name)}, Type of age: {type(age)}, Type of is_student: {type(is_student)}, Type of height: {type(height)}, Type of weight: {type(weight)}, Type of BMI: {type(BMI)}, Type of address: {type(address)}, Type of money: {type(money)} ")

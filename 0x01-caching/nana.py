### 1. Basic Arithmetic
python
# Basic Arithmetic in Python
a = 5
b = 3
print(f"Addition: {a + b}")  # 8
print(f"Subtraction: {a - b}")  # 2
print(f"Multiplication: {a * b}")  # 15
print(f"Division: {a / b}")  # 1.666...


### 2. Conditional Statements
python
# Conditional Statements
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


### 3. Loops
#### For Loop
python
# For Loop
for i in range(5):  # Will iterate from 0 to 4
    print(i)


#### While Loop
python
# While Loop
i = 0
while i < 5:
    print(i)
    i += 1


### 4. Functions
python
# Defining and Calling a Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!


### 5. Lists and List Comprehensions

# Lists and List Comprehensions
my_list = [1, 2, 3, 4, 5]
squared_list = [x ** 2 for x in my_list]  # Squaring each element in my_list
print(squared_list)  # [1, 4, 9, 16, 25]


### 6. Dictionaries
python
# Working with Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Accessing dictionary value


### 7. File Handling
python
# Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a File
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to simulate calculator operations with predefined inputs
def simulate_calculator(choice, num1, num2):
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

# Simulate different operations
simulate_calculator('1', 10, 5)  # Addition
simulate_calculator('2', 10, 5)  # Subtraction
simulate_calculator('3', 10, 5)  # Multiplication
simulate_calculator('4', 10, 5)  # Division
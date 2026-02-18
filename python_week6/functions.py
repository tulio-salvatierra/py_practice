# def greet():
#     print("Hello, welcome to Python programming!")
#     print("Let's learn about functions.")
    
# greet()

# def introduce(name, age):
#     print(f"Hello, my name is {name} and I am {age} years old.")
    
# introduce("Alice", 25)
# introduce("Bob", 30)

# def add(a, b):
#     result = a + b
#     return result

# sum1 = add(5, 10)
# print(f"The sum of 5 and 10 is: {sum1}")

# def create_user(name, age=18, city='Unknown'):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"City: {city}")
    
# create_user("Alice")
# create_user("Bob", age=25)
# create_user("Charlie", city="New York")

# global_var = "I am a global"

# def my_function():
#     local_var = "I am a local"
#     print(global_var)  # Accessing global variable
#     print(local_var)   # Accessing local variable
    
# my_function()

# print(global_var)  # Accessing global variable

numbers = [10, 20, 30, 40, 50]

def calculate_average(numbers):
    digit = []
    for num in numbers:
        append = digit.append(num)
    average = sum(digit) / len(digit)
    return average
print(calculate_average(numbers))


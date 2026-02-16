# student = { 'name': 'Bob', 'grade': 85}
# print(student)

# student = {}
# student['name'] = "Bob"
# student['grade'] = 85
# print(student)

# student = {'name': 'Alice', "age": 25, 'major': 'CS'}

# print(student.get('name'))
# print(student.get('goa'))
# print(student.get('gpa', 0.0))

# student = { 'name': 'Bob', 'age': 20}

# student['major'] = "CS"

# student['age'] = 21
# print(student['age'])

# del student['age']
# print(student)

# student = {'name': 'Alice', 'age': 25, 'major': 'CS'}

# keys = student.keys()
# print(keys)

# values = student.values()
# print(values)

# items = student.items()
# print(items)

# key_list = list(student.keys())

# grades = {'math': 85, 'english': 92,'science': 88}

# for subject in grades:
#     print(subject)
    
# for grade in grades.values():
#     print(grade)
        
# for subject in grades.items():
#     print(f'{subject}: {grades}')

# prices = {
#     'laptop': 999.99,
#     'mouse': 25.50,
#     'keyboard': 79.99,
#     'monitor': 299.99
# }

# total = sum(prices.values())
# print(f'Total: ${total:.2f}')

# avg = total / len(prices)
# print(f'Average: ${avg:.2f}')

# max_item = max(prices, key=prices.get)
# print(f'Most expensive: {max_item}')   

# student = {'name': 'Bob', 'age': 20}

# new_data = {'major': 'CS', 'gpa': 3.8}
# student.update(new_data)
# print(student)

# age = student.pop('age')
# print(f'Removed age : {age}')
# print(student)

# student.clear()
# print(student) 

squares = {x: x**2 for x in range(1, 6)}
print(squares)

prices = {'apple': 1.5, "banana": .75}
doubled = {k:v*2 for k, v in prices.items()}
print(doubled)

grades = {'math': 85, 'english': 92, 'science': 78}
high = {k: v for k, v in grades.items() if v >= 80}
print(high)
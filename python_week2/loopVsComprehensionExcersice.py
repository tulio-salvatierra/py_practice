numbers = [1,2,3,4,5]

# old way
doubled = []

for num in numbers:
    doubled.append(num * 2)
print(doubled)
# new way
doubled_comp = [num * 2 for num in numbers]
print(doubled_comp)

# Same result with less code!

# Squares practice in a list comprehension
squares = [n ** 2 for n in numbers]
print(squares)

# Make all uppercase
names = ["alice", "bob", "carol"]
upper = [name.upper() for name in names]
print(upper)

# Get string lengths
lengths = [len(name) for name in names]
print(lengths)

words = ["hello", "hello", "python", "is", "fun"]
lengths = [len(word) for word in words]
print(lengths)

#get only even numbers

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# get only positive numbers
mixed = [-5, 3, -1, 7, -2, 8]
positives = [v for v in mixed if v > 0]
print(positives)

# get names longer tahn 4 letters
names = ["alice", "bob", "carol", "dave", "eve"]
long_names = [name for name in names if len(name) > 4]
print(long_names)

# Student grades: [student] [subjects]
# columns: Math, English, Science

grades= [
    [95, 87, 92],
    [88, 90, 85],
    [92, 88, 94],
    [78, 85, 80]
]

print(grades[0][0])
print(grades[1][2])

print(grades[0])  # First student's grades

for student_grades in grades:
    avg = sum(student_grades) / len(student_grades)
    print(f"Average: {avg:.1f}")
    
avgs = [sum(row)/len(row) for row in grades]
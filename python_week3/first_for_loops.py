fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(fruit)
    
# process each number
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    squared = number ** 2
    print(f"{number} squared is {squared}")    
    
# range in loops
for i in range(5):
    print("Iteration number:", i)
    
    #count 1 to 10
for i in range(1, 11):
    print(i)    
    
    #count by 2's even numbers
for i in range(0, 11, 2):
    print(i)
    
    #count by 2's odd numbers
for i in range(1, 11, 2):
    print(i)
    
    #count backwards
for i in range(10, 0, -1):
    print(i)
    
    squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)


# accum pattern
numbers = [10, 25, 30, 15, 40]
total = 0
for number in numbers:
    total += number
print("Total sum:", total)

average = total / len(numbers)
print("Average:", average)

#enumerate

student = ["Alice", "Bob", "Carol", "David"]
for index, name in enumerate(student):
    print(f"Student {index + 1}: {name}")
    
    
responses = ["yes", "no", "maybe", "banana", "yesss"]

print("Invalid answers (with line numbers)")
for idx, answer in enumerate(responses, start=1):
    if answer.lower() not in ["yes", "no"]:
        print(f"Line {idx:2d}: {answer} <- not allowed answers")
        
# common loops in data processing
cities = ["new york", "Los angeles", "chicago", "houston", "PHOENIX"]
cleaned_cities = []
for city in cities:
    cleaned = city.strip().title()
    cleaned_cities.append(cleaned)
print(cleaned_cities)

sales = [120.5, 45.0, 890.75, 320.00, 675.30, 15.20]
total_sales = 0
for amount in sales:
    total_sales = 0
    high_value_count = 0
    for amount in sales:
        total_sales += amount
        if amount > 500:
            high_value_count += 1
average_sales = total_sales / len(sales)
print(f"Total Sales: ${total_sales:.2f}")
print(f"Average Sales: ${average_sales:.2f}")
print(f"Number of high value sales (> $500): {high_value_count}")


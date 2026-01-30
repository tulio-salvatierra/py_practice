# multiplication table

#for i in range(1,4):
 #   for j in range(1,4):
  #      print(f"{i} x {j} = {i*j}")
        
#for row in range(1, 6):
#    for col in range(1, 6):
#        product = row * col
#        print(f"{product:3d}", end=' ')
#    print()  # for new line after each row        
    
    
# right triangle pattern
 #for i in range(1, 6):
   #  for j in range(i):
     #    print('*', end='')
     #print()  # for new line after each row


# Nested loops for 2d data structures

#grades = [
#   [95, 87, 92],
#   [88, 90, 85],
#   [92, 88, 94]
#]
#for student_num, student_grades in enumerate(grades,1):
#    total = 0
#    for grade in student_grades:
#        total += grade
#    average = total / len(student_grades)
#    print(f"Student {student_num} average: {average:.1f}")
 
# colors = ['Red', 'Green', 'Blue']       
# sizes = ['S', 'M', 'L']
# product = []
# for color in colors:
#     for size in sizes:
#         print(f"{size} {color} shirt")
#         product.append(f"{size} {color} shirt")
# print(product)        

# while loops

# count = 0
# while count < 5000000:
#     print(f"Count is: {count}")
#     count += 1

# for i in range(5):
#     print(i)
    
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# age = -1
# while age < 0 or age > 120:
#     age = int(input("Please enter your age (0-120): "))
#     if age < 0 or age > 120:
#         print("Invalid age. Try again.")
# print(f"Your age is: {age}")

# for num in range(1, 1000):
#     if num % 7 == 0 and num % 11 != 0:
#         print(f'found it: {num}')
#         break

numbers = [5, -3, 8, -1, 12, -7, 0, 20]
for num in numbers:
    if num < 0:
        continue
    
    squared = num ** 2
    print(f"{num} Squared : {squared}")
        
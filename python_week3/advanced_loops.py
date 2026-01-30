# multiplication table

for i in range(1,4):
    for j in range(1,4):
        print(f"{i} x {j} = {i*j}")
        
for row in range(1, 6):
    for col in range(1, 6):
        product = row * col
        print(f"{product:3d}", end=' ')
    print()  # for new line after each row        
    
    
# right triangle pattern
 #for i in range(1, 6):
   #  for j in range(i):
     #    print('*', end='')
     #print()  # for new line after each row
    
 
# Nested loops for 2d data structures

    grades = [
       [95, 87, 92],
       [88, 90, 85],
       [92, 88, 94]
    ]
    
    for student_num, student_grades in enumerate(grades,1):
        total = 0
        for grade in student_grades:
            total += grade
        average = total / len(student_grades)
        print(f"Student {student_num} average: {average:.1f}")
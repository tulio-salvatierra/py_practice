# multiplication table

for i in range(1,4):
    for j in range(1,4):
        print(f"{i} x {j} = {i*j}")
        
for row in range(1, 6):
    for col in range(1, 6):
        product = row * col
        print(f"{product:3d}", end=' ')
    print()  # for new line after each row        
    
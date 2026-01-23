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
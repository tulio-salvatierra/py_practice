# def add_all(*args):
#     print(f'Received: {args}')
#     return sum(args)
    
# print(add_all(1, 2))

# print(add_all(1,2,3,4,5))

# print(add_all(10, 20, 30, 40, 50, 60))

# def find_max(*args):
#     if not args:
#         return None
#     max_val = args[0]
#     for num in args:
#         if num > max_val:
#             max_val = num
#         return max_val
# print(find_max(5,2,9,1,7))
# print(find_max(100,50,75))

# def find_max(*args):
#     return max(args) if args else None

# def create_profile(**kwargs):
#     print('Profile created: ')
#     for key, value in kwargs.items():
#         print(f'   {key}: {value}')
        
# create_profile(name='Alice', age=25)

# create_profile(name='bob', age=30, city='NYC', job='engineer')

def square(x):
    return x ** 2
result = square(5)

square_lambda = lambda x: x ** 2
result = square_lambda(5)
print(result)

result = (lambda x: x ** 2) (5)
print(result)
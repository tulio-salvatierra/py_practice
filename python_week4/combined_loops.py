# grades = [95, 45, 87, 62, 55, 92, 78,88]

# for grade in grades:
#     if grade >= 60:
#         print(f'Grade {grade} = PASSED')
#     else:
#         print(f'Grade {grade} = FAILED')

# scores = [95,87,92,88,76,94,85,90,82]

# high_score = []
# for score in scores:
#     if score >=90:
#         high_score.append(score)
# print(f'High Scores: {high_score}')

# scores = [95,87,78,92,88,76,94,85,90,82]

# a_count = 0
# b_count = 0
# c_count = 0

# for score in scores:
#     if score >= 90:
#         a_count += 1
#     elif score >= 80:
#         b_count += 1
#     elif score >= 70:
#         c_count += 1
# print(f'A count: {a_count}')
# print(f'B count: {b_count}')
# print(f'C count: {c_count}')

# ages = [5,25,15,67,45,12,70,30,8,55]

# children = []
# adults = []
# seniors = []

# for age in ages:
#     if age < 18:
#         children.append(age)
#     elif age >= 65:
#         seniors.append(age)
#     else:
#         adults.append(age)
        
# print(f'Children: {children}')
# print(f'Adults: {adults}')
# print(f'Seniors: {seniors}')

# data = [10,25,30,-5,15,40,-2,35]
# found_invalid = None

# for i, value in enumerate(data):
#     if value < 0:
#         if value < 0:
#             found_invalid = (i, value)
#             break
#     if found_invalid:
#         pos, val = found_invalid
#         print(f'Invalid value {val} found at position {pos}')
#     else:
#         print('All values are valid')
        
# students = [
#     {'name': 'Alice', 'grade': 95, 'attendance': 90},
#     {'name': 'Bob', 'grade': 92, 'attendance': 75},
#     {'name': 'Charlie', 'grade': 78, 'attendance': 95},
#     {'name': 'David', 'grade': 88, 'attendance': 85}
#     ]

# def validate_age(age):
#     errors = []
    
#     if not isinstance(age, int):
#         errors.append("Age must be an integer.")
#         return False, errors    
#     if age < 0:
#         errors.append("Age cannot be negative.")
#     if age > 120:
#         errors.append("Age too high (max 120)")
        
#     is_valid = len(errors) == 0
#     return is_valid, errors

# valid, errors = validate_age(25)
# print(f'Valid: {valid}, Errors: {errors}')

# valid, errors = validate_age(-5)
# print(f'Valid: {valid}, Errors: {errors}')

# ages = [25,-5,30,150,45,'invalid',67,0,120]
# valid_ages = []
# invalid_ages = []

# for age in ages:
    
#     if not isinstance(age, (int, float)):
#         invalid_ages.append((age, "Not a number."))
#         continue
    
#     if age < 0 <= 120:
#         valid_ages.append(age)
#     else:
#         invalid_ages.append((age, "out of range "))
# print(f'Valid ages: {len(valid_ages)}')
# print(f'Invalid ages: {len(invalid_ages)}')
# print(f'Invalid data: {invalid_ages}')

def calculate_average(scores):
    if scores is None:
        return None, 'Error: No scores provided.'
    if len(scores) == 0:
        return None, 'Error: Empty score list.'
    
    valid_scores = [s for s in scores if 0 <= s <= 100]
    if len(valid_scores) == 0:
        return None, 'Error: No valid scores.'
    
    avg = sum(valid_scores) / len(valid_scores)
    return avg, "Success"

result, message = calculate_average([95,87,92])
print(f'Average: {result}, Message: {message}')
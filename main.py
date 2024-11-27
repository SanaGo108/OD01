def find_max(list):
    max_number = list[0]
    for i in list:
        if i > max_number:
            max_number = i
    return max_number

numbers = [56, 74, 23, 98, 143, -89, -23]

print(find_max(numbers))

def find_min(list):
    min_number = list[0]
    for i in list:
        if i < min_number:
            min_number = i
    return min_number

numbers = [56, 74, 23, 98, 143, -89, -23]

print(find_min(numbers))
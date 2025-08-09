def odd_numbers(a):
    if a <= 0:
        return []
    result = []

    if a % 2 == 1:
        count = a
    else:
        count = a - 1
    result = []
    for i in range(count):
        odd_number = 2 * i + 1
        result.append(odd_number)
    
    return result


input_a = 6
print(odd_numbers(input_a))

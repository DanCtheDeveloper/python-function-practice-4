def max_num(a, b, c):
    return max(a, b, c)

result = max_num(1, 2, 3)
print("The maximum number is", result)

def multi_list(a, b, c):
    return a * b * c

result = multi_list(1, 2, 3)
print("The multiplied number is", result)

def rev_string(input):
    return input[::-1]

original_string = "Hello"
reversed_string = rev_string(original_string)
print(reversed_string)
print(original_string)
def multiply(*list):
    total: int = 1
    for number in list:
        total *= number
    return total


print(multiply(1, 2, 3, 4))

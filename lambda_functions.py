numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers))


items = [('Product 1', 10), ('Product 2', 9), ('Product 3', 12)]

items.sort(key=lambda item: item[1])
print(items)

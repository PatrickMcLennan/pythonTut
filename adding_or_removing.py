letters = ['a', 'b', 'c']

# ADD
letters.append('d')
letters.insert(0, '-')
print(letters)

# REMOVE
letters.pop()
letters.pop(0)
letters.remove('b')
del letters[0:3]
letters.clear()
print(letters)

names = [
    'Daniel',
    'Mike',
    'William'
]

# List Comprehension
length = [len(name) for name in names]

print(length)

# Dictionary Comprehension
length_two = {name:len(name) for name in names}

print(length_two)


evens = [x for x in range(10) if x % 2 == 0]
print(evens)

squares_tuple = tuple(x**2 for x in range(10))
print(squares_tuple)

squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)

squares_set = {x**2 for x in range(10)}
print(squares_set)

print(type(squares_tuple))



numbers = [n for n in range(3)]

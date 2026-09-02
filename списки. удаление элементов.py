numbers = [10, 20, 30, 40, 50]

# удаление по индексу элемента
del numbers[3]
print(numbers)

# удаление и возврат элемента
deleted = numbers.pop(1)
print(numbers)
print(deleted)

# удаление по значению элемента
fruits = ["яблоко", "банан", "вишня"]
fruits.remove("вишня")
print(fruits)

# очистка списка
items = [1,2,3,4]
items.clear()
print(items)
print(type(items))


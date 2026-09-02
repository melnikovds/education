# позиционные аргументы
def greet(name, age):
    print(f"{name} is {age} years old")

greet("Dmitry", 30)

# именованные аргументы
greet(name="Dmitry", age=30)


# *args собирает позиционные аргументы
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)
# args будет кортеж (1, 2, 3, 4)


# **kwargs собирает именованные аргументы
def print_info(**kwargs):
    print(kwargs)

print_info(name="Dima", age=30)
# kwargs будет словарь:
# {"name": "Dima", "age": 30}
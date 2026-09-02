
# при запуске эта функция также выводит название функции и
# аргрументы которые были переданы в функцию

def my_func(*args):
    print(f'''{my_func.__name__}
    {args}
    ''')
    print("i am working")

my_func(8, 4)


# здесь декоратор

def get_name_args(function):
    def wrapper(*args):
        print(f'''
        {function.__name__}
        {args}
        ''')
        function()
        return function(*args) # важно: передаём args дальше
    return wrapper # без скобок — возвращаем функцию, а не результат её вызова

#  return wrapper Возвращает саму функцию (её можно будет вызвать позже)
#  return wrapper() Вызывает функцию немедленно и возвращает её результат (обычно None)

def my_function(*args):
    print ("я работаю")

# Применяем декоратор
my_function = get_name_args(my_function)
# Теперь вызываем
my_function(1,2)

# либо декоратор можно применить через собачку
@get_name_args
def my_function(*args):
    print("i am running")

my_function(3,4)


# декоратор обволакивает другую функцию и даёт ей
# вспомогательную функциональность но не трогает саму функцию
def decorator_debug(func_two):
    def wrapper(*args, **kwargs):
        print(f'Имя функции: {func_two.__name__}')
        print(f'Аргументы функции: {args=}, {kwargs=}')
        result = func_two(*args, **kwargs)
        print(f'Результат: {result}')
        return result
    return wrapper


@decorator_debug
def add_numbers(x,y):
    return x + y

add_numbers(2,3)











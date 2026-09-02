import time
from functools import cache

@cache
def calculate(x):
    time.sleep(2)
    return x + 1

while True:
    num = int(input("Enter a number: "))
    print(calculate(num))

# если есть тяжёлая функция которая долго выполняется, то можно повесить декоратор кэш на функцию
# и теперь пайтон запоминает результат из предыдущего вызова функции


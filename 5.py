print(list(map((lambda x: x ^ 2), range(10))))

print([x ^ 2 for x in range(10)])



# лямбда функция сработает с заменой первого аргумента
# для лямбда-функции здесь задали знчения по умолчанию
x = (lambda a="fee", b="fie", c="foe": a + b + c)
print(x("wee"))


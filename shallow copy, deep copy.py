import copy

# В Python переменные — это ссылки на объекты, а не сами объекты.

x = [[1,2], [3,4]]
y = x.copy()
y[0].append(5)

print(x)
print(y)

users = [{"name": "Dima"}, {"name": "Alex"}]
copy_users = users.copy()

copy_users[0]["name"] = "Ivan"

print(users)

# Shallow copy (поверхностная копия)
# Создаётся новый контейнер,
# но вложенные объекты остаются теми же

a = [[1, 2], [3, 4]]
b = copy.copy(a)

print(a != b)

# теперь это разные списки, но внутри — те же объекты

b[0].append(999)
print(a)

# изменился и a, потому что вложенный список общий


# Deep copy (глубокая копия)
# Копируется всё рекурсивно
c = [[1, 2], [3, 4]]
d = copy.deepcopy(c)

d[0].append(999)
print(c)

# полностью независимые структуры
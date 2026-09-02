m = "10"
n = 3
print(int(m) ** n)

x = [1, 2, 3]
y = x
y.append(4)
print(x)

p = 1
for _ in range(3):
    p += p
    p -= 1
print(p)

e = 0
for i in range(5):
    if i == 3:
        break
    e += i
print(e)

a = (1, 2, [3, 4])
a[2].append(5)
print(a)

s = "python"
s = s[0].upper() + s[1:]
print(s)

c = [1, 2, 3]
d = [1, 2, 3]
if c is d:
    print('same')
else:
    print('different')

name = "Python"
print(name[::-1][2])

# здесь в генераторе списков g это локальная переменная
g = 10
lst = [g for g in range(3)]
print(g)

h = 1
total = 0
while h < 4:
    total += h
    h += 1
print(total)




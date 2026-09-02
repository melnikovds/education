data = [5, 6, 7, 8]
gen = (x - 1 for x in data)
data[2] = 10
next(gen)
print(list(gen))

a = [1, 2, 3]
a.append([4,5])
print(len(a))

fruit = "mango"
if fruit == "apple":
    print("red fruit")
elif fruit == "banana":
    print("yellow fruit")
else:
    print("tropical fruit")

x = 5
y = 10
if x > 3:
    if y < 15:
        print("A")
    else:
        print("B")
else:
    print("C")

z = 7
if z % 2 == 0:
    print("even")
else:
    if z > 5:
        print("big")
    else:
        print("small")

g = 5
e = 3
if g > 4 and e < 5:
    print(g + e)
else:
    print(g)

h = 0
for i in range(5):
    if i == 2:
        continue
    h += i
print(h)







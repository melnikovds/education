a = ["Оля", "Иван", "Боб", "Даша"]
b = ["Иван", "Даша", "Макс"]

common = []
for x in a:
    if x in b:
        common.append(x)
print(common)

c = {"Оля", "Иван", "Боб", "Даша"}
d = {"Иван", "Даша", "Макс"}
e = sorted(c & d) #общие
f = sorted(c | d) #объединение
g = sorted(c - d) #только в c
h = sorted(c ^ d) #без общих
print(e)
print(f)
print(g)
print(h)


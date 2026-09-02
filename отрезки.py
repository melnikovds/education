# зачем перебирать весь список если в пайтон есть срезы
data = [1,4,5,4,3,2,5,67,54,32,34,56,78,65,43,17,87,80,90,98,97,76]
# data[start:end:step]

result = []
for i in range(5):
    result.append(data[i])

result_two = data[:5]
print(result_two)

every_second = data[::2]
print(every_second)






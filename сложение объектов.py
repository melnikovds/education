class Expense:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __add__(self, other):
        return self.cost + other.cost

# создаём два объекта класса
food = Expense("еда", 10)
fuel = Expense("бензин", 20)

# магический метод эдд для сложения объектов
print(food + fuel)




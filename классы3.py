class Cat:
    def __init__(self, name):
        self.name = name
    def meow(self):
        return f'{self.name} says: Meow!'

cat = Cat('Whiskers')
print(cat.meow())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (f"Person("
                f"name={self.name},"
                f" age={self.age})")

p1 = Person("Alice", 30)
print(p1)


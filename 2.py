from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")


# bob = Person("Bob", 30)
# print(bob)

try:
    bob = Person("Bob", -25, )
    print(bob)
except ValueError as e:
    print(e)




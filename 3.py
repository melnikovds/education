class Player:
    def __init__(self, name, health=100,
                 score=0):
        self.name = name
        self.health = health
        self.score = score


p1 = Player("BladeRunner")
p2 = Player("CodeNinja", health=150)

print(p1.name, p1.health)
print(p2.name, p2.health)




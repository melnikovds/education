scores = [90, 75, 60, 45]
best, *rest = scores
print(best, rest)
# бест забирает первый элемент а рест забирает весь хвост

base = {"тема": "тёмная"}
cfg = {**base, "шрифт": 14}
print(cfg)

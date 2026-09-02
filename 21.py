from collections import deque

signals = deque()

signals.append("BUY BTC")
signals.append("BUY ETH")
signals.append("BUY SOL")

print(signals)

print(signals.pop())

print(signals)

x = "123"
y = "abc"
print(x.isdigit())
print(y.isalpha())


name = input("Твоё имя: ")
if not name:
    name = "Аноним"
print(name)


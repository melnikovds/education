letters = [
    'т', 'а', 'к', ' ', 'д', 'е', 'л', 'а', 'т', 'ь', ' ', 'н', 'е', ' ', 'н', 'а', 'д', 'о'
]

print(type(letters))

def join_words(letters):
    s = ""
    for letter in letters:
        s += letter
    print(s)

join_words(letters)



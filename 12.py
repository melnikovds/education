d = {
    "apple": 1,
    "banana": 2,
    "orange": 3
}

# чтобы обратиться к ключу надо проверить существует ли такой ключ
# чтобы не поймать исключение
# if key in d:
#     x = d[key]

# или через блок трай-эксепт
def check_1(d, key):
    try:
        x = d[key]
    except KeyError:
        pass




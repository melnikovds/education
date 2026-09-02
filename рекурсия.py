# рекурсия это когда функция вызывает саму себя
# пока не дойдёт до базового случая


class Category:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)

    def __repr__(self):
        return self.name

# создаём дерево категорий
apple =  Category("apple")
iphone = Category("iphone", apple)
iphone17 = Category("iphone17", iphone)

# создаём функцию которая идёт вниз по категориям и собирает всех потомков
def get_children(cat):
    result = []
    for child in cat.children:
        result.append(child)
        result.extend(get_children(child))
    return result

# рекурсионный обход вложенных категорий на сайте
# создаём класс у которого есть имя, родитель и список детей
# когда создаём подкатегорию она сама добавляется в чилдрен родителя


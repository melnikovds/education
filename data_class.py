from dataclasses import dataclass, field

# дата классы это классы
# которые предназначены для хранения данных

@dataclass
class Person:
    first_name: str
    last_name: str
    # если нам нужно хранить и полные данные то мы можем добавить в параметр
    # full_name добавить init=False чтобы инициализировать эту штуку позже
    full_name: str = field(init=False)

    # постинициализатор
    def __post_init__(self):
        self.full_name = self.first_name + ' ' + self.last_name

man = Person(first_name='Дима', last_name='Билан')
print(man.full_name)


from faker import Faker
from russian_names import RussianNames

faker = Faker("ru_RU")

def name_cargo_place():
    return faker.words(nb=1)

title = name_cargo_place()
print(title)

def get_patronymic():
    # Генерируем одно ФИО
    full_name = RussianNames(count=1, patronymic=True).get_batch()[0]

    # Разбиваем ФИО на части: фамилия, имя, отчество
    parts = full_name.split()
    surname, name, patronymic = parts[0], parts[1], parts[2]

    # Возвращаем только отчество
    return patronymic


if __name__ == "__main__":
    # Получаем отчество
    patronymic = get_patronymic()
    print("Patronymic:", patronymic)
    print(type(patronymic))
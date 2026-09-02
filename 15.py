from pprint import pprint

sample_dict = {
    'name': 'Sion',
    'age': 20,
    'message': 'Thank you for reading this article',
    'topic':'Python Libraries'
}

# прэтти принт автоматически расставляет отступы и переносы
# чтобы более наглядно была видна структура данных
# есть настройка ограничения вложенности

print(sample_dict)
pprint(sample_dict)
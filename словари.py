from collections import defaultdict

# # если мы добавляем какое-то значение к ключу которого нет то будет ошибка KeyError
# d = {}
# d["dogs"].append("Rex")

# если ключа не было изначально то он создаётся
e = defaultdict(list)
e["dogs"].append("Rex")
e["dogs"].append("Max")
print(e["dogs"])






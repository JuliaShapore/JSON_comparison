# TODO здесь писать код
import json
from typing import Callable

# Десериализация JSON файлов
with open('json_old.json', 'r', encoding='UTF-8') as f:
    old_json = json.loads(f.read())
with open('json_new.json', 'r', encoding='UTF-8') as ff:
    new_json = json.loads(ff.read())

diff_list = ["services", "staff", "datetime"]
result_dict = {}


def find_key(struct: [dict, list], key_i: str) -> Callable:
    """
        Функция поиска значений по ключу.

    """
    result = None
    if key_i in struct:
        return struct[key_i]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key_i)
            if result:
                break

        if isinstance(sub_struct, list):
            result = find_key(sub_struct, key_i)
            if result:
                break

        else:
            result = None

    return result


# Ищем значения по ключу в 2-х JSON файлах
for key in diff_list:
    old_value = find_key(old_json, key)
    new_value = find_key(new_json, key)

# Заполняем словарь с изменениями
    if not old_value == new_value:
        result_dict[key] = new_value

# Сериализация JSON файла с результатом
with open('result.json', 'w', encoding='UTF-8') as fff:
    json.dump(result_dict, fff, ensure_ascii=False)



import random

def hash_function(array_size, element):
    """
    Вычисляет хеш-значение для элемента в пределах заданного размера массива.

    :param array_size: Размер массива (целое число)
    :param element: Элемент для хеширования (целое число или строка)
    :return: Хеш-значение (целое число)
    """
    if isinstance(element, int):
        # Если элемент - целое число, используем простое хеширование
        return element % array_size
    elif isinstance(element, str):
        # Если элемент - строка, используем более сложное хеширование
        hash_value = 0
        for char in element:
            hash_value = (hash_value * 31 + ord(char)) % array_size
        return hash_value
    else:
        raise ValueError("Элемент должен быть целым числом или строкой")

# Пример использования
array_size = 100
alpha = list("abcdefghijklmnopqrstuvwxyz")

results = [0 for _ in range(1000)]

for i in range(100000):
    random.shuffle(alpha)
    element = "".join(alpha)
    hash_value = hash_function(array_size, element)
    
    results[hash_value] += 1

results.sort()
print(results)
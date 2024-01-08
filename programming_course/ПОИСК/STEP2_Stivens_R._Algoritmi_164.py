# Линейный поиск
# Найти в данном списке число введенное пользователем
# сообщить, что число найденно,
# в противном случае, что не найдено
# судья - доп. балл за юзабилити прграммы
# судья - доп. балл за PEP 257 https://habr.com/ru/articles/499358/

import random


def list_generation():
    """Вернет список целых чисел в диапазоне от 0 до 99
    Количество элементов списка от 100 до 1000"""
    numbers_list = []
    amount_of_numbers = random.randint(100, 1000)
    for i in range(amount_of_numbers):
        numbers_list.append(random.randint(0, 99))
    return numbers_list


def linear_search(values, target):
    """Линейный алгоритм поиска для массива.
    Находим индекс целевого элемента в отсортированном массиве.
    Если элемента в массиве нет, возвращаем -1."""
    for i in range(len(values)):
    # Проверяем, является ли элемент целевым.
        if values[i] == target:
            return i

        # Проверяем, прошли ли мы возможную позицию целевого элемента.
        if values[i] > target:
            return -1
    # Если мы дошли до этой строки, то целевого элемента в массиве нет.
    return -1


if __name__ == '__main__':
    # ваш комментарий
    list_numbers = list_generation()
    print(list_numbers)

    search_number = int(input("Введите целое число, которое вы ищите:"))

    if linear_search(values, target) != 1:
        print()

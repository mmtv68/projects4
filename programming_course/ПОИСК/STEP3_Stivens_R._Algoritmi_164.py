# Линейный поиск
# Измените программу таким образом, чтобы она не только сообщила
# о наличии числа в списке, но и количестве вхождений
# Подсказка: использовать рекурсию

import random


def list_generation():
    """Вернет список целых чисел в диапазоне от 0 до 99
    Количество элементов списка от 100 до 1000"""
    numbers_list = []
    amount_of_numbers = random.randint(100, 1000)
    for i in range(amount_of_numbers):
        numbers_list.append(random.randint(0, 99))
    return numbers_list


def linear_search(values, target, start=0, number_of_occurrences = 0):
    """Линейный алгоритм поиска для массива.
    Находим индекс целевого элемента в отсортированном массиве.
    Если элемента в массиве нет, возвращаем -1."""
    for i in range(start, len(values)):
    # Проверяем, является ли элемент целевым.
        if values[i] == target:
            number_of_occurrences += 1
            return linear_search(values, target, i + 1,number_of_occurrences)
        # Проверяем, прошли ли мы возможную позицию целевого элемента.
        if values[i] > target:
            return number_of_occurrences
    # Если мы дошли до этой строки, то целевого элемента в массиве нет.
    return number_of_occurrences


if __name__ == '__main__':
    # ваш комментарий
    list_numbers = list_generation()
    list_numbers.sort()
    print(list_numbers)

    search_number = int(input("Введите целое число, которое вы ищите:"))
    number_of_occ = linear_search(list_numbers, search_number)
    if number_of_occ != 0:
        print("Число присутствует в списке",number_of_occ, "раз")
    else:
        print("Число отсутствует в списке")
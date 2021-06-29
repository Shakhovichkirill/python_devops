# Задание 1
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать
# явно, в программе.

a = ['string', 5, 6.37, True]
for i in a:
    print(type(i))

# Задание 2
# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

array = []
n = int(input("Введите кол-во элементов списка: "))
m = n - 1
while n >= 1:
    array.append(input("Введите элемент списка: "))
    n -= 1
for i, _ in enumerate(array):
    if i % 2 == 0 and i < m:
        array[i + 1], array[i] = array[i:i + 2]
print(array)

# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

dict = {
    'Зима': ['1', '2', '12'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']
}
list = [
    ['Зима', ['1', '2', '12']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]
month_num = input("Введите порядковый номер месяца в году [1-12]: ")
for i, y in list:
    if month_num in y:
        print(f'{month_num} - это {i}')
for i, y in dict.items():
    if month_num in y:
        print(f"{month_num} - {i}")

# Задание 4
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

str_1 = input("Введите строку: ")
words = []
n = 1

for i in range(str_1.count(' ') + 1):
    words = str_1.split()
    if len(str(words)) <= 10:
        print(f"{n} {words [i]}")
        n += 1
    else:
        print(f"{n} {words [i] [0:10]}")
        n += 1

# Задание 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

array_2 = [9, 4, 2, 2, 1]
print(f"{array_2}, 10 - закончить ввод элементов рейтинга)")
n = int(input("Введите элемент рейтинга: "))
g = array_2.count(n)
while n != 10:
    for i in array_2:
        if g > 0:
            i = array_2.index(n)
            array_2.insert(i + g, n)
            break
        else:
            if n > i:
                j = array_2.index(i)
                array_2.insert(j, n)
                break
            elif n < array_2[len(array_2) - 1]:
                array_2.append(n)
    print(array_2)
    n = int(input("элемент рейтинга: "))


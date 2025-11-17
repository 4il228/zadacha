numbers = input('Введите числа через пробел:')

numbers_split = numbers.split(' ')
#не выполнил вторую часть задания

#список получился со строковыми элементами, а должен быть с числовыми
# преобразуем список из строк в список из чисел
for i in range(len(numbers_split)):
    numbers_split[i] = int(numbers_split[i])
#Сейчас в списке numbers_split лежат готовые числа

#реши ниже оставшуюся часть задачи
"""
Из списка удаляются все числа меньшие 20.
Список сортируется по алфавиту.
Список печатается на экран.
"""
spisok = []
for number in numbers:
    if number >= 20:
        spisok.append(number)
    
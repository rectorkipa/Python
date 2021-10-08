# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
   str = (input('Введите строку: '))
   my_list.append(str)
   if str == '':
      break

with open("first_file.txt", "w") as my_file:
   for i in my_list:
      print(i, file=my_file)


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open("second_file.txt", "r")

content = my_file.readlines()

print('Количество строк в файле: ', len(content))

print('Количеств слов в каждой строке: ')

i = 0
for i in range(len(content)):
    print(len(content[i]))
    i += 1

my_file.close()


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_file = open("third_file.txt", "r", encoding='utf-8')

content = my_file.readlines()

print('Эти сотрудники имеют оклад менее 20000: ')

i = 0
my_list = []
fee_list = []
for i in range(len(content)):
    my_list.append(content[i].split(' '))
    fee_list.append(my_list[i][1])
    if float(my_list[i][1]) < 20000:
        print(my_list[i][0])
    i += 1

for i in range(len(fee_list)):
    fee_list[i] = float(fee_list[i])
    i += 1

print(f'Средняя величина дохода сотрудников: {sum(fee_list)/i:.2f}')

my_file.close()


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_file = open('fourth_file.txt', 'r')
content = my_file.readlines()

i = 0
my_list = []
for i in range(len(content)):
    my_list.append(content[i].split(' - '))
    i += 1

my_dict = {
    0: 'Один',
    1: 'Два',
    2: 'Три',
    3: 'Четыре'
}

i = 0
for i in range(len(my_list)):
    my_list[i][0] = my_dict[i]
    i += 1

i = 0
my_new_list = []
for i in range(len(my_list)):
    el = (' - '.join([my_list[i][0], my_list[i][1]]))
    my_new_list.append(el)
    i += 1

trans_file = open('fourth_file_trans.txt', 'w')
trans_file.writelines(my_new_list)

trans_file.close()

my_file.close()



# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('fifth_file.txt', 'w') as my_file:
    my_file.write(input('Введите набор чисел, разделенных пробелами: '))

with open('fifth_file.txt') as my_file:
    for line in my_file:
        my_list = line.split()
        for i, el in enumerate(my_list):
            my_list[i] = float(el)
        print('Сумма введенных чисел равна ', sum(my_list))


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

my_file = open('sixth_file.txt', 'r', encoding='utf-8')
content_1 = my_file.readline()
content_2 = my_file.readline()
content_3 = my_file.readline()

content_1_num = re.findall('(\d+)', content_1)
content_2_num = re.findall('(\d+)', content_2)
content_3_num = re.findall('(\d+)', content_3)

for i, el in enumerate(content_1_num):
    content_1_num[i] = int(el)
for i, el in enumerate(content_2_num):
    content_2_num[i] = int(el)
for i, el in enumerate(content_3_num):
    content_3_num[i] = int(el)

str_1 = content_1[:content_1.find(':')]
str_2 = content_2[:content_2.find(':')]
str_3 = content_3[:content_3.find(':')]

my_dict = {str_1: sum(content_1_num), str_2: sum(content_2_num), str_3: sum(content_3_num)}

print(my_dict)


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('seventh_file_json.json', 'w', encoding='utf-8') as write_f:
    with open('seventh_file.txt', encoding='utf-8') as f_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
        result = [profit, {'Средняя прибыль': round(sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)
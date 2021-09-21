# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))
tel_number = input('Напишите Ваш номер телеона: ')
print('Вас зовут', name, ', а Ваш возраст', age, 'лет. Очень приятно!')
print('Я сохранил Ваш номер телефона: ', tel_number)


# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_sec = int(input('Введите время в секундах: '))
time_min = time_sec // 60
time_sec = time_sec - 60 * time_min
time_hour = time_min // 60
time_min = time_min - 60 * time_hour
print(time_hour, 'часов')
print(time_min, 'минуты')
print(time_sec, 'секунды')
time_message = (
    f"{time_hour}:"
    f"{time_min}:"
    f"{time_sec}"
    )
print(time_message)
time_result = [str(time_hour), str(time_min), str(time_sec)]
print(f"Время: {':'.join(time_result)}")


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_n = int(input('Введите число n и увидите сумму n + nn + nnn: '))
number_nn = (2 * str(number_n))
number_nnn = (3 * str(number_n))
print(number_n + int(number_nn) + int(number_nnn))


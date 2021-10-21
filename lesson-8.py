# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    def __str__(self):
        return self.date_string

    @classmethod
    def extract_transform(cls, date):
        print(*map(int, date.date_string.split('-')))

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Верная дата'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

date = Date('04-07-1984')

print(date)

Date.extract_transform(date)

# Date.validate(*map(int, date.date_string.split('-')))
#
# year, month, day = map(int, date.date_string.split('-'))
# Date.validate(day, month, year)


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, text):
        self.text = text

a = float(input('Введите делимое: '))

b = float(input('Введите делитель: '))

def do_calc(a, b):
    try:
        if b == 0:
            raise MyError('Деление но ноль!')
        return a / b
    except MyError as e:
        print('Деление на ноль запрещено! Введите другой делитель')

# do_calc(a, b)
print(do_calc(a, b))


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам
# не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class MyListError:
    def __init__(self):
        self.elements = []

        n = int(input('Введите количество элементов в списке: '))

        print(f'Введите {n} чисел для формирования списка через Enter либо stop для предварительного завершения:')
        for i in range(n):
            try:
                a = input()
                a = float(a)
                self.elements.append(a)
            except:
                if a == 'stop':
                    return None
                else:
                    print('Введенное значение не является числом!')
        return None

my_list = MyListError()

my_list.elements

print(my_list.elements)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class EquipmentWarehouse:

    def __init__(self):
        self.equipment = {}

    def __str__(self):
        return f'{self.equipment}'

    def to_accept(self, eq_element):
        if eq_element.name in self.equipment:
            self.equipment[eq_element.name] += 1
        else:
            self.equipment[eq_element.name] = 1

    def to_give(self, eq_element):
        if eq_element.name in self.equipment:
            self.equipment[eq_element.name] -= 1
        else:
            print('Техники нет на складе')


class Equipment:
    def __init__(self, name, price, color):
        self.price = price
        if color not in ['Черно-белый', 'Цветной']:
            raise ValueError('Неверное значение параметра')
        else:
            self.color = color
        self.name = name


class Printer(Equipment):

    def __init__(self, name, price, color, paint):
        super().__init__(name, price, color)
        if paint < 0 or paint > 100:
            raise ValueError('Количество краски должно быть от 0 до 100%')
        else:
            self.paint = paint

    def to_print(self):
        return f'Это принтер - {self.name}'


class Scanner(Equipment):

    def __init__(self, name, price, color):
        super().__init__(name, price, color)

    def to_scan(self):
        return f'Это сканнер- {self.name}'


class Xerox(Equipment):

    def __init__(self, name, price, color):
        super().__init__(name, price, color)

    def to_copy(self):
        return f'Это ксерокс- {self.name}'

warehouse = EquipmentWarehouse()

p = Printer('HP', 100, 'Цветной', 100)
s = Scanner('Canon', 150, 'Черно-белый')
x = Xerox('Xerox', 200, 'Черно-белый')

warehouse.to_accept(p)
warehouse.to_accept(s)
warehouse.to_accept(x)

print(p.to_print())
print(s.to_scan())
print(x.to_copy())
print('--------------------')
print(warehouse)


# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + i*b'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)

    def __str__(self):
        return f'z = {self.a} + i*{self.b}'

a = ComplexNumber(-3, 10)
b = ComplexNumber(5, -1)
print(a)
print(a + b)
print(a * b)
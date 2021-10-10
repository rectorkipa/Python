# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time

class TrafficLight():
    __color = 'Синий'

    def running(self):
        print('Красный')
        time.sleep(7)
        print('Желтый')
        time.sleep(2)
        print('Зеленый')
        time.sleep(15)

a = TrafficLight()
a.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():

    def __init__(self):
        self.__length = 5000
        self.__width = 20

    def method(self):
        mass_per = input('Введите массу асфальта для покрытия одного кв метра дороги асфальтом толщиной в 1 см в кг (например, 25): ')
        thickness = input('Введите толщину полотна в см (например, 5): ')
        self.mass = self.__width * self.__length * int(mass_per) * int(thickness) / 1000
        return self.mass

a = Road()
print(f'Масса асфальта {a.method()} т')


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    name = 'Николай'
    surname = 'Кривоногов'
    position = 'Ламер'
    __income = {'wage': 66000, 'bonus': 33000}

class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')
    def get_total_income(self):
        print(f'Доход с учетом премии: ', self._Worker__income.get('wage') + self._Worker__income.get('bonus'))

position_1 = Position()
position_1.get_full_name()
position_1.get_total_income()


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    speed = 79
    color = 'white'
    name = 'Cops'
    is_police = True

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        self.direction = input('Введите направление поворота: ')
        print('Машина повернула:', self.direction)
    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)

class TownCar(Car):
    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)
        if self.speed > 60:
            print('Превышении скорости!')

class SportCar(Car):
    def sportcar_method(self):
        print('Это спортивная машина')

class WorkCar(Car):
    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)
        if self.speed > 40:
            print('Превышении скорости!')

class PoliceCar(Car):
    def policecar_method(self):
        print('Это полицейская машина')

a = TownCar()
b = SportCar()
c = WorkCar()
d = PoliceCar()

a.go()
a.turn('')
a.show_speed()
a.stop()

b.go()
b.turn('')
b.show_speed()
b.stop()

c.go()
c.turn('')
c.show_speed()
c.stop()

d.go()
d.turn('')
d.show_speed()
d.stop()


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    title = 'название'

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        print('Запуск отрисовки с помощью: ', self.title)

class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print('Запуск отрисовки с помощью: ', self.title)

class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print('Запуск отрисовки с помощью: ', self.title)

a = Pen()
b = Pencil()
c = Handle()

a.draw()
b.draw()
c.draw()
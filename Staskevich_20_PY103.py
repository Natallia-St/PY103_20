import random


# # Task1
# Задача № 1:
# 1. Создайте класс Counter
# 2. Задайте для него динамическое свойство count, которое по умолчанию будет равно 0
# 3. Определите для него метод next таким образом, чтобы при его вызове динамическое свойство count повышало свое значение на 1
# 4. Определите метод iter.
class Counter:
    def __init__(self, count=0):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        y = self.count
        self.count += 1
        return y


element = Counter(2)
print(next(element))
print(next(element))
print(next(element))

# Task2
# Задача № 2:
# 1. Создайте класс length
# 2. Определите для него методы call, next и iter таким образом,
# чтобы экземпляр класса мог посчитать количество символов объекта, переданных в него в качестве аргумента.
class Length:
    def __init__(self, *args):
        self.args = args


    def __call__(self):
        count = 0
        for i in self.args:
            for j in i:
                count += len(str(j))
                print(len(str(j)), j)

        return count


elem = [1, 33, "sdax"]
f = Length(elem)
print(f())


# Task 3
# Напишите функцию-генератор для перечисления последовательности фибоначчи.
class Fib:
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        return self

    def __next__(self):
        y1 = self.n1
        self.n1, self.n2 = self.n2, self.n2 + self.n1
        return y1


object = Fib()
element = (iter(object))
for i in range(6):
    print(next(element))

#Task4
class Card: # Объявление класса
    def __init__(self): # Инициализация класса и объявление динамических переменных
        self.descr_1 = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.descr_2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'J', 'Q', 'K', 'A']
        # Создания списка со всеми комбинациями карт
        self.all_comb = [[i, j] for i in self.descr_1 for j in self.descr_2]
        self.max_count = 52
        print(self.all_comb)

    def __iter__(self): #Объявление встроенного метода итератора
        self.count = 0 #Счетчик карт в колоде
        return self

    def __next__(self): #Объявление встроенного метода next
        if self.count <= self.max_count:
            take_card = random.choice(self.all_comb) #Рандомный выбор карты из колоды
            self.all_comb.remove(take_card)
            self.count += 1
            return take_card
        else: #Условие завершения итерации, если счетчик карт >52
            raise StopIteration


object = Card() #Создание объекта класса
element = (iter(object)) #Вызов метода iter и передача ему в качестве параметра объекта класса - создали итератор
for el in element: #Итеррирование по объекту
    print(el)



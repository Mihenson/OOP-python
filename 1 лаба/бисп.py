from pprint import pprint
import random

def func(list):
    summ = 0
    length = 0
    for i in list:
        summ += list(i)
        length += 1
    avg = summ/length #получаем среднее значение
    print(avg) #выводим его для наглядности
    res = [] #создаём пустой список для результата обработки массива
    for i in range(len(list)):
        if list[i] <= avg:
            res.append(list[i])
        if list[i] > avg and list[i] % 2 == 1:
            res.append(list[i]) #проверка элементов списка
    pprint(res)
print("рандом или ручками?")
a = input() #определяем способ ввода данных
if a == "рандом":
    print("Кол-во элементов =")
    n = int(input())
    spisok = [] #создаём список
    for i in range(n):
        spisok.append(random.randint(0, 10)) #заполняем список случайными значениями
    pprint(spisok) #выводим список заполненный случайными значениями
    func(spisok) #вызваем обработку списка

else:
    print("Элементы массива")
    sp = input() #получаем с ввода строку
    try:
        spisok = [int(i) for i in sp.split()] #создаём и заполняем список элементами из разбитой по пробелам строки
        func(spisok) #вызваем обработку списка
    except ValueError as ve:
        spisok = [1]
        print("Надо вводить числа!!")
from random import randint
import numpy as np


print("Введите N:")
n = int(input())
print("Введите M:")
m = int(input())
a = np.array([[randint(1, 10) for j in range(m)] for i in range(n)]) # создаём и заполняем матрицу случайными значениями
with open("file.txt", 'w') as output: # открываем файл для записи
    output.write("До:" + '\n') #чтобы было понятно
    for i in a:
        output.write(str(i) + '\n') #чтобы было понятно выводим исходную матрицу
    output.write("После:" + '\n') #чтобы было понятно
    for i in range(n):
        max=a[i][0]
        for j in range(m):
            if a[i][j] > max:
                max = a[i][j]
        output.write(str(a[i]/max) + '\n') #выводим обработанную матрицу



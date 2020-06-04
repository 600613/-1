import random

# Создание одномерного массива рандомных чисел
a_arr = [random.randint(1, 10) for _ in range(10)]
print(a_arr)

# Добавление в массив n рандомных чисел
N = int(input('Введите количество рандомных чисел для добавления в массив '))
A = 0;
while A < N:
    a_arr.append(random.randint(1, 10))
    A = A + 1
print(a_arr)

# Рандомно перемешиваем массив
random.shuffle(a_arr)
print(a_arr)
"""Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро)."""

from random import randint

a = randint(0, 36)
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36]
blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35]

if a == 0:
    print('Выпало "Зеро"')
else:
    if a in reds:
        print(f'Выпало {a} красное')
    else:
        print(f'Выпало {a} черное')
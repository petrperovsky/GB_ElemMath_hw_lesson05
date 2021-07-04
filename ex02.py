"""Напишите код, проверяющий любую из теорем сложения или умножения
вероятности на примере рулетки или подбрасывания монетки."""

from random import randint

numbers = []
for i in range(1000):
    a = randint(0, 36)
    numbers.append(a)

probabilities = []
for i in range(37):
    probability_i = numbers.count(i) / 1000
    probabilities.append(probability_i)

print(f'Вероятность выпадения всех чисел в рулетке при 1000 ставках: {sum(probabilities): .2f}')

"""Сгенерируйте десять выборок случайных чисел х0, …, х9.
и постройте гистограмму распределения случайной суммы  +х1+ …+ х9."""

import numpy as np
import matplotlib.pyplot as plt

allsums = []
for i in range(11):
    x = np.random.rand(10)
    allsums.append(sum(x))
num_bins = 10
n, bins, patches = plt.hist(allsums, num_bins)
plt.xlabel('summa')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()

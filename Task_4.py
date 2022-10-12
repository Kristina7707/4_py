# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
from random import randint

k = int(input('Введите степень полинома к:'))
ratios = [randint(0,10)for i in range(k+1)]
print(ratios)

terms = []
for ratio in ratios:
    if ratio:
        ratio = ratio if k == 0 else '' if ratio == 1 else ratio
        power = 'x' if k == 1 else '' if k == 0 else f'x^{k}'
        term = f'{ratio}{power}'
        terms.append(term)

    k -= 1
polynom = ' + '.join(terms) + ' = 0'
print(polynom)

result_dir = 'files'
if not os.path.exists(result_dir):
    os.mkdir(result_dir)

with open(f'{result_dir}\\{"_".join(map(str, ratios))}.txt', 'w', encoding='utf-8') as file:
    file.write(polynom)
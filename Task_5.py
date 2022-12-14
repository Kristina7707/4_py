# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import numpy as np
from sympy import Symbol, expand
import sympy


def read_file(file):
    with open(str(file)) as data:
        tmp = data.read()
    return tmp


file1 = 'Polynomial1.txt'
file2 = 'Polynomial2.txt'

poly1 = read_file(file1).replace(' = 0', '')
poly2 = read_file(file2).replace(' = 0', '')
my_poly1 = sympy.polys.polytools.poly_from_expr(poly1)[0]
my_poly2 = sympy.polys.polytools.poly_from_expr(poly2)[0]

print(my_poly1, my_poly2)

polysum = my_poly1+my_poly2
print(polysum.as_expr())
with open('Polynomial-sum.txt', 'w') as data:
    data.write(str(polysum.as_expr()).replace('**', '^')+' = 0')
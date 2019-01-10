"""
Karl Michel Koerich , 1631968
Friday , February 22, 2018
R. Vincent , instructor
Assignment 1
"""

#polytest.py

from ex1_Karl_a1 import Polynomial

#Basic Tests

poly1 = Polynomial([1, 2, 3])
poly2 = Polynomial()
poly3 = Polynomial([1, 2, 3])
poly4 = Polynomial([0, 0, 0, 3, -90, 0, 11, 0, 0, 0, 34])
poly5 = Polynomial([1, 2, 3])
poly6 = Polynomial([-1, -2, -3])
poly7 = poly5 + poly6

assert poly1.degree() == 2
assert poly2.degree() == -1
assert poly1 == poly3
assert poly4.degree() == 10
assert poly7 == poly2
assert poly7.degree() == -1

#Ask questions about encapsulation and tests






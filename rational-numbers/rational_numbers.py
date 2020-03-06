from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.numer = self.order_signs().simplify().numer
        self.denom = self.order_signs().simplify().denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        self.numer = self.numer * other.denom + other.numer * self.denom
        self.denom = self.denom * other.denom
        return self.order_signs().simplify()

    def __sub__(self, other):
        self.numer = self.numer * other.denom - other.numer * self.denom
        self.denom = self.denom * other.denom
        return self.order_signs().simplify()

    def __mul__(self, other):
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom
        return self.order_signs().simplify()

    def __truediv__(self, other):
        self.numer = self.numer * other.denom
        self.denom = self.denom * other.numer
        return self.order_signs().simplify()

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return self.order_signs().simplify()

    def __pow__(self, power):
        self.numer = self.numer ** power
        self.denom = self.denom ** power
        return self.order_signs().simplify()

    def __rpow__(self, base):
        return (base ** self.numer) ** (1/self.denom)

    def simplify(self):
        agcd = gcd(self.numer, self.denom)
        self.numer = self.numer // agcd
        self.denom = self.denom // agcd
        return self

    def order_signs(self):
        if(self.denom < 0):
            self.numer = -1 * self.numer
            self.denom = -1 * self.denom
        return self
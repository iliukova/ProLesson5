import math
class Rational:
    def __init__(self, n: int, d: int):
        if not isinstance(n, int):
            raise TypeError('Numerator must be integer number')
        if not isinstance(d, int):
            raise TypeError('Denominator must be integer number')
        if not d:
            raise ZeroDivisionError('Denominator can`t be zero')
        self.n = n
        self.d = d

    def __eq__(self, other):
        k = math.gcd(self.n, self.d)
        self.n //= k
        self.d //= k

        k = math.gcd(other.n, other.d)
        other.n //= k
        other.d //= k
        return (self.n, self.d) == (other.n, other.d)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.n / self.d < other.n / other.d

    def __gt__(self, other):
        return self.n / self.d > other.n / other.d

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        d = self.d * other.d                #calculation common denominator
        n = d // self.d * self.n - \
            d // other.d * other.n          #calculation numerator`s difference
        return Rational(n, d)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        d = self.d * other.d
        n = d // self.d * self.n - \
            d // other.d * other.n
        return Rational(n, d)

    def __isub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        sign = 1 if self.n * self.d > 0 else -1

        d = abs(self.d) * abs(other.d)
        n = d // abs(self.d) * abs(self.n) -\
            d // abs(other.d) * abs(other.n)
        self.n = sign * n
        self.d = d
        return self

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        d = self.d * other.d  # calculation common denominator
        print ('d=', d)
        n = d // self.d * self.n + \
            d // other.d * other.n  # calculation numerator`s sum
        print ('n =', n)

        k = math.gcd(d, n)
        d //= k
        n //= k
        return Rational(n, d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        d = self.d * other.d  # calculation common denominator
        n = self.n * other.n  # calculation common numerator

        k = math.gcd(d, n)
        d //= k
        n //= k
        return Rational(n, d)

    def __str__(self):
        sign = '' if self.n * self.d >= 0 else '-'
        n, d = abs(self.n), abs(self.d)
        k = math.gcd(n, d)
        n //= k
        d //= k

        if n == d:
            return f'{sign}1'
        if d == 1:
            return f'{sign}{n}'
        if n > d:
            return f'{sign}{n // d} {n - n // d * d} / {d}'
        return f'{sign}{n} / {d}'

x1 = Rational(5, 2)
x2 = Rational(3, 4)
print(x1 == x2)         #__eq__
print(x1 != x2)         #__ne__
print(x1 < x2)          #__lt__
print(x1 > x2)          #__gt__
print(x1-x2)            #__sub__
print(x2-x1)            #__rsub__
print(x1-x2)            #__isub__
print(x1+x2)            #__add__
print(x1*x2)            #__mul__
import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        res = Complex(self.real + no.real, self.imaginary + no.imaginary)
        return res.__str__()

    def __sub__(self, no):
        res = Complex(self.real - no.real, self.imaginary - no.imaginary)
        return res.__str__()

    def __mul__(self, no):
        res = Complex((self.real * no.real - self.imaginary * no.imaginary),
                      (self.real * no.imaginary + self.imaginary * no.real))
        return res.__str__()

    def __truediv__(self, no):
        res_real = (self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        res_img = (self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        res = Complex(res_real, res_img)
        return res.__str__()

    def mod(self):
        res = Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)
        return res.__str__()

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


c = list(map(float, input().split()))
d = list(map(float, input().split()))
C = Complex(c[0], c[1])
D = Complex(d[0], d[1])
print(C)
print(D)
print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(C.mod())
print(D.mod())

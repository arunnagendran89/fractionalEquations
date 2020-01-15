from functools import reduce
from operator import mul

class FractionalOperand:
    def __init__(self, operandString = ""):
        self.whole = 0
        self.numerator = 0
        self.denominator = 1
        if operandString:
            self.parse(operandString)
            if self.denominator == 0:
                raise Exception
        else:
            self.__minified()

    def __str__(self):
        res = ""
        isUnderscore = False
        if self.whole != 0:
            res += str(self.whole)
            isUnderscore = True
        if self.numerator > 0:
            if isUnderscore:
                res += '_'
            res += str(self.numerator) + "/" + str(self.denominator)
        return res or '0'

    def parse(self, operandString):
        if '_' in operandString:
            self.whole, fraction = operandString.split('_')
            self.whole = int(self.whole)
            self.numerator, self.denominator = fraction.split('/')
        elif '/' in operandString:
            self.whole = 0
            fraction = operandString
            self.numerator, self.denominator = fraction.split('/')
        else:
            self.whole = int(operandString)
            self.numerator = 0
            self.denominator = 1
        if str(self.denominator) == '0':
            raise Exception
        self.numerator = int(self.numerator)
        self.denominator = int(self.denominator)
        self.__minified()

    def __primefactors(self, n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def __reduceFractions(self):
        nFactors = sorted(self.__primefactors(self.numerator))
        dFactors = sorted(self.__primefactors(self.denominator))
        i, j = 0, 0
        while i < len(nFactors) and j < len(nFactors):
            if nFactors[i] == dFactors[j]:
                nFactors[i] = dFactors[j] = 1
                i += 1
                j += 1
            elif nFactors[i] > dFactors[j]:
                j += 1
            elif nFactors[i] < dFactors[j]:
                i += 1
        self.denominator = dFactors and reduce(mul, dFactors, 1) or self.denominator
        self.numerator = nFactors and reduce(mul, nFactors, 1) or self.numerator

    def __minified(self):
        self.numerator = self.whole*self.denominator + self.numerator
        self.whole = self.numerator//self.denominator
        self.numerator = self.numerator - self.whole*self.denominator
        self.__reduceFractions()

    def add(self, operand2):
        self.whole = self.whole + operand2.whole
        self.numerator = self.numerator*operand2.denominator + self.denominator * operand2.numerator
        self.denominator = self.denominator*operand2.denominator
        self.__minified()

    def subtract(self, operand2):
        self.whole = self.whole - operand2.whole
        self.numerator = self.numerator * operand2.denominator - self.denominator * operand2.numerator
        self.denominator = self.denominator * operand2.denominator
        self.__minified()

    def multiply(self, operand2):
        self.numerator = self.whole * self.denominator + self.numerator
        self.whole = 0
        operand2.numerator = operand2.whole * operand2.denominator + operand2.numerator
        operand2.whole = 0
        self.numerator *= operand2.numerator
        self.denominator *= operand2.denominator
        self.__minified()

    def divide(self, operand2):
        self.numerator = self.whole * self.denominator + self.numerator
        self.whole = 0
        operand2.numerator = operand2.whole * operand2.denominator + operand2.numerator
        operand2.whole = 0
        if operand2.numerator == 0:
            raise Exception
        self.numerator *= operand2.denominator
        self.denominator *= operand2.numerator
        self.__minified()


if __name__ == '__main__':
    operand1 = FractionalOperand("11_101/4")
    operand2 = FractionalOperand("0/4")
    print(operand1)
    print(operand2)
    operand1.divide(operand2)
    print(operand1)

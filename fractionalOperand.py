class FractionalOperand:
    """
    Class to objectify fractional operand strings.
    Parameterize the whole number, numerator and denominator of a fractional operand.
    Format is <wholeNumber><underscore><numerator><forward slash><denominator>
    valid examples:
    3_1/4
    -3_1/4
    3
    -3
    -1/4
    1/4
    """
    def __init__(self, operandString = ""):
        """
        :param operandString: String containing whole number and fraction parts.
        """
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
        """
        Return string representation of this object.
        Format is <wholeNumber><underscore><numerator><forward slash><denominator>
        :return:
        """
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
        """
        Parse the input string to class parameters.
        Note that the input could be only whole number / regular fractions / irregular fractions.
        :param operandString: string representation of the operand
        """
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

    def __gcd(self, x, y):
        """
        Internal helper function to find the
        Greatest Common Divisor of two numbers. Implemented using Euclid's algorithm
        :param x, y: The two input numbers for which GCD is computed.
        :return: GCD for the two numbers.
        """
        x = abs(x)
        y = abs(y)
        if x > y:
            x, y = y, x
        while x > 0:
            temp = x
            x = y % x
            y = temp
        return y

    def __reduceFractions(self):
        """
        Convert fraction to irreducible form.
        eg:
        4/2 = 2/1
        8/6 = 4/3
        """
        gcd = self.__gcd(self.denominator, self.numerator)

        self.denominator = self.denominator // gcd
        self.numerator = self.numerator // gcd

    def __minified(self):
        """
        1. Convert irregular fractions to mixed fractions.
        2. Convert fractions to irreducible form.
        :return: minified fraction operand
        """
        isNegative = False
        if self.whole < 0:
            isNegative = True
            self.whole *= -1
        self.numerator = self.whole*self.denominator + self.numerator
        self.whole = self.numerator//self.denominator
        self.numerator = self.numerator - self.whole*self.denominator
        self.__reduceFractions()
        if isNegative:
            self.whole *= -1

    def add(self, operand2):
        """
        Subtract this fractional operand to another fractional operand.
        a_b/c subtract d_e/f
        = ((c * a + b) * f + c* (d * f + e)) / (c * f)
        :param operand2: operand to be added to self. should be of type FractionalOperand
        :return: Nothing. Sum is saved in self operand
        """
        self.whole = self.whole + operand2.whole
        self.numerator = self.numerator*operand2.denominator + self.denominator * operand2.numerator
        self.denominator = self.denominator*operand2.denominator
        self.__minified()

    def subtract(self, operand2):
        """
        Subtract this fractional operand to another fractional operand.
        a_b/c subtract d_e/f
        = ((c * a + b) * f - c* (d * f + e)) / (c * f)
        :param operand2:
        :return: Nothing. Difference is stored in self operand
        """
        self.whole = self.whole - operand2.whole
        self.numerator = self.numerator * operand2.denominator - self.denominator * operand2.numerator
        self.denominator = self.denominator * operand2.denominator
        self.__minified()

    def multiply(self, operand2):
        """
        Multiply this fractional operand to another fractional operand.
        a_b/c multiply d_e/f
        = ((c * a + b) * (d * f + e)) / (c * f)
        :param operand2:
        :return: Nothing. Product of the two operands is stored in self operand
        """
        self.numerator = self.whole * self.denominator + self.numerator
        self.whole = 0
        operand2.numerator = operand2.whole * operand2.denominator + operand2.numerator
        operand2.whole = 0
        self.numerator *= operand2.numerator
        self.denominator *= operand2.denominator
        self.__minified()

    def divide(self, operand2):
        '''
        Divide this fractional operand by another fractional operand.
        a_b/c divide d_e/f
        = (c*a + b) *f / (c *(d*f + e))
        :param operand2:
        :return: Nothing. Quotient and partition of the division operation is stored in self operand
        '''
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
    operand1 = FractionalOperand("-11_101/4")
    operand2 = FractionalOperand("4/4")
    print(operand1)
    print(operand2)
    operand1.divide(operand2)
    print(operand1)

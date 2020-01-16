from fractionalOperand import FractionalOperand

class FractionEquation:
    """
    Solver for fractional equations of the form:
    operand1<white spaces>operator<white spaces>operand2
    eg:
    '5/2  * 3_3/4'
    '2 / 4/3'
    '3_1/4 + 5/6'
    '-5_1/9 - -3/4'

    Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
    Operands and operators shall be separated by one or more spaces
    Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"
    Improper fractions and whole numbers are also allowed as operands
    """
    def __init__(self, equation = ""):
        """
        Initialize with the input equation
        :param equation: input equation of fractions with arithmetic operations.
                         should be a string
        """
        if not isinstance(equation, str):
            raise Exception
        self.equation = equation

    def solve(self):
        """
        solve the arithmetic equation of fractional operands and returns a resultant fractional operand.
        format of equation described in class description
        :return: string representation of resultant fraction
        """
        operand1Str, operatorStr, operand2Str = self.equation.split()
        print(operand1Str, operatorStr, operand2Str)
        operand1 = FractionalOperand(operand1Str)
        operand2 = FractionalOperand(operand2Str)
        if operatorStr == '+':
            operand1.add(operand2)
        elif operatorStr == '-':
            operand1.subtract(operand2)
        elif operatorStr == '*':
            operand1.multiply(operand2)
        elif operatorStr == '/':
            operand1.divide(operand2)
        else:
            raise Exception
        return str(operand1)


if __name__ == '__main__':
    print(FractionEquation('5/2                * 3_3/4').solve())
    print(FractionEquation('5/2 + 3_3/4').solve())
    print(FractionEquation('-5/2 -                     -3_3/4').solve())
    print(FractionEquation('5/2 / 30_3/40000000000000').solve())

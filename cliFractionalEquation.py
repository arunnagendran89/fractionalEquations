from fractionalEquation import FractionEquation
from exceptions import *


class CLIFractionalEquationSolver:
    def _help(self):
        return """
        Fraction Equation Solver
        
        Menu:
        Press Q to quit
        Press H to display this help menu
        
        """ + self._help_input()

    def _help_input(self):
        return """
        
        Input rules:
        1. Input the equation in the format operand1<white spaces>operator<white spaces>operand2
        2. Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
        3. Operands and operators should be separated by one or more spaces
        
        Example inputs:
        '5/2  * 3_3/4'
        '2 / 4/3'
        '3_1/4 + 5/6'
        '-5_1/9 - -3/4'
        """

    def _display(self, result):
        print('= ', result)

    def run(self):
        print(self._help())
        while True:
            val = input('? ')
            if val == 'q' or val == 'Q':
                print('Good bye!')
                exit(0)
            if val == 'h' or val == 'H':
                print(self._help())
            else:
                try:
                    fractionalEquation = FractionEquation(val.strip())
                    self._display(fractionalEquation.solve())
                except (ValueError, InvalidInputType) as e:
                    print('Invalid input!', e)
                    print(self._help_input())
                except (ZeroDenominatorException, ZeroDivisionError) as e:
                    print('Zero cannot be denominator. When dividing, the dividend cannot have zero numerator', e)
                except InvalidOperator as e:
                    print(self._help_input())
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    CLIFractionalEquationSolver().run()


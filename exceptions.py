class ZeroDenominatorException(Exception):
    def __init__(self):
        Exception.__init__(self, "Denominator cannot be zero!")


class InvalidInputType(Exception):
    def __init__(self):
        Exception.__init__(self, "Input type should be string!")


class InvalidOperator(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid operator! use one of + - * or / .")


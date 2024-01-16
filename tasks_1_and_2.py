import math


class Factorial:
    @classmethod
    def factorial(cls, number):
        if number < 0:
            raise ValueError('Only positive numbers.')
        if number == 0 or number == 1:
            return 1
        else:
            return math.factorial(number)


print(Factorial.factorial(5))


class Reverse:
    @classmethod
    def reverse_string(cls, sentence):
        return sentence[::-1]


print(Reverse.reverse_string('Today is a good day'))

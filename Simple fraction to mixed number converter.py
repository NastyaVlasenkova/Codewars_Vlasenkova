'''
5 kyu
Name: Simple fraction to mixed number converter
https://www.codewars.com/kata/556b85b433fb5e899200003f
Task: Учитывая строку, представляющую простую дробь x/y, ваша функция должна возвращать строку,
представляющую соответствующую смешанную дробь в следующем формате:
[sign]a b/c
'''


import fractions
import math
def mixed_fraction(string):
    numbers = [int(i) for i in string.split('/')]
    numbers = fractions.Fraction(numbers[0],numbers[1])
    if numbers.numerator > 0 and numbers.denominator > 0:
        quotient = str(int(math.floor(numbers)))
    else:
        quotient = str(int(math.ceil(numbers)))
    numbers = [numbers.numerator,numbers.denominator]
    remainder = str(int(math.fmod(numbers[0],numbers[1])))
    print(numbers)
    if remainder == "0":
        return quotient
    elif quotient == "0":
        return remainder + "/" + str(numbers[1])
    elif numbers[0] == 0:
        return "0"
    elif int(quotient) < 0 and int(remainder) < 0:
        return quotient + " " + str(abs(int(remainder))) + "/" + str(numbers[1])
    else:
        return quotient + " " + remainder + "/" + str(numbers[1])
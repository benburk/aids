"""Demonstrate how to synthesize other operations from subleq.
This program demonstrates that you can write the bit operators AND, OR and XOR
in terms of the subtract and branch if equal or lower (subleq) operator.
https://en.wikipedia.org/wiki/One_instruction_set_computer

https://stackoverflow.com/questions/2982729/is-it-possible-to-implement-bitwise-operators-using-integer-arithmetic
"""
import random


def my_sub(minuend: int, subtrahend: int) -> int:
    return minuend - subtrahend


def my_leq(left_side: int, right_side: int) -> bool:
    return left_side <= right_side


# now we write all other functions in terms of the above two functions


def my_add(augend: int, addend: int) -> int:
    return my_sub(augend, my_sub(0, addend))


def my_mul(multiplier: int, multiplicand: int) -> int:
    product = 0
    while my_leq(1, multiplicand):
        product = my_add(product, multiplier)
        multiplicand = my_sub(multiplicand, 1)
    return product


def my_div(dividend: int, divisor: int) -> int:
    quotient = 0
    while my_leq(divisor, dividend):
        quotient = my_add(quotient, 1)
        dividend = my_sub(dividend, divisor)
    return quotient


def my_mod(dividend: int, divisor: int) -> int:
    while my_leq(divisor, dividend):
        dividend = my_sub(dividend, divisor)
    return dividend


def my_and(arg1: int, arg2: int) -> int:

    result = 0
    d = 1

    while my_leq(1, my_mul(arg1, arg2)):

        # we look at the first bit of a and b by checking if the number is odd or even
        # for this we use the modulo operator (a mod 2 and b mod 2)
        # this results in a 1 if the number is odd (which means the first bit is 1)
        # and 0 if the number is even (which means the first bit is 0)
        # multiplying those two numbers gives the and-operator for the first bit of a and b
        # the other bits are handled by bit-shifting a and b
        # this is equivalent to multiplying (left-shift) or dividing (right-shift) by 2

        result = my_add(result, my_mul(my_mul(my_mod(arg1, 2), my_mod(arg2, 2)), d))
        d = my_mul(d, 2)
        arg1 = my_div(arg1, 2)
        arg2 = my_div(arg2, 2)

    return result


def my_or(arg1: int, arg2: int) -> int:
    result = 0
    d = 1
    while my_leq(1, my_add(arg1, arg2)):
        if my_leq(1, my_add(my_mod(arg1, 2), my_mod(arg2, 2))):
            result = my_add(result, d)
        d = my_mul(d, 2)
        arg1 = my_div(arg1, 2)
        arg2 = my_div(arg2, 2)
    return result


def my_xor(arg1: int, arg2: int) -> int:
    result = 0
    d = 1
    while my_leq(1, my_add(arg1, arg2)):
        e = my_add(my_mod(arg1, 2), my_mod(arg2, 2))
        if my_leq(e, 1):
            result = my_add(result, my_mul(e, d))
        d = my_mul(d, 2)
        arg1 = my_div(arg1, 2)
        arg2 = my_div(arg2, 2)
    return result


def test(arg1: int, arg2: int) -> None:
    assert arg1 & arg2 == my_and(arg1, arg2)
    assert arg1 | arg2 == my_or(arg1, arg2)
    assert arg1 ^ arg2 == my_xor(arg1, arg2)


for _ in range(1000):
    test(random.randint(0, 1024), random.randint(0, 1024))

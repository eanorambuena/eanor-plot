import math

def is_integer(x):
    return type(x) is int

def is__positive(x):
    return x > 0

def is_negative(x):
    return x < 0

def is_real(x):
    return type(x) in [int, float]

def Constant1(x):
    return 1

def x(y):
    return y

def symmetric_strip(string, chars = "()"):
    def string_balance(string):
        # if first "(" appears after first ")", then it's not balanced
        # else it's balanced
        first_open = string.find(chars[0])
        first_close = string.find(chars[1])
        return not (first_open > first_close)

    while (string[0] == chars[0]) and (string[-1] == chars[-1] and string_balance(string)):
        new_string = string[1:-1]
        if not string_balance(new_string):
            break
        string = new_string

    return string
    
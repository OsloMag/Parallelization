import numpy as np

def primeCheck(number):
    """ return True if the number is prime, else return False """
    if number % 2 == 0 and number != 2:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
        return True
    
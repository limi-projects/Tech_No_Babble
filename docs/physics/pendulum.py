# TO DO: Create a database of equations. Incorportate this into a general function. 
from equations import evaluate_equation# See limi-utils
def pendulum(get: str, given: dict, stdout=True, pretty=True) -> float:
    equation = 'T - 2 * pi * (L/g)**0.5'
    result = evaluate_equation(equation, get, given, stdout, pretty)
    return result

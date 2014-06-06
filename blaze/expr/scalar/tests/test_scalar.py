from blaze.expr.scalar import *
import math

x = NumberSymbol('x')
y = NumberSymbol('y')

def test_basic():
    expr = (x + y) * 3

    assert eval(str(expr)) == expr
    assert expr == Mul(Add(NumberSymbol('x'), NumberSymbol('y')), 3)


def test_eval_str():
    expr = (x + y) * 3
    assert expr.eval_str() == '(x + y) * 3'

    assert eval_str(1) == '1'
    assert eval_str('Alice') == "'Alice'"


def test_str():
    x = NumberSymbol('x', 'real')

    assert str(x + 10) == 'x + 10'

def ishashable(x):
    try:
        hash(x)
        return True
    except:
        return False

def test_NumberSymbol_is_hashable():
    assert ishashable(x)

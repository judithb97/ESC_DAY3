def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    
def subtract(a, b):
    return a - b  # <--- fix this 


# uncomment the following test
def test_subtract():
    assert subtract(2, 3) == -1

#1
def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial():
    assert abs(factorial(5) - 5*4*3*2*1) < 1e-6

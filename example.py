import pytest

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
    with pytest.raises(ValueError) as e:
        factorial(-2)
    assert str(e.value) == 'received negative input'

    
# 2
def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

def test_count_word_occurence_in_string():
    assert count_word_occurence_in_string("test for the word word, it is there twice", "word") == 2
    assert count_word_occurence_in_string("test for the word word, it is there twice", "cat") == 0

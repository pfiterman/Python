import tests_methods
import pytest

def test_add():
    assert tests_methods.add(4, 5) == 9

def test_sub():
    assert tests_methods.sub(4, 5) == -1
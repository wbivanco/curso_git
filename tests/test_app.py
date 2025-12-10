from app.utils import greet


def test_greet_name():
    assert greet("Walter") == "Hola, Walter!"


def test_greet_empty():
    assert greet("") == "Hola, GitHub!"

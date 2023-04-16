# https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file
# pytest -v  test_main.py::test_read_and_print_string
import pytest

from lista_de_exercicios.utilidades.utils import *


def test_get_string_length():
    assert get_string_length("hello") == 5
    assert get_string_length("") == 0
    assert get_string_length("こんにちは世界") == 7
    assert get_string_length("Python is awesome") == 17


# The capsys fixture provided by Pytest allows us to capture stdout output during the execution of our test function. We use this fixture to capture the output of our read_and_print_string function.
def test_read_and_print_string(capsys):
    input_str = "Hello, world!"
    expected_output = "Hello, world!"

    # Use the `capsys` fixture to capture stdout output
    # during function execution
    captured_output = capsys.readouterr()

    # Call the function
    result = read_and_print_string(input_str)

    # Check that the function returns the input string
    assert result == expected_output

    # Check that the function prints the input string
    assert captured_output.out == input_str + "\n"

# test_count_ones.py


def test_count_ones():
    assert count_ones("") == 0
    assert count_ones("hello world") == 0
    assert count_ones("1") == 1
    assert count_ones("111001011") == 6


def test_print_name_if_starts_with_a(capsys):
    # Case 1: Name starts with 'a' in lowercase
    print_name_if_starts_with_a('alice')
    captured = capsys.readouterr()
    assert captured.out == 'alice\n'

    # Case 2: Name starts with 'a' in uppercase
    print_name_if_starts_with_a('Alice')
    captured = capsys.readouterr()
    assert captured.out == 'Alice\n'

    # Case 3: Name does not start with 'a'
    print_name_if_starts_with_a('bob')
    captured = capsys.readouterr()
    assert captured.out == ''


def test_remove_spaces():
    assert remove_spaces('hello world') == [
        'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    assert remove_spaces('the quick brown fox') == [
        't', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'o', 'x']


# undone
def test_read_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Alice')
    monkeypatch.setattr('builtins.input', lambda _: '25')
    monkeypatch.setattr('builtins.input', lambda _: 'Bob')
    monkeypatch.setattr('builtins.input', lambda _: '35')
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    assert read_input() == [('Alice', 25), ('Bob', 35)]


def test_sort_data():
    data = [('Alice', 25), ('Bob', 35), ('Charlie', 30)]
    assert sort_data(data) == [('Alice', 25), ('Charlie', 30), ('Bob', 35)]

#undone
def test_car_consumption(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'ausca')
    monkeypatch.setattr('builtins.input', lambda _: '1')
    monkeypatch.setattr('builtins.input', lambda _: 'Bob')
    monkeypatch.setattr('builtins.input', lambda _: '35')
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    assert car_consumption() == []
    #assert car_consumption() == [('ausca', 1.0, 1000.0), ('Bob', 35.0, 35000.0)]

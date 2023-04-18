# https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file
# pytest -v  test_main.py::test_read_and_print_string
from io import StringIO
import sys
import io
from unittest.mock import patch

import pytest

from lista_de_exercicios.utilidades.utils import *

# 1


def test_read_and_print_string(monkeypatch, capsys):
    # Prepare test input
    input_str = "Hello, world!"
    monkeypatch.setattr('builtins.input', lambda _: input_str)

    # Call the function
    result = read_and_print_string()

    # Check the output and return value
    assert result == input_str
    captured = capsys.readouterr()
    assert captured.out.strip() == input_str

# 2


def test_get_string_length():
    assert get_string_length("hello") == 5
    assert get_string_length("") == 0
    assert get_string_length("こんにちは世界") == 7
    assert get_string_length("Python is awesome") == 17

# 3


def test_count_ones_in_a_string():
    assert count_ones("") == 0
    assert count_ones("hello world") == 0
    assert count_ones("1") == 1
    assert count_ones("111001011") == 6

# 4


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

# 5


def test_remove_spaces_of_a_vector_and_return_it():
    assert remove_spaces('hello world') == [
        'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    assert remove_spaces('the quick brown fox') == [
        't', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'o', 'x']


# test_read_input.py
# 6
def test_read_input_and_when_a_negative_value_is_entered_the_program_must_stop_and_return_the_ages_sorted(monkeypatch):
    # Prepare input values
    input_values = iter(['John', '25', 'Mary', '30', 'quit'])

    def mock_input(prompt=None):
        return next(input_values)

    # Monkeypatch input() function
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the function and verify the output
    expected_output = [('John', 25), ('Mary', 30)]
    assert read_input() == expected_output

# 6


def test_sort_data():
    data = [("John", 28), ("Mary", 22), ("Bob", 31), ("Alice", 24)]
    expected_result = [("Mary", 22), ("Alice", 24), ("John", 28), ("Bob", 31)]
    assert sort_data(data) == expected_result

# 7


def test_car_consumption(monkeypatch):
    # Test case 1: Normal case
    user_input = ['Toyota', '10', 'quit']
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: user_input.pop(0))
        result = car_consumption()
    expected_result = [('Toyota', 10.0, 10000.0)]
    assert result == expected_result

    # Test case 2: Invalid consumption input
    user_input = ['Toyota', '-10', 'quit']
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: user_input.pop(0))
        result = car_consumption()
    expected_result = []
    assert result == expected_result

    # Test case 3: Quit input before entering data
    user_input = ['quit']
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: user_input.pop(0))
        result = car_consumption()
    expected_result = []
    assert result == expected_result
# 8

# 9


def test_add_contact():
    phonebook = Phonebook()
    phonebook.add_contact("John Doe", "123-456-7890")
    assert phonebook.search_contact("John Doe").phone_number == "123-456-7890"


def test_search_contact():
    phonebook = Phonebook()
    phonebook.add_contact("John Doe", "123-456-7890")
    phonebook.add_contact("Jane Doe", "234-567-8901")
    assert phonebook.search_contact("John Doe").phone_number == "123-456-7890"
    assert phonebook.search_contact("Jane Doe").phone_number == "234-567-8901"
    assert phonebook.search_contact("Bob Smith") is None


def test_remove_contact():
    phonebook = Phonebook()
    phonebook.add_contact("John Doe", "123-456-7890")
    phonebook.add_contact("Jane Doe", "234-567-8901")
    assert phonebook.remove_contact("John Doe") is True
    assert phonebook.search_contact("John Doe") is None
    assert phonebook.remove_contact("Bob Smith") is False

# 10


def test_loan():
    person = Person("John Doe", "johndoe@example.com")
    book = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
    loan = Loan(person, book, "2022-01-01")
    assert loan.person == person
    assert loan.book == book
    assert loan.date_borrowed == "2022-01-01"
    assert loan.date_returned == None


def test_return_book():
    person = Person("John Doe", "johndoe@example.com")
    book = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
    loan = Loan(person, book, "2022-01-01")
    loan.return_book("2022-01-10")
    assert loan.date_returned == "2022-01-10"


def test_person():
    person = Person("John Doe", "johndoe@example.com")
    assert person.name == "John Doe"
    assert person.email == "johndoe@example.com"


def test_book():
    book = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
    assert book.title == "The Catcher in the Rye"
    assert book.author == "J.D. Salinger"
    assert book.isbn == "9780316769488"

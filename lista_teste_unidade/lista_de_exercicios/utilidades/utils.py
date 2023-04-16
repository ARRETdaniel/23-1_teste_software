def read_and_print_string():
    s = input("Enter a string: ")
    print(s)
    return s


def get_string_length(input_string):
    """
    Retorna o comprimento de uma determinada string.
    """
    return len(input_string)

# count_ones.py


def count_ones(s: str) -> int:
    """
    Returns the number of 1's that appear in the input string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of 1's that appear in the input string.
    """
    return sum(1 for c in s if c == '1')

# Entre com um nome e imprima o nome somente se a primeira letra do nome for “a”


def print_name_if_starts_with_a(name):
    if name.lower().startswith('a'):
        print(name)


def remove_spaces(text):
    """
    Remove spaces from a given text and return the result as a vector
    """
    return list(text.replace(' ', ''))

#


def read_input():
    data = []
    while True:
        name = input("Enter a first name (or 'quit' to exit): ")
        if name == "quit":
            break
        age = int(input("Enter an age: "))
        if age < 0:
            break
        data.append((name, age))
    return data


def sort_data(data):
    return sorted(data, key=lambda x: x[1])

# cars


def car_consumption():
    data = []
    while True:
        name = input("Enter car's name (or 'quit' to exit): ")
        if name == "quit":
            break
        consumption = float(input("consumption: "))
        if consumption <= 0:
            break
        consumption_per_kilometer = consumption*1000
        data.append((name, consumption, consumption_per_kilometer))
    return sorted(data, key=lambda x: x[1])

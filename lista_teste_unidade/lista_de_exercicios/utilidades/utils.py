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

# 7


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
# 8


def read_string():
    s1 = input("Digite a string S1 (com no máximo 20 caracteres): ")
    if len(s1) > 20:
        print("A string digitada possui mais de 20 caracteres. Serão considerados apenas os primeiros 20 caracteres.")
        s1 = s1[:20]
    return s1


def print_string_length(s):
    print("O tamanho da string é:", len(s))


def compare_strings(s1, s2):
    if s1 == s2:
        print("As strings são iguais.")
    else:
        print("As strings são diferentes.")


def concatenate_strings(s1, s2):
    print("A concatenação das strings é:", s1 + s2)


def reverse_string(s):
    print("A string invertida é:", s[::-1])


def count_character(s, c):
    print("A quantidade de vezes que o caractere aparece na string é:", s.count(c))


def replace_character(s, c1, c2):
    s = s.replace(c1, c2, 1)
    print("A string após a substituição é:", s)


def is_substring(s1, s2):
    if s2 in s1:
        print("A string", s2, "é uma substring de", s1)
    else:
        print("A string", s2, "não é uma substring de", s1)


def get_substring(s, start, length):
    substring = s[start:start+length]
    print("A substring é:", substring)


def show_menu():
    print("Escolha uma opção:")
    print("(a) Ler uma string S1")
    print("(b) Imprimir o tamanho da string S1")
    print("(c) Comparar a string S1 com uma nova string S2")
    print("(d) Concatenar a string S1 com uma nova string S2")
    print("(e) Imprimir a string S1 de forma reversa")
    print("(f) Contar quantas vezes um dado caractere aparece na string S1")
    print("(g) Substituir a primeira ocorrencia do caractere C1 da string S1 pelo caractere C2")
    print("(h) Verificar se uma string S2 é substring de S1")
    print("(i) Retornar uma substring da string S1")
    print("(q) Sair")

# 9


class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number):
        contact = Contact(name, phone_number)
        self.contacts.append(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

# 10


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Loan:
    def __init__(self, person, book, date_borrowed):
        self.person = person
        self.book = book
        self.date_borrowed = date_borrowed
        self.date_returned = None

    def return_book(self, date_returned):
        self.date_returned = date_returned

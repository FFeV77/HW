import pytest

from scr import check_document_existance, get_all_doc_owners_names, get_doc_owner_name, delete_doc, remove_doc_from_shelf, get_doc_shelf

fixture = [
    ("2207 876234", True),
    ("11-2", True),
    ("10006", True),
    ("123456", False),
    ("", False),
]

@pytest.mark.parametrize('number, result', fixture)
def test_check_document_existance(number, result):
    calc = check_document_existance(number)
    assert result == calc

def test_get_all_doc_owners_names():
    etalon = ("Аристарх Павлов", "Василий Гупкин", "Геннадий Покемонов")
    result = get_all_doc_owners_names()
    assert result == set(etalon)

def test_get_doc_owner_name(monkeypatch):
    user_doc_number = '10006'
    name = "Аристарх Павлов"
    monkeypatch.setattr('builtins.input', lambda _: user_doc_number)
    assert get_doc_owner_name() == name

def test_delete_doc(monkeypatch):
    user_doc_number = '10006'
    monkeypatch.setattr('builtins.input', lambda _: user_doc_number)
    delete_doc()
    assert get_doc_owner_name() == None
    assert get_doc_shelf() == None

def test_get_doc_shelf(monkeypatch):
    user_doc_number = '10006'
    monkeypatch.setattr('builtins.input', lambda _: user_doc_number)
    assert get_doc_shelf() == '2'

def test_remove_doc_from_shelf(monkeypatch):
    user_doc_number = '10006'
    monkeypatch.setattr('builtins.input', lambda _: user_doc_number)
    remove_doc_from_shelf(user_doc_number)
    assert get_doc_shelf() == None


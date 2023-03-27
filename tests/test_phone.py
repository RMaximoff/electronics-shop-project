import pytest
from src.phone import Phone
from src.item import Item

phone = Phone("iPhone 14", 120_000, 5, 5)
phone1 = Phone("iPhone 15", 120_000, 5, 5)
item = Item("Смартфон", 10000, 20)


def test_init():
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 5


def test_radd():
    assert item + phone == 25


def test_add():
    assert phone + phone1 == 10


def test_repr():
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 5)"


def test_str():
    assert str(phone) == 'iPhone 14'









    #     poetry run pytest --cov
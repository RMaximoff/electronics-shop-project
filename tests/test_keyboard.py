from src.keyboard import KeyBoard

kb = KeyBoard('Dark Project KD87A', 9600, 5)


def test_lang():
    assert kb.language == "EN"


def test_change_lang():
    kb.change_lang()
    assert kb.language == "RU"
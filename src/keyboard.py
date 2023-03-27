from src.item import Item


class MixinLang:

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLang):

    def __init__(self, name, price, quantity):
        Item.__init__(self, name, price, quantity)
        MixinLang.__init__(self)

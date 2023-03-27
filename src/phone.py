from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num: int):
        if num < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self._number_of_sim = num

    @classmethod
    def __verity_classes(cls, other):
        if not isinstance(other, Item | Phone):
            raise TypeError(f"Невозможно выполнить операцию")

    def __add__(self, other):
        self.__verity_classes(other)
        return self.quantity + other.quantity

    def __radd__(self, other):
        self.__verity_classes(other)
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __str__(self):
        return self._name

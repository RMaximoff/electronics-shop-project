from csv import DictReader
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    csv_file = Path.joinpath(Path(__file__).parent, 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        try:
            if len(name) > 10:
                raise ValueError('Длина наименования товара превышает 10 символов')
            self._name = name
        except ValueError as exception:
            print(f'Exception: {exception}')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @staticmethod
    def string_to_number(num: str):
        """
        Метод возвращающий число из числа-строки
        """
        return int(float(num))

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        try:
            with open(cls.csv_file, 'r') as file:
                reader = DictReader(file)
                for row in reader:
                    try:
                        cls(row['name'],
                            cls.string_to_number(row['price']),
                            cls.string_to_number(row['quantity']))
                    except KeyError:
                        raise InstantiateCSVError()

        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self._name


class InstantiateCSVError(Exception):
    """
    Исключение, возникающее при ошибке чтения данных из файла CSV.
    """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message

from moneys.moneyContract import MoneyContract


class ConverterContract:
    @classmethod
    def convert(cls, amount: float, from_currency: callable, to_currency: callable) -> float:
        pass

    @classmethod
    def add(cls, money1, money2) -> MoneyContract:
        pass

    @classmethod
    def subtract(cls, money1, money2) -> MoneyContract:
        pass

    @classmethod
    def multiply(cls, money1, money2) -> MoneyContract:
        pass

    @classmethod
    def divide(cls, money1, money2) -> MoneyContract:
        pass

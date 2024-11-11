from currencies.currencyContract import CurrencyContract
from moneys.moneyContract import MoneyContract
from converters.converter import Converter

class AbstractMoney(MoneyContract):
    def __init__(self, amount: float, currency: callable):
        self._amount = amount
        self._currency = currency

    def getAmount(self) -> float:
        return self._amount

    def getCurrency(self) -> CurrencyContract:
        return self._currency

    def __str__(self) -> str:
        return f"{self.getAmount()} {self.getCurrency().getCurrencySymbol()}"

    def checkMoney(self, other):
        if not isinstance(other, MoneyContract):
            raise ValueError("Geçersiz türde para.")

    def __add__(self, other) -> MoneyContract | None:
        self.checkMoney(other)

        return Converter.add(self, other)

    def __sub__(self, other) -> MoneyContract | None:
        self.checkMoney(other)

        return Converter.subtract(self, other)

    def __mul__(self, other) -> MoneyContract | None:
        self.checkMoney(other)

        return Converter.multiply(self, other)

    def __truediv__(self, other) -> MoneyContract | None:
        self.checkMoney(other)

        return Converter.divide(self, other)

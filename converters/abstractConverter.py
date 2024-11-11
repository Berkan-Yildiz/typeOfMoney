from converters.converterContract import ConverterContract
from moneys.moneyContract import MoneyContract
from currencies.currencyContract import CurrencyContract

class AbstractConverter(ConverterContract):
    exchangeRates = {
        'Dollar': 2,
        'Euro': 5,
        'Ytl': 10,
    }

    @classmethod
    def convert(cls, amount: float, fromCurrency: CurrencyContract, toCurrency: CurrencyContract) -> float:
        oldRate = cls.exchangeRates[fromCurrency.getCurrencyName()]
        newRate = cls.exchangeRates[toCurrency.getCurrencyName()]
        return (amount / oldRate) * newRate

    @classmethod
    def add(cls, money1, money2) -> MoneyContract:
        convertedAmount = cls.convert(money2.getAmount(), money2.getCurrency(), money1.getCurrency())
        totalAmount = money1.getAmount() + convertedAmount
        moneyClass = type(money1)
        return moneyClass(totalAmount, money1.getCurrency())

    @classmethod
    def subtract(cls, money1, money2) -> MoneyContract:
        convertedAmount = cls.convert(money2.getAmount(), money2.getCurrency(), money1.getCurrency())
        totalAmount = money1.getAmount() - convertedAmount
        moneyClass = type(money1)
        return moneyClass(totalAmount, money1.getCurrency())

    @classmethod
    def multiply(cls, money1, money2) -> MoneyContract:
        convertedAmount = cls.convert(money1.getAmount(), money1.getCurrency(), money2.getCurrency())
        totalAmount = convertedAmount * money2.getAmount()
        moneyClass = type(money1)
        return moneyClass(totalAmount, money2.getCurrency())

    @classmethod
    def divide(cls, money1, money2) -> MoneyContract:
        convertedAmount = cls.convert(money1.getAmount(), money1.getCurrency(), money2.getCurrency())
        totalAmount = convertedAmount / money2.getAmount()
        moneyClass = type(money1)
        return moneyClass(totalAmount, money2.getCurrency())

from currencies.currencyContract import CurrencyContract


class MoneyContract:
    def getCurrency(self) -> CurrencyContract:
        pass

    def getAmount(self) -> float:
        pass

    def checkMoney(self, other):
        pass

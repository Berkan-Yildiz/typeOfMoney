from currencies.currencyContract import CurrencyContract


class AbstractCurrency(CurrencyContract):
    _name: str = ""
    _symbol: str = ""

    @classmethod
    def getCurrencyName(cls) -> str:
        return cls._name

    @classmethod
    def getCurrencySymbol(cls) -> str:
        return cls._symbol

    @classmethod
    def setCurrencyName(cls, name: str) -> None:
        cls._name = name

    @classmethod
    def setCurrencySymbol(cls, symbol: str) -> None:
        cls._symbol = symbol

from pydantic.dataclasses import dataclass
import decimal

@dataclass
class Price:
    asset:str
    bid:decimal.Decimal
    ask:decimal.Decimal
    tick_value:decimal.Decimal

@dataclass
class Account:
    account_number:int
    balance:decimal.Decimal
    equity:decimal.Decimal
    profit:decimal.Decimal
    leverage:int
    margin:decimal.Decimal
    currency:str


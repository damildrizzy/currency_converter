from decimal import Decimal
import datetime
from typing import Any, List

from pydantic import BaseModel
from pydantic.datetime_parse import parse_date


class SupportedCurrency(BaseModel):
    code: str
    description: str


class Rate(BaseModel):
    currency: str
    rate: Decimal


class ConvertedModel(BaseModel):
    base: str
    to: str
    amount: Decimal
    result: int


def validate_date(v: Any):
    try:
        datetime.datetime.strptime(v, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return parse_date(v)


class StrictDate(datetime.date):
    @classmethod
    def __get_validators__(cls):
        yield validate_date


class HistoricalData(BaseModel):
    date: datetime.date
    rates: List[Rate]

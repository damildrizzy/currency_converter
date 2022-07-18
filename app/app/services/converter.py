from decimal import Decimal
from typing import List

from fastapi import Depends, HTTPException

from .. import cache


async def get_currencies(currencies=Depends(cache.get_supported_currencies)) -> List:
    return [{"code": code, "description": description} for code, description in currencies.items()]


async def check_currency_supported(base: str, to: str, supported_currencies=Depends(cache.get_supported_currencies)):
    if base not in supported_currencies:
        raise HTTPException(status_code=400, detail=f"Currency {base} not supported")
    if to not in supported_currencies:
        raise HTTPException(status_code=400, detail=f"Currency {to} not supported")


async def convert_currencies(base: str, to: str, amount: Decimal, rates=Depends(cache.get_rates)) -> int:
    exchange_rate = Decimal(rates[to]) / Decimal(rates[base])
    result: Decimal = exchange_rate * amount
    return round(result, 3)


async def get_rates_by_date(date: str, rates=Depends(cache.get_rates)):
    return [{"currency": currency, "rate": rate} for currency, rate in rates.items()]

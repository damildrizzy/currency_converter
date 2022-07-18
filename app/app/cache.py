from datetime import datetime
from typing import Dict, List

from fastapi import Depends
import aioredis
from fastapi_plugins import depends_redis
from .utils import get_rates_by_date


async def get_rates(date=None, cache: aioredis.Redis = Depends(depends_redis)) -> List[Dict]:
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    rates = await cache.hgetall(date)
    if rates == {}:
        rates = await get_rates_by_date(date)
        await cache.hmset(date, rates)
    return rates


async def get_supported_currencies(cache: aioredis.Redis = Depends(depends_redis)) -> Dict:
    currencies = await cache.hgetall("currencies")
    return currencies

import aioredis
import httpx
from fastapi_utils.tasks import repeat_every
from .settings import settings

API_URL = settings.EXCHANGE_RATE_API_URL
REDIS_URL = f"redis://{settings.redis_host}"


async def get_rates_by_date(date: str):
    async with httpx.AsyncClient() as client:
        url = f"{API_URL}/{date}?base=USD"
        response = await client.get(url)
        data = response.json()
        return data['rates']


async def get_latest_currencies():
    async with httpx.AsyncClient() as client:
        url = f"{API_URL}/symbols"
        response = await client.get(url)
        data = response.json()
        return data['symbols']


# update the supported currencies cache every 48 hours
@repeat_every(seconds=60 * 60 * 48)
async def update_currencies_cache():
    currencies = await get_latest_currencies()
    values = {v['code']: v['description'] for v in currencies.values()}
    redis = aioredis.from_url(REDIS_URL)
    await redis.hmset("currencies", values)

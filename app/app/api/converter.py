from decimal import Decimal
from typing import List, Dict
from fastapi import APIRouter, Depends, Path, HTTPException
from .. import services
from .. import schemas
from .. import models
from .deps import get_current_user

router = APIRouter()


@router.get('/currencies', response_model=List[schemas.SupportedCurrency])
async def list_supported_currencies(currencies: List = Depends(services.get_currencies)):
    return currencies


@router.get('/convert/{base}/{to}/{amount}',
            response_model=schemas.ConvertedModel,
            dependencies=[Depends(services.check_currency_supported), Depends(get_current_user)])
async def convert(
        base: str = Path(
            ...,
            title="currency to convert from"
        ),
        to: str = Path(
            ...,
            title="currency to convert to",
        ),
        amount: Decimal = Path(
            ...,
            gt=0,
            title="Amount of money",
        ),
        converted: int = Depends(services.convert_currencies)):
    return {
        "base": base,
        "to": to,
        "amount": amount,
        "result": converted
    }


@router.get("/rates/{date}", response_model=schemas.HistoricalData, dependencies=[Depends(get_current_user)])
def historical_data(
        date: schemas.StrictDate = Path(
            title="date",
            description="date string in YYYY-MM-DD format"
        ),
        rates=Depends(services.get_rates_by_date)):
    return {
        "date": date,
        "rates": rates
    }

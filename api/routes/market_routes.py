from fastapi import APIRouter
from services.market_service import get_stock_price

router = APIRouter()

@router.get("/price/{symbol}")
def stock_price(symbol: str):
    data = get_stock_price(symbol)
    return data

from fastapi import APIRouter
from services.ai_service import predict_signal

router = APIRouter()

@router.get("/signal/{symbol}")
def ai_signal(symbol: str):
    result = predict_signal(symbol)
    return result


from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/signal/{symbol}")
def ai_signal(symbol: str):
    signals = ["BUY", "SELL", "HOLD"]

    return {
        "symbol": symbol.upper(),
        "signal": random.choice(signals),
        "confidence": f"{random.randint(70,95)}%",
        "entry_price": random.randint(100,50000),
        "target": random.randint(100,60000),
        "stoploss": random.randint(50,30000)
    }

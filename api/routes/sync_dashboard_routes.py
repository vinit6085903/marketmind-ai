from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

# ==========================================
# 📊 MARKET PRICE DATA
# ==========================================
@router.get("/price")
def get_price(symbol: str = "BTCUSDT"):
    price = random.randint(60000, 70000)
    change = round(random.uniform(-3, 3), 2)

    return {
        "symbol": symbol,
        "price": price,
        "change_percent": change,
        "time": datetime.utcnow()
    }


# ==========================================
# 🧠 AI SCORE + CONVICTION
# ==========================================
@router.get("/ai-score")
def ai_score(symbol: str = "BTCUSDT"):
    return {
        "symbol": symbol,
        "ai_score": random.randint(80, 98),
        "trend": random.choice(["BULLISH", "BEARISH"]),
        "confidence": round(random.uniform(70, 95), 2),
        "volatility": round(random.uniform(1.2, 3.5), 2)
    }


# ==========================================
# 🔗 GLOBAL SYNC STATUS
# ==========================================
@router.get("/sync-status")
def sync_status():
    return {
        "sync_active": True,
        "crosshair_sync": True,
        "master_asset": "BTCUSDT",
        "latency_ms": random.randint(5, 20)
    }


# ==========================================
# 📉 MULTI TIMEFRAME DATA
# ==========================================
@router.get("/multi-tf")
def multi_timeframe(symbol: str = "BTCUSDT"):
    return {
        "symbol": symbol,
        "timeframes": {
            "1m": random.randint(60000,70000),
            "5m": random.randint(60000,70000),
            "15m": random.randint(60000,70000),
            "1h": random.randint(60000,70000),
        }
    }


# ==========================================
# 🧠 AI MASTER SIGNAL
# ==========================================
@router.get("/ai-signal")
def ai_signal():
    signals = ["STRONG BUY","BUY","HOLD","SELL"]
    return {
        "signal": random.choice(signals),
        "asset": "BTCUSDT",
        "confidence": random.randint(85,97),
        "entry": random.randint(60000,70000),
        "target": random.randint(70000,80000),
        "stoploss": random.randint(55000,60000)
    }


# ==========================================
# 💼 EXECUTE TRADE
# ==========================================
@router.post("/execute-trade")
def execute_trade(asset:str, side:str, qty:float, leverage:int):

    price = random.randint(60000,70000)

    return {
        "status":"success",
        "asset":asset,
        "side":side,
        "qty":qty,
        "leverage":leverage,
        "executed_price":price,
        "message":"Trade Executed 🚀"
    }


# ==========================================
# 📊 PORTFOLIO STATUS
# ==========================================
@router.get("/portfolio")
def portfolio():
    return {
        "balance": round(random.uniform(5000,20000),2),
        "pnl": round(random.uniform(-2000,5000),2),
        "positions": random.randint(1,5)
    }


# ==========================================
# 🖥 SYSTEM STATUS
# ==========================================
@router.get("/system")
def system():
    return {
        "server":"MarketMind AI Core",
        "status":"running",
        "latency": random.randint(5,20),
        "time": datetime.utcnow()
    }

from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

# ==========================================
# 📊 LIVE PRICE + AI SIGNAL
# ==========================================
@router.get("/signal")
def ai_signal():

    price = round(random.uniform(62000,65000),2)

    return {
        "asset":"BTCUSDT",
        "price": price,
        "change_pct": round(random.uniform(-2,3),2),
        "ai_score": random.randint(70,98),
        "signal": random.choice(["STRONG BUY","BUY","SELL","HOLD"]),
        "confidence": random.randint(70,96),
        "buy_probability": round(random.uniform(60,95),2),
        "rr_ratio": random.choice(["1:2","1:3","1:3.5","1:5"])
    }


# ==========================================
# 🎯 TRADE PLAN
# ==========================================
@router.get("/trade-plan")
def trade_plan():

    entry = round(random.uniform(63000,64000),2)

    return {
        "entry": entry,
        "target": entry + random.randint(800,2000),
        "stoploss": entry - random.randint(500,1500),
        "strategy":"AI Order Flow Breakout",
        "confidence": random.randint(80,96)
    }


# ==========================================
# 🧠 SENTIMENT FLOW
# ==========================================
@router.get("/sentiment")
def sentiment():

    return {
        "social_volume": random.randint(50,100),
        "whale_activity": random.randint(40,100),
        "retail_sentiment": random.choice(["Bullish","Bearish","Neutral"]),
        "smart_money": random.choice(["Accumulating","Distributing"])
    }


# ==========================================
# 📉 ORDER FLOW DELTA (CVD)
# ==========================================
@router.get("/cvd")
def cvd_data():

    data=[]
    value=0

    for i in range(20):
        delta=random.randint(-2000,3000)
        value+=delta
        data.append({"delta":delta,"cvd":value})

    return {"cvd":data}


# ==========================================
# 📚 DEPTH OF MARKET (ORDERBOOK)
# ==========================================
@router.get("/dom")
def depth_market():

    bids=[]
    asks=[]
    base=64234

    for i in range(10):
        bids.append({
            "price": round(base-(i*0.5),2),
            "size": round(random.uniform(1,25),2)
        })

    for i in range(10):
        asks.append({
            "price": round(base+(i*0.5),2),
            "size": round(random.uniform(1,25),2)
        })

    return {
        "bids":bids,
        "asks":asks,
        "last_price": base + random.uniform(-5,5)
    }


# ==========================================
# ⚡ EXECUTE TRADE
# ==========================================
@router.post("/execute-trade")
def execute_trade():

    return {
        "status":"Trade Executed",
        "execution_price": round(random.uniform(63000,65000),2),
        "ai_slippage": round(random.uniform(0.1,1.5),2),
        "timestamp": str(datetime.utcnow())
    }


# ==========================================
# 🤖 AI ENGINE STATUS
# ==========================================
@router.get("/engine-status")
def engine_status():

    return {
        "engine":"MarketMind Scalper AI",
        "status":"ACTIVE",
        "latency_ms": random.randint(5,20),
        "connected_exchanges":["Binance","Bybit","OKX"],
        "ai_version":"v4.2"
    }

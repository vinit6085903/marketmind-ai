from fastapi import APIRouter
import random

router = APIRouter()

# KPI cards
@router.get("/kpi")
def get_kpi():
    return {
        "total_profit": 420690,
        "profit_change": "+12.4%",
        "win_rate": 68.5,
        "profit_factor": 2.41,
        "sharpe_ratio": 1.85
    }

# Equity curve chart
@router.get("/equity")
def equity_curve():
    data = []
    value = 100000

    for i in range(30):
        value += random.randint(-2000, 5000)
        data.append({"day": i+1, "equity": value})

    return {"equity_curve": data}

# Monthly heatmap
@router.get("/heatmap")
def heatmap():
    return {
        "2024": [4.2, 8.1, -1.2, 2.4, 11.5, 5.6],
        "2023": [-0.5, 1.8, 6.2, -3.4, 2.1, 4.8, 9.1]
    }

# Trade distribution
@router.get("/distribution")
def distribution():
    return {
        "crypto": 60,
        "forex": 25,
        "stocks": 15
    }

from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter()

# ==============================
# 🧠 GLOBAL DASHBOARD DATA
# ==============================
@router.get("/")
def dashboard_overview():
    return {
        "btc_price": 64231.50,
        "ai_index": 94,
        "signal": "BUY",
        "buy_probability": 88.4,
        "risk_ratio": "1:3.5",
        "sentiment": "Greed",
        "sentiment_score": 74
    }


# ==============================
# 📊 MULTI CHART DATA
# ==============================
@router.get("/charts")
def get_charts():
    return {
        "charts":[
            {"symbol":"BTCUSDT","price":64231,"signal":"BUY","timeframe":"1H"},
            {"symbol":"ETHUSDT","price":2542,"signal":"NEUTRAL","timeframe":"15M"},
            {"symbol":"SOLUSDT","price":145,"signal":"SELL","timeframe":"4H"},
            {"symbol":"EURUSD","price":1.0824,"signal":"ACCUMULATION","timeframe":"1D"}
        ]
    }


# ==============================
# 🤖 AI MASTER SIGNAL
# ==============================
@router.get("/ai-signal")
def ai_master_signal():
    signals = ["STRONG BUY","BUY","SELL","HOLD"]
    return {
        "signal": random.choice(signals),
        "asset": "BTC/USD",
        "entry": 64231,
        "target": 68400,
        "stoploss": 61200,
        "confidence": random.randint(85,97)
    }


# ==============================
# 📉 MARKET SENTIMENT
# ==============================
@router.get("/sentiment")
def market_sentiment():
    score = random.randint(40,90)
    mood = "Greed" if score>60 else "Fear"
    return {
        "score": score,
        "mood": mood
    }


# ==============================
# ⚡ EXECUTE TRADE
# ==============================
@router.post("/trade/execute")
def execute_trade(
    symbol:str,
    side:str,
    amount:float,
    leverage:int
):
    price = random.randint(60000,65000)
    return {
        "status":"executed",
        "symbol":symbol,
        "side":side,
        "amount":amount,
        "leverage":leverage,
        "entry_price":price,
        "time":datetime.utcnow(),
        "message":"Trade executed successfully 🚀"
    }


# ==============================
# 📂 OPEN POSITIONS
# ==============================
@router.get("/positions")
def open_positions():
    return {
        "positions":[
            {"symbol":"BTCUSDT","side":"LONG","qty":0.12,"status":"LIVE"},
            {"symbol":"ETHUSDT","side":"SHORT","qty":0.5,"status":"LIVE"},
            {"symbol":"SOLUSDT","side":"LONG","qty":3,"status":"LIVE"}
        ]
    }


# ==============================
# 💰 PNL DATA
# ==============================
@router.get("/pnl")
def pnl_data():
    return {
        "total_pnl": 4210.50,
        "percentage": 2.1,
        "open_positions": 3
    }


# ==============================
# ⏱ LATENCY + SYSTEM STATUS
# ==============================
@router.get("/system")
def system_status():
    return {
        "latency": f"{random.randint(8,25)}ms",
        "status":"SYSTEM READY",
        "version":"MARKETMIND CORE v4.2",
        "time": datetime.utcnow()
    }


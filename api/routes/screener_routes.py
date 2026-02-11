from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

# =========================================
# 🔥 AI TOP PICKS SCREENER
# =========================================
@router.get("/top-picks")
def ai_top_picks():

    assets = [
        {"symbol":"BTC/USD","name":"Bitcoin","price":64281},
        {"symbol":"ETH/USD","name":"Ethereum","price":3452},
        {"symbol":"SOL/USD","name":"Solana","price":143},
        {"symbol":"DOT/USD","name":"Polkadot","price":6.85},
        {"symbol":"AAPL","name":"Apple","price":189},
        {"symbol":"EUR/USD","name":"Euro Dollar","price":1.09}
    ]

    data=[]
    for a in assets:
        score=random.randint(20,95)
        trend="Bullish" if score>70 else "Bearish" if score<40 else "Neutral"

        action="Strong Buy" if score>85 else \
               "Buy" if score>70 else \
               "Hold" if score>45 else \
               "Sell" if score>30 else "Strong Sell"

        change=round(random.uniform(-6,6),2)

        data.append({
            "asset":a["symbol"],
            "name":a["name"],
            "trend":trend,
            "ai_score":score,
            "price":a["price"],
            "change_24h":change,
            "action":action
        })

    return {
        "last_update":datetime.utcnow(),
        "data":data
    }

# =========================================
# 🔥 FILTER SCREENER
# =========================================
@router.get("/filter")
def filter_assets(
    min_score:int=50,
    trend:str="all"
):
    result=[]
    for i in range(20):
        score=random.randint(10,95)
        t="Bullish" if score>70 else "Bearish" if score<40 else "Neutral"

        if score<min_score:
            continue
        if trend!="all" and t.lower()!=trend.lower():
            continue

        result.append({
            "asset":f"COIN{i}",
            "score":score,
            "trend":t,
            "price":round(random.uniform(1,50000),2)
        })

    return {"filtered":result}

# =========================================
# 🔥 AI INSIGHT OF HOUR
# =========================================
@router.get("/insight")
def ai_insight():
    return {
        "asset":"BTC/USD",
        "pattern":"Double Bottom",
        "success_rate":88.4,
        "timeframe":"4H/1D",
        "target":67500,
        "stoploss":62100,
        "risk":"Moderate",
        "confidence":"High Probability"
    }

# =========================================
# 🔥 GLOBAL SENTIMENT BAR
# =========================================
@router.get("/sentiment")
def global_sentiment():
    bull=random.randint(50,80)
    bear=100-bull

    return {
        "bullish_percent":bull,
        "bearish_percent":bear
    }

# =========================================
# 🔥 RECENT SIGNALS
# =========================================
@router.get("/signals")
def recent_signals():

    signals=[
        {"asset":"XAU/USD","type":"SELL","score":12,"time":"10m ago"},
        {"asset":"GBP/JPY","type":"BUY","score":89,"time":"24m ago"},
        {"asset":"BTC/USD","type":"BUY","score":94,"time":"5m ago"},
        {"asset":"ETH/USD","type":"BUY","score":82,"time":"12m ago"}
    ]

    return {"signals":signals}

# =========================================
# 🔥 LIVE TICKER
# =========================================
@router.get("/ticker")
def live_ticker():
    pairs=["BTC/USD","ETH/USD","XRP/USD","AAPL","EUR/USD","SPX500","GOLD"]

    ticker=[]
    for p in pairs:
        ticker.append({
            "symbol":p,
            "change":round(random.uniform(-2,2),2)
        })

    return {"ticker":ticker}

# =========================================
# 🔥 SEARCH MARKET
# =========================================
@router.get("/search/{symbol}")
def search_market(symbol:str):

    score=random.randint(20,95)

    return {
        "asset":symbol.upper(),
        "ai_score":score,
        "trend":"Bullish" if score>70 else "Bearish",
        "suggestion":"Buy" if score>70 else "Sell",
        "confidence":random.randint(60,95)
    }

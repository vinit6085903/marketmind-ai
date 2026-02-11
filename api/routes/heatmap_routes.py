from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

# ==========================================
# 🌍 GLOBAL HEATMAP DATA
# ==========================================
@router.get("/global-heatmap")
def global_heatmap():

    return {
        "last_sync": datetime.utcnow(),
        "gainers": random.randint(300,500),
        "losers": random.randint(80,200),
        "neutral": random.randint(20,100),

        "sectors": {
            "tech":[
                {"symbol":"AAPL","change":round(random.uniform(-3,5),2),"mcap":"3.2T"},
                {"symbol":"MSFT","change":round(random.uniform(-3,5),2),"mcap":"3.1T"},
                {"symbol":"NVDA","change":round(random.uniform(-5,8),2),"mcap":"1.8T"},
                {"symbol":"GOOGL","change":round(random.uniform(-2,3),2),"mcap":"1.5T"},
            ],
            "finance":[
                {"symbol":"JPM","change":round(random.uniform(-3,3),2),"mcap":"580B"},
                {"symbol":"GS","change":round(random.uniform(-2,2),2),"mcap":"120B"},
                {"symbol":"BAC","change":round(random.uniform(-2,2),2),"mcap":"300B"},
            ],
            "crypto":[
                {"symbol":"BTC","change":round(random.uniform(-5,8),2)},
                {"symbol":"ETH","change":round(random.uniform(-5,8),2)},
            ],
            "energy":[
                {"symbol":"XOM","change":round(random.uniform(-4,3),2)},
                {"symbol":"CVX","change":round(random.uniform(-4,3),2)},
            ]
        }
    }


# ==========================================
# 🧠 AI SENTIMENT HEATMAP
# ==========================================
@router.get("/ai-sentiment")
def ai_sentiment():

    return {
        "nvda":{
            "score": random.randint(85,98),
            "sentiment":"EXTREME BULLISH"
        },
        "tsla":{
            "score": random.randint(20,40),
            "sentiment":"BEARISH"
        },
        "btc":{
            "score": random.randint(60,90),
            "sentiment":"BULLISH"
        }
    }


# ==========================================
# 📊 SECTOR ANALYTICS
# ==========================================
@router.get("/sector-analytics")
def sector_analytics():

    return {
        "tech":{
            "avg_change": round(random.uniform(-2,5),2),
            "volume": random.randint(200,800)
        },
        "finance":{
            "avg_change": round(random.uniform(-3,3),2),
            "volume": random.randint(100,500)
        },
        "crypto":{
            "avg_change": round(random.uniform(-5,10),2),
            "volume": random.randint(500,1500)
        }
    }


# ==========================================
# 📈 TOP GAINERS
# ==========================================
@router.get("/top-gainers")
def top_gainers():

    data=[]
    stocks=["NVDA","AAPL","BTC","ETH","MSFT","AMZN"]

    for s in stocks:
        data.append({
            "symbol":s,
            "change":round(random.uniform(2,10),2)
        })

    return {"gainers":data}


# ==========================================
# 📉 TOP LOSERS
# ==========================================
@router.get("/top-losers")
def top_losers():

    data=[]
    stocks=["TSLA","META","NFLX","XOM","JPM"]

    for s in stocks:
        data.append({
            "symbol":s,
            "change":round(random.uniform(-10,-2),2)
        })

    return {"losers":data}


# ==========================================
# 🧠 AI ALERTS
# ==========================================
@router.get("/ai-alerts")
def ai_alerts():

    alerts=[
        "NVDA extreme bullish breakout",
        "Tesla bearish divergence detected",
        "BTC institutional buying spike",
        "Tech sector volatility high"
    ]

    return {
        "alerts":random.sample(alerts,3),
        "time":datetime.utcnow()
    }


# ==========================================
# 🔄 MARKET STATUS
# ==========================================
@router.get("/market-status")
def market_status():

    return {
        "market":"GLOBAL",
        "status":"OPEN",
        "latency": random.randint(5,20),
        "server_time": datetime.utcnow()
    }


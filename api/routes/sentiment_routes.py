from fastapi import APIRouter
import random
from datetime import datetime, timedelta

router = APIRouter()

# ===============================
# 🔥 EXECUTIVE AI SUMMARY
# ===============================
@router.get("/summary")
def ai_summary():
    return {
        "overall_sentiment": 72,
        "market_bias": "Bullish",
        "summary": "Global markets showing resilience with strong bullish momentum in tech and AI sector.",
        "last_updated": "2 min ago",
        "status": "LIVE"
    }

# ===============================
# 🔥 GLOBAL SENTIMENT GAUGE
# ===============================
@router.get("/gauge")
def sentiment_gauge():
    score = random.randint(55,90)

    return {
        "score": score,
        "label": "Bullish" if score>65 else "Neutral",
        "fear": 20,
        "neutral": 30,
        "greed": score
    }

# ===============================
# 🔥 SENTIMENT TREND
# ===============================
@router.get("/trend")
def sentiment_trend():
    trend=[]
    value=50

    for i in range(24):
        value += random.randint(-5,8)
        value=max(10,min(95,value))
        trend.append({"hour":i,"sentiment":value})

    return {"trend":trend}

# ===============================
# 🔥 LIVE NEWS SENTIMENT
# ===============================
@router.get("/news")
def sentiment_news():

    news=[
        {
            "source":"Reuters",
            "title":"Fed signals potential rate pause",
            "sentiment":"+85 Bullish",
            "tag":["Macro","Rates"],
            "time":"2m ago"
        },
        {
            "source":"Bloomberg",
            "title":"NVIDIA demand triples overnight",
            "sentiment":"+92 Bullish",
            "tag":["AI","NVDA"],
            "time":"12m ago"
        },
        {
            "source":"WSJ",
            "title":"Crude oil stabilizes",
            "sentiment":"+45 Neutral",
            "tag":["Energy"],
            "time":"25m ago"
        },
        {
            "source":"CNBC",
            "title":"Retail spending misses estimate",
            "sentiment":"-62 Bearish",
            "tag":["Consumer"],
            "time":"45m ago"
        }
    ]

    return {"news":news}

# ===============================
# 🔥 TRENDING BUZZWORDS
# ===============================
@router.get("/buzz")
def buzzwords():
    return {
        "trending":[
            "AI Chips","NVIDIA","BTC ETF","Semiconductors",
            "Tech Rally","Cloud Data","Interest Rates",
            "Soft Landing","Inflation"
        ]
    }

# ===============================
# 🔥 SOCIAL MEDIA VOLUME
# ===============================
@router.get("/social-volume")
def social_volume():
    return {
        "twitter": "2.4M",
        "reddit": "840K",
        "stocktwits": "1.2M",
        "volume_spike_percent": random.randint(5,25)
    }

# ===============================
# 🔥 FOOTER STATS
# ===============================
@router.get("/stats")
def sentiment_stats():
    return {
        "precision": 98.4,
        "sources_tracked": 14280,
        "bull_bear_ratio": "3.2:1",
        "latency": "14ms"
    }

# ===============================
# 🔥 SEARCH SENTIMENT
# ===============================
@router.get("/search/{keyword}")
def search_sentiment(keyword:str):
    score=random.randint(40,90)

    return {
        "keyword":keyword.upper(),
        "sentiment_score":score,
        "label":"Bullish" if score>60 else "Bearish",
        "mentions":random.randint(1000,500000)
    }

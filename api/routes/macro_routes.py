from fastapi import APIRouter
import random
from datetime import datetime, timedelta

router = APIRouter()

# ==========================================
# 🏦 CENTRAL BANK RATES
# ==========================================
@router.get("/central-banks")
def central_banks():
    return {
        "fed": {"rate": 5.50, "next_meeting_days": 12},
        "ecb": {"rate": 4.50, "next_meeting_days": 18},
        "boj": {"rate": 0.10, "policy":"Hawkish Pivot"}
    }


# ==========================================
# 📅 ECONOMIC CALENDAR
# ==========================================
@router.get("/economic-calendar")
def calendar():

    events = [
        {"time":"08:30","event":"Non-Farm Payrolls","country":"USA","consensus":"180k","impact":9.4},
        {"time":"10:15","event":"ECB Press Conf","country":"EU","consensus":"-","impact":8.1},
        {"time":"14:00","event":"FOMC Minutes","country":"USA","consensus":"-","impact":9.2},
        {"time":"19:30","event":"CPI MoM","country":"JP","consensus":"0.2%","impact":7.4},
    ]
    return {"events":events}


# ==========================================
# 📈 YIELD CURVE DATA
# ==========================================
@router.get("/yield-curve")
def yield_curve():

    return {
        "us":[4.8,4.5,4.32,4.28,4.2],
        "eu":[3.1,2.8,2.6,2.5,2.4],
        "jp":[0.1,0.15,0.2,0.25,0.3],
        "spread_2_10": round(random.uniform(-80,-10),2),
        "real_yield_us": round(random.uniform(1.2,2.5),2)
    }


# ==========================================
# 🪙 COMMODITIES
# ==========================================
@router.get("/commodities")
def commodities():

    return {
        "gold":{
            "price": round(random.uniform(2100,2200),2),
            "change": round(random.uniform(-2,2),2)
        },
        "oil":{
            "price": round(random.uniform(70,90),2),
            "change": round(random.uniform(-3,3),2)
        },
        "copper":{
            "price": round(random.uniform(3.5,4.5),3),
            "change": round(random.uniform(-1,1),2)
        }
    }


# ==========================================
# 💱 CURRENCY STRENGTH
# ==========================================
@router.get("/currency-strength")
def currency_strength():

    return {
        "USD": random.randint(60,95),
        "EUR": random.randint(20,70),
        "JPY": random.randint(5,40),
        "GBP": random.randint(40,80)
    }


# ==========================================
# 🌍 GLOBAL SENTIMENT HEATMAP
# ==========================================
@router.get("/global-sentiment")
def sentiment():

    markets=["S&P500","NASDAQ","NIKKEI","DAX","FTSE","CSI300","ASX","SENSEX"]
    moods=["BULLISH","BEARISH","NEUTRAL","OVERBOUGHT"]

    data=[]
    for m in markets:
        data.append({
            "market":m,
            "sentiment":random.choice(moods)
        })

    return {"sentiment":data}


# ==========================================
# 📊 INFLATION VS GDP SCATTER
# ==========================================
@router.get("/macro-scatter")
def scatter():

    countries=["USA","EU","China","Japan","India","UK"]
    data=[]

    for c in countries:
        data.append({
            "country":c,
            "inflation": round(random.uniform(1,7),2),
            "gdp": round(random.uniform(-1,6),2)
        })

    return {"macro":data}


# ==========================================
# 🧠 AI MACRO SYNTHESIS
# ==========================================
@router.get("/ai-insights")
def ai_insights():

    insights=[
        "US yield curve inversion signals recession probability rising",
        "BoJ policy shift may strengthen Yen",
        "Gold gaining safe haven demand",
        "Oil volatility rising due to supply constraints",
        "Dollar liquidity tightening globally"
    ]

    return {
        "alerts": random.sample(insights,3),
        "risk_mode": random.choice(["RISK-ON","RISK-OFF","NEUTRAL"]),
        "ai_confidence": round(random.uniform(70,96),2)
    }


# ==========================================
# ⚡ EXECUTE MACRO HEDGE
# ==========================================
@router.post("/execute-hedge")
def execute_macro():

    return {
        "status":"Macro hedge executed",
        "hedge_type": random.choice(["USD Long","Gold Long","Bond Hedge"]),
        "risk_level": random.choice(["LOW","MEDIUM","HIGH"]),
        "timestamp": str(datetime.utcnow())
    }


# ==========================================
# 🛰 SYSTEM STATUS
# ==========================================
@router.get("/system-status")
def system_status():

    return {
        "system":"ONLINE",
        "latency_ms": random.randint(5,25),
        "engine":"MarketMind Macro Engine v4.2",
        "server_time": str(datetime.utcnow())
    }

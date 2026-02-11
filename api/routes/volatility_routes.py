from fastapi import APIRouter
import random

router = APIRouter()

# ==========================================
# 🔥 VOLATILITY SURFACE DATA (3D)
# ==========================================
@router.get("/surface")
def volatility_surface():

    strikes=[20000,25000,30000,35000,40000,45000]
    maturities=[7,14,30,60,90]

    surface=[]

    for m in maturities:
        for s in strikes:
            surface.append({
                "strike":s,
                "maturity_days":m,
                "iv": round(random.uniform(35,90),2)
            })

    return {"surface":surface}


# ==========================================
# 📊 VOL SMILE
# ==========================================
@router.get("/smile")
def vol_smile():

    strikes=[20000,25000,30000,35000,40000,45000]

    data=[]
    for s in strikes:
        data.append({
            "strike":s,
            "iv": round(random.uniform(40,80),2)
        })

    return {
        "atm_iv": round(random.uniform(45,65),2),
        "put_skew": round(random.uniform(1,8),2),
        "smile":data
    }


# ==========================================
# 📈 TERM STRUCTURE
# ==========================================
@router.get("/term-structure")
def term_structure():

    return {
        "7D": round(random.uniform(40,60),2),
        "30D": round(random.uniform(45,65),2),
        "90D": round(random.uniform(50,75),2),
        "180D": round(random.uniform(55,80),2)
    }


# ==========================================
# 🧠 AI VOLATILITY INSIGHT
# ==========================================
@router.get("/ai-insight")
def ai_insight():

    insights=[
        "Call skew increasing in short-term options",
        "Volatility expansion incoming",
        "Mean reversion likely in IV surface",
        "Market pricing high fear premium",
        "Gamma squeeze probability rising"
    ]

    return {
        "insight": random.choice(insights),
        "confidence": random.randint(65,95),
        "signal": random.choice(["BULLISH","BEARISH","HEDGE"])
    }


# ==========================================
# 📊 PORTFOLIO GREEKS
# ==========================================
@router.get("/greeks")
def greeks():

    return {
        "delta": round(random.uniform(-1,1),3),
        "gamma": round(random.uniform(0,2),3),
        "theta": round(random.uniform(-50000,-1000),2),
        "vega": round(random.uniform(1,20),2)
    }


# ==========================================
# 🚨 VOLATILITY ALERTS
# ==========================================
@router.get("/alerts")
def vol_alerts():

    alerts=[
        "IV spike detected",
        "Unusual options activity",
        "Call wall forming",
        "Put protection rising",
        "Gamma squeeze zone"
    ]

    data=[]
    for _ in range(3):
        data.append({
            "alert": random.choice(alerts),
            "strength": random.randint(60,95),
            "type": random.choice(["SPIKE","SKEW","FLOW"])
        })

    return {"alerts":data}


# ==========================================
# 💰 HEDGE STRATEGY AI
# ==========================================
@router.get("/hedge-strategy")
def hedge():

    strategies=[
        "Long straddle",
        "Short iron condor",
        "Protective puts",
        "Call ratio spread",
        "Calendar spread"
    ]

    return {
        "strategy": random.choice(strategies),
        "confidence": random.randint(60,92),
        "risk_level": random.choice(["LOW","MEDIUM","HIGH"]),
        "expected_roi": round(random.uniform(5,25),2)
    }


# ==========================================
# 📊 LIVE MARKET STATUS
# ==========================================
@router.get("/status")
def status():

    return {
        "active_asset":"BTC/USD",
        "price": round(random.uniform(60000,70000),2),
        "change": round(random.uniform(-5,5),2),
        "latency_ms": random.randint(5,25),
        "market_state": random.choice(["LIVE","VOLATILE","CALM"])
    }


# ==========================================
# 📥 HISTORICAL IV
# ==========================================
@router.get("/historical")
def historical():

    data=[]
    for i in range(30):
        data.append({
            "day":i+1,
            "iv": round(random.uniform(35,80),2)
        })

    return {"historical_iv":data}

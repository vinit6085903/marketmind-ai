from fastapi import APIRouter
import random

router = APIRouter()

# ==========================================
# 📊 CORRELATION SCATTER DATA (bubble chart)
# ==========================================
@router.get("/scatter")
def correlation_scatter():

    assets=["BTC","ETH","SOL","AAPL","TSLA","NVDA","GOLD","DXY","EURUSD"]

    data=[]
    for a in assets:
        data.append({
            "asset":a,
            "correlation": round(random.uniform(-1,1),2),
            "volatility": round(random.uniform(0.5,12),2),
            "ai_score": random.randint(40,98),
            "signal": random.choice(["BUY","SELL","NEUTRAL"])
        })

    return {"scatter":data}


# ==========================================
# 🔥 HEATMAP MATRIX
# ==========================================
@router.get("/heatmap")
def heatmap():

    assets=["BTC","ETH","SOL","AAPL","TSLA","NVDA","GOLD","DXY"]

    matrix={}

    for a in assets:
        matrix[a]={}
        for b in assets:
            if a==b:
                matrix[a][b]=1.0
            else:
                matrix[a][b]=round(random.uniform(-1,1),2)

    return {"matrix":matrix}


# ==========================================
# 🧠 AI MARKET REGIME
# ==========================================
@router.get("/ai-regime")
def regime():

    regimes=["RISK ON","RISK OFF","BULL CYCLE","BEAR PHASE","SIDEWAYS"]
    sentiment=["BULLISH","BEARISH","NEUTRAL"]

    return {
        "market_regime": random.choice(regimes),
        "sentiment": random.choice(sentiment),
        "confidence": random.randint(60,95),
        "btc_dominance": round(random.uniform(40,60),2),
        "volatility_index": round(random.uniform(10,40),2)
    }


# ==========================================
# 🚨 ANOMALY DETECTION
# ==========================================
@router.get("/anomalies")
def anomalies():

    anomalies=[
        "Gold diverging from BTC",
        "NASDAQ correlation spike",
        "ETH decoupling detected",
        "DXY inverse breakout",
        "SOL volatility expansion"
    ]

    data=[]
    for _ in range(3):
        data.append({
            "alert": random.choice(anomalies),
            "strength": random.randint(60,95),
            "type": random.choice(["DIVERGENCE","BREAKOUT","DECOUPLING"])
        })

    return {"anomalies":data}


# ==========================================
# 📈 VOLATILITY TABLE
# ==========================================
@router.get("/volatility")
def volatility():

    assets=["BTC","ETH","SOL","AAPL","TSLA","NVDA","GOLD"]

    data=[]
    for a in assets:
        data.append({
            "asset":a,
            "atr_volatility": round(random.uniform(1,10),2),
            "trend": random.choice(["UP","DOWN","SIDE"]),
            "risk_level": random.choice(["LOW","MEDIUM","HIGH"])
        })

    return {"volatility":data}


# ==========================================
# 🧠 AI INSIGHTS PANEL
# ==========================================
@router.get("/ai-insights")
def ai_insights():

    insights=[
        "BTC correlation with NASDAQ rising",
        "SOL showing early breakout signals",
        "Gold acting as hedge again",
        "Tech stocks linked to crypto momentum",
        "ETH accumulation detected"
    ]

    data=[]
    for _ in range(3):
        data.append({
            "title":"AI Insight",
            "description":random.choice(insights),
            "confidence":random.randint(60,95),
            "type":random.choice(["BULLISH","BEARISH","NEUTRAL"])
        })

    return {"insights":data}


# ==========================================
# 📊 CORRELATION SUMMARY CARDS
# ==========================================
@router.get("/summary")
def summary():

    return {
        "market_sentiment": random.choice(["Highly Correlated","Decoupling","Neutral"]),
        "avg_volatility": round(random.uniform(3,10),2),
        "anomaly": random.choice(["Gold Divergence","BTC-ETH Sync","Tech Selloff"]),
        "ai_signal": random.choice(["Strong Buy","Buy","Sell","Neutral"])
    }


# ==========================================
# 📥 EXPORT DATA (for CSV)
# ==========================================
@router.get("/export")
def export_data():

    assets=["BTC","ETH","SOL","AAPL","TSLA"]

    rows=[]
    for a in assets:
        rows.append({
            "asset":a,
            "correlation": round(random.uniform(-1,1),2),
            "volatility": round(random.uniform(1,10),2)
        })

    return {"export":rows}


# ==========================================
# 🔮 DEEP AI REPORT
# ==========================================
@router.get("/deep-report")
def deep_report():

    return {
        "report_title":"AI Correlation Intelligence Report",
        "summary":"Market entering high correlation regime. Risk-off behavior rising.",
        "top_opportunity":"SOL vs BTC breakout",
        "hedge_suggestion":"Increase gold exposure",
        "risk_alert":"Tech-crypto correlation spike",
        "confidence": random.randint(70,96)
    }

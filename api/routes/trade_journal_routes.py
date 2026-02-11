from fastapi import APIRouter
from datetime import datetime
import random
import uuid

router = APIRouter()

# in-memory db (baad me Mongo/Postgres laga dena)
trade_db = []


# ==========================================
# ➕ ADD TRADE ENTRY
# ==========================================
@router.post("/add-trade")
def add_trade(symbol:str, pnl:float, strategy:str, mood:str):

    trade={
        "id": str(uuid.uuid4()),
        "symbol": symbol,
        "pnl": pnl,
        "strategy": strategy,
        "mood": mood,
        "time": datetime.utcnow()
    }

    trade_db.append(trade)

    return {"status":"trade added","trade":trade}


# ==========================================
# 📜 ALL TRADES
# ==========================================
@router.get("/all-trades")
def all_trades():
    return {
        "total": len(trade_db),
        "trades": trade_db[::-1]
    }


# ==========================================
# 📊 PERFORMANCE SUMMARY
# ==========================================
@router.get("/performance")
def performance():

    total_pnl=sum([t["pnl"] for t in trade_db]) if trade_db else 0
    wins=[t for t in trade_db if t["pnl"]>0]
    losses=[t for t in trade_db if t["pnl"]<0]

    winrate = (len(wins)/len(trade_db)*100) if trade_db else 0

    return {
        "total_pnl": round(total_pnl,2),
        "winrate": round(winrate,2),
        "total_trades": len(trade_db),
        "wins": len(wins),
        "losses": len(losses),
        "sharpe": round(random.uniform(1.2,3.5),2)
    }


# ==========================================
# 🧠 AI TRADE REVIEW
# ==========================================
@router.get("/ai-review/{trade_id}")
def ai_review(trade_id:str):

    # dummy AI analysis
    reviews=[
        "Perfect RSI entry detected",
        "Late entry detected (FOMO)",
        "Excellent risk management",
        "Overtrading behavior found",
        "Institutional zone entry"
    ]

    return {
        "trade_id":trade_id,
        "entry_score": random.randint(60,98),
        "risk_score": random.randint(50,95),
        "psychology": random.choice(["CALM","FOMO","REVENGE","DISCIPLINED"]),
        "ai_comment": random.choice(reviews)
    }


# ==========================================
# 📈 MONTHLY PNL CHART DATA
# ==========================================
@router.get("/monthly-chart")
def monthly_chart():

    data=[]
    for i in range(30):
        pnl=round(random.uniform(-1500,3000),2)
        data.append({
            "day": i+1,
            "pnl": pnl
        })

    return {"chart":data}


# ==========================================
# 🎯 STRATEGY ANALYTICS
# ==========================================
@router.get("/strategy-analytics")
def strategy_analytics():

    strategies=["Scalp","Breakout","Swing","AI Auto","Mean Reversion"]

    data=[]
    for s in strategies:
        data.append({
            "strategy":s,
            "trades":random.randint(10,80),
            "pnl":round(random.uniform(-5000,12000),2),
            "winrate":random.randint(40,85)
        })

    return {"strategies":data}


# ==========================================
# 🧠 PSYCHOLOGY ANALYTICS
# ==========================================
@router.get("/psychology-report")
def psychology():

    return {
        "fomo_trades": random.randint(1,15),
        "revenge_trades": random.randint(1,10),
        "disciplined_trades": random.randint(10,50),
        "risk_violations": random.randint(1,8),
        "confidence_score": random.randint(60,95)
    }


# ==========================================
# 🏆 BEST TRADE
# ==========================================
@router.get("/best-trade")
def best_trade():

    if not trade_db:
        return {"msg":"no trades"}

    best=max(trade_db, key=lambda x:x["pnl"])
    return best


# ==========================================
# 💀 WORST TRADE
# ==========================================
@router.get("/worst-trade")
def worst_trade():

    if not trade_db:
        return {"msg":"no trades"}

    worst=min(trade_db, key=lambda x:x["pnl"])
    return worst


# ==========================================
# 🤖 AI COACH
# ==========================================
@router.get("/ai-coach")
def ai_coach():

    tips=[
        "Avoid revenge trading after losses",
        "Stick to risk 1% per trade",
        "Follow breakout confirmation",
        "Avoid overtrading in sideways market",
        "Best time to trade: London session"
    ]

    return {
        "coach_tip": random.choice(tips),
        "discipline_score": random.randint(60,95),
        "risk_control": random.randint(50,90)
    }

from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter()

# ==========================================
# 🔍 SEARCH ASSET / COMMAND
# ==========================================
@router.get("/search")
def search(q: str):
    assets = [
        {"symbol":"BTCUSDT","price":68432,"change":"+2.4%"},
        {"symbol":"ETHUSDT","price":3521,"change":"+1.1%"},
        {"symbol":"TSLA","price":174,"change":"-1.2%"},
        {"symbol":"AAPL","price":212,"change":"+0.8%"},
        {"symbol":"NVDA","price":910,"change":"+3.1%"},
    ]

    commands = [
        "/buy BTC",
        "/sell ETH",
        "/risk",
        "/backtest grid_bot",
        "/portfolio",
        "/ai-signal"
    ]

    return {
        "query": q,
        "assets": assets,
        "commands": commands
    }


# ==========================================
# 🤖 AI COMMAND EXECUTOR
# ==========================================
@router.post("/execute")
def execute_command(command:str):

    # BUY
    if command.startswith("/buy"):
        asset = command.split(" ")[1]
        return {
            "action":"BUY",
            "asset":asset,
            "price": random.randint(100,70000),
            "status":"order executed 🚀"
        }

    # SELL
    elif command.startswith("/sell"):
        asset = command.split(" ")[1]
        return {
            "action":"SELL",
            "asset":asset,
            "price": random.randint(100,70000),
            "status":"sell order placed 🔻"
        }

    # RISK
    elif command.startswith("/risk"):
        return {
            "portfolio_risk": round(random.uniform(1,5),2),
            "var": round(random.uniform(200,900),2),
            "message":"AI Risk calculated"
        }

    # BACKTEST
    elif command.startswith("/backtest"):
        return {
            "strategy":"Grid Bot v2",
            "profit":"18.4%",
            "winrate":"71%",
            "message":"Backtest completed"
        }

    # PORTFOLIO
    elif command.startswith("/portfolio"):
        return {
            "balance": 12450,
            "pnl": 4210,
            "positions":3
        }

    # AI SIGNAL
    elif command.startswith("/ai"):
        return {
            "signal":"STRONG BUY",
            "asset":"BTCUSDT",
            "confidence": random.randint(85,97)
        }

    else:
        return {
            "message":"Unknown command"
        }


# ==========================================
# 📊 RECENT ASSETS
# ==========================================
@router.get("/recent")
def recent_assets():
    return {
        "recent":[
            {"symbol":"BTCUSD","price":68432,"change":"+2.4%"},
            {"symbol":"TSLA","price":174,"change":"-1.2%"},
            {"symbol":"NVDA","price":910,"change":"+3.1%"}
        ]
    }


# ==========================================
# 🧠 AI RECOMMENDATIONS
# ==========================================
@router.get("/ai-setups")
def ai_setups():
    return {
        "signals":[
            {
                "asset":"NVDA",
                "type":"Breakout",
                "confidence":94,
                "target":925
            },
            {
                "asset":"AMD",
                "type":"RSI Divergence",
                "confidence":78,
                "target":165
            }
        ]
    }


# ==========================================
# 🖥 SYSTEM VERSION
# ==========================================
@router.get("/system")
def system():
    return {
        "version":"MarketMind AI v2.4.0",
        "status":"stable",
        "time": datetime.utcnow()
    }

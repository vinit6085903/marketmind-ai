from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

# =========================================
# 🔥 TRADE PREVIEW (modal data)
# =========================================
@router.get("/preview/{symbol}")
def trade_preview(symbol:str):

    price=random.randint(60000,70000)

    return {
        "symbol":symbol.upper(),
        "market":"Spot",
        "signal":"STRONG BUY",
        "volume":"2.5 Lots",
        "entry_price":price,
        "stop_loss":price-400,
        "take_profit":price+1800,
        "risk_amount":1250,
        "portfolio_impact":"1.25%",
        "liquidity":"Tier 1"
    }

# =========================================
# 🔥 EXECUTE TRADE
# =========================================
@router.post("/execute")
def execute_trade(
    symbol:str,
    volume:float,
    entry:float,
    sl:float,
    tp:float
):

    order_id=f"MM-{random.randint(100000,999999)}"

    return {
        "status":"EXECUTED",
        "order_id":order_id,
        "symbol":symbol,
        "volume":volume,
        "entry":entry,
        "stoploss":sl,
        "takeprofit":tp,
        "execution_price":entry + random.uniform(-10,10),
        "time":datetime.utcnow(),
        "message":"Trade executed successfully 🚀"
    }

# =========================================
# 🔥 CLOSE TRADE
# =========================================
@router.post("/close/{order_id}")
def close_trade(order_id:str):

    pnl=random.randint(-500,1500)

    return {
        "order_id":order_id,
        "status":"CLOSED",
        "pnl":pnl,
        "closed_time":datetime.utcnow()
    }

# =========================================
# 🔥 OPEN POSITIONS
# =========================================
@router.get("/positions")
def open_positions():

    positions=[
        {
            "order_id":"MM123456",
            "symbol":"BTC/USD",
            "type":"BUY",
            "entry":64200,
            "current":65100,
            "pnl":900
        },
        {
            "order_id":"MM789654",
            "symbol":"ETH/USD",
            "type":"BUY",
            "entry":3400,
            "current":3520,
            "pnl":320
        }
    ]

    return {"positions":positions}

# =========================================
# 🔥 ORDER HISTORY
# =========================================
@router.get("/history")
def trade_history():

    history=[]
    for i in range(10):
        history.append({
            "order_id":f"MM{random.randint(10000,99999)}",
            "symbol":"BTC/USD",
            "type":"BUY",
            "profit":random.randint(-500,2000),
            "date":str(datetime.utcnow())
        })

    return {"history":history}

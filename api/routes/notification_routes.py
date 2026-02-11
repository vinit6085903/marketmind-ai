from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter()

# =========================================
# 🔥 ALL NOTIFICATIONS
# =========================================
@router.get("/")
def get_notifications():

    notifications = [
        {
            "id":1,
            "type":"BUY",
            "symbol":"BTC/USDT",
            "confidence":92,
            "entry":64230,
            "sl":63800,
            "time":"2m ago",
            "status":"NEW"
        },
        {
            "id":2,
            "type":"SELL",
            "symbol":"ETH/USD",
            "confidence":81,
            "price":2450,
            "trend":"Bearish",
            "time":"14m ago"
        },
        {
            "id":3,
            "type":"UPDATE",
            "title":"TSLA Sentiment Shift",
            "message":"Institutional whales buying detected. Sentiment changed to Bullish",
            "time":"1h ago"
        }
    ]

    return {"notifications":notifications}

# =========================================
# 🔥 CREATE SIGNAL NOTIFICATION
# =========================================
@router.post("/create-signal")
def create_signal(symbol:str, signal:str):

    return {
        "message":"Signal created",
        "symbol":symbol,
        "signal":signal,
        "time":datetime.utcnow()
    }

# =========================================
# 🔥 MARK ALL READ
# =========================================
@router.post("/mark-read")
def mark_all_read():
    return {"status":"All notifications marked as read"}

# =========================================
# 🔥 TRADE FROM NOTIFICATION
# =========================================
@router.post("/trade/{symbol}")
def trade_from_notification(symbol:str):

    order_id = f"ORD-{random.randint(10000,99999)}"

    return {
        "status":"EXECUTED",
        "symbol":symbol,
        "order_id":order_id,
        "message":"Trade executed from notification 🚀"
    }

# =========================================
# 🔥 BOOKMARK SIGNAL
# =========================================
@router.post("/bookmark/{id}")
def bookmark_signal(id:int):
    return {"message":f"Notification {id} bookmarked"}

# =========================================
# 🔥 SYSTEM ALERTS
# =========================================
@router.get("/system")
def system_alerts():

    alerts=[
        {
            "title":"Order Executed",
            "msg":"Order #8829 filled at $2448",
            "type":"success"
        },
        {
            "title":"Server Update",
            "msg":"AI engine upgraded v2.1",
            "type":"info"
        }
    ]

    return {"system_alerts":alerts}

# =========================================
# 🔥 SECURITY ALERTS
# =========================================
@router.get("/security")
def security_alerts():
    return {
        "security":[
            {
                "title":"New Login",
                "location":"New York",
                "time":"5 min ago"
            },
            {
                "title":"API Key Used",
                "time":"10 min ago"
            }
        ]
    }

# =========================================
# 🔥 MARGIN WARNING
# =========================================
@router.get("/margin-warning")
def margin_warning():

    return {
        "warning":"Account leverage exceeding 10x",
        "level":"HIGH",
        "action":"Reduce position or add funds"
    }

from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

# =========================================
# 🔥 EXCHANGES STATUS
# =========================================
@router.get("/exchanges")
def exchanges():

    return {
        "exchanges":[
            {"name":"Binance","status":"Connected","type":"Trading & Staking"},
            {"name":"Coinbase","status":"Connected","type":"Read Only"},
            {"name":"Interactive Brokers","status":"Disconnected","type":"Stocks/Forex"},
            {"name":"MetaTrader 5","status":"Disconnected","type":"Forex"}
        ]
    }

# =========================================
# 🔥 ACTIVE API KEYS
# =========================================
@router.get("/api-keys")
def api_keys():

    keys=[
        {
            "name":"Main Trading Bot Alpha",
            "exchange":"Binance",
            "permissions":["Read","Trade"],
            "created":"2023-11-12",
            "status":"Active"
        },
        {
            "name":"Analytics Fetcher",
            "exchange":"Coinbase",
            "permissions":["Read"],
            "created":"2024-01-05",
            "status":"Active"
        },
        {
            "name":"Arbitrage Scanner",
            "exchange":"Kraken",
            "permissions":["Read","Trade"],
            "created":"2023-08-19",
            "status":"Disabled"
        }
    ]

    return {"api_keys":keys}

# =========================================
# 🔥 CREATE NEW API KEY
# =========================================
@router.post("/generate-key")
def generate_key():

    key=f"MM-{random.randint(100000,999999)}"
    secret=f"SEC-{random.randint(100000,999999)}"

    return {
        "api_key":key,
        "secret":secret,
        "created":datetime.utcnow()
    }

# =========================================
# 🔥 DELETE KEY
# =========================================
@router.delete("/delete/{name}")
def delete_key(name:str):
    return {"message":f"{name} deleted successfully"}

# =========================================
# 🔥 SECURITY HEALTH
# =========================================
@router.get("/security-score")
def security_score():

    score=random.randint(85,100)

    return {
        "security_score":score,
        "status":"Highly Secure" if score>90 else "Moderate"
    }

# =========================================
# 🔥 2FA STATUS
# =========================================
@router.get("/2fa")
def twofa():
    return {
        "enabled":True,
        "method":"Google Authenticator",
        "last_used":"2 min ago"
    }

# =========================================
# 🔥 IP WHITELIST
# =========================================
@router.get("/ip-whitelist")
def ip_whitelist():
    return {
        "ips":[
            {"ip":"192.168.1.104","label":"Office"},
            {"ip":"14.12.98.241","label":"AWS Bot"}
        ]
    }

# =========================================
# 🔥 LOGIN SESSION INFO
# =========================================
@router.get("/session")
def session_info():
    return {
        "location":"New York, USA",
        "device":"MacBook Pro M2",
        "ip":"192.168.1.104",
        "last_login":"2 min ago"
    }

from fastapi import APIRouter
import random

router = APIRouter()

# ===============================
# 🔥 TOP RISK METRICS
# ===============================
@router.get("/metrics")
def risk_metrics():
    return {
        "var_value": 124500,
        "var_confidence": "+0.5%",
        "drawdown": 4.21,
        "drawdown_today": -1.2,
        "margin_utilization": 68.5,
        "margin_limit": 85,
        "risk_exposure": 1.42
    }

# ===============================
# 🔥 CORRELATION MATRIX
# ===============================
@router.get("/correlation")
def correlation_matrix():
    return {
        "assets": ["EUR/USD", "BTC/USD", "S&P500", "GOLD", "OIL"],
        "matrix": [
            [1.00, 0.42, 0.12, 0.55, -0.18],
            [0.42, 1.00, 0.68, 0.05, 0.22],
            [0.12, 0.68, 1.00, -0.35, 0.41],
            [0.55, 0.05, -0.35, 1.00, 0.48],
        ]
    }

# ===============================
# 🔥 WHAT IF SIMULATION
# ===============================
@router.post("/simulate")
def what_if(entry_price: float, stop_loss_percent: float, asset: str):
    
    var_change = random.randint(2000,8000)
    drawdown_change = round(random.uniform(0.1,0.8),2)

    return {
        "asset": asset,
        "entry_price": entry_price,
        "stop_loss": stop_loss_percent,
        "projected_var_change": var_change,
        "drawdown_increase": drawdown_change
    }

# ===============================
# 🔥 STRESS TEST
# ===============================
@router.get("/stress/{scenario}")
def stress_test(scenario: str):

    scenarios = {
        "2008": {"loss": -900000, "recovery_days": 220, "survival": 70},
        "covid": {"loss": -600000, "recovery_days": 120, "survival": 82},
        "flash": {"loss": -1240000, "recovery_days": 142, "survival": 84}
    }

    data = scenarios.get(scenario.lower(), scenarios["flash"])

    return {
        "scenario": scenario.upper(),
        "estimated_loss": data["loss"],
        "recovery_days": data["recovery_days"],
        "survivability": data["survival"]
    }

# ===============================
# 🔥 VIX VOLATILITY
# ===============================
@router.get("/volatility")
def volatility():
    current = round(random.uniform(18,35),1)

    return {
        "vix": current,
        "status": "LOW" if current<20 else "MODERATE" if current<30 else "HIGH",
        "historical_avg": 18.2,
        "crisis_peak": 82.4
    }

# ===============================
# 🔥 AI REBALANCE
# ===============================
@router.post("/rebalance")
def ai_rebalance():

    return {
        "msg": "AI Portfolio Rebalanced ⚡",
        "actions": [
            "Reduced BTC exposure 5%",
            "Increased Gold hedge 3%",
            "Adjusted Forex risk"
        ]
    }

# ===============================
# 🔥 ALERTS SIDEBAR
# ===============================
@router.get("/alerts")
def alerts():
    return {
        "alerts": [
            {"msg": "USD/JPY SIGNAL", "type": "info"},
            {"msg": "VOL BREACH", "type": "danger"},
            {"msg": "AI REBALANCING", "type": "primary"},
            {"msg": "MARGIN OK", "type": "success"},
        ]
    }

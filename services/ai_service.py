import random

def predict_signal(symbol: str):
    signals = ["BUY 📈", "SELL 📉", "HOLD ⏳"]

    return {
        "symbol": symbol.upper(),
        "ai_signal": random.choice(signals),
        "confidence": f"{random.randint(70,95)}%"
    }

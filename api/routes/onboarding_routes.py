from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter()

# ==========================================
# 🧠 ONBOARDING STATUS
# ==========================================
@router.get("/status")
def onboarding_status():

    return {
        "user":"pro_trader",
        "plan":"PRO",
        "completed": False,
        "current_step": 1,
        "total_steps": 5,
        "progress_percent": 20,
        "ai_assistant":"MarketMind Neural Guide"
    }


# ==========================================
# 📘 ONBOARDING STEPS
# ==========================================
@router.get("/steps")
def onboarding_steps():

    return [
        {
            "step":1,
            "title":"Platform Introduction",
            "desc":"Understand dashboard, signals & AI engine",
            "completed":False
        },
        {
            "step":2,
            "title":"Connect Exchange",
            "desc":"Connect Binance, Bybit or broker",
            "completed":False
        },
        {
            "step":3,
            "title":"Risk Profile Setup",
            "desc":"Set capital & risk management",
            "completed":False
        },
        {
            "step":4,
            "title":"AI Strategy Selection",
            "desc":"Choose scalping, swing or macro AI",
            "completed":False
        },
        {
            "step":5,
            "title":"Live Trading Ready",
            "desc":"Activate AI engine",
            "completed":False
        }
    ]


# ==========================================
# ➡️ NEXT STEP
# ==========================================
@router.post("/next-step")
def next_step(step:int):

    next_s = step + 1
    progress = int((next_s/5)*100)

    return {
        "current_step": next_s,
        "progress_percent": progress,
        "message": f"Step {next_s} activated",
        "ai_voice":"Onboarding progressing..."
    }


# ==========================================
# ⬅️ BACK STEP
# ==========================================
@router.post("/prev-step")
def prev_step(step:int):

    prev_s = max(1, step-1)
    progress = int((prev_s/5)*100)

    return {
        "current_step": prev_s,
        "progress_percent": progress,
        "message":"Moved back"
    }


# ==========================================
# ⏭ SKIP TOUR
# ==========================================
@router.post("/skip")
def skip_onboarding():

    return {
        "status":"skipped",
        "redirect":"dashboard",
        "ai_msg":"Welcome directly to MarketMind Pro"
    }


# ==========================================
# 🎯 COMPLETE ONBOARDING
# ==========================================
@router.post("/complete")
def complete_onboarding():

    return {
        "status":"completed",
        "ai_engine":"Activated",
        "welcome_msg":"You are now fully onboarded 🚀",
        "timestamp":str(datetime.utcnow())
    }


# ==========================================
# 🤖 AI INTRO MESSAGE
# ==========================================
@router.get("/ai-intro")
def ai_intro():

    msgs=[
        "Welcome trader. Initializing neural engines.",
        "Scanning markets & preparing alpha signals.",
        "Your AI trading environment is ready.",
        "Institutional-grade tools unlocked."
    ]

    return {
        "ai_name":"MarketMind AI",
        "message": random.choice(msgs),
        "voice_enabled": True
    }

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

# ==============================
# 👤 USER PROFILE DATA
# ==============================
@router.get("/")
def get_profile():
    return {
        "name": "Alex Thorne",
        "role": "Lead Quant Strategist",
        "firm": "Global Quant Partners",
        "member_since": "Oct 2021",
        "accuracy": 98.4,
        "plan": "Hedge Fund Pro"
    }


# ==============================
# ✏️ UPDATE PROFILE
# ==============================
@router.post("/update")
def update_profile(name:str, firm:str):
    return {
        "message": "Profile updated successfully",
        "name": name,
        "firm": firm,
        "updated_at": datetime.utcnow()
    }


# ==============================
# 🎨 THEME SETTINGS
# ==============================
@router.get("/theme")
def get_theme():
    return {
        "theme": "neon_blue",
        "opacity": 65,
        "blur": 12,
        "glow": True
    }


@router.post("/theme/update")
def update_theme(theme:str, opacity:int, blur:int, glow:bool):
    return {
        "message": "Theme updated",
        "theme": theme,
        "opacity": opacity,
        "blur": blur,
        "glow": glow
    }


# ==============================
# 🔔 NOTIFICATION SETTINGS
# ==============================
@router.get("/notifications")
def get_notification_settings():
    return {
        "sound": True,
        "desktop": True,
        "sms": False
    }


@router.post("/notifications/update")
def update_notification_settings(sound:bool, desktop:bool, sms:bool):
    return {
        "message": "Notification settings updated",
        "sound": sound,
        "desktop": desktop,
        "sms": sms
    }


# ==============================
# 🖥 TERMINAL PRESET
# ==============================
@router.get("/terminal")
def get_terminal_settings():
    return {
        "preset": "tradingview_pro",
        "shortcuts": {
            "buy":"ALT+B",
            "sell":"ALT+S",
            "clear":"CTRL+D"
        }
    }


@router.post("/terminal/update")
def update_terminal(preset:str):
    return {
        "message":"Terminal preset updated",
        "preset":preset
    }


# ==============================
# 🔐 SECURITY SETTINGS
# ==============================
@router.get("/security")
def security_status():
    return {
        "2FA": True,
        "api_keys": 3,
        "last_login": "Today",
        "location": "New York"
    }


# ==============================
# 💾 SAVE ALL SETTINGS BUTTON
# ==============================
@router.post("/save-all")
def save_all_settings():
    return {
        "status":"success",
        "message":"All configuration saved successfully 🚀"
    }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import market_routes, ai_routes

app = FastAPI(title="MarketMind AI", version="1.0")

# CORS (frontend connect ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes include
app.include_router(market_routes.router, prefix="/market", tags=["Market"])
app.include_router(ai_routes.router, prefix="/ai", tags=["AI"])

@app.get("/")
def home():
    return {"message": "MarketMind AI running "}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import dashboard_routes, trade_routes, ai_routes

app = FastAPI(title="MarketMind AI Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard_routes.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(trade_routes.router, prefix="/trades", tags=["Trades"])
app.include_router(ai_routes.router, prefix="/ai", tags=["AI"])

@app.get("/")
def home():
    return {"msg": "MarketMind AI running "}

from api.routes import risk_routes

app.include_router(risk_routes.router, prefix="/risk", tags=["Risk Engine"])

from api.routes import portfolio_routes

app.include_router(portfolio_routes.router, prefix="/portfolio", tags=["Portfolio"])
from api.routes import backtest_routes

app.include_router(backtest_routes.router, prefix="/backtest", tags=["Backtester"])

from api.routes import sentiment_routes

app.include_router(sentiment_routes.router, prefix="/sentiment", tags=["AI Sentiment"])

from api.routes import screener_routes

app.include_router(screener_routes.router, prefix="/screener", tags=["AI Screener"])

from api.routes import settings_routes

app.include_router(
    settings_routes.router,
    prefix="/settings",
    tags=["Settings & API"]
)

from api.routes import trade_routes

app.include_router(
    trade_routes.router,
    prefix="/trade",
    tags=["AI Trading Engine"]
)

from api.routes import notification_routes

app.include_router(
    notification_routes.router,
    prefix="/notifications",
    tags=["Notification Center"]
)

from api.routes import profile_routes

app.include_router(
    profile_routes.router,
    prefix="/profile",
    tags=["User Profile & Settings"]
)


from api.routes import dashboard_routes

app.include_router(
    dashboard_routes.router,
    prefix="/dashboard",
    tags=["AI Trading Dashboard"]
)

from api.routes import sync_routes

app.include_router(
    sync_routes.router,
    prefix="/sync",
    tags=["Global Sync Engine"]
)

from api.routes import command_routes

app.include_router(
    command_routes.router,
    prefix="/command",
    tags=["AI Command Bar"]
)

from api.routes import sync_dashboard_routes

app.include_router(
    sync_dashboard_routes.router,
    prefix="/sync",
    tags=["MarketMind Sync Dashboard"]
)

from api.routes import heatmap_routes

app.include_router(
    heatmap_routes.router,
    prefix="/heatmap",
    tags=["Global Market Heatmap"]
)

from api.routes import trade_journal_routes

app.include_router(
    trade_journal_routes.router,
    prefix="/journal",
    tags=["AI Trade Journal"]
)

from api.routes import correlation_routes

app.include_router(
    correlation_routes.router,
    prefix="/correlation",
    tags=["AI Correlation Engine"]
)

from api.routes import volatility_routes

app.include_router(
    volatility_routes.router,
    prefix="/volatility",
    tags=["AI Volatility Engine"]
)
from api.routes import optimizer_routes

app.include_router(
    optimizer_routes.router,
    prefix="/optimizer",
    tags=["AI Strategy Optimizer"]
)

from api.routes import macro_routes

app.include_router(
    macro_routes.router,
    prefix="/macro",
    tags=["Global Macro AI"]
)

from api.routes import orderflow_routes

app.include_router(
    orderflow_routes.router,
    prefix="/orderflow",
    tags=["Orderflow AI"]
)



from api.routes import onboarding_routes

app.include_router(
    onboarding_routes.router,
    prefix="/onboarding",
    tags=["Onboarding AI"]
)


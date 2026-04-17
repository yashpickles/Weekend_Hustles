import os
from pathlib import Path

# --- Project Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "db" / "finance_council.db"
MOM_OUTPUT_DIR = BASE_DIR / "data" / "outputs"

# --- Hardware / Model Config ---
# Using OpenAI client (compatible with Ollama/vLLM)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_API_KEY = "ollama"  # Logic doesn't check key, but client might need one

# Models (as per V2 spec)
MODEL_STRATEGIST = "llama3.1:8b-instruct-q4_K_M"
MODEL_QUANT = "phi3.5:3.8b" 
MODEL_RISK = "gemma2:2b"
MODEL_CRITIC = "llama3.1:8b-instruct-q4_K_M"
MODEL_ORCHESTRATOR = "gemma2:2b"

# --- Asset Universe (V2 Section 3.1) ---
ASSETS = {
    "INDEX_CORE": "^NSEI",       # Nifty 50
    "INDEX_CONFIRM": "^BSESN",   # Sensex
    "VOLATILITY": "^INDIAVIX",   # India VIX
    "COMMODITY_GOLD": "GOLDBEES.NS",
    "COMMODITY_GLOBAL": "GC=F",  # Gold Futures
    "COMMODITY_OIL": "CL=F",     # Crude Oil
    "CURRENCY": "INR=X",         # USD/INR
    "CASH": "LIQUIDBEES.NS"
}

# --- Regime Constants (V2 Section 4) ---
# "Regime precedes Indicator"
REGIME_THRESHOLDS = {
    "ADX_TRENDING": 25,
    "VIX_CRASH": 22,
    "EMA_SHORT": 50,
    "EMA_LONG": 200,
}

# --- Risk Constitution (V2 Section 7) ---
CAPITAL_BASE = 100000.0  # INR

RISK_LIMITS = {
    "MAX_EQUITY": 0.50,      # 50%
    "MAX_COMMODITY": 0.20,   # 20% (Gold + Oil)
    "MAX_OIL": 0.10,         # 10% (Sub-limit for Oil)
    "MAX_CURRENCY": 0.10,    # 10% (Hedge only)
    "SINGLE_ASSET": 0.15,    # 15%
    "EMERGENCY_BUFFER": 0.20 # 20% (from Risk Officer prompt) -- V2 prompt says 30% "if unsure", V1 said 20%. Sticking to stricter safe buffer.
}

REBALANCE_TRIGGER = {
    "DRIFT_PCT": 0.05,       # 5%
    "DRAWDOWN_FREEZE": 0.10  # 10%
}

# --- PMS Configuration (Systematic Monthly Investment) ---
PMS_CONFIG = {
    "MONTHLY_BUDGET": 100000.0,
    "REVIEW_MONTHS": 6,
    "DB_PATH": BASE_DIR / "data" / "pms_portfolio.json"
}

STOCK_UNIVERSE = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "SBIN.NS", "BHARTIARTL.NS", "ITC.NS", "KOTAKBANK.NS",
    "LICI.NS", "LT.NS", "AXISBANK.NS", "ASIANPAINT.NS", "HCLTECH.NS",
    "MARUTI.NS", "TITAN.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS", "BAJFINANCE.NS",
    "WIPRO.NS", "TATAMOTORS.NS", "M&M.NS", "ADANIENT.NS", "POWERGRID.NS",
    "NTPC.NS", "JSWSTEEL.NS", "TATASTEEL.NS", "ONGC.NS", "HINDALCO.NS",
    "GRASIM.NS", "COALINDIA.NS", "SBILIFE.NS", "BAJAJFINSV.NS", "BRITANNIA.NS",
    "TECHM.NS", "DRREDDY.NS", "CIPLA.NS", "DIVISLAB.NS", "APOLLOHOSP.NS",
    "EICHERMOT.NS", "HEROMOTOCO.NS", "TATACONSUM.NS", "BPCL.NS", "INDUSINDBK.NS",
    "NESTLEIND.NS", "BAJAJ-AUTO.NS", "UPL.NS", "ADANIPORTS.NS", "SHRIRAMFIN.NS"
]

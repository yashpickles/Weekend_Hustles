# AI Council PMS V1 - Portfolio Management System
> **"The Council of Kangs"** - Multi-Agent AI Portfolio Manager

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-orange.svg)](https://ollama.ai/)

## Overview

PMS V1 is an **autonomous AI-powered portfolio management system** that uses multiple LLM agents to make investment decisions. Built to run on consumer hardware (RTX 4080), it manages a ₹100,000 monthly SIP across Indian equities using a momentum-based strategy.

### Key Features
- 🤖 **Multi-Agent Architecture**: Quant analyst + Strategist working together
- 📊 **Momentum Strategy**: ADX-based trend following
- 💰 **Monthly SIP**: Systematic ₹100K investment
- 📈 **Nifty 50 Benchmark**: Performance tracking vs passive index
- 🔄 **Semi-Annual Rebalancing**: -5% stop-loss trigger
- 📝 **Transparent Reports**: Detailed monthly statements

---

## Architecture

```
┌─────────────────────────────────────────────┐
│         Data Layer (fetcher.py)             │
│  • Yahoo Finance API                        │
│  • Technical Indicators (ADX, RSI, EMA)     │
│  • Momentum Screening (Top 5)               │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│        Agent Layer (LLMs via Ollama)        │
│  ┌──────────────┐      ┌────────────────┐   │
│  │ Quant Agent  │──────▶│ Strategist    │   │
│  │ (phi3.5)     │      │ (llama3.1:8b)  │   │
│  │ Pick 2-3     │      │ Allocate %     │   │
│  └──────────────┘      └────────────────┘   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│    Portfolio Manager (manager.py)           │
│  • JSON-based storage                       │
│  • Buy/Sell execution                       │
│  • Performance tracking                     │
│  • Benchmark shadow ledger                  │
└─────────────────────────────────────────────┘
```

---

## Installation

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- NVIDIA GPU with 8GB+ VRAM (recommended)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/ai-council-pms.git
cd ai-council-pms/PMS_V1
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- yfinance
- pandas
- pandas_ta
- openai (for Ollama API compatibility)

### Step 3: Download LLM Models
```bash
# Install required Ollama models
ollama pull llama3.1:8b-instruct-q4_K_M
ollama pull phi3.5:3.8b
```

### Step 4: Verify Ollama is Running
```bash
curl http://localhost:11434/api/tags
```

---

## Usage

### Quick Start
```bash
# Run backtest on Jan 2023 - Sept 2025
python scripts/simulate_pms.py
```

### Configuration
Edit `config/settings.py` to customize:

| Setting | Default | Description |
|---------|---------|-------------|
| `MONTHLY_BUDGET` | ₹100,000 | SIP amount per month |
| `STOCK_UNIVERSE` | Nifty 50 | Stock screening universe |
| `MODEL_QUANT` | phi3.5:3.8b | Stock picker LLM |
| `MODEL_STRATEGIST` | llama3.1:8b | Allocator LLM |

### Output
Results are saved to `data/outputs/MOM_PMS.md`:
```markdown
# PMS Monthly Statement: 2023-01-01
Portfolio Value: ₹100,000 | Cash: ₹20,000

## 1. Portfolio Snapshot
| Ticker | Price | Return % | Value |
|--------|-------|----------|-------|
| RELIANCE.NS | ₹2,500 | +5.2% | ₹12,500 |

## 2. Stock Screener (Top Candidates)
[
  {"ticker": "RELIANCE.NS", "adx": 32.5, "rsi": 45.2, "trend": "UPTREND"}
]

## 3. Quant Selection
Picks: ['RELIANCE.NS', 'INFY.NS']
Rationale: Strong momentum indicators...

## 4. Strategist Allocation
{
  "RELIANCE.NS": "30%",
  "INFY.NS": "20%",
  "GOLDBEES.NS": "10%",
  "LIQUIDBEES.NS": "40%"
}

## Performance Comparison (v. Nifty 50 SIP)
| Portfolio Return | +5.2% |
| Benchmark Return | +4.8% |
| Alpha | +0.4% |
```

---

## Strategy Details

### Momentum Screening Criteria
Stocks must pass all 3 filters:
1. **ADX > 25** (strong trend)
2. **Price > EMA(200)** (long-term uptrend)
3. **RSI < 70** (not overbought)

### Risk Management
| Rule | Value |
|------|-------|
| Max Equity | 60% |
| Max Gold | 20% |
| Min Debt | 20% |
| Stop-Loss | -5% (semi-annual) |

### Allocation Constraints
- **Systematic**: ₹100,000 invested **every month**
- **Conservative**: Minimum 20% in LIQUIDBEES (safety buffer)
- **Benchmark**: Nifty 50 SIP for comparison

---

## File Structure

```
PMS_V1/
├── config/
│   └── settings.py          # Configuration constants
├── data/
│   ├── db/
│   │   └── pms_portfolio.json  # Portfolio state
│   └── outputs/
│       └── MOM_PMS.md       # Monthly reports
├── scripts/
│   ├── simulate_pms.py      # Main backtest script
│   └── run_pms_now.py       # Live mode (for future)
├── src/
│   ├── agents/
│   │   └── client.py        # Ollama LLM client
│   ├── data/
│   │   └── fetcher.py       # Yahoo Finance + screening
│   └── pms/
│       ├── manager.py       # Portfolio operations
│       └── pms_orchestrator.py  # Main controller
└── requirements.txt
```

---

## How It Works: Monthly Cycle

```python
# Pseudocode for monthly investment cycle

1. DEPOSIT ₹100,000 into portfolio
2. SCREEN Nifty 50 stocks (momentum filter)
   → Returns top 5 candidates

3. QUANT AGENT (phi3.5:3.8b)
   Input: Top 5 stocks with ADX, RSI, EMA data
   Output: Select 2-3 best stocks + reasoning
   
4. REBALANCE CHECK (every 6 months)
   If any stock < -5% return:
     → SELL entire position
   
5. STRATEGIST AGENT (llama3.1:8b)
   Input: Selected stocks, portfolio value, budget
   Output: Allocation percentages
   Example: {"RELIANCE.NS": "30%", "GOLDBEES.NS": "10%", ...}
   
6. EXECUTE ORDERS
   - Buy stocks at current prices
   - Sweep idle cash into LIQUIDBEES
   
7. GENERATE REPORT
   - Calculate returns
   - Compare vs Nifty 50 benchmark
   - Save to MOM_PMS.md
```

---

## Performance (Example: Jan 2023 - Sept 2025)

| Metric | Value |
|--------|-------|
| Total Invested | ₹3,300,000 (33 months × ₹100K) |
| Portfolio Value | ~₹3,500,000 (example) |
| Absolute Return | ~+6% |
| Nifty 50 Return | ~+5% |
| **Alpha** | **+1%** |

> ⚠️ **Note**: Actual results vary based on market conditions. V1 uses basic momentum strategy without advanced risk management.

---

## Limitations

### Known Issues
1. **Yahoo Finance Data**: Uses dividend-adjusted prices (may not match exact execution prices)
2. **Relaxed Risk Management**: 60% max equity, -5% stop-loss (too lenient)
3. **Single Strategy**: Only momentum, fails in sideways markets
4. **No Concentration Limits**: Can over-allocate to single stocks
5. **Semi-Annual Rebalancing**: Should be monthly for faster responses
---

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'yfinance'"
```bash
pip install -r requirements.txt
```

### Error: "Connection refused to localhost:11434"
```bash
# Start Ollama service
ollama serve
```

### Models too slow?
Use smaller/quantized models:
```python
# In config/settings.py
MODEL_STRATEGIST = "llama3.1:8b-instruct-q4_K_M"  # 4-bit quantization
```

---

## Development

### Run Tests
```bash
python -m pytest tests/
```

### Add New Stocks
Edit `STOCK_UNIVERSE` in `config/settings.py`:
```python
STOCK_UNIVERSE = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS",
    # Add your stocks here (must have .NS suffix for NSE)
]
```

---

## Roadmap

- [x] V1: Basic momentum strategy
- [ ] V2: Multi-benchmark, shadow ledger
- [ ] V3: Risk management, True_Close prices
- [ ] V4: Multi-strategy (value + mean reversion)
- [ ] V5: Live trading integration

---

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Citation

If you use this in your research/project:
```
@software{ai_council_pms_v1,
  title = {AI Council PMS V1: Multi-Agent Portfolio Manager},
  author = {Your Name},
  year = {2023},
  url = {https://github.com/yashpickles/Weekend_Hustles/AI_Council/PMS/PMS_V1}
}
```

---

## Contact

- GitHub Issues: [Submit Bug Reports](https://github.com/yashpickles/Weekend_Hustles/AI_Council/PMS/PMS_V1/issues)
- Email: yashsa1311@gmail.com

---

**Disclaimer**: This is an experimental research project. Not financial advice. Past performance does not guarantee future results. Use at your own risk.

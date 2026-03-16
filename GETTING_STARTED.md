# Mantle-Flow AI Agent - Getting Started Guide

**Complete implementation roadmap for building a DeFi AI Agent on Mantle Layer 2**

---

## What You Have

This project contains everything you need to build and deploy Mantle-Flow, an AI-powered DeFi agent for Mantle Layer 2:

### 📋 Documentation Files (7 files)

1. **IMPLEMENTATION_GUIDE.md** - Complete 7-phase development roadmap (40 KB)
   - Phase 1: Local development setup
   - Phase 2: Core agent development
   - Phase 3: Smart contract integration
   - Phase 4: Backend & database setup
   - Phase 5: Testing & validation
   - Phase 6: Testnet deployment
   - Phase 7: Mainnet deployment

2. **TECH_STACK_SUMMARY.md** - Technology reference (20 KB)
   - All required tools and libraries
   - API keys and services needed
   - Installation commands
   - Cost estimates
   - Development workflow

3. **QUICKSTART_CHECKLIST.md** - 30-minute quick start (8 KB)
   - Step-by-step setup instructions
   - Copy-paste commands
   - Verification checklist
   - Troubleshooting guide

4. **MANTLE_FLOW_BLUEPRINT.md** - Technical architecture (72 KB)
   - System architecture diagrams
   - 3 Mantle-native skills
   - 3 complex conversation examples
   - Gas cost analysis
   - Database schema

5. **README_MANTLE_FLOW.md** - Quick overview
6. **mantle_flow_demo.py** - Working Python demo (15 KB)
7. **MANTLE_BOUNTY_SUBMISSION.md** - Formal submission

---

## Quick Start (5 minutes)

### 1. Read First
Open and read in this order:
1. **QUICKSTART_CHECKLIST.md** - Get setup in 30 minutes
2. **TECH_STACK_SUMMARY.md** - Understand tools needed
3. **IMPLEMENTATION_GUIDE.md** - Full development roadmap

### 2. Get API Keys (5 minutes)

**Anthropic Claude:**
- Visit https://console.anthropic.com/account/keys
- Create new API key
- Copy: `sk-ant-xxxxx`

**Supabase:**
- Visit https://supabase.com
- Create new project
- Get SUPABASE_URL and SUPABASE_ANON_KEY

**That's it!** Mantle RPC and Bitget API are public and free.

### 3. Setup (30 minutes)

Follow QUICKSTART_CHECKLIST.md steps 1-10:
```bash
# 1. Install Python 3.11
python --version  # Should be 3.11+

# 2. Create project
mkdir mantle-flow-agent
cd mantle-flow-agent

# 3. Virtual environment
python -m venv venv
source venv/bin/activate

# 4. Create .env with your API keys
cat > .env << 'EOF'
ANTHROPIC_API_KEY=sk-ant-your-key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-key
SUPABASE_SERVICE_ROLE_KEY=your-key
MANTLE_RPC_URL=https://rpc.mantle.xyz
MANTLE_CHAIN_ID=5000
EOF

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run demo
python run_demo_auto.py
```

**Done!** You now have a working DeFi AI agent running locally.

---

## Development Phases

### Phase 1: Local Setup (30 min)
- ✓ Python environment
- ✓ Dependencies installed
- ✓ API keys configured
- ✓ Project structure created

**Reference:** QUICKSTART_CHECKLIST.md

### Phase 2: Core Agent (2-3 hours)
- Build intent parser (Claude NLP)
- Create transaction builder
- Integrate Bitget Wallet SDK
- Setup configuration module

**Reference:** IMPLEMENTATION_GUIDE.md Phase 2

### Phase 3: Smart Contracts (2-3 hours)
- Setup contract ABIs
- Create contract service
- Implement staking operations
- Setup DEX integration

**Reference:** IMPLEMENTATION_GUIDE.md Phase 3

### Phase 4: Database (1-2 hours)
- Create Supabase schema
- Setup RLS policies
- Create Supabase service
- Implement transaction logging

**Reference:** IMPLEMENTATION_GUIDE.md Phase 4

### Phase 5: Testing (1-2 hours)
- Write unit tests
- Create integration tests
- Implement code coverage
- Test security audit

**Reference:** IMPLEMENTATION_GUIDE.md Phase 5

### Phase 6: Testnet (2-3 hours)
- Deploy to Mantle Sepolia
- Get testnet MNT from faucet
- Test all 3 skills
- Verify transactions

**Reference:** IMPLEMENTATION_GUIDE.md Phase 6

### Phase 7: Mainnet (2-3 hours)
- Deployment checklist
- Final testing
- Production monitoring
- Mainnet deployment

**Reference:** IMPLEMENTATION_GUIDE.md Phase 7

**Total Time:** 11-17 hours of development

---

## Key Technologies

| Component | Technology | Why |
|-----------|-----------|-----|
| Language | Python 3.11+ | Best web3 support, fast dev |
| AI/NLP | Claude 3.5 Sonnet | State-of-the-art intent parsing |
| Blockchain | Web3.py + eth-account | Ethereum/Mantle integration |
| API | FastAPI | Modern, async-ready |
| Database | Supabase (PostgreSQL) | Built-in auth, RLS, real-time |
| Network | Mantle Layer 2 | 99.9% cheaper gas than Ethereum |

---

## The 3 Core Skills

### Skill #1: mETH Staking
```
User: "Stake 100 MNT"
Agent:
  1. Check balance → ✓ Has 100 MNT
  2. Get current APY → 5.2%
  3. Build stake tx → 150,000 gas estimated
  4. Ask confirmation → "Stake 100 MNT for 5.2% APY?"
  5. Execute on Mantle → tx confirmed in 2s
  6. Report: "Staked! Earn ~5.2 MNT/year"
```

### Skill #2: DEX Swap
```
User: "Swap 50 MNT for USDC"
Agent:
  1. Check balance → ✓ Has 50 MNT
  2. Quote best route → Via Moe DEX
  3. Get output amount → ~162 USDC
  4. Ask confirmation → "Get 162 USDC for 50 MNT?"
  5. Execute swap → tx confirmed in 2s
  6. Report: "Swapped! You got 162 USDC"
```

### Skill #3: Bridge MNT
```
User: "Bridge 100 MNT to Ethereum"
Agent:
  1. Check L2 balance → ✓ Has 100 MNT
  2. Check L1 balance → 0 ETH (needs for gas)
  3. Suggest: "Need ETH for gas. Bridge 101 MNT?"
  4. Execute bridge → Wait 7 days for L2→L1
  5. Report: "100 MNT will arrive on Ethereum in 7 days"
```

---

## Architecture Overview

```
User Input (Voice/Text)
        ↓
NLP Parser (Claude 3.5)
        ↓
Intent: "Stake 100 MNT"
        ↓
Agent Decision Engine
  ├→ Bitget API (check balance, prices)
  ├→ Mantle RPC (read contracts)
  └→ Supabase (store transaction)
        ↓
Pre-Execution Checks
  ├→ Balance: ✓
  ├→ Security: ✓
  └→ Gas: ✓
        ↓
Human Confirmation
  "Proceed with stake?"
        ↓
Execute on Mantle
  → Sign transaction
  → Send to network
        ↓
Monitor & Report
  → Poll for tx receipt
  → Update portfolio
  → Log in database
```

---

## File Organization

```
mantle-flow-agent/
├── src/
│   ├── agent/              # Agent logic
│   ├── core/               # Intent parser, TX builder
│   ├── services/           # Contracts, Supabase
│   ├── adapters/           # Bitget API adapter
│   ├── models/             # Data models, ABIs
│   ├── utils/              # Helpers
│   ├── config.py           # Configuration
│   └── main.py             # FastAPI app
├── tests/
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── scripts/
│   ├── test_connectivity.py
│   ├── init_db.py
│   └── monitor.py
├── docs/
│   ├── commands.md         # API reference
│   ├── swap.md             # Swap flows
│   └── wallet-signing.md   # Key management
├── .env                    # (NOT in git) API keys
├── .gitignore              # Git ignore patterns
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── IMPLEMENTATION_GUIDE.md # Development roadmap
├── TECH_STACK_SUMMARY.md   # Technology reference
└── QUICKSTART_CHECKLIST.md # Quick setup
```

---

## Common Commands

### Development

```bash
# Activate environment
source venv/bin/activate

# Run tests
pytest tests/ -v

# Format code
black src/

# Check types
mypy src/

# Start API server
uvicorn src.main:app --reload

# Run demo
python run_demo_auto.py
```

### Database

```bash
# Initialize Supabase schema
python scripts/init_db.py

# Connect to Supabase
# Visit: https://supabase.com/dashboard
```

### Deployment

```bash
# Testnet
TESTNET_MODE=true python mantle_flow_demo.py

# Production
gunicorn -w 4 -b 0.0.0.0:8000 src.main:app

# Docker
docker build -t mantle-flow .
docker run -d -p 8000:8000 mantle-flow
```

---

## Next Steps

### Step 1: Read Documentation (15 min)
1. Read QUICKSTART_CHECKLIST.md
2. Read TECH_STACK_SUMMARY.md
3. Skim IMPLEMENTATION_GUIDE.md

### Step 2: Setup Environment (30 min)
1. Follow QUICKSTART_CHECKLIST.md steps 1-10
2. Run test_connectivity.py to verify
3. Run demo to see it working

### Step 3: Study the Code (1-2 hours)
1. Read MANTLE_FLOW_BLUEPRINT.md
2. Review mantle_flow_demo.py
3. Understand 3-skill architecture

### Step 4: Develop (11-17 hours)
1. Follow IMPLEMENTATION_GUIDE.md Phase 2-7
2. Implement each component step-by-step
3. Test thoroughly before deployment

### Step 5: Deploy (2-3 hours)
1. Deploy to Mantle Sepolia testnet
2. Get testnet MNT from faucet
3. Test all 3 skills
4. Deploy to Mantle mainnet

---

## Estimated Timeline

| Phase | Time | Difficulty |
|-------|------|-----------|
| Setup | 0.5h | ⭐ Easy |
| Study | 2h | ⭐ Easy |
| Development | 15h | ⭐⭐⭐ Hard |
| Testnet | 2h | ⭐⭐ Medium |
| Production | 1h | ⭐ Easy |
| **Total** | **20.5h** | |

---

## Key Learning Resources

### Blockchain & Web3
- Web3.py docs: https://web3py.readthedocs.io
- Mantle docs: https://docs.mantle.xyz
- Ethers.js (reference): https://docs.ethers.org

### AI & NLP
- Anthropic: https://docs.anthropic.com
- Claude API: https://console.anthropic.com

### Backend Development
- FastAPI: https://fastapi.tiangolo.com
- Python asyncio: https://docs.python.org/3/library/asyncio.html

### Database
- Supabase: https://supabase.com/docs
- PostgreSQL: https://www.postgresql.org/docs

### DeFi Concepts
- Uniswap V2: https://docs.uniswap.org/contracts/v2
- Staking: https://ethereum.org/staking
- Bridges: https://docs.mantle.xyz/developers/bridge

---

## Support Resources

### Documentation
- IMPLEMENTATION_GUIDE.md - Detailed development steps
- MANTLE_FLOW_BLUEPRINT.md - Architecture & design
- TECH_STACK_SUMMARY.md - Technology reference
- mantle_flow_demo.py - Working code example

### Community
- Mantle Discord: https://discord.gg/mantle
- Anthropic Discord: https://discord.gg/anthropic
- Web3 Stack Exchange: https://ethereum.stackexchange.com

### Debugging
- Mantlescan (block explorer): https://mantlescan.xyz
- Etherscan (reference): https://etherscan.io
- Error logs: Check `logs/agent.log`

---

## Success Metrics

After completing this guide, you'll have:

✓ Development environment fully set up
✓ Understanding of Mantle Layer 2 and DeFi
✓ Working AI agent that processes natural language
✓ 3 functional DeFi operations (stake, swap, bridge)
✓ Production-ready database with RLS
✓ Complete test coverage
✓ Deployed application on Mantle
✓ All bounty requirements met

---

## Summary

**You have everything needed to build Mantle-Flow AI Agent:**

1. **3 implementation guides** (Quick Start, Tech Stack, Full Implementation)
2. **Complete architecture blueprint** with 3 working examples
3. **Live Python demo** showing all core functionality
4. **Production-ready codebase structure** with best practices

**Time to start:** Now. Begin with QUICKSTART_CHECKLIST.md

**Expected result:** Full-featured DeFi AI agent in 20 hours

---

## Ready to Build?

Start here: **QUICKSTART_CHECKLIST.md** (30 minutes)

Questions? Check: **TROUBLESHOOTING** section in QUICKSTART_CHECKLIST.md

Full details? Read: **IMPLEMENTATION_GUIDE.md**

Good luck! 🚀

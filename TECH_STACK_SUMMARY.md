# Mantle-Flow AI Agent - Technology Stack Summary

## Overview

This document provides a quick reference for all technologies, tools, libraries, and services needed to build and deploy the Mantle-Flow AI Agent.

---

## 1. CORE TECHNOLOGIES

### Programming Language
- **Python 3.11+** - Primary language for agent implementation
  - Why: Excellent web3 libraries, fast development, widely supported
  - Download: https://python.org
  - Verify: `python --version`

### AI/NLP
- **Claude 3.5 Sonnet API** - Intent parsing and decision making
  - Purpose: Natural language understanding for user commands
  - API Version: Latest (claude-3-5-sonnet-20241022)
  - Pricing: $3 per 1M input tokens, $15 per 1M output tokens
  - Documentation: https://docs.anthropic.com
  - Get API Key: https://console.anthropic.com/account/keys

### Blockchain Integration
- **Web3.py 6.11.0+** - Ethereum/Mantle RPC interaction
  - Purpose: Smart contract calls, transaction building, gas estimation
  - Install: `pip install web3==6.11.0`
  - Docs: https://web3py.readthedocs.io

- **eth-account 0.10.0+** - BIP-39 mnemonic & key derivation
  - Purpose: Wallet creation, private key management, transaction signing
  - Install: `pip install eth-account==0.10.0`
  - Docs: https://eth-account.readthedocs.io

### Network Access
- **Mantle RPC Endpoint** - L2 network access
  - Mainnet: `https://rpc.mantle.xyz`
  - Testnet: `https://rpc.sepolia.mantle.xyz`
  - Backup: `https://mantle-rpc.publicnode.com`
  - No authentication required

---

## 2. BACKEND & API

### Web Framework
- **FastAPI 0.104.0+** - REST API framework
  - Purpose: HTTP endpoints for AI agent operations
  - Install: `pip install fastapi==0.104.0`
  - Why: Fast, async-ready, automatic API documentation

### ASGI Server
- **Uvicorn 0.24.0+** - ASGI web server
  - Purpose: Run FastAPI application
  - Install: `pip install uvicorn==0.24.0`
  - Command: `uvicorn src.main:app --host 0.0.0.0 --port 8000`

### Data Validation
- **Pydantic 2.5.0+** - Request/response validation
  - Purpose: Type validation, serialization
  - Install: `pip install pydantic==2.5.0`

### HTTP Client
- **httpx 0.25.0+** - Async HTTP client
  - Purpose: Bitget API calls, external API integration
  - Install: `pip install httpx==0.25.0`

- **aiohttp 3.9.1+** - Alternative async HTTP client
  - Install: `pip install aiohttp==3.9.1`

---

## 3. DATABASE

### Primary Database
- **Supabase (PostgreSQL)** - Data storage & authentication
  - Purpose: User wallets, transaction logs, portfolio data
  - Pricing: Free tier (500MB storage, 25K requests/day)
  - Website: https://supabase.com
  - Features: Built-in auth, RLS policies, real-time subscriptions

### Python Database Client
- **supabase-py 2.2.0+** - Supabase Python client
  - Install: `pip install supabase==2.2.0`
  - Docs: https://supabase.com/docs/reference/python

### SQL Toolkit
- **SQLAlchemy 2.0.23+** - ORM (optional)
  - Install: `pip install sqlalchemy==2.0.23`

### PostgreSQL Adapter
- **psycopg2-binary 2.9.9+** - PostgreSQL driver
  - Install: `pip install psycopg2-binary==2.9.9`

---

## 4. SECURITY & ENCRYPTION

### Cryptography
- **cryptography 41.0.7+** - Encryption/decryption
  - Purpose: Encrypt mnemonics in database
  - Install: `pip install cryptography==41.0.7`
  - Algorithm: AES-256-GCM

### Environment Variables
- **python-dotenv 1.0.0+** - Load .env files
  - Install: `pip install python-dotenv==1.0.0`

---

## 5. TESTING

### Test Framework
- **pytest 7.4.3+** - Unit & integration testing
  - Install: `pip install pytest==7.4.3`
  - Command: `pytest tests/ -v`

### Async Testing
- **pytest-asyncio 0.21.1+** - Async test support
  - Install: `pip install pytest-asyncio==0.21.1`

### Coverage
- **pytest-cov 4.1.0+** - Code coverage reporting
  - Install: `pip install pytest-cov==4.1.0`
  - Command: `pytest tests/ --cov=src --cov-report=html`

---

## 6. CODE QUALITY

### Code Formatter
- **black 23.11.0+** - Auto code formatting
  - Install: `pip install black==23.11.0`
  - Command: `black src/`

### Linter
- **pylint 3.0.3+** - Code analysis
  - Install: `pip install pylint==3.0.3`
  - Command: `pylint src/`

### Type Checker
- **mypy 1.7.1+** - Static type checking
  - Install: `pip install mypy==1.7.1`
  - Command: `mypy src/`

---

## 7. LOGGING & MONITORING

### Logging
- **python-json-logger 2.0.7+** - JSON logging
  - Install: `pip install python-json-logger==2.0.7`
  - Purpose: Structured logging for debugging

### Monitoring (Optional)
- **Sentry** - Error tracking
  - Website: https://sentry.io
  - Purpose: Production error monitoring

- **LogRocket** - Session replay (optional)
  - Website: https://logrocket.com

---

## 8. TASK QUEUE (OPTIONAL)

### Background Jobs
- **Celery 5.3.0+** - Distributed task queue
  - Install: `pip install celery==5.3.0`
  - Purpose: Background monitoring, auto-compounding
  - Message Broker: Redis or RabbitMQ

### Message Broker
- **Redis** - Message broker for Celery
  - Install: `brew install redis` (macOS)
  - Or use Heroku Redis, Upstash, etc.

---

## 9. UTILITY LIBRARIES

### JSON Processing
- **requests 2.31.0+** - HTTP requests
  - Install: `pip install requests==2.31.0`
  - Alternative to httpx for synchronous code

### Configuration
- **pyyaml 6.0.1+** - YAML configuration files
  - Install: `pip install pyyaml==6.0.1`

---

## 10. DEVELOPMENT TOOLS

### Version Control
- **Git 2.40+** - Source code management
  - Download: https://git-scm.com

### Package Manager
- **pip** - Python package manager (built-in)
  - Included with Python 3.4+

### Alternative Package Manager
- **Poetry 1.5.0+** - Dependency management
  - Install: `curl -sSL https://install.python-poetry.org | python3 -`
  - Website: https://python-poetry.org

### Virtual Environment
- **venv** - Python environment isolation (built-in)
  - Create: `python -m venv venv`

### IDE/Editor
- **VS Code** - Recommended
  - Download: https://code.visualstudio.com
  - Extensions: Python, Pylance, Thunder Client

- **PyCharm** - Professional IDE (optional)
  - Download: https://jetbrains.com/pycharm

### API Testing
- **Postman** - API testing tool
  - Download: https://postman.com

- **curl** - Command-line HTTP client (built-in)

- **Thunder Client** - VS Code extension

---

## 11. DEPLOYMENT TOOLS

### Containerization
- **Docker 24.0+** - Container runtime
  - Download: https://docker.com
  - Install: `brew install docker-desktop` (macOS)

### Container Orchestration
- **Docker Compose 2.20+** - Multi-container management
  - Install: Usually comes with Docker Desktop

### WSGI Server (Alternative to Uvicorn)
- **Gunicorn 21.2.0+** - Python WSGI HTTP Server
  - Install: `pip install gunicorn==21.2.0`
  - Command: `gunicorn -w 4 -b 0.0.0.0:8000 src.main:app`

### Hosting Platforms
- **Heroku** - PaaS hosting
  - Website: https://heroku.com

- **AWS EC2** - Cloud VPS
  - Website: https://aws.amazon.com

- **DigitalOcean** - Simple cloud hosting
  - Website: https://digitalocean.com

- **Railway** - Modern PaaS
  - Website: https://railway.app

---

## 12. EXTERNAL APIS & SERVICES

### Blockchain Data
- **Etherscan API** - Ethereum block explorer
  - Website: https://etherscan.io/apis
  - Purpose: Token info, transaction verification

- **Mantlescan API** - Mantle block explorer
  - Website: https://mantlescan.xyz/apis
  - Purpose: Mantle-specific data

### Market Data
- **Bitget Wallet API** - Market data & swap quotes
  - Base URL: `https://copenapi.bgwapi.io`
  - No authentication required
  - Docs: https://docs.bgwapi.io

### Price Data (Optional)
- **CoinGecko API** - Cryptocurrency prices
  - Website: https://coingecko.com/api
  - Free tier: 10-50 calls/second

- **Chainlink Data Feeds** - On-chain price feeds
  - Website: https://chain.link
  - Purpose: Decentralized price oracle

---

## 13. DEPENDENCIES INSTALLATION SUMMARY

### Quick Install

```bash
# Clone/create project
git clone <repo> mantle-flow-agent
cd mantle-flow-agent

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Verify installation
python -c "import web3, anthropic, supabase; print('✓ All dependencies installed')"
```

### By Category

```bash
# Web3 & Blockchain
pip install web3==6.11.0 eth-account==0.10.0 eth-keys==0.5.1

# AI/NLP
pip install anthropic==0.25.0

# API & Framework
pip install fastapi==0.104.0 uvicorn==0.24.0 pydantic==2.5.0

# Database
pip install supabase==2.2.0 psycopg2-binary==2.9.9 sqlalchemy==2.0.23

# HTTP
pip install httpx==0.25.0 aiohttp==3.9.1 requests==2.31.0

# Security
pip install cryptography==41.0.7 python-dotenv==1.0.0

# Testing
pip install pytest==7.4.3 pytest-asyncio==0.21.1 pytest-cov==4.1.0

# Code Quality
pip install black==23.11.0 pylint==3.0.3 mypy==1.7.1

# Utilities
pip install pyyaml==6.0.1 python-json-logger==2.0.7
```

---

## 14. ENVIRONMENT CHECKLIST

Before starting development, verify you have:

```bash
# ✓ Python 3.11+
python --version

# ✓ pip
pip --version

# ✓ Git
git --version

# ✓ Virtual environment created
ls venv/

# ✓ .env file with credentials
ls -la .env

# ✓ Dependencies installed
pip list | grep -E "web3|anthropic|fastapi"

# ✓ Supabase project created
# Check: https://supabase.com/dashboard

# ✓ Anthropic API key active
# Check: https://console.anthropic.com/account/keys

# ✓ Mantle RPC accessible
curl -X POST https://rpc.mantle.xyz \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
```

---

## 15. RECOMMENDED DEVELOPMENT WORKFLOW

### Daily Development

```bash
# 1. Start session
source venv/bin/activate

# 2. Start local services (if using Redis/Postgres)
docker-compose up -d

# 3. Run tests
pytest tests/ -v

# 4. Start development server
uvicorn src.main:app --reload

# 5. In another terminal, run monitoring
python scripts/monitor.py
```

### Before Commit

```bash
# Code formatting
black src/ tests/

# Linting
pylint src/

# Type checking
mypy src/

# Testing
pytest tests/ --cov=src

# Git commit
git add .
git commit -m "Feature: description"
```

### Deployment

```bash
# Production build
pip install -r requirements-prod.txt

# Database migration
python scripts/init_db.py

# Start production server
gunicorn -w 4 -b 0.0.0.0:8000 src.main:app
```

---

## COST ESTIMATE

### Free Tier Services
- Supabase: 500MB storage, 25K req/day (free)
- Claude API: $0 initial credit, then ~$0.50/day (low usage)
- Mantle RPC: Free public endpoint
- Bitget API: Free market data
- GitHub: Free private repos

### Minimal Monthly Cost

| Service | Cost | Notes |
|---------|------|-------|
| Supabase Pro | $25 | 100GB storage, 500K req/day |
| Claude API | $10-50 | Depends on usage |
| VPS (DigitalOcean) | $5-20 | Droplet hosting |
| **Total** | **$40-95** | Minimum viable |

### Production Monthly Cost

| Service | Cost | Notes |
|---------|------|-------|
| Supabase Pro | $25 | 100GB storage |
| Claude API | $100-500 | Higher usage |
| AWS/EC2 | $20-100 | Depending on load |
| Redis (optional) | $0-30 | Upstash Redis |
| Monitoring | $0-50 | Sentry, etc. |
| **Total** | **$145-705** | Production grade |

---

## NEXT STEPS

1. **Install Python 3.11+** from https://python.org
2. **Create project directory** and initialize git
3. **Create .env file** with API keys from:
   - Anthropic: https://console.anthropic.com
   - Supabase: https://supabase.com
4. **Install dependencies**: `pip install -r requirements.txt`
5. **Follow IMPLEMENTATION_GUIDE.md** Phase 1

---

## SUPPORT & RESOURCES

| Topic | Resource |
|-------|----------|
| Web3.py | https://web3py.readthedocs.io |
| Anthropic | https://docs.anthropic.com |
| Supabase | https://supabase.com/docs |
| FastAPI | https://fastapi.tiangolo.com |
| Mantle Docs | https://docs.mantle.xyz |
| Bitget Wallet | https://docs.bgwapi.io |
| Python | https://docs.python.org/3.11 |

---

Generated: 2026-03-16
Version: 1.0

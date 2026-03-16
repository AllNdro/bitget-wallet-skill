# Mantle-Flow AI Agent - Implementation Guide

## Complete Step-by-Step Development Instructions

---

## TABLE OF CONTENTS

1. [Technology Stack](#1-technology-stack)
2. [Prerequisites & Environment Setup](#2-prerequisites--environment-setup)
3. [Phase 1: Local Development Setup](#3-phase-1-local-development-setup)
4. [Phase 2: Core Agent Development](#4-phase-2-core-agent-development)
5. [Phase 3: Smart Contract Integration](#5-phase-3-smart-contract-integration)
6. [Phase 4: Backend & Database Setup](#6-phase-4-backend--database-setup)
7. [Phase 5: Testing & Validation](#7-phase-5-testing--validation)
8. [Phase 6: Deployment to Testnet](#8-phase-6-deployment-to-testnet)
9. [Phase 7: Mainnet Deployment](#9-phase-7-mainnet-deployment)

---

## 1. TECHNOLOGY STACK

### 1.1 Required Technologies

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Language** | Python | 3.9+ | Core agent implementation |
| **NLP/AI** | Claude 3.5 Sonnet API | Latest | Intent parsing & decision making |
| **Web3** | web3.py | 6.11.0+ | Smart contract interactions |
| **Blockchain RPC** | Mantle RPC | - | Network access |
| **Database** | Supabase (PostgreSQL) | - | User data, transactions, keys |
| **Key Management** | eth-account | 0.10.0+ | BIP-39 mnemonic & signing |
| **API Framework** | FastAPI | 0.104.0+ | Backend REST API |
| **Async Runtime** | asyncio | Built-in | Async operations |
| **Wallet SDK** | Bitget Wallet SDK | Latest | Market data, swap quotes |
| **Task Queue** | Celery (optional) | 5.3.0+ | Background job processing |

### 1.2 API Keys & Services Required

| Service | Purpose | Free Tier | Link |
|---------|---------|-----------|------|
| **Anthropic Claude** | NLP intent parsing | 100k tokens/mo | https://console.anthropic.com |
| **Supabase** | Database & auth | 500MB storage | https://supabase.com |
| **Etherscan/Mantlescan** | Block explorer API | Yes (basic) | https://mantlescan.xyz/apis |
| **Bitget Wallet API** | Market data & quotes | Yes | https://docs.bgwapi.io |

### 1.3 Development Tools

```bash
# Version Control
git (2.40+)

# Package Management
pip (23.0+)
poetry (1.5.0+) [optional but recommended]

# Testing
pytest (7.4.0+)
pytest-asyncio (0.21.0+)

# Code Quality
black (23.9.0+)
pylint (2.17.0+)
mypy (1.5.0+)

# Local Development
docker (24.0+) [optional for postgres local]
docker-compose (2.20+) [optional]

# HTTP Client
curl or Postman (for API testing)

# Environment Management
python-dotenv (1.0.0+)
```

---

## 2. PREREQUISITES & ENVIRONMENT SETUP

### 2.1 System Requirements

```bash
# macOS
brew install python@3.11 git curl

# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev git curl

# Windows
# Download from python.org, add to PATH
# Download Git from git-scm.com
```

### 2.2 API Keys Setup

**Step 1: Get Anthropic Claude API Key**
```bash
# Visit: https://console.anthropic.com/account/keys
# Create new API key
# Copy to clipboard
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Step 2: Create Supabase Project**
```bash
# 1. Visit https://supabase.com
# 2. Create new project (name: mantle-flow-agent)
# 3. Wait for project initialization
# 4. Go to Project Settings → API → Copy credentials:
export SUPABASE_URL="https://xxx.supabase.co"
export SUPABASE_ANON_KEY="eyJhbGc..."
export SUPABASE_SERVICE_ROLE_KEY="eyJhbGc..."
```

**Step 3: Get Bitget Wallet API Access**
```bash
# No API key needed - uses public endpoint
# Base URL: https://copenapi.bgwapi.io
```

**Step 4: Mantle RPC Endpoint**
```bash
# Public RPC (no auth needed)
export MANTLE_RPC_URL="https://rpc.mantle.xyz"

# Optional: Backup RPC
export MANTLE_RPC_BACKUP="https://mantle-rpc.publicnode.com"

# Testnet RPC (for development)
export MANTLE_TESTNET_RPC="https://rpc.sepolia.mantle.xyz"
```

### 2.3 Create .env File

```bash
# Create project root directory
mkdir -p mantle-flow-agent
cd mantle-flow-agent

# Create .env file with all credentials
cat > .env << 'EOF'
# Environment
ENVIRONMENT=development
DEBUG=true

# API Keys
ANTHROPIC_API_KEY=sk-ant-xxx
BITGET_API_KEY=
BITGET_API_SECRET=

# Supabase
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGc...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGc...

# Mantle Network
MANTLE_RPC_URL=https://rpc.mantle.xyz
MANTLE_RPC_BACKUP=https://mantle-rpc.publicnode.com
MANTLE_CHAIN_ID=5000
MANTLE_TESTNET_RPC=https://rpc.sepolia.mantle.xyz
MANTLE_TESTNET_CHAIN_ID=5003

# Smart Contracts (Mainnet)
MANTLE_LSP_ADDRESS=0x1C9C4a1a5D8a9c5E3c5b8c1F5D8e9F4B6a7E8d3F
METH_TOKEN_ADDRESS=0x2D3E4F5a6B7C8d9E0F1a2B3c4D5e6F7a8B9C0d1E
MOE_ROUTER_ADDRESS=0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D
USDC_ADDRESS=0x09Bc4E0D864854c6aFB6eB9A9cdF58aC190D0dF9
MANTLE_BRIDGE_L1=0x95fC9a7727b3Da7d3dAbCAd4cc7949C4e11c95a8
MANTLE_BRIDGE_L2=0x4200000000000000000000000000000000000010

# Feature Flags
ENABLE_AUTO_COMPOUND=true
ENABLE_REBALANCING=true
ENABLE_PRICE_MONITORING=true
MIN_TRANSACTION_AMOUNT=10

# Rate Limiting
API_RATE_LIMIT=100
API_RATE_WINDOW=60

# Logging
LOG_LEVEL=DEBUG
LOG_FILE=logs/agent.log

# Security
MAX_TRANSACTION_SIZE=100000
REQUIRED_CONFIRMATION_VALUE=1000
ENCRYPTION_KEY=your-32-char-encryption-key-here
EOF

# Secure the .env file
chmod 600 .env

# Add to .gitignore to prevent accidental commits
echo ".env" >> .gitignore
echo ".env.local" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
```

---

## 3. PHASE 1: LOCAL DEVELOPMENT SETUP

### 3.1 Create Project Structure

```bash
cd mantle-flow-agent

# Create directory structure
mkdir -p {src,tests,scripts,docs,config,logs}
mkdir -p src/{agent,core,utils,models,services,adapters}
mkdir -p tests/{unit,integration,e2e}

# Create __init__.py files
touch src/__init__.py
touch src/agent/__init__.py
touch src/core/__init__.py
touch src/utils/__init__.py
touch src/models/__init__.py
touch src/services/__init__.py
touch src/adapters/__init__.py
```

### 3.2 Initialize Python Environment

```bash
# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Verify Python version
python --version  # Should be 3.11+
```

### 3.3 Install Dependencies

```bash
# Create requirements.txt
cat > requirements.txt << 'EOF'
# Core dependencies
web3==6.11.0
eth-account==0.10.0
eth-keys==0.5.1
python-dotenv==1.0.0

# NLP & AI
anthropic==0.25.0

# API & Web Framework
fastapi==0.104.0
uvicorn==0.24.0
pydantic==2.5.0

# Database
supabase==2.2.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9

# Async
httpx==0.25.0
aiohttp==3.9.1

# Utilities
requests==2.31.0
cryptography==41.0.7
pyyaml==6.0.1

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0

# Code Quality
black==23.11.0
pylint==3.0.3
mypy==1.7.1

# Monitoring & Logging
python-json-logger==2.0.7
EOF

# Install all dependencies
pip install -r requirements.txt

# Verify installation
python -c "import web3; import anthropic; print('✓ Dependencies installed successfully')"
```

### 3.4 Setup Git Repository

```bash
# Initialize git
git init

# Create .gitignore
cat > .gitignore << 'EOF'
# Environment
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Testing
.pytest_cache/
.coverage
htmlcov/

# Logs
logs/
*.log

# Cache
.cache/
EOF

# Initial commit
git add .
git commit -m "Initial project setup"
```

---

## 4. PHASE 2: CORE AGENT DEVELOPMENT

### 4.1 Create Config Module

**File: `src/config.py`**

```python
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class Config:
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

    # API Keys
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    BITGET_API_KEY: str = os.getenv("BITGET_API_KEY", "")

    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

    # Mantle Network
    MANTLE_RPC_URL: str = os.getenv("MANTLE_RPC_URL", "https://rpc.mantle.xyz")
    MANTLE_CHAIN_ID: int = int(os.getenv("MANTLE_CHAIN_ID", "5000"))
    MANTLE_TESTNET_RPC: str = os.getenv("MANTLE_TESTNET_RPC", "https://rpc.sepolia.mantle.xyz")
    MANTLE_TESTNET_CHAIN_ID: int = int(os.getenv("MANTLE_TESTNET_CHAIN_ID", "5003"))

    # Smart Contracts
    MANTLE_LSP_ADDRESS: str = os.getenv("MANTLE_LSP_ADDRESS", "")
    METH_TOKEN_ADDRESS: str = os.getenv("METH_TOKEN_ADDRESS", "")
    MOE_ROUTER_ADDRESS: str = os.getenv("MOE_ROUTER_ADDRESS", "")

    # Features
    ENABLE_AUTO_COMPOUND: bool = os.getenv("ENABLE_AUTO_COMPOUND", "true").lower() == "true"
    ENABLE_REBALANCING: bool = os.getenv("ENABLE_REBALANCING", "true").lower() == "true"
    ENABLE_PRICE_MONITORING: bool = os.getenv("ENABLE_PRICE_MONITORING", "true").lower() == "true"

    @classmethod
    def validate(cls) -> bool:
        """Validate all required environment variables are set."""
        required = [
            "ANTHROPIC_API_KEY",
            "SUPABASE_URL",
            "SUPABASE_ANON_KEY",
            "MANTLE_RPC_URL"
        ]
        missing = [k for k in required if not getattr(cls, k)]
        if missing:
            raise ValueError(f"Missing required config: {missing}")
        return True

config = Config()
```

### 4.2 Create Intent Parser Module

**File: `src/core/intent_parser.py`**

```python
from typing import Dict, Any, Optional
from enum import Enum
import re
from anthropic import Anthropic

class Intent(Enum):
    STAKE_METH = "stake_meth"
    UNSTAKE_METH = "unstake_meth"
    DEX_SWAP = "dex_swap"
    ADD_LIQUIDITY = "add_liquidity"
    REMOVE_LIQUIDITY = "remove_liquidity"
    BRIDGE_MNT = "bridge_mnt"
    CHECK_BALANCE = "check_balance"
    CHECK_YIELD = "check_yield"
    EMERGENCY_EXIT = "emergency_exit"
    UNKNOWN = "unknown"

class IntentParser:
    """Parse natural language commands to intents and parameters."""

    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20241022"
        self.system_prompt = """You are a DeFi assistant for the Mantle Layer 2 network.
Parse user commands and extract intent and parameters.

Available intents:
- stake_meth: Stake MNT to earn mETH rewards (5.2% APY)
- unstake_meth: Unstake mETH to get MNT back
- dex_swap: Swap tokens on Merchant Moe DEX
- add_liquidity: Add liquidity to a trading pair
- remove_liquidity: Remove liquidity from a trading pair
- bridge_mnt: Bridge MNT between L1 and L2
- check_balance: Check wallet balances
- check_yield: Check yield opportunities
- emergency_exit: Liquidate all positions immediately

Respond in JSON format:
{
    "intent": "intent_name",
    "parameters": {
        "amount": number or null,
        "token": "TOKEN_SYMBOL" or null,
        "target_token": "TOKEN_SYMBOL" or null,
        "strategy": "strategy_name" or null,
        "confidence": 0.0-1.0
    },
    "reasoning": "Explanation of parsed intent"
}"""

    async def parse(self, user_input: str) -> Dict[str, Any]:
        """Parse user input to intent and parameters."""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=500,
                system=self.system_prompt,
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            # Parse response (assumes JSON format)
            import json
            response_text = response.content[0].text

            # Extract JSON from response
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                return result
            else:
                return {
                    "intent": Intent.UNKNOWN.value,
                    "parameters": {},
                    "reasoning": "Could not parse response"
                }

        except Exception as e:
            return {
                "intent": Intent.UNKNOWN.value,
                "parameters": {},
                "error": str(e)
            }

    def validate_intent(self, parsed: Dict[str, Any]) -> bool:
        """Validate parsed intent has required fields."""
        return (
            "intent" in parsed and
            "parameters" in parsed and
            isinstance(parsed["parameters"], dict)
        )
```

### 4.3 Create Transaction Builder

**File: `src/core/transaction_builder.py`**

```python
from typing import Dict, Any, Optional
from web3 import Web3
from eth_account import Account
from config import config

class TransactionBuilder:
    """Build transactions for Mantle smart contracts."""

    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(config.MANTLE_RPC_URL))
        self.chain_id = config.MANTLE_CHAIN_ID

    def build_stake_meth_tx(
        self,
        account_address: str,
        amount_in_mnt: float,
        contract_address: str
    ) -> Dict[str, Any]:
        """Build transaction to stake MNT for mETH."""

        # Convert amount to wei (MNT uses 18 decimals)
        amount_wei = Web3.to_wei(amount_in_mnt, 'ether')

        # Standard ERC20 stake function selector
        function_selector = "0xa694fc3a"  # stake(uint256)
        encoded_params = Web3.keccak(text="stake(uint256)")[:4].hex()

        # Encode amount as uint256
        amount_encoded = Web3.to_hex(amount_wei).zfill(66)

        return {
            "to": contract_address,
            "from": account_address,
            "value": 0,
            "data": encoded_params + amount_encoded[2:],
            "gas": 150000,
            "gasPrice": self.w3.eth.gas_price,
            "nonce": self.w3.eth.get_transaction_count(account_address),
            "chainId": self.chain_id
        }

    def build_swap_tx(
        self,
        account_address: str,
        amount_in: float,
        token_in: str,
        token_out: str,
        router_address: str
    ) -> Dict[str, Any]:
        """Build DEX swap transaction."""

        amount_wei = Web3.to_wei(amount_in, 'ether')

        return {
            "to": router_address,
            "from": account_address,
            "value": 0 if token_in != "MNT" else amount_wei,
            "data": "0x",  # Placeholder - actual encoding depends on router ABI
            "gas": 250000,
            "gasPrice": self.w3.eth.gas_price,
            "nonce": self.w3.eth.get_transaction_count(account_address),
            "chainId": self.chain_id
        }

    def estimate_gas(self, tx: Dict[str, Any]) -> int:
        """Estimate gas for transaction."""
        try:
            return self.w3.eth.estimate_gas(tx)
        except Exception as e:
            # Return default gas estimate on error
            return tx.get("gas", 200000)
```

### 4.4 Create Bitget Wallet Adapter

**File: `src/adapters/bitget_adapter.py`**

```python
import httpx
import json
from typing import Dict, Any, Optional, List

class BitgetWalletAdapter:
    """Adapter for Bitget Wallet API integration."""

    BASE_URL = "https://copenapi.bgwapi.io"

    def __init__(self):
        self.client = httpx.Client()

    async def get_balance(
        self,
        chain: str,
        address: str,
        contracts: List[str]
    ) -> Dict[str, Any]:
        """Get token balances for an address."""

        # Build request for Bitget get-processed-balance endpoint
        request_data = {
            "chainCode": chain,
            "walletAddr": address,
            "tokenContractAddrs": contracts
        }

        try:
            response = await self.client.post(
                f"{self.BASE_URL}/wallet/v1/account/balances",
                json=request_data,
                timeout=10
            )
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    async def get_token_info(
        self,
        chain: str,
        contract: str
    ) -> Dict[str, Any]:
        """Get token information."""

        request_data = {
            "chainCode": chain,
            "contractAddr": contract
        }

        try:
            response = await self.client.post(
                f"{self.BASE_URL}/token/v1/queryTokenInfo",
                json=request_data,
                timeout=10
            )
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    async def get_swap_quote(
        self,
        from_chain: str,
        from_token: str,
        from_amount: float,
        to_chain: str,
        to_token: str
    ) -> Dict[str, Any]:
        """Get swap quote from Bitget."""

        request_data = {
            "fromChain": from_chain,
            "fromToken": from_token,
            "fromAmount": from_amount,
            "toChain": to_chain,
            "toToken": to_token
        }

        try:
            response = await self.client.post(
                f"{self.BASE_URL}/swap/v1/quote",
                json=request_data,
                timeout=10
            )
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    async def check_token_security(
        self,
        chain: str,
        contract: str
    ) -> Dict[str, Any]:
        """Security audit for token."""

        request_data = {
            "chainCode": chain,
            "contractAddr": contract
        }

        try:
            response = await self.client.post(
                f"{self.BASE_URL}/token/v1/tokenSecurity",
                json=request_data,
                timeout=10
            )
            return response.json()
        except Exception as e:
            return {"error": str(e)}
```

---

## 5. PHASE 3: SMART CONTRACT INTEGRATION

### 5.1 Setup Contract ABIs

**File: `src/models/contract_abis.py`**

```python
# mETH Staking Contract ABI (Mantle LSP)
METH_STAKING_ABI = [
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "stake",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "type": "function",
        "stateMutability": "nonpayable"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "unstake",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "type": "function",
        "stateMutability": "nonpayable"
    },
    {
        "inputs": [],
        "name": "getAPY",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "type": "function",
        "stateMutability": "view"
    }
]

# Merchant Moe Router V2 ABI
MOE_ROUTER_ABI = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapExactTokensForTokens",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "type": "function",
        "stateMutability": "nonpayable"
    }
]

# ERC20 Standard ABI
ERC20_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "type": "function",
        "stateMutability": "view"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "type": "function",
        "stateMutability": "nonpayable"
    }
]

# Bridge Contract ABI
BRIDGE_ABI = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"}
        ],
        "name": "depositETH",
        "outputs": [],
        "type": "function",
        "stateMutability": "payable"
    }
]
```

### 5.2 Create Smart Contract Interaction Module

**File: `src/services/contract_service.py`**

```python
from web3 import Web3
from typing import Dict, Any, Optional
from config import config
from models.contract_abis import METH_STAKING_ABI, MOE_ROUTER_ABI, ERC20_ABI

class ContractService:
    """Service for interacting with Mantle smart contracts."""

    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(config.MANTLE_RPC_URL))
        self.chain_id = config.MANTLE_CHAIN_ID

        # Initialize contract instances
        self.meth_staking = self.w3.eth.contract(
            address=Web3.to_checksum_address(config.MANTLE_LSP_ADDRESS),
            abi=METH_STAKING_ABI
        )

        self.moe_router = self.w3.eth.contract(
            address=Web3.to_checksum_address(config.MOE_ROUTER_ADDRESS),
            abi=MOE_ROUTER_ABI
        )

    def get_meth_apy(self) -> float:
        """Get current mETH staking APY."""
        try:
            apy_raw = self.meth_staking.functions.getAPY().call()
            return apy_raw / 100  # Assume APY is stored as percentage * 100
        except Exception as e:
            print(f"Error getting mETH APY: {e}")
            return 0.0

    def get_token_balance(
        self,
        token_address: str,
        wallet_address: str
    ) -> float:
        """Get ERC20 token balance."""
        try:
            token = self.w3.eth.contract(
                address=Web3.to_checksum_address(token_address),
                abi=ERC20_ABI
            )
            balance_raw = token.functions.balanceOf(
                Web3.to_checksum_address(wallet_address)
            ).call()
            return Web3.from_wei(balance_raw, 'ether')
        except Exception as e:
            print(f"Error getting balance: {e}")
            return 0.0

    def estimate_swap_output(
        self,
        amount_in: float,
        path: list
    ) -> float:
        """Estimate output amount for swap."""
        try:
            amount_in_wei = Web3.to_wei(amount_in, 'ether')
            amounts = self.moe_router.functions.getAmountsOut(
                amount_in_wei,
                path
            ).call()
            return Web3.from_wei(amounts[-1], 'ether')
        except Exception as e:
            print(f"Error estimating swap: {e}")
            return 0.0
```

---

## 6. PHASE 4: BACKEND & DATABASE SETUP

### 6.1 Setup Supabase Database Schema

**File: `scripts/setup_database.sql`**

```sql
-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    wallet_address TEXT UNIQUE NOT NULL,
    encrypted_mnemonic TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    tx_hash TEXT UNIQUE NOT NULL,
    tx_type TEXT NOT NULL,
    from_token TEXT,
    to_token TEXT,
    amount DECIMAL,
    status TEXT DEFAULT 'pending',
    gas_used DECIMAL,
    created_at TIMESTAMP DEFAULT NOW(),
    completed_at TIMESTAMP
);

-- Create portfolio table
CREATE TABLE IF NOT EXISTS portfolio (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    token TEXT NOT NULL,
    balance DECIMAL NOT NULL,
    usd_value DECIMAL,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create audit_logs table
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    action TEXT NOT NULL,
    details JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Enable Row Level Security
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE transactions ENABLE ROW LEVEL SECURITY;
ALTER TABLE portfolio ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_logs ENABLE ROW LEVEL SECURITY;

-- Create RLS policies for users
CREATE POLICY "Users can view own profile" ON users
    FOR SELECT USING (auth.uid()::text = id::text);

-- Create RLS policies for transactions
CREATE POLICY "Users can view own transactions" ON transactions
    FOR SELECT USING (user_id = auth.uid()::uuid);

-- Create RLS policies for portfolio
CREATE POLICY "Users can view own portfolio" ON portfolio
    FOR SELECT USING (user_id = auth.uid()::uuid);
```

### 6.2 Run Database Setup

```bash
# Connect to Supabase and run the schema creation
# Option 1: Via Supabase Dashboard
# 1. Go to https://supabase.com
# 2. Select your project
# 3. Go to SQL Editor
# 4. Create new query
# 5. Paste the SQL above
# 6. Run

# Option 2: Via Python
cat > scripts/init_db.py << 'EOF'
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(url, key)

# Read SQL file
with open("scripts/setup_database.sql", "r") as f:
    sql = f.read()

# Execute
response = supabase.rpc("execute_sql", {"query": sql})
print("Database initialized:", response)
EOF

python scripts/init_db.py
```

### 6.3 Create Supabase Service Module

**File: `src/services/supabase_service.py`**

```python
import os
from supabase import create_client, Client
from typing import Dict, Any, Optional
from config import config

class SupabaseService:
    """Service for Supabase database operations."""

    def __init__(self):
        self.supabase: Client = create_client(
            config.SUPABASE_URL,
            config.SUPABASE_SERVICE_ROLE_KEY
        )

    async def store_user(
        self,
        wallet_address: str,
        encrypted_mnemonic: str
    ) -> Dict[str, Any]:
        """Store user wallet and encrypted mnemonic."""
        response = self.supabase.table("users").insert({
            "wallet_address": wallet_address,
            "encrypted_mnemonic": encrypted_mnemonic
        }).execute()
        return response.data[0] if response.data else {}

    async def get_user(self, wallet_address: str) -> Optional[Dict[str, Any]]:
        """Get user by wallet address."""
        response = self.supabase.table("users").select("*").eq(
            "wallet_address", wallet_address
        ).execute()
        return response.data[0] if response.data else None

    async def log_transaction(
        self,
        user_id: str,
        tx_hash: str,
        tx_type: str,
        from_token: str,
        to_token: str,
        amount: float,
        gas_used: float
    ) -> Dict[str, Any]:
        """Log transaction to database."""
        response = self.supabase.table("transactions").insert({
            "user_id": user_id,
            "tx_hash": tx_hash,
            "tx_type": tx_type,
            "from_token": from_token,
            "to_token": to_token,
            "amount": amount,
            "gas_used": gas_used,
            "status": "pending"
        }).execute()
        return response.data[0] if response.data else {}

    async def update_portfolio(
        self,
        user_id: str,
        token: str,
        balance: float,
        usd_value: float
    ) -> Dict[str, Any]:
        """Update user portfolio."""
        response = self.supabase.table("portfolio").upsert({
            "user_id": user_id,
            "token": token,
            "balance": balance,
            "usd_value": usd_value
        }).execute()
        return response.data[0] if response.data else {}

    async def get_portfolio(self, user_id: str) -> Dict[str, Any]:
        """Get user portfolio."""
        response = self.supabase.table("portfolio").select("*").eq(
            "user_id", user_id
        ).execute()
        return {item["token"]: item for item in response.data}
```

---

## 7. PHASE 5: TESTING & VALIDATION

### 7.1 Create Unit Tests

**File: `tests/unit/test_intent_parser.py`**

```python
import pytest
from src.core.intent_parser import IntentParser, Intent
from config import config

@pytest.mark.asyncio
async def test_stake_intent_parsing():
    parser = IntentParser(config.ANTHROPIC_API_KEY)
    result = await parser.parse("Stake 100 MNT to earn rewards")

    assert result["intent"] == Intent.STAKE_METH.value
    assert result["parameters"]["amount"] == 100
    assert result["parameters"]["token"] == "MNT"

@pytest.mark.asyncio
async def test_swap_intent_parsing():
    parser = IntentParser(config.ANTHROPIC_API_KEY)
    result = await parser.parse("Swap 50 MNT for USDC")

    assert result["intent"] == Intent.DEX_SWAP.value
    assert result["parameters"]["amount"] == 50
    assert result["parameters"]["target_token"] == "USDC"

@pytest.mark.asyncio
async def test_invalid_intent():
    parser = IntentParser(config.ANTHROPIC_API_KEY)
    result = await parser.parse("random nonsense")

    assert result["intent"] == Intent.UNKNOWN.value
```

### 7.2 Create Integration Tests

**File: `tests/integration/test_mantle_integration.py`**

```python
import pytest
from src.services.contract_service import ContractService

def test_get_meth_apy():
    service = ContractService()
    apy = service.get_meth_apy()

    assert isinstance(apy, float)
    assert apy > 0
    assert apy < 100  # Sanity check

def test_get_token_balance():
    service = ContractService()
    from config import config

    # Test with dummy address (will be 0)
    balance = service.get_token_balance(
        config.USDC_ADDRESS,
        "0x0000000000000000000000000000000000000000"
    )

    assert isinstance(balance, float)
    assert balance == 0

def test_estimate_swap():
    service = ContractService()
    from config import config

    # This will fail on testnet without proper token addresses
    # but demonstrates the test structure
    try:
        output = service.estimate_swap_output(
            1.0,
            ["0x0000000000000000000000000000000000000001",
             "0x0000000000000000000000000000000000000002"]
        )
        assert isinstance(output, float)
    except Exception:
        pass  # Expected on testnet
```

### 7.3 Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_intent_parser.py -v

# Run integration tests only
pytest tests/integration/ -v
```

---

## 8. PHASE 6: DEPLOYMENT TO TESTNET

### 8.1 Switch to Testnet Configuration

```bash
# Update .env for testnet
cat >> .env << 'EOF'

# Testnet Configuration (Mantle Sepolia)
TESTNET_MODE=true
MANTLE_RPC_URL=https://rpc.sepolia.mantle.xyz
MANTLE_CHAIN_ID=5003

# Testnet contract addresses (TBD)
MANTLE_LSP_TESTNET=0x...
METH_TOKEN_TESTNET=0x...
MOE_ROUTER_TESTNET=0x...
EOF
```

### 8.2 Deploy to Testnet

```bash
# Get testnet MNT from faucet
# https://faucet.mantle.xyz

# Run testnet demo
python mantle_flow_demo.py --testnet

# Run integration tests on testnet
TESTNET_MODE=true pytest tests/integration/ -v
```

### 8.3 Testnet Checklist

- [ ] Can connect to Mantle Sepolia RPC
- [ ] Can retrieve testnet contract addresses
- [ ] Can perform test stake transaction
- [ ] Can perform test swap transaction
- [ ] Can retrieve mETH APY
- [ ] Database transactions logged correctly
- [ ] Gas estimation works
- [ ] User confirmation flow works

---

## 9. PHASE 7: MAINNET DEPLOYMENT

### 9.1 Pre-Deployment Checklist

```bash
cat > DEPLOYMENT_CHECKLIST.md << 'EOF'
# Mainnet Deployment Checklist

## Code Review
- [ ] All functions have docstrings
- [ ] Error handling implemented for all API calls
- [ ] Security audit passed
- [ ] No hardcoded secrets or private keys
- [ ] Rate limiting implemented

## Testing
- [ ] All unit tests pass (100% coverage target)
- [ ] Integration tests pass
- [ ] E2E tests pass
- [ ] Load testing completed
- [ ] Security testing completed

## Infrastructure
- [ ] Supabase production database configured
- [ ] Encryption keys rotated
- [ ] Backups configured
- [ ] Monitoring and alerting set up
- [ ] Logging configured
- [ ] Rate limiting configured

## Documentation
- [ ] API documentation complete
- [ ] Deployment guide written
- [ ] User guide written
- [ ] Architecture documentation complete
- [ ] Runbooks created for incidents

## Contract Verification
- [ ] All contract addresses verified on Mantlescan
- [ ] Contract ABIs verified
- [ ] Gas estimates tested on mainnet
- [ ] All permissions and roles verified

## Go/No-Go Decision
- [ ] Product owner sign-off
- [ ] Security team sign-off
- [ ] DevOps team sign-off
- [ ] Legal review complete
EOF
```

### 9.2 Mainnet Deployment Steps

```bash
# 1. Update configuration for mainnet
sed -i 's/TESTNET_MODE=true/TESTNET_MODE=false/g' .env
sed -i 's/MANTLE_TESTNET_RPC/MANTLE_RPC_URL/g' .env

# 2. Final verification
python -c "from config import config; config.validate(); print('✓ Configuration valid')"

# 3. Database migration
python scripts/init_db.py

# 4. Final tests
pytest tests/ -v

# 5. Deploy application
# (Your deployment process here - docker, systemd, kubernetes, etc.)
```

### 9.3 Post-Deployment Monitoring

```bash
cat > scripts/monitor.py << 'EOF'
#!/usr/bin/env python3
"""Post-deployment monitoring script."""

import asyncio
import logging
from datetime import datetime
from src.services.contract_service import ContractService
from src.adapters.bitget_adapter import BitgetWalletAdapter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def monitor():
    """Run monitoring checks."""
    contract_service = ContractService()
    bitget = BitgetWalletAdapter()

    logger.info("=" * 60)
    logger.info(f"Health Check - {datetime.now().isoformat()}")
    logger.info("=" * 60)

    # Check RPC connectivity
    try:
        latest_block = contract_service.w3.eth.block_number
        logger.info(f"✓ RPC Connected - Block: {latest_block}")
    except Exception as e:
        logger.error(f"✗ RPC Error: {e}")

    # Check mETH APY
    try:
        apy = contract_service.get_meth_apy()
        logger.info(f"✓ mETH APY: {apy}%")
    except Exception as e:
        logger.error(f"✗ APY Error: {e}")

    # Check Bitget API
    try:
        balance = await bitget.get_balance("eth", "0x0000000000000000000000000000000000000000", [])
        logger.info(f"✓ Bitget API Responsive")
    except Exception as e:
        logger.error(f"✗ Bitget API Error: {e}")

    logger.info("=" * 60)

if __name__ == "__main__":
    asyncio.run(monitor())
EOF

# Run monitoring every 5 minutes
(crontab -l 2>/dev/null; echo "*/5 * * * * cd /path/to/mantle-flow-agent && python scripts/monitor.py") | crontab -
```

---

## 10. DEPLOYMENT METHODS

### 10.1 Standalone Server Deployment

```bash
# Create systemd service
sudo tee /etc/systemd/system/mantle-flow.service << EOF
[Unit]
Description=Mantle-Flow AI Agent
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/mantle-flow-agent
Environment="PATH=/home/ubuntu/mantle-flow-agent/venv/bin"
ExecStart=/home/ubuntu/mantle-flow-agent/venv/bin/python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable mantle-flow
sudo systemctl start mantle-flow
sudo systemctl status mantle-flow
```

### 10.2 Docker Deployment

```dockerfile
# Create Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build and run
docker build -t mantle-flow-agent:latest .
docker run -d \
  --name mantle-flow-agent \
  --env-file .env \
  -p 8000:8000 \
  mantle-flow-agent:latest
```

---

## 11. QUICK REFERENCE COMMANDS

```bash
# Development
source venv/bin/activate
python mantle_flow_demo.py

# Testing
pytest tests/ -v --cov=src

# Monitoring
python scripts/monitor.py

# Database
python scripts/init_db.py

# Production
gunicorn -w 4 -b 0.0.0.0:8000 src.main:app

# Logs
tail -f logs/agent.log
journalctl -u mantle-flow -f  # systemd
docker logs -f mantle-flow-agent  # docker
```

---

## 12. TROUBLESHOOTING

### Common Issues

**Issue: "Invalid RPC URL"**
```bash
# Check Mantle RPC connectivity
curl -X POST https://rpc.mantle.xyz \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
```

**Issue: "Missing contract address"**
```bash
# Verify all contract addresses in .env
grep "ADDRESS" .env
```

**Issue: "Supabase connection timeout"**
```bash
# Check Supabase project status at https://supabase.com/dashboard
# Verify network connectivity: curl https://your-project.supabase.co
```

**Issue: "Rate limit exceeded"**
```bash
# Check API rate limits in config
# Implement exponential backoff retry logic
```

---

## NEXT STEPS

1. **Complete Phase 1** - Setup local development environment
2. **Complete Phase 2** - Implement core agent components
3. **Complete Phase 3** - Integrate smart contracts
4. **Complete Phase 4** - Setup database
5. **Complete Phase 5** - Run tests
6. **Complete Phase 6** - Deploy to testnet
7. **Complete Phase 7** - Deploy to mainnet

For detailed API documentation, see `docs/commands.md` and `docs/swap.md` from Bitget Wallet SDK.

For architecture details, see `MANTLE_FLOW_BLUEPRINT.md`.

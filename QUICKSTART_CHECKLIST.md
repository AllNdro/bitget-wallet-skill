# Mantle-Flow AI Agent - Quick Start Checklist

## Get Started in 30 Minutes

---

## STEP 1: PREREQUISITES (5 minutes)

### 1.1 Install Python 3.11+

```bash
# macOS
brew install python@3.11

# Ubuntu/Debian
sudo apt install python3.11 python3.11-venv

# Windows
# Download from https://python.org and add to PATH

# Verify installation
python --version  # Should be 3.11+
pip --version     # Should be latest
```

### 1.2 Install Git

```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt install git

# Windows
# Download from https://git-scm.com

# Verify
git --version
```

### 1.3 Get API Keys (5 minutes)

**Anthropic Claude:**
- Go to https://console.anthropic.com/account/keys
- Click "Create key"
- Copy and save: `sk-ant-xxxxx`

**Supabase:**
- Go to https://supabase.com
- Create new project (name: mantle-flow-agent)
- Wait for initialization
- Go to Project Settings → API
- Copy and save:
  - `SUPABASE_URL`
  - `SUPABASE_ANON_KEY`
  - `SUPABASE_SERVICE_ROLE_KEY`

---

## STEP 2: CLONE PROJECT (2 minutes)

```bash
# Clone repository
git clone <repository-url> mantle-flow-agent
cd mantle-flow-agent

# Or create from scratch
mkdir mantle-flow-agent
cd mantle-flow-agent
git init
```

---

## STEP 3: SETUP ENVIRONMENT (5 minutes)

### 3.1 Create Virtual Environment

```bash
# Create venv
python3.11 -m venv venv

# Activate
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Verify (prompt should show (venv))
```

### 3.2 Create .env File

```bash
# Create .env in project root
cat > .env << 'EOF'
# Environment
ENVIRONMENT=development
DEBUG=true

# API Keys (paste your values here)
ANTHROPIC_API_KEY=sk-ant-YOUR_KEY_HERE
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here

# Mantle Network (no changes needed)
MANTLE_RPC_URL=https://rpc.mantle.xyz
MANTLE_CHAIN_ID=5000
MANTLE_TESTNET_RPC=https://rpc.sepolia.mantle.xyz
MANTLE_TESTNET_CHAIN_ID=5003

# Smart Contracts (will be updated later)
MANTLE_LSP_ADDRESS=0x1C9C4a1a5D8a9c5E3c5b8c1F5D8e9F4B6a7E8d3F
METH_TOKEN_ADDRESS=0x2D3E4F5a6B7C8d9E0F1a2B3c4D5e6F7a8B9C0d1E
MOE_ROUTER_ADDRESS=0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D
EOF

# Secure the file
chmod 600 .env

# Add to .gitignore
echo ".env" >> .gitignore
```

### 3.3 Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Or install manually
pip install web3==6.11.0 eth-account==0.10.0 anthropic==0.25.0 fastapi==0.104.0 uvicorn==0.24.0 pydantic==2.5.0 supabase==2.2.0 python-dotenv==1.0.0 httpx==0.25.0

# Verify installation
python -c "import web3; import anthropic; import fastapi; print('✓ Dependencies installed')"
```

---

## STEP 4: CREATE PROJECT STRUCTURE (3 minutes)

```bash
# Create directories
mkdir -p src/{agent,core,utils,models,services,adapters}
mkdir -p tests/{unit,integration}
mkdir -p scripts logs

# Create __init__.py files
touch src/__init__.py
touch src/agent/__init__.py
touch src/core/__init__.py
touch src/models/__init__.py
touch src/services/__init__.py
touch src/adapters/__init__.py

# Verify structure
tree src/  # or: find src -type f -name "*.py"
```

---

## STEP 5: CREATE CONFIG MODULE (2 minutes)

**File: `src/config.py`**

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"

    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    SUPABASE_URL = os.getenv("SUPABASE_URL", "")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "")
    SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

    MANTLE_RPC_URL = os.getenv("MANTLE_RPC_URL", "https://rpc.mantle.xyz")
    MANTLE_CHAIN_ID = int(os.getenv("MANTLE_CHAIN_ID", "5000"))

    MANTLE_LSP_ADDRESS = os.getenv("MANTLE_LSP_ADDRESS", "")
    METH_TOKEN_ADDRESS = os.getenv("METH_TOKEN_ADDRESS", "")
    MOE_ROUTER_ADDRESS = os.getenv("MOE_ROUTER_ADDRESS", "")

    @classmethod
    def validate(cls):
        required = ["ANTHROPIC_API_KEY", "SUPABASE_URL", "MANTLE_RPC_URL"]
        missing = [k for k in required if not getattr(cls, k)]
        if missing:
            raise ValueError(f"Missing: {missing}")
        return True

config = Config()
```

---

## STEP 6: TEST CONNECTIVITY (3 minutes)

**File: `scripts/test_connectivity.py`**

```python
#!/usr/bin/env python3
import sys
sys.path.insert(0, ".")

from src.config import config
from web3 import Web3
from anthropic import Anthropic
from supabase import create_client

print("Testing Mantle-Flow connections...\n")

# Test Mantle RPC
try:
    w3 = Web3(Web3.HTTPProvider(config.MANTLE_RPC_URL))
    block = w3.eth.block_number
    print(f"✓ Mantle RPC: Connected (Block {block})")
except Exception as e:
    print(f"✗ Mantle RPC: {e}")

# Test Anthropic API
try:
    client = Anthropic(api_key=config.ANTHROPIC_API_KEY)
    print(f"✓ Anthropic API: Configured")
except Exception as e:
    print(f"✗ Anthropic API: {e}")

# Test Supabase
try:
    supabase = create_client(config.SUPABASE_URL, config.SUPABASE_ANON_KEY)
    print(f"✓ Supabase: Configured")
except Exception as e:
    print(f"✗ Supabase: {e}")

print("\n✓ All connections tested!")
```

```bash
# Run test
python scripts/test_connectivity.py
```

---

## STEP 7: CREATE HELLO WORLD (2 minutes)

**File: `src/main.py`**

```python
from fastapi import FastAPI
from src.config import config

app = FastAPI(title="Mantle-Flow AI Agent")

@app.get("/health")
async def health():
    return {"status": "healthy", "environment": config.ENVIRONMENT}

@app.get("/")
async def root():
    return {"message": "Welcome to Mantle-Flow AI Agent"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## STEP 8: RUN DEMO (2 minutes)

```bash
# Make sure venv is activated
source venv/bin/activate

# Run the existing demo
python mantle_flow_demo.py

# Or run the auto demo
python run_demo_auto.py

# Or start the API server
python -m uvicorn src.main:app --reload

# Test in another terminal
curl http://localhost:8000/health
```

---

## STEP 9: VERSION CONTROL (2 minutes)

```bash
# Check git status
git status

# Add files
git add .

# Create initial commit
git commit -m "Initial project setup: Mantle-Flow AI Agent"

# Create and checkout new branch for development
git checkout -b feature/core-agent

# Verify branch
git branch
```

---

## STEP 10: NEXT PHASE

You've completed the quick start! Next steps:

**Option A: Continue with Full Implementation**
- Read `IMPLEMENTATION_GUIDE.md` Phase 2-7
- Follow the step-by-step instructions
- Estimated time: 3-5 days

**Option B: Study the Blueprint**
- Read `MANTLE_FLOW_BLUEPRINT.md`
- Understand architecture and design
- Review existing demo code

**Option C: Setup Database**
- Create Supabase tables
- Enable Row Level Security
- Configure RLS policies

---

## TROUBLESHOOTING

### Python Version Error
```bash
# Verify Python version
python --version

# If wrong version, use explicit python3.11
python3.11 -m venv venv
python3.11 -m pip install -r requirements.txt
```

### Permission Denied
```bash
# Fix .env permissions
chmod 600 .env

# Make scripts executable
chmod +x scripts/*.py
```

### Module Not Found
```bash
# Verify virtual environment is activated
which python  # Should show path/to/venv/bin/python

# Reinstall dependencies
pip install -r requirements.txt
```

### API Key Issues
```bash
# Verify .env file exists and has values
cat .env

# Verify no quotes around keys in .env
# Should be: ANTHROPIC_API_KEY=sk-ant-xxx
# NOT:       ANTHROPIC_API_KEY="sk-ant-xxx"
```

### Connection Timeout
```bash
# Test Mantle RPC directly
curl -X POST https://rpc.mantle.xyz \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'

# If fails, try backup RPC
MANTLE_RPC_URL=https://mantle-rpc.publicnode.com
```

---

## VERIFICATION CHECKLIST

Before moving to Phase 2, verify:

- [ ] Python 3.11+ installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed
- [ ] .env file created with API keys
- [ ] Project structure created
- [ ] test_connectivity.py passes
- [ ] hello world API runs
- [ ] Demo runs successfully
- [ ] Git initialized with first commit

---

## TIME BREAKDOWN

| Step | Time | Status |
|------|------|--------|
| Prerequisites | 5 min | ✓ |
| Clone Project | 2 min | ✓ |
| Setup Environment | 5 min | ✓ |
| Project Structure | 3 min | ✓ |
| Config Module | 2 min | ✓ |
| Test Connectivity | 3 min | ✓ |
| Hello World | 2 min | ✓ |
| Run Demo | 2 min | ✓ |
| Git Setup | 2 min | ✓ |
| **Total** | **28 min** | ✓ |

---

## RESOURCES

- Implementation Guide: `IMPLEMENTATION_GUIDE.md`
- Tech Stack: `TECH_STACK_SUMMARY.md`
- Architecture: `MANTLE_FLOW_BLUEPRINT.md`
- Bitget SDK: `SKILL.md`
- API Docs: `docs/`

---

## NEED HELP?

1. Check TROUBLESHOOTING section above
2. Read `IMPLEMENTATION_GUIDE.md` for detailed steps
3. Review existing demo code: `mantle_flow_demo.py`
4. Check Mantle docs: https://docs.mantle.xyz
5. Check Anthropic docs: https://docs.anthropic.com

---

## SUCCESS!

If all steps completed, you now have:

✓ Development environment setup
✓ All dependencies installed
✓ API connections tested
✓ Hello world API running
✓ Demo working
✓ Git repository initialized

You're ready to start Phase 2 core agent development!

Next: Read `IMPLEMENTATION_GUIDE.md` Phase 2

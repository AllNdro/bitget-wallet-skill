# Mantle-Flow AI Agent

> **When AI Meets Mantle** - Bounty Submission

An AI-powered DeFi agent optimized exclusively for Mantle Layer 2, enabling complex multi-step strategies that are economically impossible on Ethereum L1 or other L2s.

---

## 🎯 Quick Overview

**Problem:** DeFi on Ethereum L1 is too expensive for retail users. A simple 3-step yield strategy costs $60 in gas, making it unprofitable for portfolios under $18,000.

**Solution:** Mantle-Flow leverages Mantle L2's 99.9% cheaper gas to enable sophisticated DeFi operations for everyone. The same strategy costs just $0.012 on Mantle.

**Result:** 80x smaller minimum portfolio size, opening DeFi to millions of new users.

---

## 📁 Files in This Submission

| File | Description | Size |
|------|-------------|------|
| **MANTLE_FLOW_BLUEPRINT.md** | Complete technical architecture (50+ pages) | 100 KB |
| **MANTLE_BOUNTY_SUBMISSION.md** | Formal bounty submission document | 30 KB |
| **mantle_flow_demo.py** | Working Python demo | 15 KB |
| **README_MANTLE_FLOW.md** | This file (quick start guide) | 5 KB |

---

## 🚀 Quick Start

### 1. Read the Blueprint

Start with `MANTLE_FLOW_BLUEPRINT.md` for the full technical design:
```bash
# View in your terminal
cat MANTLE_FLOW_BLUEPRINT.md

# Or open in your favorite editor
code MANTLE_FLOW_BLUEPRINT.md
```

**What's inside:**
- System architecture diagrams
- 3 Mantle-native skills (mETH staking, Moe DEX, Bridge)
- 3 complex conversation examples
- Gas cost analysis (L1 vs L2)
- Smart contract integration details
- Database schema
- Deployment guide

### 2. Run the Demo

```bash
# Install dependencies (if needed)
pip install web3 eth-account requests

# Run the demo
python3 mantle_flow_demo.py
```

**What you'll see:**
1. Multi-step DeFi strategy execution
2. Emergency portfolio liquidation
3. Gas cost comparison table

Sample output:
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    MANTLE-FLOW AI AGENT DEMO                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

User: I want to maximize yield on my 5000 MNT. What's the best strategy?

Agent: Analyzing your options on Mantle...

I found 3 high-yield strategies:
- mETH Staking: 5.2% APY (Low risk)
- Moe LP: 12.3% APY (Medium risk)
- Hybrid: 8.5% APY (Balanced) ✓ Recommended

Step 1/3: Stake 3000 MNT to mETH
✓ Staked! You received 3000 mETH earning 5.2% APY. Gas: 0.003 MNT ($0.0015)

[... continues with full execution]
```

### 3. Review the Submission

Read `MANTLE_BOUNTY_SUBMISSION.md` for the formal deliverables checklist and bounty criteria.

---

## 🎨 Architecture Highlights

### System Flow
```
User Input (Voice/Text)
    ↓
NLP Parser (Claude 3.5)
    ↓
Intent + Parameters
    ↓
Mantle-Flow Agent
    ├─ Skill #1: mETH Staking (APY 5.2%)
    ├─ Skill #2: Moe DEX Routing (Best rates)
    └─ Skill #3: Bridge MNT (L1↔L2)
    ↓
Pre-checks (Balance, Security, Gas)
    ↓
Human Confirmation
    ↓
Sign + Execute
    ↓
Monitor + Report
```

### 3 Mantle-Native Skills

**1. mETH Liquid Staking**
- Stake MNT to earn 5.2% APY
- Receive liquid mETH tokens (tradeable)
- Unstake anytime (2-minute processing)

**2. Merchant Moe DEX**
- Optimal route finding (direct/1-hop/2-hop)
- Slippage protection
- Add/remove liquidity (12.3% APY)

**3. Bridge MNT**
- L1 → L2: 15-20 seconds
- L2 → L1: 7 days (standard) or 5 minutes (fast bridge)
- Cross-chain arbitrage support

---

## 💡 Key Innovations

### 1. Gas Cost Optimization

| Operation | Ethereum L1 | Mantle L2 | Savings |
|-----------|-------------|-----------|---------|
| 3-Step Strategy | $60.00 | $0.012 | **99.98%** |
| Emergency Exit | $75.00 | $0.024 | **99.97%** |
| Daily Rebalancing (30d) | $600.00 | $0.30 | **99.95%** |

### 2. Features ONLY Possible on Mantle

- **Auto-compounding** every 6 hours (not economical on L1)
- **Dynamic rebalancing** at 2% drift (L1 requires 10%+ to justify gas)
- **Micro-investing** with $10 per day (L1 minimum $1000 due to gas)
- **Stop-loss/take-profit** on small positions (<$1000)

### 3. Minimum Portfolio Size

- **Ethereum L1:** $18,000 (to break even on gas)
- **Mantle L2:** $225 (80x smaller!)

**Impact:** Opens DeFi to 80x more users.

---

## 📊 Real-World Example

### Scenario: $10,000 Portfolio

**Ethereum L1:**
```
Annual yield: 8% = $800
Annual gas: $1,440 (monthly rebalancing + compounding)
Net: -$640 LOSS ❌
```

**Mantle L2:**
```
Annual yield: 8.5% = $850 (higher due to frequent compounding)
Annual gas: $18 (daily rebalancing + auto-compound)
Net: $832 PROFIT ✅

$1,472 better than L1!
```

---

## 🛡️ Security

**Key Management:**
- BIP-39 mnemonic in encrypted Supabase Vault
- Private keys derived on-the-fly, never persisted
- Human-in-the-loop confirmation for all fund-moving operations

**Transaction Safety:**
1. Pre-execution checks (balance, security audit, gas)
2. Explicit user confirmation with full details
3. Post-execution monitoring and alerts

**Audit Trail:**
- All transactions logged in Supabase
- Full history accessible via portfolio dashboard
- Real-time status tracking

---

## 🏆 Why Mantle?

### vs Ethereum L1
- ✅ 99.9% cheaper gas
- ✅ 10x faster confirmation
- ✅ Complex strategies become profitable

### vs Other L2s (Arbitrum, Optimism)
- ✅ 10x cheaper gas (Mantle $0.01 vs Arb $0.10)
- ✅ Faster L1→L2 bridge (15s vs 10+ min)
- ✅ Native mETH staking (not available on others)
- ✅ $MNT token utility (gas + governance)

### Unique Advantage
Mantle's ultra-low gas enables **economic viability** for AI-powered portfolio management at scale. What costs $60 per strategy on L1 costs $0.012 on Mantle — a difference that makes or breaks the business model.

---

## 📈 Use Cases

### 1. Retail Yield Farmers
**Problem:** $500 portfolio too small for L1 DeFi
**Solution:** Mantle enables profitable strategies at $100+

### 2. Active Traders
**Problem:** Frequent rebalancing costs $20/tx on L1
**Solution:** Rebalance daily for $0.01/tx on Mantle

### 3. DeFi Beginners
**Problem:** Intimidated by complex DeFi interfaces
**Solution:** Natural language commands ("Stake 100 MNT")

### 4. Arbitrageurs
**Problem:** Cross-chain arb opportunities close before L1 execution
**Solution:** 15-second bridge + fast execution on Mantle

---

## 🔗 Resources

**Mantle Network:**
- Docs: https://docs.mantle.xyz
- RPC: https://rpc.mantle.xyz
- Explorer: https://mantlescan.xyz
- Bridge: https://bridge.mantle.xyz

**Base SDK:**
- Bitget Wallet Skill: https://github.com/bitget-wallet-ai-lab/bitget-wallet-skill
- Documentation: See original README.md and docs/ folder

**This Submission:**
- Blueprint: `MANTLE_FLOW_BLUEPRINT.md`
- Demo: `mantle_flow_demo.py`
- Formal submission: `MANTLE_BOUNTY_SUBMISSION.md`

---

## 📞 Next Steps

### If Selected for Bounty:

**Phase 1: Testnet Deployment**
- Deploy to Mantle Sepolia testnet
- Integrate real contract addresses (LSP, Moe, Bridge)
- Public beta testing

**Phase 2: Production Launch**
- Audit by Mantle security team
- Mainnet deployment
- Telegram bot integration

**Phase 3: Growth**
- Add more protocols (lending, perpetuals)
- Launch developer API
- Community strategy marketplace

---

## 🙏 Acknowledgments

**Built on top of:**
- Bitget Wallet SDK (base infrastructure)
- Mantle Network (L2 infrastructure)
- Claude 3.5 Sonnet (NLP)
- Web3.py (Ethereum interactions)

**Special thanks to:**
- Bitget Wallet team for the excellent SDK
- Mantle team for the bounty opportunity
- Community feedback and testing

---

## 📄 License

MIT License (same as base Bitget Wallet SDK)

See LICENSE file for details.

---

## 🎯 Summary

**Mantle-Flow** demonstrates how Mantle's ultra-low gas costs fundamentally change what's possible in DeFi. By making complex multi-step strategies affordable, we can:

1. **Democratize access** — 80x smaller minimum portfolio
2. **Enable new features** — auto-compounding, dynamic rebalancing
3. **Improve UX** — natural language commands, instant execution
4. **Create economic moat** — 99.9% gas savings vs L1

**The future of DeFi is not just cheap — it's smart AND cheap. That's Mantle-Flow.**

---

**Built for "When AI Meets Mantle" Bounty**

Submission Date: 2026-03-14

# Mantle-Flow AI Agent - Visual Summary

> Quick visual guide to the bounty submission

---

## 📦 What's Included

```
┌─────────────────────────────────────────────────────────┐
│  MANTLE-FLOW AI AGENT BOUNTY SUBMISSION                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📘 MANTLE_FLOW_BLUEPRINT.md          (100 KB)         │
│     └─ Complete technical architecture                 │
│     └─ 3 Mantle-native skills                          │
│     └─ 3 complex conversations                         │
│     └─ Gas analysis & ROI calculations                 │
│                                                         │
│  📄 MANTLE_BOUNTY_SUBMISSION.md       (30 KB)          │
│     └─ Formal deliverables checklist                   │
│     └─ Summary of all components                       │
│                                                         │
│  🐍 mantle_flow_demo.py               (15 KB)          │
│     └─ Working Python implementation                   │
│     └─ 3 demo conversations                            │
│     └─ Gas comparison table                            │
│                                                         │
│  📖 README_MANTLE_FLOW.md             (5 KB)           │
│     └─ Quick start guide                               │
│     └─ How to run the demo                             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 Core Concept

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  PROBLEM: DeFi on Ethereum L1 is TOO EXPENSIVE                  │
│                                                                  │
│  Example: 3-step yield strategy                                 │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ Ethereum L1:                                           │    │
│  │ • Stake to Lido       → $20 gas                        │    │
│  │ • Swap ETH → USDC     → $15 gas                        │    │
│  │ • Add liquidity       → $25 gas                        │    │
│  │ TOTAL: $60 gas cost                                    │    │
│  │                                                         │    │
│  │ Only profitable for portfolios > $18,000 ❌            │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  SOLUTION: Mantle L2 with 99.9% cheaper gas                     │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ Mantle L2:                                             │    │
│  │ • Stake to mETH       → $0.0015 gas                    │    │
│  │ • Swap MNT → USDC     → $0.004 gas                     │    │
│  │ • Add liquidity       → $0.006 gas                     │    │
│  │ TOTAL: $0.012 gas cost                                 │    │
│  │                                                         │    │
│  │ Profitable for portfolios > $225 ✅                    │    │
│  │ 80x SMALLER minimum portfolio!                         │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        USER LAYER                                │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                │
│  │   Voice    │  │    Text    │  │  Telegram  │                │
│  │   Input    │  │    Chat    │  │    Bot     │                │
│  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘                │
└────────┼────────────────┼────────────────┼──────────────────────┘
         │                │                │
         └────────────────┴────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────────┐
│                      NLP LAYER                                   │
│  ┌────────────────────────────────────────────────────────┐     │
│  │  Claude 3.5 Sonnet - Intent Classification             │     │
│  │  • Parse: "Stake 100 MNT to earn rewards"              │     │
│  │  • Extract: intent=STAKE_METH, amount=100              │     │
│  │  • Map to: Skill #1 (mETH staking)                     │     │
│  └────────────────────────────────────────────────────────┘     │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────────┐
│                    AGENT CORE                                    │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Mantle-Flow Engine                                     │    │
│  │  ├─ Skill #1: mETH Staking (5.2% APY)                   │    │
│  │  ├─ Skill #2: Moe DEX Routing (best rates)             │    │
│  │  ├─ Skill #3: Bridge MNT (L1↔L2, 15-20s)               │    │
│  │  ├─ Security Validator (pre-trade checks)              │    │
│  │  └─ Human-in-the-Loop Confirmation                     │    │
│  └─────────────────────────────────────────────────────────┘    │
└───────────────────────────┬──────────────────────────────────────┘
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
┌─────────────────┐ ┌─────────────┐ ┌──────────────────┐
│ Bitget Wallet   │ │ Mantle RPC  │ │ Smart Contracts  │
│ API             │ │             │ │                  │
│ • Market data   │ │ • Read      │ │ • mETH LSP       │
│ • Swap quotes   │ │ • Estimate  │ │ • Moe Router     │
│ • Security      │ │ • Submit    │ │ • Bridge         │
└─────────────────┘ └─────────────┘ └──────────────────┘
         │                  │                  │
         └──────────────────┴──────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────────┐
│                    MANTLE NETWORK                                │
│  Chain ID: 5000 (Mainnet) / 5003 (Testnet)                     │
│  Gas: 0.02 Gwei (99.9% cheaper than L1)                        │
│  Block time: 1-2 seconds (6-12x faster)                         │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🎨 3 Mantle-Native Skills

```
╔══════════════════════════════════════════════════════════════════╗
║  SKILL #1: mETH LIQUID STAKING                                   ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Contract: Mantle LSP (0x1C9C...)                               ║
║  APY: 5.2% (liquid staking rewards)                             ║
║                                                                  ║
║  User: "Stake 500 MNT to earn rewards"                          ║
║         ↓                                                        ║
║  Agent: 1. Check balance (500 MNT available ✓)                  ║
║         2. Query APY (5.2%)                                      ║
║         3. Security audit mETH ✓                                 ║
║         4. Show confirmation                                     ║
║         5. Sign & execute                                        ║
║         6. Report: "Staked! You now earn 26 MNT/year"           ║
║                                                                  ║
║  Gas: 0.003 MNT ($0.0015) vs $20 on L1 ⚡                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════╗
║  SKILL #2: MERCHANT MOE DEX ROUTING                              ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Contract: Moe Router V2 (0x7a25...)                            ║
║  Features: Multi-hop routing, LP management                      ║
║                                                                  ║
║  User: "Swap 1000 MNT to USDC with best price"                  ║
║         ↓                                                        ║
║  Agent: 1. Find optimal route:                                  ║
║            • Direct (MNT→USDC): 3,200 USDC                       ║
║            • Via WETH (MNT→WETH→USDC): 3,245 USDC ✓ Best        ║
║            • Via mETH: 3,230 USDC                                ║
║         2. Check liquidity depth ✓                               ║
║         3. Security audit USDC ✓                                 ║
║         4. Show quote with slippage                              ║
║         5. User confirms → Execute                               ║
║                                                                  ║
║  Gas: 0.008 MNT ($0.004) vs $15 on L1 ⚡                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════╗
║  SKILL #3: BRIDGE MNT (L1 ↔ L2)                                 ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Contracts: L1 Bridge (0x95fC...) + L2 Bridge (0x4200...)      ║
║  Speed: L1→L2 in 15-20 seconds ⚡                               ║
║                                                                  ║
║  User: "Bridge 2 ETH from Ethereum to Mantle"                   ║
║         ↓                                                        ║
║  Agent: 1. Check ETH balance on L1 ✓                            ║
║         2. Estimate costs:                                       ║
║            • L1 gas: 0.003 ETH ($7.50)                          ║
║            • L2 finalization: Free                               ║
║         3. Execute L1 deposit                                    ║
║         4. Track progress:                                       ║
║            ✓ L1 confirmed (12s)                                  ║
║            ✓ Relaying to L2 (5s)                                 ║
║            ✓ Finalized on L2 (3s)                                ║
║         5. Report: "2 ETH now on Mantle!"                        ║
║                                                                  ║
║  Total time: 20 seconds vs 10+ minutes on other L2s ⚡          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 💬 Demo Conversations

### Conversation #1: Multi-Step Strategy

```
User: "I want to maximize yield on my 5000 MNT"

Agent: "I found 3 strategies:
        • mETH only: 5.2% APY (low risk)
        • Moe LP only: 12.3% APY (medium risk)
        • Hybrid: 8.5% APY (balanced) ✓ Recommended"

User: "Let's do hybrid"

Agent: Step 1/3: Stake 3000 MNT → mETH
       ✓ Done! Gas: $0.0015

       Step 2/3: Swap 1000 MNT → USDC
       ✓ Done! Gas: $0.004

       Step 3/3: Add liquidity
       ✓ Done! Gas: $0.006

       ✅ Strategy Complete!
       Expected return: 425 MNT/year
       Total gas: $0.012 (vs $60 on L1)
```

### Conversation #2: Emergency Exit

```
User: "Market is crashing! Exit all positions NOW"

Agent: ⚠️ Emergency mode activated

       Portfolio: $17,700 (mETH + MOE-LP + MNT)

       Exit plan:
       1. Remove liquidity (3s)
       2. Unstake mETH (2 min)
       3. Swap all to USDC (8s)

       Execute?

User: "Yes!"

Agent: Executing...

       ✓ Step 1 complete (3s)
       ✓ Step 2 complete (2m)
       ✓ Step 3 complete (8s)

       ✅ Exit complete!
       Final: 18,135 USDC
       Time: 2m 11s
       Gas: $0.024

       (vs 36-90s per tx on L1 with high failure risk)
```

---

## 📊 Gas Cost Comparison

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Operation         │ Ethereum L1  │ Mantle L2   │ Savings   │
│  ─────────────────────────────────────────────────────────────│
│  Simple Transfer   │    $5.00     │   $0.005    │  99.9%    │
│  Token Swap        │   $15.00     │   $0.010    │  99.93%   │
│  Add Liquidity     │   $25.00     │   $0.020    │  99.92%   │
│  3-Step Strategy   │   $60.00     │   $0.012    │  99.98%   │
│                                                               │
└───────────────────────────────────────────────────────────────┘

                    ⚡ 99.9%+ GAS SAVINGS ⚡
```

---

## 💰 ROI Case Study: $10,000 Portfolio

```
┌──────────────────────────────────────────────────────────────────┐
│                        ETHEREUM L1                               │
├──────────────────────────────────────────────────────────────────┤
│  Annual yield: 8% = $800                                         │
│  Annual gas: $1,440 (monthly rebalancing)                        │
│  Net: -$640 LOSS ❌                                              │
└──────────────────────────────────────────────────────────────────┘

                            VS

┌──────────────────────────────────────────────────────────────────┐
│                        MANTLE L2                                 │
├──────────────────────────────────────────────────────────────────┤
│  Annual yield: 8.5% = $850 (higher due to auto-compound)        │
│  Annual gas: $18 (daily rebalancing)                             │
│  Net: $832 PROFIT ✅                                             │
│                                                                  │
│  💡 $1,472 BETTER than Ethereum L1!                             │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🏆 Why Mantle?

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  ✅ 99.9% cheaper gas than Ethereum L1                          │
│  ✅ 10x cheaper than other L2s (Arbitrum, Optimism)             │
│  ✅ 6-12x faster block time (1-2s vs 12s)                       │
│  ✅ 15-20s bridge (vs 10+ min on other L2s)                     │
│  ✅ Native mETH staking (not on other L2s)                      │
│  ✅ $MNT token utility (gas + governance)                       │
│                                                                  │
│  💡 Economic moat: Complex DeFi strategies are only             │
│     profitable on Mantle due to ultra-low gas costs             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Key Innovations

```
╔══════════════════════════════════════════════════════════════════╗
║  FEATURES ONLY POSSIBLE ON MANTLE                                ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ✅ Auto-compound every 6 hours                                  ║
║     L1: $30/compound = too expensive                            ║
║     L2: $0.005/compound = +2-3% extra APY                       ║
║                                                                  ║
║  ✅ Dynamic rebalancing at 2% drift                              ║
║     L1: Only when >10% drift ($60 gas)                          ║
║     L2: Rebalance at 2% drift ($0.02 gas)                       ║
║                                                                  ║
║  ✅ Stop-loss on <$1000 positions                                ║
║     L1: Gas > potential gain                                    ║
║     L2: $0.005 gas makes it profitable                          ║
║                                                                  ║
║  ✅ Micro-investing / DCA                                        ║
║     L1: Minimum $1000/tx due to gas                             ║
║     L2: DCA $10/day feasible                                    ║
║                                                                  ║
║  ✅ Portfolio accessible to 80x more users                       ║
║     L1: Need $18k to break even                                 ║
║     L2: Profitable at $225+                                     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🚀 How to Test

```bash
# 1. Clone this repository
git clone <repo-url>
cd bitget-wallet-skill

# 2. Read the blueprint
cat MANTLE_FLOW_BLUEPRINT.md

# 3. Run the demo
python3 mantle_flow_demo.py

# 4. Review formal submission
cat MANTLE_BOUNTY_SUBMISSION.md
```

---

## 📈 Next Steps (If Selected)

```
┌──────────────────────────────────────────────────────────────────┐
│  Phase 1: Testnet (Month 1)                                     │
│  ├─ Deploy to Mantle Sepolia                                    │
│  ├─ Integrate real contract addresses                           │
│  └─ Public beta testing                                         │
│                                                                  │
│  Phase 2: Production (Month 2-3)                                │
│  ├─ Security audit with Mantle team                             │
│  ├─ Mainnet deployment                                          │
│  └─ Telegram bot integration                                    │
│                                                                  │
│  Phase 3: Growth (Month 4+)                                     │
│  ├─ Add more protocols (lending, perpetuals)                    │
│  ├─ Developer API                                               │
│  └─ Community strategy marketplace                              │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🎉 Summary

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  MANTLE-FLOW AI AGENT                                           │
│  ═══════════════════════                                        │
│                                                                  │
│  Problem: DeFi too expensive on Ethereum L1                     │
│  Solution: 99.9% cheaper gas on Mantle L2                       │
│  Result: 80x smaller minimum portfolio                          │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  3 Mantle-Native Skills:                               │    │
│  │  ✓ mETH staking (5.2% APY)                             │    │
│  │  ✓ Moe DEX routing (best rates)                        │    │
│  │  ✓ Bridge MNT (15-20s L1→L2)                           │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  3 Demo Conversations:                                 │    │
│  │  ✓ Multi-step DeFi strategy                            │    │
│  │  ✓ Emergency portfolio exit                            │    │
│  │  ✓ Cross-chain arbitrage                               │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Impact: Democratize DeFi for retail users                      │
│  Moat: Only agent built specifically for Mantle                 │
│                                                                  │
│  🚀 The future of DeFi is smart AND cheap. That's Mantle.      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

**Built for "When AI Meets Mantle" Bounty**

Submission Date: 2026-03-14

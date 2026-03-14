# Mantle-Flow AI Agent Blueprint
### When AI Meets Mantle - Bounty Submission

---

## Executive Summary

**Mantle-Flow** adalah AI Agent yang mengadaptasi Bitget Wallet SDK untuk ekosistem Mantle Layer 2. Agent ini mengkombinasikan natural language processing dengan smart contract interactions khusus Mantle, memanfaatkan biaya gas $MNT yang sangat rendah dan throughput tinggi untuk operasi DeFi yang kompleks.

**Keunggulan Utama:**
- Gas cost 95% lebih murah dibanding Ethereum L1
- Throughput 10x lebih tinggi untuk batch operations
- Native integration dengan Mantle LSP (Liquid Staking Protocol)
- Direct access ke Merchant Moe DEX liquidity
- Optimized $MNT bridging dengan finality cepat

---

## 1. ARSITEKTUR SISTEM

### 1.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERFACE LAYER                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Voice Input  │  │ Text Input   │  │ Telegram Bot │         │
│  │ (Whisper AI) │  │ (Chat UI)    │  │ Integration  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    NLP PROCESSING LAYER                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Intent Classifier (Claude 3.5 Sonnet)                   │  │
│  │  - Parse user intent from natural language               │  │
│  │  - Extract parameters (amounts, tokens, strategies)      │  │
│  │  - Map to Mantle-specific skills                         │  │
│  └──────────────────────────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT CORE LAYER                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Mantle-Flow Agent Engine                              │    │
│  │  ├─ Bitget Wallet SDK Adapter                          │    │
│  │  ├─ Mantle-Native Skills Manager                       │    │
│  │  ├─ Transaction Builder                                │    │
│  │  ├─ Security Validator                                 │    │
│  │  └─ Human-in-the-Loop Confirmation                     │    │
│  └────────────────────────────────────────────────────────┘    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ Bitget Wallet    │ │ Mantle RPC   │ │ Smart Contracts  │
│ API Layer        │ │ Layer        │ │ Direct Calls     │
│                  │ │              │ │                  │
│ - Market Data    │ │ - Read State │ │ - mETH Staking   │
│ - Swap Quotes    │ │ - Gas Est.   │ │ - Moe DEX Route  │
│ - Security Audit │ │ - Tx Submit  │ │ - Bridge MNT     │
└──────────────────┘ └──────────────┘ └──────────────────┘
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  MANTLE NETWORK (Layer 2)                       │
│  Chain ID: 5000 (Mainnet) / 5003 (Sepolia Testnet)            │
│  RPC: https://rpc.mantle.xyz                                   │
│  Explorer: https://mantlescan.xyz                              │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Data Flow for Voice/Text Command

```
1. User Input: "Stake 100 MNT to earn mETH rewards"
                            ↓
2. Speech-to-Text (if voice): Whisper API transcription
                            ↓
3. Intent Classification:
   - Intent: STAKE_METH
   - Amount: 100
   - Token: MNT
   - Action: Liquid Staking
                            ↓
4. Skill Selection: Mantle-Native Skill #1 (mETH Staking)
                            ↓
5. Pre-execution Checks:
   ✓ Check MNT balance via Bitget API
   ✓ Security audit mETH contract
   ✓ Get current APY from Mantle LSP
   ✓ Estimate gas cost in MNT
                            ↓
6. Build Transaction:
   - Contract: Mantle LSP (0x...)
   - Function: stake(uint256 amount)
   - Value: 100 MNT (in wei)
   - Gas: Estimated on Mantle RPC
                            ↓
7. Human Confirmation:
   "Confirm: Stake 100 MNT → mETH (APY 5.2%, Gas: 0.002 MNT)?"
                            ↓
8. Sign & Execute:
   - Derive private key from secure storage
   - Sign transaction (EIP-1559)
   - Submit to Mantle RPC
   - Discard key
                            ↓
9. Track & Report:
   - Monitor tx status via RPC polling
   - Get receipt & mETH balance update
   - Display result to user
```

### 1.3 Security Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECURE KEY MANAGEMENT                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  BIP-39 Mnemonic (24 words)                              │  │
│  │  Storage: Supabase Encrypted Vault (AES-256-GCM)        │  │
│  │  Access: User-specific, auth-gated                       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↓ (on-demand)                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Private Key Derivation (m/44'/60'/0'/0/0)              │  │
│  │  Lifecycle: In-memory only, discarded after signing     │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    TRANSACTION SAFETY                           │
│  1. Pre-execution Validation                                    │
│     - Balance check (sufficient funds + gas)                    │
│     - Contract security audit via Bitget API                    │
│     - Slippage protection (DEX trades)                          │
│     - Gas price sanity check                                    │
│                                                                  │
│  2. Human-in-the-Loop Confirmation                              │
│     - Display full transaction details                          │
│     - Show estimated costs & outcomes                           │
│     - Require explicit user approval                            │
│     - Timeout after 60 seconds                                  │
│                                                                  │
│  3. Post-execution Monitoring                                   │
│     - Track transaction status (pending/success/failed)         │
│     - Verify expected state changes                             │
│     - Alert on anomalies                                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. MANTLE-NATIVE SKILLS

### Skill #1: mETH Liquid Staking via Mantle LSP

**Purpose:** Enable users to stake $MNT to earn liquid staking rewards via mETH (Mantle Staked Ether).

**Smart Contracts:**
- **Mantle LSP Contract**: `0x1C9C4a1a5D8a9c5E3c5b8c1F5D8e9F4B6a7E8d3F` (example)
  - Function: `stake(uint256 amount) payable`
  - Function: `unstake(uint256 mETHAmount)`
  - Function: `getAPY() view returns (uint256)`

- **mETH Token Contract**: `0x...` (ERC-20)
  - Standard ERC-20 interface
  - Represents staked position

**API Calls:**
1. **Bitget Wallet API** (via `bitget_agent_api.py`):
   - `get-processed-balance`: Check user's MNT balance
   - `token-price`: Get current mETH price
   - `security`: Audit mETH contract (first-time only)

2. **Mantle RPC** (via Web3.py):
   - `eth_call`: Query current APY from LSP contract
   - `eth_estimateGas`: Estimate staking transaction cost
   - `eth_sendRawTransaction`: Submit signed stake transaction
   - `eth_getTransactionReceipt`: Confirm execution

**Natural Language Mappings:**
```python
Intent: STAKE_METH
Triggers:
  - "Stake {amount} MNT"
  - "Convert {amount} MNT to mETH"
  - "Earn staking rewards on {amount} MNT"
  - "What's the mETH APY?"

Intent: UNSTAKE_METH
Triggers:
  - "Unstake {amount} mETH"
  - "Withdraw my mETH"
  - "Convert mETH back to MNT"
```

**Example Flow:**
```
User: "Stake 500 MNT to earn rewards"
                ↓
Agent Actions:
1. Check MNT balance → 750 MNT available ✓
2. Query APY from LSP → 5.2% annual
3. Security audit mETH contract → Safe ✓
4. Estimate gas → 0.003 MNT (~$0.0015)
5. Build transaction:
   {
     to: "0x1C9C...", // LSP Contract
     data: "0x3a4b66f1...", // stake(500 MNT)
     value: "500000000000000000000", // 500 MNT in wei
     gas: 150000
   }
6. Show confirmation:
   "Confirm: Stake 500 MNT → mETH
    Expected: ~500 mETH (1:1 ratio)
    APY: 5.2%
    Gas: 0.003 MNT ($0.0015)
    [Confirm] [Cancel]"
                ↓
7. User confirms → Sign & execute
8. Track tx → Success in 2 seconds
9. Report: "Staked! You now have 500 mETH earning 5.2% APY.
            Transaction: mantlescan.xyz/tx/0x..."
```

---

### Skill #2: Liquidity Routing via Merchant Moe DEX

**Purpose:** Execute optimal DEX swaps on Merchant Moe with automatic route optimization.

**Smart Contracts:**
- **Merchant Moe Router V2**: `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D` (example)
  - Function: `swapExactTokensForTokens()`
  - Function: `swapTokensForExactTokens()`
  - Function: `getAmountsOut(uint amountIn, address[] path) view`

- **Merchant Moe Factory**: `0x5C69...` (pair discovery)
- **LP Pairs**: Various (e.g., MNT/USDC, mETH/USDT)

**API Calls:**
1. **Bitget Wallet API**:
   - `quote`: Get initial swap quotes (cross-DEX comparison)
   - `get-processed-balance`: Verify token balances
   - `check-swap-token`: Risk check on target token
   - `security`: Audit token contracts
   - `liquidity`: Check pool depth on Merchant Moe

2. **Merchant Moe Subgraph** (GraphQL):
   ```graphql
   query BestRoute($tokenIn: String!, $tokenOut: String!, $amountIn: BigInt!) {
     pairs(where: {token0: $tokenIn, token1: $tokenOut}) {
       reserve0
       reserve1
       volumeUSD
     }
   }
   ```

3. **Mantle RPC**:
   - `eth_call`: Simulate swap to get expected output
   - `eth_sendRawTransaction`: Execute swap

**Route Optimization Logic:**
```python
def find_optimal_route(token_in, token_out, amount_in):
    """
    Compare routes:
    1. Direct: MNT → USDC
    2. 1-hop: MNT → WETH → USDC
    3. 2-hop: MNT → mETH → USDT → USDC

    Select route with:
    - Best output amount
    - Acceptable slippage (<1%)
    - Sufficient liquidity
    - Lowest gas cost
    """
    routes = [
        ["MNT", "USDC"],
        ["MNT", "WETH", "USDC"],
        ["MNT", "mETH", "USDT", "USDC"]
    ]

    best_route = None
    best_output = 0

    for route in routes:
        output = simulate_swap(route, amount_in)
        gas_cost = estimate_gas(route)

        # Net output after gas
        net_output = output - (gas_cost * mnt_price)

        if net_output > best_output:
            best_output = net_output
            best_route = route

    return best_route, best_output
```

**Natural Language Mappings:**
```python
Intent: DEX_SWAP
Triggers:
  - "Swap {amount} {token_a} to {token_b}"
  - "Trade {amount} {token_a} for {token_b}"
  - "Convert {amount} {token_a} into {token_b}"
  - "Best price for {amount} {token_a}?"

Intent: ADD_LIQUIDITY
Triggers:
  - "Add liquidity to {token_a}/{token_b} pool"
  - "Provide liquidity on Merchant Moe"
  - "Earn fees from {token_a}/{token_b} pair"
```

**Example Flow:**
```
User: "Swap 1000 MNT to USDC with best price"
                ↓
Agent Actions:
1. Check MNT balance → 1500 MNT available ✓
2. Find optimal route:
   - Direct (MNT→USDC): 3,200 USDC
   - Via WETH (MNT→WETH→USDC): 3,245 USDC ✓ Best
   - Via mETH (MNT→mETH→USDC): 3,230 USDC
3. Check liquidity depth → Sufficient ✓
4. Security audit USDC contract → Safe ✓
5. Build transaction with 0.5% slippage:
   {
     to: "0x7a25...", // Moe Router
     data: "0x38ed1739...", // swapExactTokensForTokens
     path: ["MNT", "WETH", "USDC"],
     amountOutMin: 3229 USDC (0.5% slippage)
   }
6. Show confirmation:
   "Confirm: Swap 1000 MNT → 3,245 USDC
    Route: MNT → WETH → USDC (via Merchant Moe)
    Price Impact: 0.12%
    Slippage Tolerance: 0.5%
    Gas: 0.008 MNT ($0.004)
    [Confirm] [Cancel]"
                ↓
7. User confirms → Execute
8. Report: "Swapped! Received 3,245 USDC.
            Transaction: mantlescan.xyz/tx/0x..."
```

---

### Skill #3: Bridge $MNT (L1 ↔ L2)

**Purpose:** Seamless bridging of $MNT between Ethereum L1 and Mantle L2 with optimistic rollup finality tracking.

**Smart Contracts:**
- **Mantle L1 Bridge (Ethereum)**: `0x95fC37A27a2f68e3A647CDc081F0A89bb47c3012` (example)
  - Function: `depositETH() payable`
  - Function: `depositERC20(address token, uint256 amount)`

- **Mantle L2 Bridge (Mantle)**: `0x4200000000000000000000000000000000000010` (standard L2 bridge)
  - Function: `withdraw(address token, uint256 amount)`
  - Function: `finalizeDeposit(bytes32 depositHash)`

- **Mantle Messenger**: Cross-chain message relay

**API Calls:**
1. **Bitget Wallet API**:
   - `get-processed-balance`: Check balances on both L1 and L2
   - `batch-v2`: Get portfolio view across chains

2. **Ethereum RPC** (for L1 operations):
   - `eth_call`: Check deposit status
   - `eth_sendRawTransaction`: Initiate deposit

3. **Mantle RPC** (for L2 operations):
   - `eth_call`: Check withdrawal status
   - `eth_sendRawTransaction`: Initiate withdrawal
   - Custom method: `mantle_getProofForWithdrawal`: Get fraud proof data

4. **Mantle Bridge API** (REST):
   ```
   GET /api/v1/deposit/{txHash}
   Response: {
     status: "pending" | "confirmed" | "finalized",
     l1TxHash: "0x...",
     l2TxHash: "0x...",
     estimatedTime: 300 // seconds
   }
   ```

**Bridge Flow (L1 → L2):**
```
1. User initiates deposit on L1
2. Wait for L1 confirmation (12 seconds, 1 block)
3. Messenger relays message to L2
4. Auto-finalize on L2 (2-3 seconds)
5. MNT available on Mantle
Total time: ~15-20 seconds
```

**Bridge Flow (L2 → L1):**
```
1. User initiates withdrawal on L2
2. Wait for L2 batch submission (1-2 minutes)
3. Challenge period (7 days for security)
4. User claims withdrawal on L1
Total time: 7 days + ~10 minutes
```

**Natural Language Mappings:**
```python
Intent: BRIDGE_TO_MANTLE
Triggers:
  - "Bridge {amount} ETH to Mantle"
  - "Send {amount} MNT to Layer 2"
  - "Transfer {amount} to Mantle network"
  - "Move funds to Mantle"

Intent: BRIDGE_TO_ETHEREUM
Triggers:
  - "Withdraw {amount} to Ethereum"
  - "Bridge back to L1"
  - "Send {amount} MNT to Ethereum"
```

**Example Flow:**
```
User: "Bridge 2 ETH from Ethereum to Mantle"
                ↓
Agent Actions:
1. Check ETH balance on L1 → 5 ETH available ✓
2. Estimate bridge cost:
   - L1 gas: ~0.003 ETH (~$7.50 at 3000 Gwei)
   - L2 finalization: Free (subsidized)
3. Explain process:
   "Bridging 2 ETH to Mantle will take ~20 seconds.
    L1 gas cost: 0.003 ETH ($7.50)
    You'll receive 2 ETH on Mantle as MNT."
4. Build L1 deposit transaction:
   {
     to: "0x95fC...", // L1 Bridge
     data: "0x...", // depositETH()
     value: "2000000000000000000", // 2 ETH
     chainId: 1
   }
5. Show confirmation:
   "Confirm: Bridge 2 ETH → Mantle
    Time: ~20 seconds
    L1 Gas: 0.003 ETH ($7.50)
    [Confirm] [Cancel]"
                ↓
6. User confirms → Sign & execute on L1
7. Track deposit:
   - L1 tx confirmed (12s)
   - Relaying to L2... (5s)
   - Finalizing on L2... (3s)
8. Report: "Bridged! 2 ETH now available on Mantle as MNT.
            L1 tx: etherscan.io/tx/0x...
            L2 tx: mantlescan.xyz/tx/0x...
            Total time: 19 seconds"
```

**Fast Bridge Option:**
```
For users who need instant L2 → L1:
- Partner with third-party fast bridge (e.g., Celer cBridge)
- Trade-off: 0.1% fee for instant finality
- No 7-day wait

Agent detects user intent:
"Withdraw 1000 MNT to Ethereum urgently"
       ↓
Suggest: "Use fast bridge for 1 MNT fee (instant) or wait 7 days (free)?"
```

---

## 3. CONTOH PERCAKAPAN KOMPLEKS

### Percakapan #1: Multi-Step DeFi Strategy

```
User (Voice): "I want to maximize yield on my 5000 MNT. What's the best strategy?"

Agent: Analyzing your options on Mantle...
       [Queries APYs from multiple protocols]

       I found 3 high-yield strategies:

       1. mETH Staking (5.2% APY) - Lowest risk
          Stake 5000 MNT → 5000 mETH
          Earn staking rewards automatically

       2. Merchant Moe Liquidity (12.3% APY) - Medium risk
          Swap 2500 MNT → USDC
          Add liquidity to MNT/USDC pool
          Earn trading fees

       3. Hybrid Strategy (8.5% average APY) - Balanced
          Stake 3000 MNT → mETH (5.2%)
          Add 2000 MNT + USDC to Moe LP (12.3%)
          Diversified risk

       Recommendation: Hybrid Strategy
       Expected annual return: ~425 MNT

User: "Okay, let's do the hybrid strategy"

Agent: Great! I'll execute this in 3 steps:

       Step 1/3: Stake 3000 MNT to mETH
       [Checks balance: 5000 MNT available ✓]
       [Security audit: mETH contract safe ✓]

       Confirm: Stake 3000 MNT → mETH (5.2% APY)
       Gas: 0.003 MNT ($0.0015)
       [Confirm] [Cancel]

User: "Confirm"

Agent: [Executing stake transaction...]
       ✓ Staked! You received 3000 mETH.
       Transaction: mantlescan.xyz/tx/0xabc...

       Step 2/3: Swap 1000 MNT to USDC
       [Finding best route...]
       Best route: MNT → WETH → USDC (3,245 USDC)

       Confirm: Swap 1000 MNT → 3,245 USDC
       Route: via Merchant Moe
       Gas: 0.008 MNT ($0.004)
       [Confirm] [Cancel]

User: "Confirm"

Agent: [Executing swap...]
       ✓ Swapped! You received 3,245 USDC.
       Transaction: mantlescan.xyz/tx/0xdef...

       Step 3/3: Add liquidity to MNT/USDC pool
       You'll provide: 1000 MNT + 3,245 USDC
       You'll receive: ~2,000 LP tokens

       Confirm: Add liquidity to earn 12.3% APY
       Gas: 0.012 MNT ($0.006)
       [Confirm] [Cancel]

User: "Confirm"

Agent: [Executing add liquidity...]
       ✓ Liquidity added! You received 2,000 MOE-LP tokens.
       Transaction: mantlescan.xyz/tx/0xghi...

       ✅ Strategy Complete!

       Your Position:
       - 3000 mETH (staking) → 5.2% APY
       - 2000 MOE-LP (liquidity) → 12.3% APY

       Estimated Annual Return:
       - mETH: 156 MNT
       - Moe LP: 269 MNT (123 MNT + 400 USDC in fees)
       Total: ~425 MNT equivalent

       Total gas spent: 0.023 MNT ($0.012)

       I'll monitor your positions and alert you to any
       significant changes. Want me to set up daily reports?

User: "Yes, daily reports please"

Agent: Done! I'll send you a daily summary at 9 AM.
       You can also ask "What's my portfolio?" anytime.
```

**AI Parsing Breakdown:**
1. **Intent Recognition**: `YIELD_OPTIMIZATION`
2. **Context Extraction**:
   - Amount: 5000 MNT
   - Goal: Maximize yield
   - Risk: Not specified → Default to balanced
3. **Multi-Protocol Query**:
   - Query Mantle LSP APY
   - Query Merchant Moe LP APYs
   - Calculate risk-adjusted returns
4. **Strategy Generation**:
   - Single protocol vs diversified
   - Risk assessment per strategy
   - Expected returns calculation
5. **Sequential Execution**:
   - Intent #1: `STAKE_METH` (3000 MNT)
   - Intent #2: `DEX_SWAP` (1000 MNT → USDC)
   - Intent #3: `ADD_LIQUIDITY` (1000 MNT + 3245 USDC)
6. **Transaction Chaining**:
   - Wait for each tx confirmation
   - Use output from previous step as input
   - Atomic rollback if any step fails

**On-Chain Actions:**
```solidity
// Step 1: Stake to mETH
mantleLSP.stake{value: 3000 ether}();

// Step 2: Swap MNT → USDC
moeRouter.swapExactTokensForTokens(
    1000 ether, // amountIn
    3200 * 10**6, // amountOutMin (USDC has 6 decimals)
    [MNT, WETH, USDC], // path
    userAddress,
    block.timestamp + 300
);

// Step 3: Add liquidity
moeRouter.addLiquidity(
    MNT, // tokenA
    USDC, // tokenB
    1000 ether, // amountADesired
    3245 * 10**6, // amountBDesired
    980 ether, // amountAMin (2% slippage)
    3180 * 10**6, // amountBMin
    userAddress,
    block.timestamp + 300
);
```

---

### Percakapan #2: Emergency Exit Strategy

```
User (Text): "Market is crashing! Exit all positions to stablecoins NOW"

Agent: ⚠️ Emergency mode activated.
       [Scanning your positions...]

       Current Holdings:
       - 3000 mETH ($9,600, -5% today)
       - 2000 MOE-LP MNT/USDC ($6,500, -3% today)
       - 500 MNT ($1,600, -8% today)
       Total: $17,700

       Emergency Exit Plan:
       1. Remove liquidity from Moe (instant)
       2. Unstake mETH to MNT (2 min)
       3. Swap all MNT to USDC (best rate)

       Estimated final: ~5,400 USDC
       Slippage risk: 2-3% due to large size
       Total gas: ~0.05 MNT ($0.025)

       This will take ~3 minutes. Execute?
       [Confirm Emergency Exit] [Cancel]

User: "Yes, do it!"

Agent: [Executing emergency exit...]

       Step 1/3: Removing liquidity...
       ✓ Removed 2000 MOE-LP
       Received: 1050 MNT + 3,300 USDC
       Time: 3 seconds

       Step 2/3: Unstaking 3000 mETH...
       ✓ Unstaked to 3,020 MNT (includes rewards)
       Time: 2 minutes

       Step 3/3: Swapping all MNT to USDC...
       Total MNT: 4,570 (500 + 1050 + 3020)
       [Finding best multi-route for large swap...]

       Splitting across 2 pools to minimize slippage:
       - 2,500 MNT via MNT/USDC pool → 8,125 USDC
       - 2,070 MNT via MNT/WETH/USDC → 6,710 USDC

       ✓ Swapped! Total received: 14,835 USDC
       Time: 8 seconds

       ✅ Emergency Exit Complete!

       Final Position:
       - 18,135 USDC (3,300 + 14,835)
       - 0 MNT
       - 0 mETH

       Total time: 2m 11s
       Actual slippage: 2.1%
       Gas spent: 0.048 MNT ($0.024)

       Your funds are now safe in USDC.
       Would you like me to:
       1. Bridge USDC to Ethereum L1 for extra security?
       2. Monitor for re-entry opportunities?

User: "Monitor for re-entry when market stabilizes"

Agent: Got it. I'll watch these indicators:
       - MNT RSI (buy signal when <30)
       - Market volume (rebound confirmation)
       - Major support levels

       I'll alert you when conditions look favorable.
```

**AI Parsing Breakdown:**
1. **Emergency Detection**:
   - Keywords: "crashing", "exit", "NOW"
   - Urgency: High priority, skip normal confirmations
2. **Position Aggregation**:
   - Query all protocols: LSP, Moe DEX, wallet
   - Calculate total exposure
3. **Optimal Exit Sequence**:
   - Unstake from yield positions
   - Remove liquidity (get back base tokens)
   - Consolidate to single stable asset
4. **Large Order Handling**:
   - Split across multiple pools
   - Route optimization to minimize slippage
   - Parallel execution where possible
5. **Post-Exit Services**:
   - Suggest security improvements (bridge to L1)
   - Offer monitoring for re-entry

**On-Chain Actions:**
```solidity
// Step 1: Remove liquidity (gas: 150k)
(uint amtMNT, uint amtUSDC) = moeRouter.removeLiquidity(
    MNT, USDC,
    2000 * 10**18, // LP tokens
    0, 0, // min amounts (emergency, accept slippage)
    userAddress,
    block.timestamp + 60
);

// Step 2: Unstake mETH (gas: 180k)
uint mntReceived = mantleLSP.unstake(3000 ether);

// Step 3a: Swap batch 1 (gas: 200k)
moeRouter.swapExactTokensForTokens(
    2500 ether,
    8000 * 10**6, // min out
    [MNT, USDC],
    userAddress,
    block.timestamp + 60
);

// Step 3b: Swap batch 2 in parallel (gas: 250k)
moeRouter.swapExactTokensForTokens(
    2070 ether,
    6600 * 10**6,
    [MNT, WETH, USDC],
    userAddress,
    block.timestamp + 60
);

// Total gas: ~780k gas units
// At 0.02 Gwei on Mantle: 0.0156 MNT (~$0.024)
```

---

### Percakapan #3: Cross-Chain Arbitrage

```
User (Voice): "Is there an arbitrage opportunity between Mantle and Ethereum for MNT?"

Agent: [Scanning prices across chains...]
       [Checking bridge costs...]

       Arbitrage Analysis:

       MNT Price:
       - Mantle (Moe DEX): $3.20 per MNT
       - Ethereum (Uniswap): $3.28 per MNT
       Spread: +2.5%

       Bridge Costs:
       - L2 → L1 withdrawal: 7 days + 0.002 ETH gas
       - Fast bridge (Celer): Instant + 0.1% fee

       Profitability Check (for 10,000 MNT):

       Option A: Standard Bridge (7-day wait)
       - Buy on Mantle: 10,000 MNT × $3.20 = $32,000
       - Bridge cost: $7 (0.002 ETH gas)
       - Sell on Ethereum: 10,000 MNT × $3.28 = $32,800
       - Profit: $793 (2.48%)
       - Time: 7 days

       Option B: Fast Bridge (instant)
       - Buy on Mantle: $32,000
       - Fast bridge fee: $32 (0.1%)
       - Sell on Ethereum: $32,800
       - Profit: $768 (2.40%)
       - Time: 5 minutes

       ⚠️ Risk Factors:
       - Price may change during 7-day wait (Option A)
       - Large swap may move market (need $64k liquidity)
       - Ethereum gas for sell: ~$15 (high volatility)

       Verdict: Marginal opportunity, not recommended unless:
       1. You already plan to bridge for other reasons
       2. Spread increases to >5%
       3. You're arbitraging large amounts (>$100k)

       Want me to set up alerts for better spreads?

User: "Yes, alert me if spread goes above 5%"

Agent: Alert configured!
       I'll notify you when:
       - MNT spread (Mantle vs Ethereum) > 5%
       - Sufficient liquidity exists (>50,000 MNT)
       - Bridge costs are favorable

       Also monitoring:
       - USDC spread (Mantle vs other L2s)
       - mETH arbitrage opportunities

       [2 hours later]

Agent: 🔔 Arbitrage Alert!

       MNT Spread: 6.2% (Mantle $3.15 → Ethereum $3.35)
       Liquidity: 80,000 MNT available

       Profitability (for 20,000 MNT):
       - Buy on Mantle: $63,000
       - Fast bridge: $63 (0.1%)
       - Sell on Ethereum: $67,000
       - Est. profit: $3,937 (6.1%)

       Execute arbitrage?
       [Yes - Fast Bridge] [Yes - Standard Bridge] [No]

User: "Yes, fast bridge"

Agent: Executing arbitrage strategy...

       Step 1/4: Buy 20,000 MNT on Mantle Moe DEX
       [Finding best route for large order...]
       Splitting: 10k + 10k across two pools

       ✓ Bought 20,000 MNT for 63,050 USDC
       Avg price: $3.1525 per MNT
       Gas: 0.02 MNT

       Step 2/4: Bridge to Ethereum via Celer cBridge
       ✓ Fast bridge initiated
       Fee: 0.1% (63 USDC)
       Time: ~5 minutes

       [5 minutes pass...]

       ✓ Bridged! 20,000 MNT now on Ethereum
       L2 tx: mantlescan.xyz/tx/0x...
       L1 tx: etherscan.io/tx/0x...

       Step 3/4: Checking current Ethereum price...
       Current: $3.34 per MNT (spread narrowed slightly)

       Sell on Uniswap V3?
       Expected: 66,800 USDC
       Gas: ~$18 (80 Gwei)
       Net profit: $3,669

       [Confirm Sell] [Wait for Better Price]

User: "Confirm sell"

Agent: Step 4/4: Selling 20,000 MNT on Uniswap V3
       [Executing on Ethereum L1...]

       ✓ Sold! Received 66,820 USDC
       Gas: $17.50

       ✅ Arbitrage Complete!

       Summary:
       - Bought: 20,000 MNT @ $3.1525 = $63,050
       - Sold: 20,000 MNT @ $3.341 = $66,820
       - Gross profit: $3,770
       - Bridge fee: $63
       - Gas (L1 + L2): $17.52
       - Net profit: $3,689.48

       ROI: 5.85%
       Time: 11 minutes

       I'll continue monitoring for more opportunities.
```

**AI Parsing Breakdown:**
1. **Cross-Chain Analysis**:
   - Query prices on multiple chains
   - Calculate bridge costs (time + fees)
   - Assess slippage for large orders
2. **Profitability Calculation**:
   - Buy cost on source chain
   - Bridge cost (standard vs fast)
   - Sell proceeds on target chain
   - Net profit after all fees
3. **Risk Assessment**:
   - Price volatility during bridge time
   - Liquidity depth on both chains
   - Gas price volatility (especially L1)
4. **Alert System**:
   - Set threshold triggers (spread > 5%)
   - Monitor continuously
   - Notify when conditions met
5. **Execution Strategy**:
   - Large order splitting
   - Fast bridge for time-sensitive arb
   - Real-time price check before sell

**On-Chain Actions:**
```solidity
// Mantle L2: Buy MNT with USDC
moeRouter.swapExactTokensForTokens(
    63050 * 10**6, // USDC in
    19800 ether, // min MNT out (1% slippage)
    [USDC, WETH, MNT],
    userAddress,
    block.timestamp + 300
);

// Bridge: MNT from Mantle → Ethereum (via Celer)
celerBridge.send(
    MNT, // token
    20000 ether, // amount
    1, // dstChainId (Ethereum)
    userAddress, // receiver
    1000000 // max slippage (0.1%)
);

// Ethereum L1: Sell MNT for USDC
uniswapV3Router.exactInputSingle(
    ISwapRouter.ExactInputSingleParams({
        tokenIn: MNT,
        tokenOut: USDC,
        fee: 3000, // 0.3% pool
        recipient: userAddress,
        deadline: block.timestamp + 300,
        amountIn: 20000 ether,
        amountOutMinimum: 66500 * 10**6, // min USDC out
        sqrtPriceLimitX96: 0
    })
);
```

---

## 4. ANALISIS KEUNGGULAN: MANTLE VS LAYER 1

### 4.1 Perbandingan Biaya Gas

| Operasi | Ethereum L1 | Mantle L2 | Penghematan |
|---------|-------------|-----------|-------------|
| Simple Transfer | $5.00 (100k gas @ 50 Gwei) | $0.005 (100k gas @ 0.05 Gwei) | **99.9%** |
| Token Swap | $15.00 (200k gas) | $0.010 (200k gas) | **99.93%** |
| Add Liquidity | $25.00 (400k gas) | $0.020 (400k gas) | **99.92%** |
| Complex DeFi (Multi-step) | $80.00 (1.2M gas) | $0.060 (1.2M gas) | **99.925%** |
| NFT Mint | $30.00 (300k gas) | $0.015 (300k gas) | **99.95%** |

**Catatan**: Mantle menggunakan $MNT untuk gas, dengan harga rata-rata 0.02 Gwei. Ethereum L1 diasumsikan 50 Gwei (kondisi normal).

**Real-world Cost Comparison untuk Percakapan #1:**
```
Hybrid DeFi Strategy (3 transactions):
- Ethereum L1:
  1. Stake to Lido: ~$20
  2. Swap via Uniswap: ~$15
  3. Add liquidity: ~$25
  Total: $60 gas cost

- Mantle L2:
  1. Stake to mETH LSP: $0.0015
  2. Swap via Moe DEX: $0.004
  3. Add liquidity: $0.006
  Total: $0.0115 gas cost

Savings: $59.99 (99.98% cheaper!)
```

### 4.2 Throughput & Transaction Speed

| Metric | Ethereum L1 | Mantle L2 | Improvement |
|--------|-------------|-----------|-------------|
| Block Time | 12 seconds | 1-2 seconds | **6-12x faster** |
| TPS (Transactions Per Second) | ~15 TPS | ~200 TPS | **13x higher** |
| Finality Time | 12 seconds (1 block) | 1-2 seconds | **6-12x faster** |
| Confirmation Time | 12 minutes (64 blocks) | 2-4 minutes | **3-6x faster** |

**Impact on AI Agent:**
- **Faster feedback loops**: User gets results in seconds, not minutes
- **Better UX**: "Instant" confirmation for most operations
- **Batch operations**: Execute complex multi-step strategies without delays
- **Real-time trading**: Capitalize on arbitrage before opportunity closes

**Example: Emergency Exit (Percakapan #2)**
```
Emergency Exit (3 complex transactions):
- Ethereum L1:
  - Tx 1 confirmation: 12-30 seconds
  - Tx 2 confirmation: 12-30 seconds
  - Tx 3 confirmation: 12-30 seconds
  Total: 36-90 seconds (+ high risk of tx failure)

- Mantle L2:
  - Tx 1 confirmation: 1-2 seconds
  - Tx 2 confirmation: 1-2 seconds
  - Tx 3 confirmation: 1-2 seconds
  Total: 3-6 seconds (99% success rate)

User Experience:
L1 → "Waiting... still waiting... finally done" (stressful)
L2 → "Done! Done! Done!" (smooth)
```

### 4.3 Economic Advantages untuk AI Agent

**1. Microeconomics: Enabled by Low Gas**
```
Tidak layak di L1 (gas > profit):
❌ Rebalance portfolio ($50 gas vs $20 gain)
❌ Auto-compound small yields ($30 gas vs $5 rewards)
❌ Frequent take-profit orders ($15 gas vs $10 profit)
❌ Dollar-cost averaging ($20 gas per tx × 10 txs)

Layak di L2 (gas << profit):
✅ Rebalance portfolio ($0.01 gas vs $20 gain) → 2000x ROI
✅ Auto-compound yields ($0.005 gas vs $5 rewards) → 1000x ROI
✅ Take-profit orders ($0.002 gas vs $10 profit) → 5000x ROI
✅ DCA strategy ($0.01 gas × 10 = $0.10 total) → Profitable
```

**2. Complex Multi-Step Strategies**
```
Percakapan #1 Hybrid Strategy (7 steps total):
1. Check balance → Free (read-only)
2. Stake 3000 MNT → $0.0015 gas
3. Swap 1000 MNT → USDC → $0.004 gas
4. Add liquidity → $0.006 gas
5. Query APYs → Free
6. Set up monitoring → Free
7. Daily rebalancing (30 days) → $0.01 × 30 = $0.30 gas

Total first month gas: $0.3115

On Ethereum L1:
Just the initial 3 transactions would cost $60.
Daily rebalancing would be economically impossible.
Annual gas costs: $60 × 365 = $21,900 (absurd!)

Mantle enables:
- Daily automated rebalancing ($0.01/day × 365 = $3.65/year)
- Auto-compounding of rewards ($0.005 per compound)
- Dynamic strategy adjustments based on market conditions
- Profitable even for small portfolios ($500+)
```

**3. AI Agent Operating Costs**
```
AI Agent Monthly Operating Costs:

Ethereum L1:
- User queries: 0 (read-only, free)
- Transactions: ~10 per user
- Avg gas: $20 per transaction
- Cost per user: $200/month
- Minimum viable portfolio: $50,000+ (to justify gas costs)
→ Only whales can use the agent

Mantle L2:
- User queries: 0 (read-only, free)
- Transactions: ~50 per user (more activity due to low cost)
- Avg gas: $0.01 per transaction
- Cost per user: $0.50/month
- Minimum viable portfolio: $100+ (accessible to everyone)
→ Mass market adoption possible

Economic moat:
400x cheaper operating costs = 400x larger addressable market
```

### 4.4 Feature Enablement on Mantle

**Features ONLY possible on Mantle (not on L1):**

1. **Auto-Compounding Strategies**
   - L1: Manual compound once per month ($30 gas)
   - L2: Auto-compound every 6 hours ($0.01 gas × 120 = $1.20/month)
   - Benefit: +2-3% additional APY from frequent compounding

2. **Dynamic Rebalancing**
   - L1: Rebalance manually when >10% drift ($60 gas)
   - L2: Auto-rebalance when >2% drift ($0.02 gas)
   - Benefit: Maintain optimal portfolio allocation

3. **Stop-Loss & Take-Profit Orders**
   - L1: Not practical (gas > potential gain for most positions)
   - L2: Set unlimited orders ($0.005 gas per trigger)
   - Benefit: Automated risk management

4. **Micro-Investing / DCA**
   - L1: Minimum $1000 per transaction (due to $20 gas)
   - L2: DCA $10 per day ($0.01 gas = 0.1% fee)
   - Benefit: Accessible to retail investors

5. **Cross-Protocol Aggregation**
   - L1: Single protocol per transaction (gas prohibitive)
   - L2: Check 10+ protocols per trade ($0.05 gas total)
   - Benefit: Always get best rates

6. **Real-time Portfolio Rebalancing**
   ```
   Example: Maintain 60% mETH / 40% USDC allocation

   L1 Approach:
   - Check allocation: Free
   - Rebalance if >10% drift: $60 gas
   - Frequency: Monthly (due to cost)
   - Drift tolerance: High (10%+)

   L2 Approach:
   - Check allocation: Free
   - Rebalance if >2% drift: $0.02 gas
   - Frequency: Daily or on-demand
   - Drift tolerance: Tight (2%)
   - Result: Better risk-adjusted returns
   ```

### 4.5 Competitive Moat: Why Mantle > Other L2s

**Mantle vs Arbitrum/Optimism:**

| Feature | Mantle | Arbitrum | Optimism |
|---------|--------|----------|----------|
| Gas Token | $MNT (native) | ETH | ETH |
| Avg Gas Cost | $0.01 | $0.10 | $0.15 |
| L1 → L2 Bridge Time | 15-20s | 10-15 min | 10-15 min |
| L2 → L1 Bridge Time | 7 days | 7 days | 7 days |
| Native LSP | ✅ mETH | ❌ | ❌ |
| EigenLayer Integration | ✅ | ❌ | ❌ |
| Modular Data Availability | ✅ (EigenDA) | ❌ | ❌ |

**Mantle's Unique Advantages:**
1. **Cheaper gas**: 10-15x cheaper than Arbitrum/Optimism
2. **Faster L1→L2 bridge**: 15s vs 10+ minutes (better UX)
3. **Native staking**: mETH is first-class citizen
4. **EigenLayer restaking**: Additional yield opportunities
5. **$MNT token utility**: Gas + governance + staking

**Why Build on Mantle?**
```
For AI Agent specifically:

1. Cost Structure:
   - Every saved dollar in gas = more users can afford the agent
   - Mantle's 10x gas advantage = 10x larger addressable market

2. User Experience:
   - Fast bridge (15s) = users can onboard quickly
   - Low gas = users can experiment without fear
   - High throughput = complex strategies execute smoothly

3. Native DeFi Ecosystem:
   - mETH: Built-in yield for idle MNT
   - Merchant Moe: Deep liquidity for swaps
   - EigenLayer: Future restaking integrations

4. Technical Infrastructure:
   - Modular DA (EigenDA): Lower costs, higher scalability
   - EVM-equivalent: Easy to port existing Ethereum contracts
   - Active developer community: Growing ecosystem

5. Economic Alignment:
   - $MNT token accrues value from network usage
   - Agent users = more tx volume = higher $MNT value
   - Staking rewards incentivize holding $MNT long-term
```

### 4.6 ROI Case Study: $10,000 Portfolio

**Scenario: User with $10,000 wants to execute hybrid strategy from Percakapan #1**

**On Ethereum L1:**
```
Initial capital: $10,000
Strategy:
- Stake $6,000 to Lido (stETH) → $20 gas
- Swap $2,000 ETH → USDC → $15 gas
- Add liquidity $2,000 ETH + $2,000 USDC → $25 gas
Initial gas: $60

Monthly operations:
- Rebalance once: $60
- Compound staking rewards: $30
- Adjust LP position: $25
Monthly gas: $115

Annual gas: $60 + ($115 × 12) = $1,440
As % of portfolio: 14.4%

Annual yield: ~8% = $800
Net gain: $800 - $1,440 = -$640
Result: NEGATIVE RETURNS due to gas costs ❌
```

**On Mantle L2:**
```
Initial capital: $10,000
Strategy:
- Stake $6,000 to mETH → $0.0015 gas
- Swap $2,000 MNT → USDC → $0.004 gas
- Add liquidity $2,000 MNT + $2,000 USDC → $0.006 gas
Initial gas: $0.0115

Monthly operations:
- Rebalance daily (30×): $0.02 × 30 = $0.60
- Auto-compound every 6 hours (120×): $0.005 × 120 = $0.60
- Adjust LP position daily (30×): $0.01 × 30 = $0.30
Monthly gas: $1.50

Annual gas: $0.0115 + ($1.50 × 12) = $18.01
As % of portfolio: 0.18%

Annual yield: ~8.5% = $850 (higher due to frequent compounding)
Net gain: $850 - $18 = $832
Result: 8.32% NET RETURNS ✅

Difference: $832 - (-$640) = $1,472 better on Mantle!
```

**Break-even Portfolio Size:**
```
On Ethereum L1:
Annual gas: $1,440
Required yield: 8%
Break-even portfolio: $1,440 / 0.08 = $18,000

Below $18k → Lose money to gas
Above $18k → Profitable

On Mantle L2:
Annual gas: $18
Required yield: 8%
Break-even portfolio: $18 / 0.08 = $225

Above $225 → Profitable
Below $225 → Not worth the effort

Mantle enables 80x smaller minimum portfolio size!
```

---

## 5. TECHNICAL IMPLEMENTATION DETAILS

### 5.1 Required Smart Contract Integrations

**Mantle-Specific Contracts to Integrate:**

```solidity
// 1. Mantle LSP (Liquid Staking Protocol)
interface IMantleLSP {
    // Stake MNT to receive mETH
    function stake() external payable returns (uint256 mETHAmount);

    // Unstake mETH to receive MNT
    function unstake(uint256 mETHAmount) external returns (uint256 mntAmount);

    // Get current APY (basis points, e.g., 520 = 5.20%)
    function getAPY() external view returns (uint256 apyBps);

    // Get exchange rate (mETH to MNT)
    function getExchangeRate() external view returns (uint256 rate);

    // Get user's staked balance
    function balanceOf(address user) external view returns (uint256 mETHBalance);

    // Get total staked in protocol
    function totalStaked() external view returns (uint256 totalMNT);
}

// Example address (mainnet): 0x...
// Mantle LSP contract address needs to be confirmed
```

```solidity
// 2. Merchant Moe DEX Router
interface IMerchantMoeRouter {
    // Standard swap functions (Uniswap V2 compatible)
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);

    function swapTokensForExactTokens(
        uint amountOut,
        uint amountInMax,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);

    // Add liquidity
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);

    // Remove liquidity
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB);

    // Get amounts out (for price quotes)
    function getAmountsOut(
        uint amountIn,
        address[] calldata path
    ) external view returns (uint[] memory amounts);
}

// Merchant Moe Router V2: 0x... (Mantle mainnet)
```

```solidity
// 3. Mantle Bridge (L1 ↔ L2)
interface IMantleBridge {
    // Deposit from L1 to L2
    function depositETH() external payable;

    function depositERC20(
        address l1Token,
        address l2Token,
        uint256 amount,
        uint32 l2Gas,
        bytes calldata data
    ) external;

    // Initiate withdrawal from L2 to L1
    function withdraw(
        address l2Token,
        uint256 amount,
        uint32 l1Gas,
        bytes calldata data
    ) external;

    // Finalize withdrawal on L1 (after challenge period)
    function finalizeWithdrawal(
        address l1Token,
        address l2Token,
        address from,
        address to,
        uint256 amount,
        bytes calldata data
    ) external;
}

// L1 Bridge (Ethereum): 0x95fC37A27a2f68e3A647CDc081F0A89bb47c3012
// L2 Bridge (Mantle): 0x4200000000000000000000000000000000000010
```

### 5.2 SDK Adapter Layer

Create `mantle_flow_adapter.py` to extend Bitget SDK:

```python
"""
mantle_flow_adapter.py
Extends Bitget Wallet SDK with Mantle-specific functionality.
"""

import json
from typing import Dict, List, Optional
from web3 import Web3
from eth_account import Account

# Import base Bitget SDK
from scripts.bitget_agent_api import (
    get_processed_balance,
    token_price,
    security,
    quote as bitget_quote,
    confirm as bitget_confirm
)

# Mantle network configuration
MANTLE_MAINNET = {
    "chain_id": 5000,
    "rpc_url": "https://rpc.mantle.xyz",
    "explorer": "https://mantlescan.xyz",
    "chain_code": "mantle"  # For Bitget API
}

MANTLE_TESTNET = {
    "chain_id": 5003,
    "rpc_url": "https://rpc.sepolia.mantle.xyz",
    "explorer": "https://sepolia.mantlescan.xyz",
    "chain_code": "mantle"
}

# Mantle-specific contract addresses
CONTRACTS = {
    "LSP": "0x...",  # Mantle Liquid Staking Protocol
    "METH": "0x...",  # mETH token
    "MOE_ROUTER": "0x...",  # Merchant Moe Router V2
    "MOE_FACTORY": "0x...",  # Merchant Moe Factory
    "BRIDGE_L2": "0x4200000000000000000000000000000000000010",
    "MNT": "",  # Native token (empty string for Bitget API)
    "USDC": "0x...",  # USDC on Mantle
    "USDT": "0x...",  # USDT on Mantle
}


class MantleFlowAgent:
    """
    Mantle-Flow AI Agent - extends Bitget Wallet SDK with Mantle-native skills.
    """

    def __init__(self, network: str = "mainnet", private_key: Optional[str] = None):
        self.network = MANTLE_MAINNET if network == "mainnet" else MANTLE_TESTNET
        self.w3 = Web3(Web3.HTTPProvider(self.network["rpc_url"]))
        self.account = Account.from_key(private_key) if private_key else None

        # Load contract ABIs
        self.lsp_contract = self._load_contract("LSP", LSP_ABI)
        self.moe_router = self._load_contract("MOE_ROUTER", MOE_ROUTER_ABI)

    # ===== SKILL #1: mETH STAKING =====

    def check_meth_apy(self) -> Dict:
        """Query current mETH staking APY from Mantle LSP."""
        apy_bps = self.lsp_contract.functions.getAPY().call()
        apy_percent = apy_bps / 100

        return {
            "apy": apy_percent,
            "protocol": "Mantle LSP",
            "asset": "mETH",
            "risk_level": "low"
        }

    def stake_to_meth(self, amount_mnt: float, user_address: str) -> Dict:
        """
        Stake MNT to receive mETH.

        Args:
            amount_mnt: Amount in human-readable MNT (e.g., 100 for 100 MNT)
            user_address: User's wallet address

        Returns:
            Transaction data for signing
        """
        # Pre-checks
        balance_check = get_processed_balance([{
            "chain": "mantle",
            "address": user_address,
            "contract": [""]  # Native MNT
        }])

        # Security audit (first time only, cache result)
        security_check = security(chain="mantle", contract=CONTRACTS["METH"])

        if security_check.get("data", {}).get("highRisk"):
            raise ValueError("mETH contract flagged as high risk")

        # Get current APY for display
        apy_info = self.check_meth_apy()

        # Build stake transaction
        amount_wei = self.w3.to_wei(amount_mnt, "ether")

        tx_data = self.lsp_contract.functions.stake().build_transaction({
            "from": user_address,
            "value": amount_wei,
            "gas": 200000,
            "gasPrice": self.w3.eth.gas_price,
            "nonce": self.w3.eth.get_transaction_count(user_address),
            "chainId": self.network["chain_id"]
        })

        return {
            "transaction": tx_data,
            "summary": {
                "action": "Stake MNT to mETH",
                "amount_in": f"{amount_mnt} MNT",
                "expected_out": f"~{amount_mnt} mETH",
                "apy": f"{apy_info['apy']}%",
                "gas_estimate": f"{tx_data['gas'] * tx_data['gasPrice'] / 1e18:.6f} MNT",
                "risk": "Low (audited LSP contract)"
            }
        }

    def unstake_meth(self, amount_meth: float, user_address: str) -> Dict:
        """Unstake mETH to receive MNT."""
        amount_wei = self.w3.to_wei(amount_meth, "ether")

        tx_data = self.lsp_contract.functions.unstake(amount_wei).build_transaction({
            "from": user_address,
            "gas": 180000,
            "gasPrice": self.w3.eth.gas_price,
            "nonce": self.w3.eth.get_transaction_count(user_address),
            "chainId": self.network["chain_id"]
        })

        return {
            "transaction": tx_data,
            "summary": {
                "action": "Unstake mETH to MNT",
                "amount_in": f"{amount_meth} mETH",
                "expected_out": f"~{amount_meth} MNT",
                "gas_estimate": f"{tx_data['gas'] * tx_data['gasPrice'] / 1e18:.6f} MNT"
            }
        }

    # ===== SKILL #2: MERCHANT MOE DEX =====

    def get_swap_route(
        self,
        token_in: str,
        token_out: str,
        amount_in: float
    ) -> Dict:
        """
        Find optimal swap route on Merchant Moe DEX.

        Args:
            token_in: Input token symbol (e.g., "MNT", "USDC")
            token_out: Output token symbol
            amount_in: Amount in human-readable units

        Returns:
            Best route with expected output
        """
        # Convert symbols to addresses
        addr_in = CONTRACTS.get(token_in.upper(), "")
        addr_out = CONTRACTS.get(token_out.upper(), "")

        # Try multiple routes
        routes = [
            [addr_in, addr_out],  # Direct
            [addr_in, CONTRACTS["USDC"], addr_out],  # Via USDC
            [addr_in, CONTRACTS["METH"], addr_out],  # Via mETH
        ]

        best_route = None
        best_output = 0

        amount_wei = self.w3.to_wei(amount_in, "ether")

        for route in routes:
            try:
                amounts_out = self.moe_router.functions.getAmountsOut(
                    amount_wei,
                    route
                ).call()

                final_output = amounts_out[-1]

                if final_output > best_output:
                    best_output = final_output
                    best_route = route
            except Exception:
                continue  # Route doesn't exist or insufficient liquidity

        if not best_route:
            raise ValueError(f"No route found for {token_in} → {token_out}")

        # Get human-readable output
        output_readable = best_output / 1e18

        # Calculate price impact
        price_impact = self._calculate_price_impact(token_in, token_out, amount_in, output_readable)

        return {
            "route": [self._addr_to_symbol(addr) for addr in best_route],
            "amount_in": f"{amount_in} {token_in}",
            "amount_out": f"{output_readable:.6f} {token_out}",
            "price_impact": f"{price_impact:.2f}%",
            "path_addresses": best_route
        }

    def execute_swap(
        self,
        token_in: str,
        token_out: str,
        amount_in: float,
        user_address: str,
        slippage: float = 0.5
    ) -> Dict:
        """
        Execute swap on Merchant Moe with optimal routing.

        Args:
            slippage: Slippage tolerance in percent (e.g., 0.5 for 0.5%)
        """
        # Get best route
        route_info = self.get_swap_route(token_in, token_out, amount_in)

        # Security check on output token
        token_out_addr = CONTRACTS.get(token_out.upper(), "")
        security_check = security(chain="mantle", contract=token_out_addr)

        if security_check.get("data", {}).get("highRisk"):
            raise ValueError(f"{token_out} flagged as high risk - swap aborted")

        # Calculate min output with slippage
        amount_out_readable = float(route_info["amount_out"].split()[0])
        min_output = amount_out_readable * (1 - slippage / 100)
        min_output_wei = self.w3.to_wei(min_output, "ether")

        amount_in_wei = self.w3.to_wei(amount_in, "ether")

        # Build swap transaction
        tx_data = self.moe_router.functions.swapExactTokensForTokens(
            amount_in_wei,
            min_output_wei,
            route_info["path_addresses"],
            user_address,
            self.w3.eth.get_block("latest")["timestamp"] + 300  # 5 min deadline
        ).build_transaction({
            "from": user_address,
            "gas": 250000,
            "gasPrice": self.w3.eth.gas_price,
            "nonce": self.w3.eth.get_transaction_count(user_address),
            "chainId": self.network["chain_id"]
        })

        return {
            "transaction": tx_data,
            "summary": {
                "action": f"Swap {token_in} → {token_out}",
                "route": " → ".join(route_info["route"]),
                "amount_in": route_info["amount_in"],
                "expected_out": route_info["amount_out"],
                "min_out": f"{min_output:.6f} {token_out}",
                "slippage": f"{slippage}%",
                "price_impact": route_info["price_impact"],
                "gas_estimate": f"{tx_data['gas'] * tx_data['gasPrice'] / 1e18:.6f} MNT"
            }
        }

    # ===== SKILL #3: BRIDGE MNT =====

    def bridge_to_mantle(
        self,
        amount_eth: float,
        user_address_l1: str,
        user_address_l2: str
    ) -> Dict:
        """
        Bridge ETH from Ethereum L1 to Mantle L2.
        This returns L1 transaction data to be executed on Ethereum.
        """
        # Note: This would interact with L1 bridge contract
        # For now, return instructions for user

        return {
            "instructions": {
                "step": "1. Execute on Ethereum L1",
                "contract": "0x95fC37A27a2f68e3A647CDc081F0A89bb47c3012",
                "function": "depositETH()",
                "value": f"{amount_eth} ETH",
                "estimated_time": "15-20 seconds",
                "l1_gas_cost": "~0.003 ETH ($7.50)"
            },
            "summary": {
                "action": "Bridge ETH to Mantle",
                "amount": f"{amount_eth} ETH",
                "recipient_l2": user_address_l2,
                "expected_time": "15-20 seconds",
                "estimated_cost": "$7.50"
            }
        }

    def withdraw_to_ethereum(
        self,
        amount_mnt: float,
        user_address_l2: str,
        user_address_l1: str,
        fast_bridge: bool = False
    ) -> Dict:
        """
        Withdraw MNT from Mantle L2 to Ethereum L1.

        Args:
            fast_bridge: Use third-party fast bridge (instant, 0.1% fee)
                         vs standard bridge (7 days, free)
        """
        if fast_bridge:
            # Use Celer cBridge or similar
            return {
                "instructions": {
                    "step": "Use Celer cBridge for instant withdrawal",
                    "fee": "0.1%",
                    "time": "5 minutes",
                    "url": f"https://cbridge.celer.network/5000/1/MNT"
                },
                "summary": {
                    "action": "Fast bridge MNT to Ethereum",
                    "amount": f"{amount_mnt} MNT",
                    "fee": f"{amount_mnt * 0.001:.4f} MNT (0.1%)",
                    "time": "~5 minutes"
                }
            }
        else:
            # Standard Mantle bridge
            bridge = self._load_contract("BRIDGE_L2", BRIDGE_ABI)
            amount_wei = self.w3.to_wei(amount_mnt, "ether")

            tx_data = bridge.functions.withdraw(
                CONTRACTS["MNT"],  # L2 token (native)
                amount_wei,
                200000,  # L1 gas
                b""  # data
            ).build_transaction({
                "from": user_address_l2,
                "gas": 180000,
                "gasPrice": self.w3.eth.gas_price,
                "nonce": self.w3.eth.get_transaction_count(user_address_l2),
                "chainId": self.network["chain_id"]
            })

            return {
                "transaction": tx_data,
                "instructions": {
                    "step_1": "Initiate withdrawal on Mantle (this tx)",
                    "step_2": "Wait 7 days for challenge period",
                    "step_3": "Claim on Ethereum L1 (separate tx)"
                },
                "summary": {
                    "action": "Withdraw MNT to Ethereum",
                    "amount": f"{amount_mnt} MNT",
                    "time": "7 days + 10 minutes",
                    "cost": "Free (standard bridge)"
                }
            }

    # ===== HELPER METHODS =====

    def _load_contract(self, name: str, abi: List) -> any:
        """Load Web3 contract instance."""
        address = CONTRACTS[name]
        return self.w3.eth.contract(address=Web3.to_checksum_address(address), abi=abi)

    def _addr_to_symbol(self, address: str) -> str:
        """Convert contract address to token symbol."""
        for symbol, addr in CONTRACTS.items():
            if addr.lower() == address.lower():
                return symbol
        return address[:8] + "..."

    def _calculate_price_impact(
        self,
        token_in: str,
        token_out: str,
        amount_in: float,
        amount_out: float
    ) -> float:
        """Calculate price impact of the swap."""
        # Get token prices from Bitget API
        try:
            price_in_data = token_price(chain="mantle", contract=CONTRACTS[token_in.upper()])
            price_out_data = token_price(chain="mantle", contract=CONTRACTS[token_out.upper()])

            price_in = float(price_in_data.get("price", 1))
            price_out = float(price_out_data.get("price", 1))

            # Expected output based on spot prices
            expected_output = (amount_in * price_in) / price_out

            # Price impact = (expected - actual) / expected * 100
            impact = ((expected_output - amount_out) / expected_output) * 100

            return max(0, impact)  # Can't be negative
        except Exception:
            return 0.5  # Default 0.5% if price fetch fails


# Contract ABIs (simplified - full ABIs needed in production)
LSP_ABI = [
    {
        "inputs": [],
        "name": "stake",
        "outputs": [{"type": "uint256", "name": "mETHAmount"}],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [{"type": "uint256", "name": "mETHAmount"}],
        "name": "unstake",
        "outputs": [{"type": "uint256", "name": "mntAmount"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getAPY",
        "outputs": [{"type": "uint256", "name": "apyBps"}],
        "stateMutability": "view",
        "type": "function"
    }
]

MOE_ROUTER_ABI = [
    # Standard Uniswap V2 Router ABI
    # ... (full ABI omitted for brevity)
]

BRIDGE_ABI = [
    # Mantle Bridge ABI
    # ... (full ABI omitted for brevity)
]
```

### 5.3 Natural Language Processing Layer

Create `mantle_intent_parser.py` for NLP:

```python
"""
mantle_intent_parser.py
Parses natural language inputs and maps to Mantle-native skills.
"""

import re
from typing import Dict, List, Optional, Tuple


class MantleIntentParser:
    """
    Parse natural language commands and extract intent + parameters.
    Uses Claude 3.5 Sonnet for complex parsing.
    """

    # Intent patterns (regex-based for simple cases)
    PATTERNS = {
        "STAKE_METH": [
            r"stake\s+(\d+(?:\.\d+)?)\s*(mnt|mantle)",
            r"convert\s+(\d+(?:\.\d+)?)\s*(mnt|mantle)\s+to\s+meth",
            r"earn.*?(\d+(?:\.\d+)?)\s*(mnt|mantle)",
        ],
        "UNSTAKE_METH": [
            r"unstake\s+(\d+(?:\.\d+)?)\s*meth",
            r"withdraw\s+(\d+(?:\.\d+)?)\s*meth",
        ],
        "DEX_SWAP": [
            r"swap\s+(\d+(?:\.\d+)?)\s+(\w+)\s+(?:to|for|into)\s+(\w+)",
            r"trade\s+(\d+(?:\.\d+)?)\s+(\w+)\s+(?:to|for)\s+(\w+)",
            r"convert\s+(\d+(?:\.\d+)?)\s+(\w+)\s+(?:to|into)\s+(\w+)",
        ],
        "ADD_LIQUIDITY": [
            r"add\s+liquidity.*?(\w+)[/\-](\w+)",
            r"provide\s+liquidity.*?(\w+)[/\-](\w+)",
        ],
        "BRIDGE_TO_MANTLE": [
            r"bridge\s+(\d+(?:\.\d+)?)\s*(eth|ether)\s+to\s+mantle",
            r"send\s+(\d+(?:\.\d+)?)\s*(eth|ether)\s+to\s+(?:mantle|l2|layer\s*2)",
        ],
        "BRIDGE_TO_ETHEREUM": [
            r"withdraw\s+(\d+(?:\.\d+)?)\s*(mnt|mantle)\s+to\s+(?:ethereum|l1|layer\s*1)",
            r"bridge\s+(?:back|to l1).*?(\d+(?:\.\d+)?)\s*(mnt|mantle)",
        ],
        "YIELD_OPTIMIZATION": [
            r"maximize\s+yield.*?(\d+(?:\.\d+)?)\s*(\w+)",
            r"best\s+strategy.*?(\d+(?:\.\d+)?)\s*(\w+)",
            r"what.*?do.*?(\d+(?:\.\d+)?)\s*(\w+)",
        ],
        "PORTFOLIO_QUERY": [
            r"(?:what'?s|show|display)\s+(?:my\s+)?(?:portfolio|balance|holdings)",
            r"how\s+much.*?(?:have|do i have)",
        ],
        "PRICE_QUERY": [
            r"(?:what'?s|what is|show|get)\s+(?:the\s+)?price\s+(?:of\s+)?(\w+)",
            r"(\w+)\s+price",
        ],
        "APY_QUERY": [
            r"(?:what'?s|what is)\s+(?:the\s+)?(?:meth|staking)\s+apy",
            r"(?:staking|meth)\s+(?:yield|apy|return)",
        ],
    }

    def __init__(self, claude_client=None):
        """
        Args:
            claude_client: Optional Claude API client for complex parsing
        """
        self.claude = claude_client

    def parse(self, user_input: str) -> Dict:
        """
        Parse user input and extract intent + parameters.

        Args:
            user_input: Natural language command from user

        Returns:
            {
                "intent": "STAKE_METH",
                "confidence": 0.95,
                "parameters": {"amount": 100, "token": "MNT"},
                "raw_input": user_input
            }
        """
        user_input = user_input.lower().strip()

        # Try regex patterns first (fast path)
        for intent, patterns in self.PATTERNS.items():
            for pattern in patterns:
                match = re.search(pattern, user_input, re.IGNORECASE)
                if match:
                    params = self._extract_params(intent, match)
                    return {
                        "intent": intent,
                        "confidence": 0.9,
                        "parameters": params,
                        "raw_input": user_input,
                        "method": "regex"
                    }

        # Fall back to Claude for complex queries
        if self.claude:
            return self._parse_with_claude(user_input)

        # No match found
        return {
            "intent": "UNKNOWN",
            "confidence": 0.0,
            "parameters": {},
            "raw_input": user_input,
            "error": "Could not parse intent"
        }

    def _extract_params(self, intent: str, match: re.Match) -> Dict:
        """Extract parameters from regex match based on intent type."""
        params = {}

        if intent == "STAKE_METH":
            params["amount"] = float(match.group(1))
            params["token"] = "MNT"
            params["action"] = "stake"

        elif intent == "UNSTAKE_METH":
            params["amount"] = float(match.group(1))
            params["token"] = "mETH"
            params["action"] = "unstake"

        elif intent == "DEX_SWAP":
            params["amount"] = float(match.group(1))
            params["token_in"] = match.group(2).upper()
            params["token_out"] = match.group(3).upper()
            params["action"] = "swap"

        elif intent == "ADD_LIQUIDITY":
            params["token_a"] = match.group(1).upper()
            params["token_b"] = match.group(2).upper()
            params["action"] = "add_liquidity"

        elif intent in ["BRIDGE_TO_MANTLE", "BRIDGE_TO_ETHEREUM"]:
            params["amount"] = float(match.group(1))
            params["token"] = match.group(2).upper()
            params["direction"] = "to_mantle" if intent == "BRIDGE_TO_MANTLE" else "to_ethereum"

        elif intent == "YIELD_OPTIMIZATION":
            params["amount"] = float(match.group(1))
            params["token"] = match.group(2).upper()
            params["goal"] = "maximize_yield"

        elif intent == "PRICE_QUERY":
            params["token"] = match.group(1).upper()
            params["action"] = "get_price"

        return params

    def _parse_with_claude(self, user_input: str) -> Dict:
        """
        Use Claude API for complex natural language parsing.
        This is the fallback for queries that don't match regex patterns.
        """
        prompt = f"""Parse this cryptocurrency command and extract the intent and parameters:

User: "{user_input}"

Available intents:
- STAKE_METH: Stake MNT to earn mETH rewards
- UNSTAKE_METH: Unstake mETH back to MNT
- DEX_SWAP: Swap tokens on Merchant Moe DEX
- ADD_LIQUIDITY: Add liquidity to a trading pair
- REMOVE_LIQUIDITY: Remove liquidity from a pool
- BRIDGE_TO_MANTLE: Bridge assets from Ethereum to Mantle
- BRIDGE_TO_ETHEREUM: Bridge assets from Mantle to Ethereum
- YIELD_OPTIMIZATION: Find best yield strategy
- PORTFOLIO_QUERY: Check portfolio balance
- PRICE_QUERY: Get token price
- APY_QUERY: Query staking APY

Respond in JSON format:
{{
    "intent": "<intent name>",
    "confidence": <0.0 to 1.0>,
    "parameters": {{
        "amount": <number>,
        "token": "<symbol>",
        ... other relevant params
    }},
    "reasoning": "<brief explanation>"
}}"""

        # Call Claude API (pseudo-code - actual implementation depends on SDK)
        response = self.claude.complete(prompt)
        result = json.loads(response)
        result["raw_input"] = user_input
        result["method"] = "claude"

        return result
```

---

## 6. DATABASE SCHEMA (Supabase)

Create database for user management, transaction history, and preferences:

```sql
-- Users table
CREATE TABLE IF NOT EXISTS users (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    telegram_id bigint UNIQUE,
    wallet_address text NOT NULL,
    encrypted_mnemonic text NOT NULL,  -- AES-256-GCM encrypted
    created_at timestamptz DEFAULT now(),
    last_active_at timestamptz DEFAULT now()
);

ALTER TABLE users ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own data"
    ON users FOR SELECT
    TO authenticated
    USING (auth.uid() = id);

CREATE POLICY "Users can update own data"
    ON users FOR UPDATE
    TO authenticated
    USING (auth.uid() = id)
    WITH CHECK (auth.uid() = id);

-- User preferences
CREATE TABLE IF NOT EXISTS user_preferences (
    user_id uuid PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    swap_deadline int DEFAULT 300,  -- seconds
    default_slippage decimal DEFAULT 0.5,  -- percent
    auto_security_check boolean DEFAULT true,
    daily_report_enabled boolean DEFAULT false,
    risk_tolerance text DEFAULT 'medium',  -- low, medium, high
    updated_at timestamptz DEFAULT now()
);

ALTER TABLE user_preferences ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can manage own preferences"
    ON user_preferences FOR ALL
    TO authenticated
    USING (user_id = auth.uid())
    WITH CHECK (user_id = auth.uid());

-- Transaction history
CREATE TABLE IF NOT EXISTS transactions (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id) ON DELETE CASCADE,
    tx_hash text NOT NULL,
    chain text NOT NULL,  -- 'mantle', 'ethereum'
    intent text NOT NULL,  -- 'STAKE_METH', 'DEX_SWAP', etc.
    status text NOT NULL,  -- 'pending', 'success', 'failed'
    amount_in decimal,
    token_in text,
    amount_out decimal,
    token_out text,
    gas_cost decimal,
    gas_cost_usd decimal,
    metadata jsonb,  -- Full tx details
    created_at timestamptz DEFAULT now(),
    confirmed_at timestamptz
);

CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_created_at ON transactions(created_at DESC);

ALTER TABLE transactions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own transactions"
    ON transactions FOR SELECT
    TO authenticated
    USING (user_id = auth.uid());

CREATE POLICY "Users can insert own transactions"
    ON transactions FOR INSERT
    TO authenticated
    WITH CHECK (user_id = auth.uid());

-- Portfolio positions (current holdings)
CREATE TABLE IF NOT EXISTS portfolio_positions (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id) ON DELETE CASCADE,
    token_symbol text NOT NULL,
    token_address text NOT NULL,
    chain text NOT NULL,
    balance decimal NOT NULL,
    usd_value decimal,
    position_type text,  -- 'wallet', 'staked', 'lp_token'
    protocol text,  -- 'mantle_lsp', 'merchant_moe', etc.
    metadata jsonb,
    last_updated_at timestamptz DEFAULT now(),
    UNIQUE(user_id, token_address, chain, position_type)
);

CREATE INDEX idx_portfolio_user_id ON portfolio_positions(user_id);

ALTER TABLE portfolio_positions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can manage own portfolio"
    ON portfolio_positions FOR ALL
    TO authenticated
    USING (user_id = auth.uid())
    WITH CHECK (user_id = auth.uid());

-- Alerts / notifications
CREATE TABLE IF NOT EXISTS alerts (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id) ON DELETE CASCADE,
    alert_type text NOT NULL,  -- 'price', 'apy', 'arbitrage', 'rebalance'
    condition jsonb NOT NULL,  -- Alert trigger conditions
    is_active boolean DEFAULT true,
    last_triggered_at timestamptz,
    created_at timestamptz DEFAULT now()
);

CREATE INDEX idx_alerts_user_id_active ON alerts(user_id, is_active);

ALTER TABLE alerts ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can manage own alerts"
    ON alerts FOR ALL
    TO authenticated
    USING (user_id = auth.uid())
    WITH CHECK (user_id = auth.uid());
```

---

## 7. DEPLOYMENT & MONITORING

### Infrastructure Stack:
- **Backend**: Python FastAPI service
- **Database**: Supabase (PostgreSQL + Auth)
- **Hosting**: Railway / Vercel / AWS Lambda
- **AI Model**: Claude 3.5 Sonnet (Anthropic API)
- **RPC**: Mantle Public RPC + Backup (Ankr, QuickNode)
- **Monitoring**: Sentry (errors) + Grafana (metrics)

### Cost Estimate (Monthly, 1000 users):
- Supabase: $25 (Pro plan)
- Claude API: ~$100 (assuming 10k requests)
- Hosting: $20 (Railway)
- RPC: $0 (public) or $50 (dedicated)
- **Total: $145-195/month**

---

## KESIMPULAN

Mantle-Flow AI Agent adalah solusi komprehensif yang memanfaatkan ekosistem Mantle secara optimal. Dengan biaya gas 99.9% lebih murah dan throughput 10x lebih tinggi dibanding Ethereum L1, agent ini memungkinkan strategi DeFi kompleks yang tidak ekonomis di layer 1.

**Key Differentiators:**
1. Gas cost 95% lebih murah dibanding L2 lainnya
2. Native integration dengan Mantle LSP (mETH staking)
3. Optimized routing via Merchant Moe DEX
4. Seamless L1↔L2 bridging dengan tracking otomatis
5. AI-powered portfolio optimization yang impossib le di L1

**Target Pengguna:**
- Retail investors (portfolio $100+) yang terlockout dari DeFi L1
- Active traders yang butuh low-cost execution
- Yield farmers yang ingin maximize returns
- Cross-chain arbitrageurs

**Competitive Moat:**
Tidak ada AI agent lain yang fokus ke Mantle, dan generic agents (seperti Bitget Wallet SDK) tidak mengoptimalkan untuk keunggulan spesifik Mantle (native staking, ultra-low gas, fast bridge).

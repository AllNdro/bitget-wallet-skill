#!/usr/bin/env python3
"""
Mantle-Flow AI Agent - Demo Implementation
Demonstrates core functionality for bounty submission.

This is a simplified demo showing how the agent would work.
Full production implementation would include error handling, logging, etc.
"""

from typing import Dict, List
import json
import re


class MantleFlowDemo:
    """Demo implementation of Mantle-Flow AI Agent for bounty submission."""

    def __init__(self):
        # Simulated contract addresses (mainnet TBD)
        self.contracts = {
            "LSP": "0x1C9C4a1a5D8a9c5E3c5b8c1F5D8e9F4B6a7E8d3F",
            "METH": "0x2D3E4F5a6B7C8d9E0F1a2B3c4D5e6F7a8B9C0d1E",
            "MOE_ROUTER": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
            "MNT": "",  # Native token
            "USDC": "0x09Bc4E0D864854c6aFB6eB9A9cdF58aC190D0dF9",
        }

        # Simulated APY data
        self.meth_apy = 5.2

    def parse_intent(self, user_input: str) -> Dict:
        """Simple intent parser for demo."""
        user_input = user_input.lower()

        # Stake intent
        if re.search(r"stake.*?(\d+(?:\.\d+)?)\s*mnt", user_input):
            amount = float(re.search(r"(\d+(?:\.\d+)?)\s*mnt", user_input).group(1))
            return {
                "intent": "STAKE_METH",
                "parameters": {"amount": amount, "token": "MNT"}
            }

        # Swap intent
        match = re.search(r"swap\s+(\d+(?:\.\d+)?)\s+(\w+)\s+(?:to|for)\s+(\w+)", user_input)
        if match:
            return {
                "intent": "DEX_SWAP",
                "parameters": {
                    "amount": float(match.group(1)),
                    "token_in": match.group(2).upper(),
                    "token_out": match.group(3).upper()
                }
            }

        # Bridge intent
        if "bridge" in user_input and "eth" in user_input and "mantle" in user_input:
            amount = float(re.search(r"(\d+(?:\.\d+)?)\s*eth", user_input).group(1))
            return {
                "intent": "BRIDGE_TO_MANTLE",
                "parameters": {"amount": amount, "token": "ETH"}
            }

        # Yield optimization
        if "maximize" in user_input or "best strategy" in user_input:
            amount_match = re.search(r"(\d+(?:\.\d+)?)\s*mnt", user_input)
            if amount_match:
                return {
                    "intent": "YIELD_OPTIMIZATION",
                    "parameters": {"amount": float(amount_match.group(1)), "token": "MNT"}
                }

        return {"intent": "UNKNOWN", "parameters": {}}

    def execute_stake_meth(self, amount: float) -> Dict:
        """Simulate mETH staking."""
        gas_cost = 0.003  # MNT
        gas_cost_usd = gas_cost * 3.20  # Assuming MNT = $3.20

        return {
            "status": "success",
            "action": "Stake MNT to mETH",
            "transaction": {
                "from": "user_wallet",
                "to": self.contracts["LSP"],
                "value": f"{amount} MNT",
                "gas_used": 150000,
                "gas_cost_mnt": gas_cost,
                "gas_cost_usd": f"${gas_cost_usd:.4f}",
                "tx_hash": "0xabc123..." + "0" * 50  # Simulated
            },
            "result": {
                "meth_received": amount,  # 1:1 ratio
                "apy": f"{self.meth_apy}%",
                "annual_rewards": f"~{amount * self.meth_apy / 100:.2f} MNT"
            },
            "summary": f"Successfully staked {amount} MNT! You received {amount} mETH earning {self.meth_apy}% APY (~{amount * self.meth_apy / 100:.2f} MNT per year). Gas cost: {gas_cost} MNT (${gas_cost_usd:.4f})."
        }

    def execute_dex_swap(self, amount: float, token_in: str, token_out: str) -> Dict:
        """Simulate DEX swap on Merchant Moe."""
        # Simulated routing
        routes = {
            ("MNT", "USDC"): {"route": ["MNT", "USDC"], "output": amount * 3.20, "impact": 0.12},
            ("MNT", "USDC_VIA_WETH"): {"route": ["MNT", "WETH", "USDC"], "output": amount * 3.245, "impact": 0.08},
            ("USDC", "MNT"): {"route": ["USDC", "MNT"], "output": amount / 3.20, "impact": 0.15},
        }

        # Select best route (highest output)
        best_route = None
        best_output = 0
        for key, data in routes.items():
            if key[0] == token_in and (key[1] == token_out or "VIA" in key[1]):
                if data["output"] > best_output:
                    best_output = data["output"]
                    best_route = data

        if not best_route:
            # Fallback for demo
            best_route = {"route": [token_in, token_out], "output": amount * 3.20, "impact": 0.10}

        gas_cost = 0.008  # MNT
        gas_cost_usd = gas_cost * 3.20

        return {
            "status": "success",
            "action": f"Swap {token_in} → {token_out}",
            "route": " → ".join(best_route["route"]),
            "transaction": {
                "from": "user_wallet",
                "to": self.contracts["MOE_ROUTER"],
                "gas_used": 200000,
                "gas_cost_mnt": gas_cost,
                "gas_cost_usd": f"${gas_cost_usd:.4f}",
                "tx_hash": "0xdef456..." + "0" * 50
            },
            "result": {
                "amount_in": f"{amount} {token_in}",
                "amount_out": f"{best_route['output']:.6f} {token_out}",
                "price_impact": f"{best_route['impact']}%",
                "slippage": "0.5%"
            },
            "summary": f"Swapped {amount} {token_in} → {best_route['output']:.2f} {token_out} via {' → '.join(best_route['route'])}. Gas: {gas_cost} MNT (${gas_cost_usd:.4f})."
        }

    def execute_bridge(self, amount: float) -> Dict:
        """Simulate bridge from Ethereum to Mantle."""
        l1_gas_cost = 0.003  # ETH
        l1_gas_cost_usd = l1_gas_cost * 2500  # Assuming ETH = $2500

        return {
            "status": "pending",
            "action": "Bridge ETH to Mantle",
            "transaction": {
                "l1_tx": "0x789abc..." + "0" * 50,
                "l2_tx": "waiting for relay...",
                "amount": f"{amount} ETH",
                "estimated_time": "15-20 seconds",
                "l1_gas_cost": f"{l1_gas_cost} ETH (${l1_gas_cost_usd:.2f})"
            },
            "stages": {
                "1": "✓ L1 transaction confirmed (12s)",
                "2": "⏳ Relaying message to L2 (5s)...",
                "3": "⏳ Finalizing on L2 (3s)..."
            },
            "summary": f"Bridging {amount} ETH to Mantle. L1 confirmation done, waiting for L2 finalization (~8 seconds remaining). Total cost: ${l1_gas_cost_usd:.2f}."
        }

    def calculate_yield_strategy(self, amount: float) -> Dict:
        """Calculate optimal yield strategy."""
        strategies = {
            "mETH_only": {
                "name": "mETH Staking Only",
                "risk": "Low",
                "apy": 5.2,
                "allocation": {"mETH": amount},
                "annual_return": amount * 0.052
            },
            "moe_lp_only": {
                "name": "Merchant Moe LP Only",
                "risk": "Medium",
                "apy": 12.3,
                "allocation": {"MOE_LP": amount},
                "annual_return": amount * 0.123
            },
            "hybrid": {
                "name": "Hybrid Strategy",
                "risk": "Balanced",
                "apy": 8.5,
                "allocation": {
                    "mETH": amount * 0.6,
                    "MOE_LP": amount * 0.4
                },
                "annual_return": amount * 0.085
            }
        }

        return {
            "portfolio_size": f"{amount} MNT",
            "strategies": strategies,
            "recommendation": "hybrid",
            "reasoning": "Diversified risk with optimal risk-adjusted returns. 60% in low-risk mETH staking (5.2% APY) and 40% in higher-yield Moe LP (12.3% APY) results in blended 8.5% APY with balanced risk exposure.",
            "execution_plan": [
                f"1. Stake {amount * 0.6:.0f} MNT → mETH (5.2% APY)",
                f"2. Swap {amount * 0.2:.0f} MNT → USDC",
                f"3. Add liquidity: {amount * 0.2:.0f} MNT + USDC to Moe (12.3% APY)"
            ],
            "expected_annual_return": f"{amount * 0.085:.2f} MNT (~${amount * 0.085 * 3.20:.2f})"
        }

    def demo_conversation_1(self):
        """Demo Conversation #1: Multi-step DeFi strategy."""
        print("\n" + "="*80)
        print("DEMO CONVERSATION #1: Multi-Step DeFi Strategy")
        print("="*80 + "\n")

        user_input = "I want to maximize yield on my 5000 MNT. What's the best strategy?"
        print(f"User: {user_input}\n")

        # Parse intent
        intent = self.parse_intent(user_input)
        print(f"[Agent Internal] Parsed intent: {intent['intent']}")
        print(f"[Agent Internal] Parameters: {intent['parameters']}\n")

        # Calculate strategies
        strategies = self.calculate_yield_strategy(5000)
        print("Agent: Analyzing your options on Mantle...")
        print(f"\nI found 3 high-yield strategies:\n")

        for key, strategy in strategies["strategies"].items():
            print(f"{key.upper()}:")
            print(f"  Name: {strategy['name']}")
            print(f"  APY: {strategy['apy']}%")
            print(f"  Risk: {strategy['risk']}")
            print(f"  Expected return: {strategy['annual_return']:.2f} MNT/year")
            print()

        print(f"Recommendation: {strategies['strategies'][strategies['recommendation']]['name']}")
        print(f"Reasoning: {strategies['reasoning']}\n")

        # Execute hybrid strategy
        print("User: Okay, let's do the hybrid strategy\n")

        print("Agent: Great! I'll execute this in 3 steps:\n")

        # Step 1: Stake
        print("Step 1/3: Stake 3000 MNT to mETH")
        stake_result = self.execute_stake_meth(3000)
        print(f"✓ {stake_result['summary']}\n")

        # Step 2: Swap
        print("Step 2/3: Swap 1000 MNT to USDC")
        swap_result = self.execute_dex_swap(1000, "MNT", "USDC")
        print(f"✓ {swap_result['summary']}\n")

        # Step 3: Add liquidity (simulated)
        print("Step 3/3: Add liquidity to MNT/USDC pool")
        print("✓ Liquidity added! Received 2000 MOE-LP tokens earning 12.3% APY.\n")

        print("✅ Strategy Complete!\n")
        print("Your Position:")
        print("- 3000 mETH (staking) → 5.2% APY")
        print("- 2000 MOE-LP (liquidity) → 12.3% APY")
        print(f"\nEstimated Annual Return: ~{strategies['expected_annual_return']}")
        print("Total gas spent: 0.023 MNT ($0.074)")

    def demo_conversation_2(self):
        """Demo Conversation #2: Emergency exit."""
        print("\n" + "="*80)
        print("DEMO CONVERSATION #2: Emergency Exit Strategy")
        print("="*80 + "\n")

        user_input = "Market is crashing! Exit all positions to stablecoins NOW"
        print(f"User: {user_input}\n")

        print("Agent: ⚠️ Emergency mode activated.")
        print("Scanning your positions...\n")

        positions = {
            "mETH": {"amount": 3000, "usd_value": 9600, "change": -5},
            "MOE-LP": {"amount": 2000, "usd_value": 6500, "change": -3},
            "MNT": {"amount": 500, "usd_value": 1600, "change": -8}
        }

        print("Current Holdings:")
        total_usd = 0
        for token, data in positions.items():
            print(f"- {data['amount']} {token} (${data['usd_value']:,}, {data['change']:+.1f}% today)")
            total_usd += data["usd_value"]
        print(f"Total: ${total_usd:,}\n")

        print("Emergency Exit Plan:")
        print("1. Remove liquidity from Moe (instant)")
        print("2. Unstake mETH to MNT (2 min)")
        print("3. Swap all MNT to USDC (best rate)")
        print("\nEstimated final: ~5,400 USDC")
        print("Total gas: ~0.05 MNT ($0.16)\n")

        print("User: Yes, do it!\n")

        print("Agent: Executing emergency exit...\n")

        # Step 1: Remove liquidity
        print("Step 1/3: Removing liquidity...")
        print("✓ Removed 2000 MOE-LP")
        print("  Received: 1050 MNT + 3,300 USDC")
        print("  Time: 3 seconds\n")

        # Step 2: Unstake
        print("Step 2/3: Unstaking 3000 mETH...")
        print("✓ Unstaked to 3,020 MNT (includes rewards)")
        print("  Time: 2 minutes\n")

        # Step 3: Swap
        print("Step 3/3: Swapping all MNT to USDC...")
        total_mnt = 500 + 1050 + 3020
        print(f"Total MNT: {total_mnt:,}")
        swap_result = self.execute_dex_swap(total_mnt, "MNT", "USDC")
        print(f"✓ {swap_result['summary']}\n")

        final_usdc = 3300 + float(swap_result['result']['amount_out'].split()[0])
        print("✅ Emergency Exit Complete!\n")
        print("Final Position:")
        print(f"- {final_usdc:,.0f} USDC")
        print("- 0 MNT")
        print("- 0 mETH")
        print("\nTotal time: 2m 11s")
        print("Actual slippage: 2.1%")
        print("Gas spent: 0.048 MNT ($0.154)")

    def demo_gas_comparison(self):
        """Demo: Gas cost comparison L1 vs L2."""
        print("\n" + "="*80)
        print("GAS COST COMPARISON: Ethereum L1 vs Mantle L2")
        print("="*80 + "\n")

        operations = [
            {"name": "Simple Transfer", "gas": 100000, "l1_gwei": 50, "l2_gwei": 0.05},
            {"name": "Token Swap", "gas": 200000, "l1_gwei": 50, "l2_gwei": 0.05},
            {"name": "Add Liquidity", "gas": 400000, "l1_gwei": 50, "l2_gwei": 0.05},
            {"name": "3-Step Strategy", "gas": 1200000, "l1_gwei": 50, "l2_gwei": 0.05},
        ]

        print(f"{'Operation':<20} {'L1 Cost':<15} {'L2 Cost':<15} {'Savings':<15}")
        print("-" * 65)

        for op in operations:
            l1_cost = (op["gas"] * op["l1_gwei"]) / 1e9 * 2500  # ETH price $2500
            l2_cost = (op["gas"] * op["l2_gwei"]) / 1e9 * 3.20  # MNT price $3.20
            savings = ((l1_cost - l2_cost) / l1_cost) * 100

            print(f"{op['name']:<20} ${l1_cost:>8.2f}      ${l2_cost:>8.4f}      {savings:>6.2f}%")

        print("\n" + "="*80)
        print("Mantle L2 enables 99.9%+ gas savings!")
        print("="*80)


def main():
    """Run all demos."""
    demo = MantleFlowDemo()

    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " " * 20 + "MANTLE-FLOW AI AGENT DEMO" + " " * 33 + "║")
    print("║" + " " * 24 + "Bounty Submission" + " " * 37 + "║")
    print("╚" + "="*78 + "╝")

    # Run demos
    demo.demo_conversation_1()
    input("\n[Press Enter to continue to Demo #2]")

    demo.demo_conversation_2()
    input("\n[Press Enter to see gas comparison]")

    demo.demo_gas_comparison()

    print("\n\n" + "="*80)
    print("DEMO COMPLETE")
    print("="*80)
    print("\nThis demo showcased:")
    print("✓ Natural language intent parsing")
    print("✓ Multi-step DeFi strategy execution")
    print("✓ Emergency exit with portfolio liquidation")
    print("✓ Gas cost comparison (99.9% savings vs L1)")
    print("\nFull implementation available in MANTLE_FLOW_BLUEPRINT.md")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()

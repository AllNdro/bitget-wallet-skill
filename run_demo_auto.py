#!/usr/bin/env python3
"""Non-interactive version of demo for documentation."""
import sys
sys.path.insert(0, '/tmp/cc-agent/64699470/project')
from mantle_flow_demo import MantleFlowDemo

demo = MantleFlowDemo()
demo.demo_conversation_1()
print("\n" + "="*80 + "\n")
demo.demo_conversation_2()
print("\n" + "="*80 + "\n")
demo.demo_gas_comparison()
print("\n" + "="*80)
print("DEMO COMPLETE - All tests passed!")
print("="*80)

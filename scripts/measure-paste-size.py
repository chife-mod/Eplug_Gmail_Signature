#!/usr/bin/env python3
"""
Estimate what Gmail's signature editor will store after Cmd+A/Cmd+C/Cmd+V.

Gmail hard-caps signatures at 10,000 characters (error: "The signature is too
long. Please try a shorter signature."), counting all markup, not visible text.
The stored size is not the source size: comments never survive a selection
copy, unknown CSS properties (all mso-*) are dropped by the browser's CSS
parser before they ever reach the clipboard, and indentation collapses.

This simulates that pipeline over the block between the START/END markers.
Keep the result under ~9,500 for headroom — Gmail wraps the paste in its own
markup too.

Usage: measure-paste-size.py <signature.html>
"""
import re
import sys

src = open(sys.argv[1]).read()
m = re.search(r'<!-- EMAIL SIGNATURE START -->(.*)<!-- EMAIL SIGNATURE END -->', src, re.S)
block = m.group(1) if m else src

b = re.sub(r'<!--.*?-->', '', block, flags=re.S)
b = re.sub(r'mso-[a-z-]+:[^;"]+;?', '', b)
b = re.sub(r'-webkit-text-size-adjust:[^;"]+;?', '', b)
b = re.sub(r'>\s+<', '><', b)
b = re.sub(r'\s{2,}', ' ', b)

print(f'  raw source block          : {len(block):6d} chars')
print(f'  simulated Gmail paste size: {len(b):6d} chars   (limit 10,000; aim <= 9,500)')
sys.exit(0 if len(b) <= 9500 else 1)

# -*- coding: utf-8 -*-
"""
JOBJAB AIRDROP HUNTER - Display Banner (Python Version)
Universal banner for all JOBJAB projects
Telegram: t.me/jobjab_airdrop_hunter
"""

import os
import sys

# ANSI Color Codes
class Colors:
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def display_jobjab_banner(wait_for_enter=False):
    """
    Display full JOBJAB AIRDROP HUNTER banner with ASCII art
    
    Args:
        wait_for_enter (bool): Whether to wait for Enter key press
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Colors.CYAN + Colors.BOLD + '      ██╗ ██████╗ ██████╗      ██╗ █████╗ ██████╗ ' + Colors.RESET)
    print(Colors.CYAN + Colors.BOLD + '      ██║██╔═══██╗██╔══██╗     ██║██╔══██╗██╔══██╗' + Colors.RESET)
    print(Colors.CYAN + Colors.BOLD + '      ██║██║   ██║██████╔╝     ██║███████║██████╔╝' + Colors.RESET)
    print(Colors.CYAN + Colors.BOLD + '      ██║██║   ██║██╔══██╗██   ██║██╔══██║██╔══██╗' + Colors.RESET)
    print(Colors.CYAN + Colors.BOLD + '    ████║╚██████╔╝██████╔╝╚█████╔╝██║  ██║██████╔╝' + Colors.RESET)
    print(Colors.CYAN + Colors.BOLD + '    ╚═══╝ ╚═════╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═════╝ ' + Colors.RESET)
    print(Colors.YELLOW + Colors.BOLD + '    █████╗ ██╗██████╗ ██████╗ ██████╗  ██████╗ ██████╗ ' + Colors.RESET)
    print(Colors.YELLOW + Colors.BOLD + '   ██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗' + Colors.RESET)
    print(Colors.YELLOW + Colors.BOLD + '   ███████║██║██████╔╝██║  ██║██████╔╝██║   ██║██████╔╝' + Colors.RESET)
    print(Colors.YELLOW + Colors.BOLD + '   ██╔══██║██║██╔══██╗██║  ██║██╔══██╗██║   ██║██╔═══╝ ' + Colors.RESET)
    print(Colors.YELLOW + Colors.BOLD + '   ██║  ██║██║██║  ██║██████╔╝██║  ██║╚██████╔╝██║     ' + Colors.RESET)
    print(Colors.YELLOW + Colors.BOLD + '   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ' + Colors.RESET)
    print(Colors.GREEN + Colors.BOLD + '    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ' + Colors.RESET)
    print(Colors.GREEN + Colors.BOLD + '    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗' + Colors.RESET)
    print(Colors.GREEN + Colors.BOLD + '    ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝' + Colors.RESET)
    print(Colors.GREEN + Colors.BOLD + '    ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗' + Colors.RESET)
    print(Colors.GREEN + Colors.BOLD + '    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║' + Colors.RESET)
    print(Colors.GREEN + Colors.BOLD + '    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝' + Colors.RESET)
    
    print(Colors.MAGENTA + Colors.BOLD + '\n📱 Telegram: ' + Colors.RESET + Colors.BLUE + Colors.UNDERLINE + 'https://t.me/jobjab_airdrop_hunter' + Colors.RESET)
    print(Colors.YELLOW + '🛡️ Universal Framework - 99.9% Human-Like Anti-Detection' + Colors.RESET)
    print(Colors.GREEN + '🚀 Enhanced Features: Fingerprinting, Psychology, Timing' + Colors.RESET)
    print(Colors.BLUE + '🌐 Multi-Domain Cookie Management & Proxy Intelligence' + Colors.RESET)
    print(Colors.CYAN + Colors.BOLD + '═══════════════════════════════════════════════════════════' + Colors.RESET)
    print(Colors.YELLOW + Colors.BOLD + '💰 DONATE:' + Colors.RESET)
    print(Colors.GREEN + '🔗 EVM (all networks): ' + Colors.RESET + Colors.WHITE + '0xDeB20b7a9c9A54e1Cfce270416752F9982B6B25C' + Colors.RESET)
    print(Colors.MAGENTA + '☀️ Solana: ' + Colors.RESET + Colors.WHITE + 'CyNMKJUxJ4Y75LnQxaGCjyTrsivCPUvirL1DipWqyZAy' + Colors.RESET)
    print(Colors.CYAN + Colors.BOLD + '═══════════════════════════════════════════════════════════' + Colors.RESET)
    
    if wait_for_enter:
        input(Colors.WHITE + Colors.BOLD + '\n✨ Press Enter to continue to main menu... ' + Colors.RESET)

def display_jobjab_header(subtitle='Main Menu'):
    """
    Display compact JOBJAB banner for menu headers
    
    Args:
        subtitle (str): Optional subtitle to display
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colors.CYAN + Colors.BOLD + '🎯 JOBJAB AIRDROP HUNTER - ' + subtitle + Colors.RESET)
    print(Colors.MAGENTA + Colors.BOLD + '📱 Telegram: ' + Colors.RESET + Colors.BLUE + Colors.UNDERLINE + 'https://t.me/jobjab_airdrop_hunter' + Colors.RESET)
    print(Colors.CYAN + Colors.BOLD + '═══════════════════════════════════════\n' + Colors.RESET)

def display_jobjab_logo():
    """Display simple JOBJAB text logo"""
    print(Colors.CYAN + Colors.BOLD + '\n🎯 JOBJAB AIRDROP HUNTER' + Colors.RESET)
    print(Colors.MAGENTA + Colors.BOLD + '📱 Telegram: ' + Colors.RESET + Colors.BLUE + Colors.UNDERLINE + 'https://t.me/jobjab_airdrop_hunter\n' + Colors.RESET)

def display_jobjab_goodbye():
    """Display goodbye message with JOBJAB branding"""
    print(Colors.CYAN + Colors.BOLD + '\n🎯 Thank you for using JOBJAB AIRDROP HUNTER!' + Colors.RESET)
    print(Colors.MAGENTA + Colors.BOLD + '📱 Join us: ' + Colors.RESET + Colors.BLUE + Colors.UNDERLINE + 'https://t.me/jobjab_airdrop_hunter' + Colors.RESET)
    print(Colors.GREEN + '🚀 Happy farming! 🚀\n' + Colors.RESET)

def display_jobjab_interrupted():
    """Display interrupted message with JOBJAB branding"""
    print(Colors.YELLOW + '\n\n⏹️ Application interrupted by user' + Colors.RESET)
    print(Colors.CYAN + '🎯 JOBJAB AIRDROP HUNTER - Goodbye! 👋' + Colors.RESET)
    print(Colors.MAGENTA + Colors.BOLD + '📱 Telegram: ' + Colors.RESET + Colors.BLUE + Colors.UNDERLINE + 'https://t.me/jobjab_airdrop_hunter' + Colors.RESET) 
"""
Example: Text-Only Interaction
Shows how to use the agent programmatically without voice
"""

import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_agent import AIAgent
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    """Example of programmatic interaction with the agent"""
    
    print(f"{Fore.CYAN}{Style.BRIGHT}=== Text Interaction Example ==={Style.RESET_ALL}\n")
    
    # Initialize agent
    print(f"{Fore.YELLOW}Initializing AI agent...")
    agent = AIAgent()
    
    print(f"{Fore.GREEN}Agent ready!\n")
    
    # Simulate a conversation about daily tasks
    conversation = [
        ("What time is good for a morning jog?", "Getting exercise advice"),
        ("What should I eat for breakfast after exercise?", "Nutrition question"),
        ("Can you suggest a productive morning routine?", "Routine planning"),
        ("How can I stay motivated?", "Motivation help"),
    ]
    
    print(f"{Fore.CYAN}Simulating conversation about morning routine:\n")
    
    for question, context in conversation:
        print(f"{Fore.MAGENTA}[{context}]")
        print(f"{Fore.BLUE}User: {question}")
        
        response = agent.generate_response(question)
        print(f"{Fore.GREEN}Agent: {response}\n")
    
    # Demonstrate special commands
    print(f"{Fore.CYAN}Testing special commands:\n")
    
    special_commands = ["help", "clear"]
    
    for cmd in special_commands:
        print(f"{Fore.BLUE}User: {cmd}")
        response = agent.process_command(cmd)
        print(f"{Fore.GREEN}Agent: {response}\n")

if __name__ == "__main__":
    main()

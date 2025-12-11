"""
Simple test script to verify the AI agent works in text mode
without requiring microphone or speakers
"""

from ai_agent import AIAgent
from colorama import Fore, Style, init
import config

init(autoreset=True)

def test_agent():
    """Test the AI agent with sample interactions"""
    print(f"{Fore.CYAN}{Style.BRIGHT}=== AI Agent Test ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Testing AI agent functionality...\n")
    
    # Initialize agent
    try:
        agent = AIAgent()
        print(f"\n{Fore.GREEN}Agent initialized successfully!\n")
    except Exception as e:
        print(f"{Fore.RED}Error initializing agent: {e}")
        return False
    
    # Test conversations
    test_inputs = [
        "Hello, how are you?",
        "What can you help me with?",
        "Tell me something interesting",
        "What's your favorite color?",
        "goodbye"
    ]
    
    print(f"{Fore.CYAN}Running test conversations...\n")
    
    for user_input in test_inputs:
        print(f"{Fore.BLUE}User: {user_input}")
        
        try:
            response = agent.process_command(user_input)
            print(f"{Fore.GREEN}Agent: {response}\n")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}\n")
            return False
    
    print(f"{Fore.GREEN}{Style.BRIGHT}All tests completed successfully!{Style.RESET_ALL}")
    return True

if __name__ == "__main__":
    success = test_agent()
    exit(0 if success else 1)

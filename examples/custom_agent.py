"""
Example: Custom AI Agent Configuration
Shows how to create a custom agent with specific behavior
"""

from ai_agent import AIAgent
from colorama import Fore, init
import config

init(autoreset=True)

def main():
    """Example of using the AI agent with custom settings"""
    
    print(f"{Fore.CYAN}=== Custom Agent Example ===\n")
    
    # Create agent with different model
    print(f"{Fore.YELLOW}Loading custom model...")
    agent = AIAgent(model_name=config.ALTERNATIVE_MODELS["assistant"])
    
    # Example conversations with context memory
    conversations = [
        "My name is Alex and I'm learning Python.",
        "What programming language am I learning?",
        "Can you help me understand functions?",
        "What was my name again?",
    ]
    
    print(f"{Fore.GREEN}Starting conversation with context memory...\n")
    
    for user_input in conversations:
        print(f"{Fore.BLUE}User: {user_input}")
        response = agent.process_command(user_input)
        print(f"{Fore.GREEN}Agent: {response}\n")
    
    # Clear history and test
    print(f"{Fore.YELLOW}Clearing conversation history...\n")
    agent.clear_history()
    
    print(f"{Fore.BLUE}User: What was my name?")
    response = agent.process_command("What was my name?")
    print(f"{Fore.GREEN}Agent: {response}\n")
    
    print(f"{Fore.CYAN}Note: After clearing history, the agent doesn't remember your name!")

if __name__ == "__main__":
    main()

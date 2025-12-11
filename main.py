"""
Voice-Activated AI Agent
Main application entry point

This AI agent can be controlled by voice and is designed for hands-free use,
such as while driving or when you can't be at the computer.
"""

import sys
import argparse
from colorama import Fore, Style, init

import config
from voice_input import VoiceInput
from voice_output import VoiceOutput
from ai_agent import AIAgent

init(autoreset=True)


class VoiceAIAssistant:
    """Main application class for the voice AI assistant"""
    
    def __init__(self, model_name: str = None, no_voice: bool = False):
        """
        Initialize the voice AI assistant
        
        Args:
            model_name: Optional custom model name to use
            no_voice: If True, disable voice input/output for text-only mode
        """
        print(f"{Fore.CYAN}{Style.BRIGHT}=== Voice-Activated AI Assistant ==={Style.RESET_ALL}")
        print(f"{Fore.CYAN}Initializing components...\n")
        
        self.no_voice = no_voice
        
        # Initialize AI Agent
        model = model_name if model_name else config.MODEL_NAME
        self.agent = AIAgent(model_name=model)
        
        if not no_voice:
            # Initialize Voice components
            try:
                self.voice_input = VoiceInput()
                self.voice_output = VoiceOutput()
            except Exception as e:
                print(f"{Fore.RED}Error initializing voice components: {e}")
                print(f"{Fore.YELLOW}Falling back to text-only mode")
                self.no_voice = True
        
        print(f"\n{Fore.GREEN}{Style.BRIGHT}Ready to assist!{Style.RESET_ALL}\n")
    
    def run_voice_mode(self):
        """Run the assistant in voice-interactive mode"""
        print(f"{Fore.CYAN}Voice mode activated!")
        print(f"{Fore.YELLOW}Tips for best results:")
        print(f"  - Speak clearly and at a normal pace")
        print(f"  - Minimize background noise")
        print(f"  - Wait for the beep before speaking")
        print(f"{Fore.YELLOW}Say 'goodbye' or 'exit' to quit\n")
        
        # Welcome message
        self.voice_output.speak("Hello! I'm your AI assistant. How can I help you today?")
        
        def handle_voice_input(text: str):
            """Handle recognized voice input"""
            print(f"{Fore.BLUE}You: {Style.BRIGHT}{text}")
            
            # Process with AI agent
            response = self.agent.process_command(text)
            
            # Speak response
            self.voice_output.speak(response)
            
            # Check for exit commands
            if any(word in text.lower() for word in ["exit", "quit", "goodbye", "bye"]):
                sys.exit(0)
        
        try:
            # Start continuous listening
            self.voice_input.continuous_listen(handle_voice_input)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Shutting down...")
            self.voice_output.speak("Goodbye!")
    
    def run_text_mode(self):
        """Run the assistant in text-only mode"""
        print(f"{Fore.CYAN}Text mode activated!")
        print(f"{Fore.YELLOW}Type your messages and press Enter")
        print(f"{Fore.YELLOW}Type 'exit', 'quit', or 'goodbye' to quit\n")
        
        print(f"{Fore.GREEN}Agent: Hello! I'm your AI assistant. How can I help you today?")
        
        try:
            while True:
                # Get user input
                user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}").strip()
                
                if not user_input:
                    continue
                
                # Process with AI agent
                response = self.agent.process_command(user_input)
                
                # Display response
                print(f"{Fore.GREEN}Agent: {Style.BRIGHT}{response}")
                
                # Check for exit commands
                if any(word in user_input.lower() for word in ["exit", "quit", "goodbye", "bye"]):
                    break
                    
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Shutting down...")
            print(f"{Fore.GREEN}Agent: Goodbye!")
    
    def run(self):
        """Run the assistant in appropriate mode"""
        if self.no_voice:
            self.run_text_mode()
        else:
            self.run_voice_mode()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Voice-Activated AI Assistant using Hugging Face",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Run with default settings (voice mode)
  python main.py --text             # Run in text-only mode (no voice)
  python main.py --model small      # Use smaller/faster model
  python main.py --no-wake-word     # Disable wake word requirement
        """
    )
    
    parser.add_argument(
        "--text",
        action="store_true",
        help="Run in text-only mode (disable voice input/output)"
    )
    
    parser.add_argument(
        "--model",
        choices=["small", "medium", "large", "assistant"],
        default="medium",
        help="Choose model size (default: medium)"
    )
    
    parser.add_argument(
        "--no-wake-word",
        action="store_true",
        help="Disable wake word requirement (always listening)"
    )
    
    args = parser.parse_args()
    
    # Configure based on arguments
    if args.no_wake_word:
        config.ENABLE_WAKE_WORD = False
    
    # Select model
    model_map = {
        "small": config.ALTERNATIVE_MODELS["small"],
        "medium": config.MODEL_NAME,
        "large": config.ALTERNATIVE_MODELS["large"],
        "assistant": config.ALTERNATIVE_MODELS["assistant"],
    }
    model_name = model_map[args.model]
    
    # Create and run assistant
    try:
        assistant = VoiceAIAssistant(model_name=model_name, no_voice=args.text)
        assistant.run()
    except Exception as e:
        print(f"{Fore.RED}Fatal error: {e}")
        if config.DEBUG:
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()

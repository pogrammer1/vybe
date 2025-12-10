"""
AI Agent Core Module
Handles conversation and task processing using Hugging Face models
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import List, Dict, Optional
import config
from colorama import Fore, Style, init

init(autoreset=True)


class AIAgent:
    """Core AI agent using Hugging Face transformers"""
    
    def __init__(self, model_name: str = config.MODEL_NAME):
        print(f"{Fore.YELLOW}Loading AI model: {model_name}")
        print(f"{Fore.YELLOW}This may take a few moments on first run...")
        
        self.model_name = model_name
        self.conversation_history = []
        
        # Load tokenizer and model
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                cache_dir=str(config.CACHE_DIR)
            )
            
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                cache_dir=str(config.CACHE_DIR),
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                low_cpu_mem_usage=True
            )
            
            # Move model to GPU if available
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self.model.to(self.device)
            
            print(f"{Fore.GREEN}Model loaded successfully on {self.device}!")
            
            # Set padding token
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
        except Exception as e:
            print(f"{Fore.RED}Error loading model: {e}")
            raise
    
    def generate_response(self, user_input: str) -> str:
        """
        Generate a response to user input
        
        Args:
            user_input: User's text input
            
        Returns:
            Generated response text
        """
        try:
            # Add user input to conversation history
            if config.ENABLE_CONTEXT_MEMORY:
                self.conversation_history.append(user_input)
                
                # Limit history length (stores both user input and assistant response)
                # Each turn = 2 messages (user + assistant), so multiply by 2
                max_messages = config.MAX_HISTORY_LENGTH * 2
                if len(self.conversation_history) > max_messages:
                    self.conversation_history = self.conversation_history[-max_messages:]
            
            # Prepare input with conversation context
            if config.ENABLE_CONTEXT_MEMORY and len(self.conversation_history) > 1:
                # Include recent conversation history
                context = " ".join(self.conversation_history[-config.MAX_HISTORY_LENGTH:])
                input_text = context + self.tokenizer.eos_token
            else:
                input_text = user_input + self.tokenizer.eos_token
            
            # Tokenize input
            inputs = self.tokenizer.encode(
                input_text,
                return_tensors="pt",
                truncation=True,
                max_length=1000
            ).to(self.device)
            
            # Generate response
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_new_tokens=config.MAX_RESPONSE_LENGTH,
                    temperature=config.TEMPERATURE,
                    top_p=config.TOP_P,
                    do_sample=True,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                    no_repeat_ngram_size=3,
                )
            
            # Decode response
            response = self.tokenizer.decode(
                outputs[0][inputs.shape[-1]:],
                skip_special_tokens=True
            )
            
            # Clean up response
            response = response.strip()
            
            # Add response to history
            if config.ENABLE_CONTEXT_MEMORY:
                self.conversation_history.append(response)
            
            return response if response else "I'm not sure how to respond to that."
            
        except Exception as e:
            if config.DEBUG:
                print(f"{Fore.RED}Error generating response: {e}")
            return "I apologize, I encountered an error processing your request."
    
    def process_command(self, user_input: str) -> str:
        """
        Process user input and determine response
        
        Args:
            user_input: User's voice input as text
            
        Returns:
            Response text
        """
        user_input = user_input.strip()
        
        # Check for special commands (case-insensitive)
        user_input_lower = user_input.lower()
        
        if any(word in user_input_lower for word in ["exit", "quit", "goodbye", "bye"]):
            return "Goodbye! Have a great day!"
        
        if "help" in user_input_lower:
            return self._get_help_message()
        
        if "clear" in user_input_lower or "reset" in user_input_lower:
            self.clear_history()
            return "I've cleared our conversation history."
        
        # Generate AI response (preserve original case for better context)
        response = self.generate_response(user_input)
        return response
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        if config.VERBOSE:
            print(f"{Fore.YELLOW}Conversation history cleared")
    
    def _get_help_message(self) -> str:
        """Return help message"""
        return (
            "I'm your voice-activated AI assistant. "
            "You can ask me questions, have conversations, or get help with tasks. "
            "Say 'goodbye' to exit, or 'clear' to reset our conversation."
        )

"""
Configuration settings for the Voice AI Agent
"""

import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).parent
MODELS_DIR = BASE_DIR / "models"
CACHE_DIR = BASE_DIR / "cache"

# Ensure directories exist
MODELS_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

# Hugging Face Model Configuration
MODEL_NAME = "microsoft/DialoGPT-medium"  # Conversational model
ALTERNATIVE_MODELS = {
    "small": "microsoft/DialoGPT-small",      # Faster, less capable
    "large": "microsoft/DialoGPT-large",      # Slower, more capable
    "assistant": "facebook/blenderbot-400M-distill",  # Task-oriented
}

# Speech Recognition Settings
SPEECH_RECOGNITION_LANGUAGE = "en-US"
WAKE_WORD = "hey assistant"  # Wake word to activate the agent
ENERGY_THRESHOLD = 4000  # Microphone sensitivity (adjust based on environment)
PAUSE_THRESHOLD = 1.0  # Seconds of silence before considering phrase complete

# Text-to-Speech Settings
TTS_ENGINE = "pyttsx3"  # Options: "pyttsx3" (offline), "gtts" (online)
TTS_RATE = 175  # Speaking rate (words per minute)
TTS_VOLUME = 0.9  # Volume level (0.0 to 1.0)

# AI Agent Settings
MAX_HISTORY_LENGTH = 5  # Number of conversation turns to remember
MAX_RESPONSE_LENGTH = 150  # Maximum tokens in response
TEMPERATURE = 0.8  # Creativity level (0.0 to 1.0)
TOP_P = 0.9  # Nucleus sampling parameter

# Features
ENABLE_WAKE_WORD = True  # Require wake word to activate
ENABLE_VOICE_FEEDBACK = True  # Audio confirmation when listening
ENABLE_CONTEXT_MEMORY = True  # Remember conversation context
ENABLE_PROGRAMMING_MODE = False  # Future feature for programming assistance

# Debug Settings
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
VERBOSE = os.getenv("VERBOSE", "false").lower() == "true"

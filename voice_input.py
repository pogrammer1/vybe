"""
Speech Recognition Module
Handles voice input from the user
"""

from typing import Optional
import config
from colorama import Fore, Style, init

init(autoreset=True)

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False
    sr = None


class VoiceInput:
    """Handles speech-to-text conversion"""
    
    def __init__(self):
        if not SPEECH_RECOGNITION_AVAILABLE:
            raise ImportError(
                "speech_recognition not available. "
                "Install with: pip install SpeechRecognition pyaudio"
            )
        
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Configure recognizer
        self.recognizer.energy_threshold = config.ENERGY_THRESHOLD
        self.recognizer.pause_threshold = config.PAUSE_THRESHOLD
        self.recognizer.dynamic_energy_threshold = True
        
        # Adjust for ambient noise
        print(f"{Fore.YELLOW}Calibrating microphone for ambient noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        print(f"{Fore.GREEN}Microphone calibrated!")
    
    def listen(self, prompt: str = "Listening...") -> Optional[str]:
        """
        Listen for voice input and convert to text
        
        Args:
            prompt: Message to display while listening
            
        Returns:
            Transcribed text or None if recognition failed
        """
        try:
            with self.microphone as source:
                print(f"{Fore.CYAN}{prompt}")
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
            
            print(f"{Fore.YELLOW}Processing speech...")
            
            # Use Google Speech Recognition (free, no API key needed)
            text = self.recognizer.recognize_google(
                audio, 
                language=config.SPEECH_RECOGNITION_LANGUAGE
            )
            
            # Return original text (case preserved for proper nouns)
            # Command processing will handle case normalization if needed
            return text
            
        except sr.WaitTimeoutError:
            print(f"{Fore.RED}No speech detected. Timeout.")
            return None
        except sr.UnknownValueError:
            print(f"{Fore.RED}Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"{Fore.RED}Speech recognition service error: {e}")
            return None
        except Exception as e:
            if config.DEBUG:
                print(f"{Fore.RED}Error in speech recognition: {e}")
            return None
    
    def wait_for_wake_word(self) -> bool:
        """
        Wait for the wake word to be spoken
        
        Returns:
            True if wake word detected, False otherwise
        """
        print(f"{Fore.MAGENTA}Say '{config.WAKE_WORD}' to activate...")
        
        text = self.listen(prompt=f"{Fore.CYAN}Waiting for wake word...")
        
        # Check for wake word (case-insensitive)
        if text and config.WAKE_WORD.lower() in text.lower():
            print(f"{Fore.GREEN}Wake word detected!")
            return True
        
        return False
    
    def continuous_listen(self, callback):
        """
        Continuously listen for voice input
        
        Args:
            callback: Function to call with recognized text
        """
        print(f"{Fore.GREEN}Starting continuous listening mode...")
        print(f"{Fore.YELLOW}Press Ctrl+C to stop")
        
        try:
            while True:
                if config.ENABLE_WAKE_WORD:
                    if not self.wait_for_wake_word():
                        continue
                
                text = self.listen()
                if text:
                    callback(text)
                    
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Stopping listening mode...")

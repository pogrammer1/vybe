"""
Text-to-Speech Module
Handles voice output to the user
"""

import pyttsx3
from typing import Optional
import config
from colorama import Fore, Style, init

init(autoreset=True)


class VoiceOutput:
    """Handles text-to-speech conversion"""
    
    def __init__(self, engine_type: str = config.TTS_ENGINE):
        self.engine_type = engine_type
        
        if engine_type == "pyttsx3":
            self._init_pyttsx3()
        elif engine_type == "gtts":
            print(f"{Fore.YELLOW}gTTS engine selected (requires internet)")
        else:
            raise ValueError(f"Unknown TTS engine: {engine_type}")
    
    def _init_pyttsx3(self):
        """Initialize pyttsx3 engine"""
        try:
            self.engine = pyttsx3.init()
            
            # Configure voice properties
            self.engine.setProperty('rate', config.TTS_RATE)
            self.engine.setProperty('volume', config.TTS_VOLUME)
            
            # Try to set a better voice if available
            voices = self.engine.getProperty('voices')
            if voices:
                # Prefer female voice if available (usually index 1)
                voice_index = 1 if len(voices) > 1 else 0
                self.engine.setProperty('voice', voices[voice_index].id)
            
            print(f"{Fore.GREEN}Text-to-speech engine initialized!")
            
        except Exception as e:
            print(f"{Fore.RED}Error initializing TTS engine: {e}")
            print(f"{Fore.YELLOW}TTS may not work properly")
            self.engine = None
    
    def speak(self, text: str, display: bool = True):
        """
        Convert text to speech and play it
        
        Args:
            text: Text to speak
            display: Whether to print the text to console
        """
        if display:
            print(f"{Fore.GREEN}Agent: {Style.BRIGHT}{text}")
        
        if self.engine_type == "pyttsx3":
            self._speak_pyttsx3(text)
        elif self.engine_type == "gtts":
            self._speak_gtts(text)
    
    def _speak_pyttsx3(self, text: str):
        """Speak using pyttsx3 (offline)"""
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                if config.DEBUG:
                    print(f"{Fore.RED}Error speaking: {e}")
    
    def _speak_gtts(self, text: str):
        """Speak using gTTS (online)"""
        try:
            from gtts import gTTS
            import tempfile
            import os
            from pydub import AudioSegment
            from pydub.playback import play
            
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_file = fp.name
            
            # Generate speech
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(temp_file)
            
            # Play audio
            audio = AudioSegment.from_mp3(temp_file)
            play(audio)
            
            # Clean up
            os.remove(temp_file)
            
        except ImportError:
            print(f"{Fore.RED}gTTS or pydub not available. Install with: pip install gtts pydub")
        except Exception as e:
            if config.DEBUG:
                print(f"{Fore.RED}Error with gTTS: {e}")
    
    def confirmation_sound(self):
        """Play a confirmation sound when agent is listening"""
        if config.ENABLE_VOICE_FEEDBACK:
            self.speak("Yes?", display=False)

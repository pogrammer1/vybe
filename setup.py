#!/usr/bin/env python3
"""
Setup and verification script for the Voice AI Assistant
"""

import sys
import subprocess
import importlib.util
from colorama import Fore, Style, init

init(autoreset=True)


def check_python_version():
    """Check if Python version is adequate"""
    print(f"{Fore.CYAN}Checking Python version...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"{Fore.RED}✗ Python 3.8+ required, found {version.major}.{version.minor}")
        return False
    
    print(f"{Fore.GREEN}✓ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    spec = importlib.util.find_spec(import_name)
    if spec is None:
        print(f"{Fore.RED}✗ {package_name} not installed")
        return False
    
    print(f"{Fore.GREEN}✓ {package_name}")
    return True


def install_requirements():
    """Install requirements from requirements.txt"""
    print(f"\n{Fore.CYAN}Installing dependencies...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print(f"{Fore.GREEN}✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}✗ Failed to install dependencies")
        return False


def check_dependencies():
    """Check if all required packages are installed"""
    print(f"\n{Fore.CYAN}Checking dependencies...")
    
    packages = [
        ("transformers", "transformers"),
        ("torch", "torch"),
        ("speech_recognition", "speech_recognition"),
        ("pyttsx3", "pyttsx3"),
        ("colorama", "colorama"),
    ]
    
    all_installed = True
    for package, import_name in packages:
        if not check_package(package, import_name):
            all_installed = False
    
    return all_installed


def test_microphone():
    """Test if microphone is accessible"""
    print(f"\n{Fore.CYAN}Testing microphone access...")
    
    try:
        import speech_recognition as sr
        
        # Try to list microphones
        mics = sr.Microphone.list_microphone_names()
        
        if not mics:
            print(f"{Fore.YELLOW}⚠ No microphones detected")
            print(f"{Fore.YELLOW}  Voice mode may not work, but text mode will")
            return False
        
        print(f"{Fore.GREEN}✓ Found {len(mics)} microphone(s)")
        if len(mics) <= 3:  # Only show if not too many
            for i, mic in enumerate(mics):
                print(f"  {i}: {mic}")
        return True
        
    except Exception as e:
        print(f"{Fore.YELLOW}⚠ Could not test microphone: {e}")
        return False


def test_tts():
    """Test text-to-speech"""
    print(f"\n{Fore.CYAN}Testing text-to-speech...")
    
    try:
        import pyttsx3
        engine = pyttsx3.init()
        print(f"{Fore.GREEN}✓ Text-to-speech engine available")
        return True
    except Exception as e:
        print(f"{Fore.YELLOW}⚠ TTS may not work: {e}")
        return False


def main():
    """Main setup verification"""
    print(f"{Fore.CYAN}{Style.BRIGHT}=== Voice AI Assistant Setup ==={Style.RESET_ALL}\n")
    
    checks_passed = []
    
    # Check Python version
    checks_passed.append(check_python_version())
    
    # Check if dependencies are installed
    if not check_dependencies():
        print(f"\n{Fore.YELLOW}Some dependencies are missing.")
        response = input(f"{Fore.CYAN}Install now? (y/n): ").lower()
        
        if response == 'y':
            if install_requirements():
                checks_passed.append(True)
            else:
                checks_passed.append(False)
        else:
            print(f"{Fore.YELLOW}You can install later with: pip install -r requirements.txt")
            checks_passed.append(False)
    else:
        checks_passed.append(True)
    
    # Optional checks
    test_microphone()
    test_tts()
    
    # Summary
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== Setup Summary ==={Style.RESET_ALL}")
    
    if all(checks_passed):
        print(f"{Fore.GREEN}✓ All required components are ready!")
        print(f"\n{Fore.CYAN}You can now run the assistant:")
        print(f"  {Fore.WHITE}python main.py          {Fore.CYAN}# Voice mode")
        print(f"  {Fore.WHITE}python main.py --text   {Fore.CYAN}# Text mode")
        print(f"  {Fore.WHITE}python test_agent.py    {Fore.CYAN}# Run tests")
    else:
        print(f"{Fore.YELLOW}⚠ Some components need attention")
        print(f"{Fore.YELLOW}  See messages above for details")
        print(f"\n{Fore.CYAN}You can still use text mode:")
        print(f"  {Fore.WHITE}python main.py --text")


if __name__ == "__main__":
    main()

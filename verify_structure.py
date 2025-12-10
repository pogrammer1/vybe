"""
Minimal verification that the agent structure is correct
This test checks functionality without downloading large AI models
"""

import sys
from colorama import Fore, Style, init
import config

init(autoreset=True)

def test_basic_structure():
    """Test basic imports and structure"""
    print(f"{Fore.CYAN}{Style.BRIGHT}=== Minimal Structure Test ==={Style.RESET_ALL}\n")
    
    tests_passed = 0
    tests_total = 0
    
    # Test 1: Configuration
    tests_total += 1
    print(f"{Fore.CYAN}Test 1: Configuration module")
    try:
        assert hasattr(config, 'MODEL_NAME')
        assert hasattr(config, 'WAKE_WORD')
        assert hasattr(config, 'MAX_HISTORY_LENGTH')
        print(f"{Fore.GREEN}✓ Configuration loaded correctly")
        print(f"  Model: {config.MODEL_NAME}")
        print(f"  Wake word: '{config.WAKE_WORD}'")
        tests_passed += 1
    except AssertionError as e:
        print(f"{Fore.RED}✗ Configuration test failed: {e}")
    
    # Test 2: Voice Input module
    tests_total += 1
    print(f"\n{Fore.CYAN}Test 2: Voice Input module")
    try:
        from voice_input import VoiceInput, SPEECH_RECOGNITION_AVAILABLE
        print(f"{Fore.GREEN}✓ Voice input module loads")
        if SPEECH_RECOGNITION_AVAILABLE:
            print(f"{Fore.GREEN}  Speech recognition available")
        else:
            print(f"{Fore.YELLOW}  Speech recognition not available (optional)")
        tests_passed += 1
    except Exception as e:
        print(f"{Fore.RED}✗ Voice input module failed: {e}")
    
    # Test 3: Voice Output module
    tests_total += 1
    print(f"\n{Fore.CYAN}Test 3: Voice Output module")
    try:
        from voice_output import VoiceOutput, PYTTSX3_AVAILABLE
        print(f"{Fore.GREEN}✓ Voice output module loads")
        if PYTTSX3_AVAILABLE:
            print(f"{Fore.GREEN}  Text-to-speech available")
        else:
            print(f"{Fore.YELLOW}  Text-to-speech not available (optional)")
        tests_passed += 1
    except Exception as e:
        print(f"{Fore.RED}✗ Voice output module failed: {e}")
    
    # Test 4: AI Agent module
    tests_total += 1
    print(f"\n{Fore.CYAN}Test 4: AI Agent module")
    try:
        import ai_agent
        print(f"{Fore.GREEN}✓ AI agent module loads")
        tests_passed += 1
    except Exception as e:
        print(f"{Fore.RED}✗ AI agent module failed: {e}")
    
    # Test 5: Main application module
    tests_total += 1
    print(f"\n{Fore.CYAN}Test 5: Main application module")
    try:
        import main
        print(f"{Fore.GREEN}✓ Main application module loads")
        tests_passed += 1
    except Exception as e:
        print(f"{Fore.RED}✗ Main application module failed: {e}")
    
    # Test 6: File structure
    tests_total += 1
    print(f"\n{Fore.CYAN}Test 6: Required files")
    import os
    required_files = [
        'main.py', 'config.py', 'ai_agent.py',
        'voice_input.py', 'voice_output.py',
        'requirements.txt', 'README.md', 'GETTING_STARTED.md'
    ]
    missing = [f for f in required_files if not os.path.exists(f)]
    if not missing:
        print(f"{Fore.GREEN}✓ All required files present")
        tests_passed += 1
    else:
        print(f"{Fore.RED}✗ Missing files: {missing}")
    
    # Summary
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== Test Summary ==={Style.RESET_ALL}")
    print(f"Passed: {tests_passed}/{tests_total}")
    
    if tests_passed == tests_total:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}✓ All structure tests passed!{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}The agent is ready to use!")
        print(f"\n{Fore.YELLOW}Next steps:")
        print(f"  1. Run: python main.py --text")
        print(f"     (Text mode - will download AI model on first run)")
        print(f"  2. Install voice deps: pip install SpeechRecognition pyaudio pyttsx3")
        print(f"  3. Run: python main.py")
        print(f"     (Voice mode - requires microphone)")
        return 0
    else:
        print(f"\n{Fore.RED}{Style.BRIGHT}✗ Some tests failed{Style.RESET_ALL}")
        return 1

if __name__ == "__main__":
    sys.exit(test_basic_structure())

"""
Quick test to verify imports and basic structure without loading models
"""

import sys
from colorama import Fore, Style, init

init(autoreset=True)

def test_imports():
    """Test that all modules can be imported"""
    print(f"{Fore.CYAN}Testing imports...")
    
    try:
        import config
        print(f"{Fore.GREEN}✓ config module")
    except Exception as e:
        print(f"{Fore.RED}✗ config module: {e}")
        return False
    
    try:
        import voice_input
        print(f"{Fore.GREEN}✓ voice_input module")
    except Exception as e:
        print(f"{Fore.RED}✗ voice_input module: {e}")
        return False
    
    try:
        import voice_output
        print(f"{Fore.GREEN}✓ voice_output module")
    except Exception as e:
        print(f"{Fore.RED}✗ voice_output module: {e}")
        return False
    
    try:
        import ai_agent
        print(f"{Fore.GREEN}✓ ai_agent module")
    except Exception as e:
        print(f"{Fore.RED}✗ ai_agent module: {e}")
        return False
    
    try:
        import main
        print(f"{Fore.GREEN}✓ main module")
    except Exception as e:
        print(f"{Fore.RED}✗ main module: {e}")
        return False
    
    return True

def test_config():
    """Test configuration values"""
    print(f"\n{Fore.CYAN}Testing configuration...")
    
    try:
        import config
        
        assert hasattr(config, 'MODEL_NAME'), "MODEL_NAME not defined"
        assert hasattr(config, 'WAKE_WORD'), "WAKE_WORD not defined"
        assert hasattr(config, 'CACHE_DIR'), "CACHE_DIR not defined"
        
        print(f"{Fore.GREEN}✓ Configuration valid")
        print(f"  Model: {config.MODEL_NAME}")
        print(f"  Wake word: {config.WAKE_WORD}")
        print(f"  Cache dir: {config.CACHE_DIR}")
        
        return True
    except Exception as e:
        print(f"{Fore.RED}✗ Configuration test failed: {e}")
        return False

def test_structure():
    """Test that required files exist"""
    import os
    
    print(f"\n{Fore.CYAN}Testing file structure...")
    
    required_files = [
        'main.py',
        'config.py',
        'ai_agent.py',
        'voice_input.py',
        'voice_output.py',
        'requirements.txt',
        'README.md',
        'GETTING_STARTED.md',
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"{Fore.GREEN}✓ {file}")
        else:
            print(f"{Fore.RED}✗ {file} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all quick tests"""
    print(f"{Fore.CYAN}{Style.BRIGHT}=== Quick Structure Test ==={Style.RESET_ALL}\n")
    
    results = []
    
    results.append(test_imports())
    results.append(test_config())
    results.append(test_structure())
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== Test Summary ==={Style.RESET_ALL}")
    
    if all(results):
        print(f"{Fore.GREEN}{Style.BRIGHT}✓ All tests passed!{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}The agent structure is ready.")
        print(f"{Fore.YELLOW}Note: Full model tests require downloading AI models (~500MB)")
        print(f"{Fore.CYAN}Run 'python test_agent.py' to test with models (takes longer)")
        return 0
    else:
        print(f"{Fore.RED}{Style.BRIGHT}✗ Some tests failed{Style.RESET_ALL}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

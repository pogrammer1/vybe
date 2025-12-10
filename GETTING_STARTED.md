# Getting Started with Voice AI Assistant

Welcome! This guide will help you get started with your new voice-activated AI assistant.

## Step 1: Install Dependencies

Run the setup script to check and install dependencies:

```bash
python setup.py
```

Or manually install:

```bash
pip install -r requirements.txt
```

## Step 2: Test the Installation

Run the test script to verify everything works:

```bash
python test_agent.py
```

This will test the AI agent in text mode (no microphone needed).

## Step 3: Choose Your Mode

### Option A: Voice Mode (Recommended)

If you have a microphone and want hands-free interaction:

```bash
python main.py
```

1. Wait for "Say 'hey assistant' to activate..."
2. Say the wake word: "Hey assistant"
3. Ask your question or give a command
4. Listen to the response
5. Repeat or say "goodbye" to exit

### Option B: Text Mode

If you prefer typing or don't have a microphone:

```bash
python main.py --text
```

1. Type your message and press Enter
2. Read the AI's response
3. Continue the conversation
4. Type "goodbye" to exit

## Step 4: Customize (Optional)

Edit `config.py` to customize:

- Change the wake word
- Adjust microphone sensitivity
- Switch to different AI models
- Modify voice settings
- Enable/disable features

## Common Use Cases

### While Driving
```
You: "Hey assistant, remind me to buy groceries"
AI: "I'll remember that for you. You need to buy groceries."
```

### General Questions
```
You: "What's the capital of France?"
AI: "The capital of France is Paris."
```

### Conversations
```
You: "Tell me a fun fact"
AI: "Did you know that honey never spoils? Archaeologists have found 3000-year-old honey that's still edible!"
```

## Tips

1. **Speak Clearly**: Enunciate your words for better recognition
2. **Minimize Noise**: Use in a quiet environment for best results
3. **Wait for Confirmation**: Listen for the "listening" prompt before speaking
4. **Be Patient**: First run downloads AI models (may take a few minutes)
5. **Use Text Mode**: If voice isn't working, text mode always works

## Troubleshooting

### Microphone Issues
- Check your microphone is connected and working
- Try adjusting `ENERGY_THRESHOLD` in config.py
- Run `python setup.py` to test microphone

### Model Download Slow
- First run downloads ~500MB AI model
- Subsequent runs use cached model (much faster)
- Be patient or use a smaller model: `python main.py --model small`

### Recognition Errors
- Speak more clearly
- Reduce background noise
- Increase pause between wake word and command
- Check internet connection (required for speech recognition)

## Next Steps

1. Try different models: `python main.py --model large`
2. Disable wake word: `python main.py --no-wake-word`
3. Customize the configuration in `config.py`
4. Read the full README.md for advanced features

## Need Help?

- Run `python main.py --help` for all options
- Check README.md for detailed documentation
- Open an issue on GitHub for support

Enjoy your AI assistant! 🎙️🤖

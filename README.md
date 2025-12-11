# 🎙️ Voice-Activated AI Assistant

A hands-free, voice-controlled AI assistant built with Hugging Face transformers and modern Python libraries. Perfect for everyday tasks, especially when you can't be at your computer (like while driving to work). Testing vibe code potential/flaws.

## ✨ Features

- 🗣️ **Voice Interaction**: Speak naturally to interact with the AI
- 🧠 **Powered by Hugging Face**: Uses state-of-the-art language models
- 🚀 **Wake Word Activation**: Optional "Hey Assistant" wake word
- 💾 **Context Memory**: Remembers conversation history
- 🎯 **Multiple Modes**: Voice mode or text-only mode
- ⚡ **Flexible Models**: Choose from small, medium, or large models
- 🛡️ **Privacy-Focused**: Can run completely offline (with pyttsx3 TTS)
- 🔧 **Extensible**: Built for future enhancements including programming assistance

## 🎯 Use Cases

- **While Driving**: Get information, have conversations, or manage tasks hands-free
- **Cooking**: Ask for conversions, timers, or recipe help without touching your device
- **Exercising**: Get motivation, track workouts, or answer questions
- **Multitasking**: Interact with AI while working on other tasks
- **Accessibility**: Voice control for those who need alternative input methods
- **Future: Programming Help**: Will evolve to assist with coding projects

## 📋 Prerequisites

- Python 3.8 or higher
- Microphone for voice input
- Speakers/headphones for audio output
- (Optional) GPU for faster model inference

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/pogrammer1/LLM-Course-hugging-face.git
cd LLM-Course-hugging-face
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: On some systems, you may need to install additional dependencies:

**Linux (Ubuntu/Debian)**:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio espeak
```

**macOS**:
```bash
brew install portaudio
```

**Windows**: PyAudio should work out of the box, but if you have issues:
```bash
pip install pipwin
pipwin install pyaudio
```

### 3. Run the Assistant

**Voice Mode (default)**:
```bash
python main.py
```

**Text-Only Mode** (no microphone needed):
```bash
python main.py --text
```

## 🎛️ Configuration

Edit `config.py` to customize:

- **Model Selection**: Change `MODEL_NAME` to use different Hugging Face models
- **Wake Word**: Customize `WAKE_WORD` (default: "hey assistant")
- **Speech Settings**: Adjust `ENERGY_THRESHOLD` for microphone sensitivity
- **TTS Settings**: Change voice rate, volume, and engine
- **AI Behavior**: Adjust temperature, response length, and memory

## 💻 Usage

### Voice Mode

1. Run `python main.py`
2. Say "Hey Assistant" to activate (if wake word is enabled)
3. Speak your question or command
4. Listen to the AI's response
5. Say "goodbye" or "exit" to quit

### Text Mode

1. Run `python main.py --text`
2. Type your messages and press Enter
3. Read the AI's responses
4. Type "goodbye" or "exit" to quit

## 🎨 Command Line Options

```bash
python main.py [OPTIONS]

Options:
  --text              Run in text-only mode (no voice)
  --model {small,medium,large,assistant}
                     Choose model size (default: medium)
  --no-wake-word     Disable wake word (always listening)
  -h, --help         Show help message
```

### Model Options

- **small**: Faster, lower resource usage, less capable (DialoGPT-small)
- **medium**: Balanced performance and quality (DialoGPT-medium, default)
- **large**: Best quality, slower, more resources (DialoGPT-large)
- **assistant**: Task-oriented assistant (BlenderBot)

## 📚 Examples

### Basic Conversation
```
You: Hey assistant, what's the weather like today?
Agent: I don't have real-time weather data, but I can help you with other questions!

You: Tell me a joke.
Agent: Why don't scientists trust atoms? Because they make up everything!
```

### Everyday Tasks
```
You: Remind me about my meeting at 3 PM.
Agent: I'll keep that in mind! You have a meeting at 3 PM.

You: What's 15% of 80?
Agent: 15% of 80 is 12.
```

### Getting Help
```
You: Help
Agent: I'm your voice-activated AI assistant. You can ask me questions, 
       have conversations, or get help with tasks. Say 'goodbye' to exit, 
       or 'clear' to reset our conversation.
```

## 🏗️ Architecture

The project is organized into modular components:

```
├── main.py           # Main application entry point
├── ai_agent.py       # AI core using Hugging Face transformers
├── voice_input.py    # Speech recognition module
├── voice_output.py   # Text-to-speech module
├── config.py         # Configuration settings
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

### Component Overview

- **AIAgent**: Handles conversation logic and response generation using Hugging Face models
- **VoiceInput**: Manages microphone input and speech-to-text conversion
- **VoiceOutput**: Handles text-to-speech synthesis
- **Configuration**: Centralized settings for easy customization

## 🔧 Customization

### Using Different AI Models

The assistant uses Hugging Face models. You can easily switch to other models:

```python
# In config.py, change MODEL_NAME to any compatible model:
MODEL_NAME = "microsoft/DialoGPT-large"  # Larger, more capable
MODEL_NAME = "facebook/blenderbot-400M-distill"  # Task-oriented
MODEL_NAME = "EleutherAI/gpt-neo-125M"  # Alternative architecture
```

### Adjusting Speech Recognition

```python
# In config.py
ENERGY_THRESHOLD = 4000  # Increase for noisy environments
PAUSE_THRESHOLD = 1.0    # How long to wait for end of speech
```

### Changing Voice Output

```python
# In config.py
TTS_ENGINE = "pyttsx3"  # Offline (default)
TTS_ENGINE = "gtts"     # Online, better quality

TTS_RATE = 175  # Words per minute (150-200 is typical)
TTS_VOLUME = 0.9  # 0.0 to 1.0
```

## 🚗 Tips for Using While Driving

⚠️ **Safety First**: Always prioritize safe driving!

- Use voice activation to avoid manual interaction
- Keep conversations brief
- Don't let the assistant distract you from the road
- Use at appropriate times (e.g., stopped at lights, highway driving)
- Consider using Bluetooth speakers for better audio

## 🔮 Future Enhancements

This agent is designed to grow with your needs:

- [ ] **Programming Assistant**: Help with coding questions, debug issues, generate code
- [ ] **Task Management**: Create reminders, to-do lists, calendar integration
- [ ] **External APIs**: Weather, news, traffic information
- [ ] **Context Awareness**: Remember user preferences and history across sessions
- [ ] **Multi-language Support**: Support for multiple languages
- [ ] **Emotion Detection**: Respond to user sentiment
- [ ] **Smart Home Integration**: Control IoT devices
- [ ] **Code Repository Analysis**: Understand and navigate codebases

## 🐛 Troubleshooting

### Microphone Not Working

```bash
# Test your microphone
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"
```

### PyAudio Installation Issues

**Linux**:
```bash
sudo apt-get install python3-dev portaudio19-dev
pip install pyaudio
```

**macOS**:
```bash
brew install portaudio
pip install pyaudio
```

**Windows**: Download pre-built wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

### Model Download Slow

Models are downloaded on first run and cached. Subsequent runs will be faster.
You can also pre-download models:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
```

### Speech Recognition Errors

- Ensure you have an internet connection (Google Speech Recognition requires it)
- Speak clearly and reduce background noise
- Adjust `ENERGY_THRESHOLD` in `config.py`

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! This is a learning project, and improvements are encouraged.

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

## 🙏 Acknowledgments

- **Hugging Face**: For amazing transformer models and libraries
- **Microsoft**: For DialoGPT conversational model
- **Google**: For speech recognition services
- **Open Source Community**: For the fantastic Python libraries

---

**Built with ❤️ using Hugging Face and modern Python**

*Compare this with your from-scratch implementation to see different approaches!*

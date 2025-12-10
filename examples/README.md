# Examples Directory

This directory contains example scripts demonstrating different ways to use the Voice AI Assistant.

## Available Examples

### 1. `custom_agent.py`
Demonstrates how to:
- Use different AI models
- Work with conversation context/memory
- Clear and manage conversation history
- Test context-dependent responses

Run with:
```bash
python examples/custom_agent.py
```

### 2. `text_interaction.py`
Shows how to:
- Use the agent programmatically without voice
- Simulate conversations
- Test special commands
- Integrate the agent into other applications

Run with:
```bash
python examples/text_interaction.py
```

## Creating Your Own Examples

You can create your own examples by:

1. Importing the necessary modules:
```python
from ai_agent import AIAgent
from voice_input import VoiceInput
from voice_output import VoiceOutput
import config
```

2. Initializing components:
```python
agent = AIAgent()
voice_in = VoiceInput()
voice_out = VoiceOutput()
```

3. Building your custom logic:
```python
user_input = voice_in.listen()
response = agent.process_command(user_input)
voice_out.speak(response)
```

## Use Case Ideas

- **Task Manager**: Build a voice-controlled to-do list
- **Timer/Reminder**: Create voice-activated timers
- **Learning Assistant**: Interactive learning with quizzes
- **Storyteller**: Generate and narrate stories
- **Code Helper**: Ask programming questions (future enhancement)

Feel free to experiment and create your own examples!

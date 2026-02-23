# 🎭 OpenClaw Meme Generator Skill

A powerful meme generation skill for OpenClaw that supports both classic meme templates and AI-powered custom meme creation.

## Features

✨ **Classic Templates**: Pre-built templates for popular meme formats
- Drake Hotline Bling
- Distracted Boyfriend
- Change My Mind
- Galaxy Brain / Expanding Brain
- Woman Yelling at Cat

🤖 **AI Generation**: Create custom memes using AI image generation (OpenAI DALL-E)

🎨 **Smart Text Rendering**: Automatic text wrapping, stroke effects, and optimal positioning

## Installation

```bash
# Clone the repository
git clone https://github.com/bigguybobby/meme-generator-skill.git
cd meme-generator-skill

# Install dependencies
pip install -r requirements.txt

# Make the script executable (optional)
chmod +x meme_generator.py
```

## Quick Start

### List available templates
```bash
python meme_generator.py --list
```

### Generate a Drake meme
```bash
python meme_generator.py --template drake \
  --top "Manually creating memes" \
  --bottom "Using OpenClaw Meme Generator" \
  --output my_meme.png
```

### Generate a Change My Mind meme
```bash
python meme_generator.py --template change-my-mind \
  --top "OpenClaw makes AI accessible"
```

### Generate an AI meme
```bash
export OPENAI_API_KEY="your-api-key"
python meme_generator.py --ai "A cat realizing it's Monday morning" --output cat_monday.png
```

## Usage

### Basic Syntax
```bash
python meme_generator.py [OPTIONS]
```

### Options
- `--template, -t NAME`: Specify meme template (drake, distracted-boyfriend, etc.)
- `--top TEXT`: Top text for the meme
- `--bottom TEXT`: Bottom text for the meme
- `--ai DESCRIPTION`: Generate AI meme from description
- `--output, -o PATH`: Output file path (default: meme_output.png)
- `--list, -l`: List all available templates

## Template Guide

### Drake (`drake`)
Two-panel format with disapproval (top) and approval (bottom).
```bash
python meme_generator.py -t drake --top "Old way" --bottom "New way"
```

### Distracted Boyfriend (`distracted-boyfriend`)
Three-character format representing temptation.
```bash
python meme_generator.py -t distracted-boyfriend --top "Current task" --bottom "Shiny new project"
```

### Change My Mind (`change-my-mind`)
Single statement on a sign.
```bash
python meme_generator.py -t change-my-mind --top "Your controversial opinion here"
```

### Galaxy Brain (`galaxy-brain`)
Escalating levels of thinking (use newlines or multiple calls).
```bash
python meme_generator.py -t galaxy-brain --top "Level 1 thinking" --bottom "Level 2 thinking"
```

### Woman Yelling at Cat (`woman-yelling-cat`)
Two-panel accusation vs confusion format.
```bash
python meme_generator.py -t woman-yelling-cat --top "Accusation" --bottom "Confused response"
```

## AI Meme Generation

To use AI-powered meme generation, you need an OpenAI API key:

1. Get your API key from [OpenAI Platform](https://platform.openai.com)
2. Set the environment variable:
   ```bash
   export OPENAI_API_KEY="sk-your-api-key"
   ```
3. Generate memes:
   ```bash
   python meme_generator.py --ai "A developer's face when their code works on the first try"
   ```

## OpenClaw Integration

This skill is designed to work seamlessly with OpenClaw's agent framework.

### Install as OpenClaw Skill
```bash
# Copy to OpenClaw skills directory
cp -r meme-generator-skill ~/.openclaw/skills/meme-generator

# Or symlink for development
ln -s $(pwd) ~/.openclaw/skills/meme-generator
```

### Use from OpenClaw
Once installed, you can ask your OpenClaw agent:
- "Generate a Drake meme about productivity"
- "Create a meme using the distracted boyfriend template"
- "Make an AI meme about coffee addiction"

## Template Images

The skill includes placeholder templates that are generated programmatically. For better results, you can add your own template images to the `templates/` directory:

- `drake_template.png` (600x600)
- `distracted_boyfriend_template.png` (800x450)
- `change_my_mind_template.png` (700x500)
- `galaxy_brain_template.png` (600x800)
- `woman_yelling_cat_template.png` (800x400)

## Development

### Project Structure
```
meme-generator-skill/
├── SKILL.md              # OpenClaw skill metadata
├── README.md             # This file
├── meme_generator.py     # Main generation script
├── requirements.txt      # Python dependencies
└── templates/            # Meme template images (optional)
```

### Adding New Templates

1. Add template configuration to `TEMPLATES` dict in `meme_generator.py`
2. Implement text positioning logic
3. Optionally add template image to `templates/` directory
4. Update documentation

## Requirements

- Python 3.8+
- Pillow (PIL) for image processing
- OpenAI Python library (optional, for AI memes)

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Support

For issues, questions, or suggestions:
- GitHub Issues: https://github.com/bigguybobby/meme-generator-skill/issues
- NEAR AI Marketplace: Job #5aa59a97

## Credits

Created for the NEAR AI Agent Marketplace
Built with OpenClaw framework

---

**Made with ❤️ for the meme community** 🎭

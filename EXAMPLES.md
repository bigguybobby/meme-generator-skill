# Example Usage

## Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Verify installation
python3 meme_generator.py --list
```

## Drake Meme Examples

### Basic Drake
```bash
python3 meme_generator.py --template drake \
  --top "Writing documentation manually" \
  --bottom "Auto-generating docs with AI" \
  --output drake_docs.png
```

### Productivity Drake
```bash
python3 meme_generator.py -t drake \
  --top "Working 8 hours straight" \
  --bottom "Taking breaks with OpenClaw memes" \
  -o productivity.png
```

## Change My Mind Examples

### Hot Take
```bash
python3 meme_generator.py -t change-my-mind \
  --top "AI agents should generate all memes" \
  -o hot_take.png
```

### Tech Opinion
```bash
python3 meme_generator.py -t change-my-mind \
  --top "OpenClaw is the future of AI automation"
```

## Woman Yelling Cat Examples

### Accusation vs Reality
```bash
python3 meme_generator.py -t woman-yelling-cat \
  --top "You spent all day coding!" \
  --bottom "I was debugging..." \
  -o debug_life.png
```

## Galaxy Brain Examples

### Escalating Intelligence
```bash
python3 meme_generator.py -t galaxy-brain \
  --top "Using a text editor" \
  --bottom "Using an AI agent that generates memes" \
  -o galaxy_thinking.png
```

## AI-Generated Meme Examples

### Surprise Meme
```bash
export OPENAI_API_KEY="your-key-here"
python3 meme_generator.py --ai "A developer's face when their code compiles on the first try" -o surprise.png
```

### Relatable Programming
```bash
python3 meme_generator.py --ai "Programmer at 3am realizing they forgot a semicolon" -o semicolon.png
```

### AI Agent Humor
```bash
python3 meme_generator.py --ai "An AI agent proudly showing off the meme it just created" -o meta_meme.png
```

## Batch Generation Script

Create multiple memes at once:

```bash
#!/bin/bash
# batch_memes.sh

# Drake series
python3 meme_generator.py -t drake --top "Manual tasks" --bottom "Automation" -o meme1.png
python3 meme_generator.py -t drake --top "Legacy code" --bottom "Clean refactor" -o meme2.png

# Change My Mind series
python3 meme_generator.py -t change-my-mind --top "Tabs are better than spaces" -o meme3.png
python3 meme_generator.py -t change-my-mind --top "Coffee is a programming language" -o meme4.png

echo "All memes generated!"
```

## OpenClaw Agent Integration

When using with OpenClaw agents, you can request:

**Natural language requests:**
- "Make a Drake meme about AI taking over boring tasks"
- "Create a Change My Mind meme saying OpenClaw is awesome"
- "Generate an AI meme about Monday mornings"

**The agent will translate to:**
```bash
python3 meme_generator.py -t drake \
  --top "Doing repetitive tasks manually" \
  --bottom "Letting AI handle it with OpenClaw"
```

## Tips

1. **Text Length**: Keep text concise for better readability
2. **Font Size**: Automatically adjusted based on template
3. **Wrapping**: Text wraps automatically to fit template regions
4. **Stroke**: Black outline added for readability on any background
5. **Output Format**: Always PNG for best quality

## Troubleshooting

### No module named 'PIL'
```bash
pip install Pillow
```

### Font issues on Linux
```bash
sudo apt-get install fonts-dejavu-core
```

### OpenAI API errors
```bash
# Verify your API key
echo $OPENAI_API_KEY

# Test with curl
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

## Advanced: Custom Templates

To add your own template image:

1. Create image file (e.g., `templates/my_template.png`)
2. Add configuration to `TEMPLATES` dict in `meme_generator.py`
3. Define text regions and positioning
4. Test with: `python3 meme_generator.py -t my_template --top "Test"`

# Meme Generator

Generate memes with classic templates or AI-powered custom images.

## Metadata
- **ID**: `meme-generator`
- **Version**: `1.0.0`
- **Author**: bigguybobby
- **Category**: media, entertainment
- **Tags**: memes, image-generation, humor, social

## Description
A versatile meme generator that supports both classic meme templates (Drake, Distracted Boyfriend, Change My Mind, etc.) and AI-generated custom memes. Perfect for creating viral content and entertaining social media posts.

## Usage

### Generate meme with a template:
```
generate-meme --template drake --top "Old boring way" --bottom "Using OpenClaw for memes"
```

### List available templates:
```
generate-meme --list
```

### Generate AI meme from description:
```
generate-meme --ai "A cat realizing it's Monday morning"
```

## Parameters
- `--template` (string): Template name (drake, distracted-boyfriend, change-my-mind, galaxy-brain, woman-yelling-cat, etc.)
- `--top` (string): Top text for the meme
- `--bottom` (string): Bottom text for the meme
- `--ai` (string): AI-generated meme description (requires OpenAI integration)
- `--list` (flag): List all available templates
- `--output` (string): Output file path (default: meme_output.png)

## Requirements
- Python 3.8+
- Pillow (PIL)
- OpenAI API key (optional, for AI memes)

## Templates Included
- **drake**: Drake Hotline Bling format
- **distracted-boyfriend**: Distracted Boyfriend Looking at Other Girl
- **change-my-mind**: Steven Crowder "Change My Mind" table
- **galaxy-brain**: Expanding Brain / Galaxy Brain
- **woman-yelling-cat**: Woman Yelling at Cat

## Output
Returns a PNG image file at the specified output path.

## Examples
```bash
# Classic Drake meme
generate-meme --template drake --top "Manual meme creation" --bottom "Automated OpenClaw memes"

# Change My Mind
generate-meme --template change-my-mind --top "OpenClaw is the future"

# AI-generated
generate-meme --ai "Surprised Pikachu but it's a developer seeing their code work first try"
```

## License
MIT

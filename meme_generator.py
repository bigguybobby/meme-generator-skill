#!/usr/bin/env python3
"""
OpenClaw Meme Generator Skill
Generates memes using classic templates or AI descriptions
"""

import argparse
import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Template configurations: (width, height, top_text_y, bottom_text_y, single_text_y)
TEMPLATES = {
    "drake": {
        "file": "drake_template.png",
        "width": 600,
        "height": 600,
        "top_region": (300, 0, 600, 300),  # Top right quadrant
        "bottom_region": (300, 300, 600, 600),  # Bottom right quadrant
        "description": "Drake Hotline Bling - disapproval vs approval"
    },
    "distracted-boyfriend": {
        "file": "distracted_boyfriend_template.png",
        "width": 800,
        "height": 450,
        "positions": {
            "girlfriend": (50, 50),  # Left text
            "other_woman": (400, 50),  # Center text
            "boyfriend": (650, 350)  # Right bottom text
        },
        "description": "Distracted Boyfriend looking at another girl"
    },
    "change-my-mind": {
        "file": "change_my_mind_template.png",
        "width": 700,
        "height": 500,
        "sign_region": (200, 250, 550, 350),
        "description": "Steven Crowder 'Change My Mind' table sign"
    },
    "galaxy-brain": {
        "file": "galaxy_brain_template.png",
        "width": 600,
        "height": 800,
        "levels": [
            (320, 100),   # Level 1 (small brain)
            (320, 300),   # Level 2
            (320, 500),   # Level 3
            (320, 700)    # Level 4 (galaxy brain)
        ],
        "description": "Expanding Brain / Galaxy Brain progression"
    },
    "woman-yelling-cat": {
        "file": "woman_yelling_cat_template.png",
        "width": 800,
        "height": 400,
        "left_region": (50, 300, 350, 380),   # Woman side
        "right_region": (450, 300, 750, 380),  # Cat side
        "description": "Woman Yelling at Confused Cat"
    }
}

def get_font(size=40):
    """Get a font, trying common system fonts"""
    font_options = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Windows/Fonts/arialbd.ttf",
    ]
    
    for font_path in font_options:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except:
                pass
    
    # Fallback to default
    return ImageFont.load_default()

def create_blank_template(template_name):
    """Create a blank template image with placeholder graphics"""
    config = TEMPLATES[template_name]
    width = config["width"]
    height = config["height"]
    
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    if template_name == "drake":
        # Draw Drake-style two-panel vertical split
        draw.rectangle([0, 0, 300, 300], fill='#FF6B6B', outline='black', width=3)
        draw.rectangle([0, 300, 300, 600], fill='#4ECDC4', outline='black', width=3)
        draw.rectangle([300, 0, 600, 300], fill='#FFE66D', outline='black', width=3)
        draw.rectangle([300, 300, 600, 600], fill='#95E1D3', outline='black', width=3)
        draw.text((150, 150), "👎", fill='black', font=get_font(80), anchor="mm")
        draw.text((150, 450), "👍", fill='black', font=get_font(80), anchor="mm")
        
    elif template_name == "distracted-boyfriend":
        # Three-region template
        draw.rectangle([0, 0, width, height], fill='#87CEEB', outline='black', width=3)
        draw.ellipse([20, 150, 120, 300], fill='#FF69B4', outline='black', width=2)  # Girlfriend
        draw.ellipse([350, 100, 450, 250], fill='#FF1493', outline='black', width=2)  # Other woman
        draw.ellipse([600, 200, 700, 350], fill='#4169E1', outline='black', width=2)  # Boyfriend
        draw.text((70, 360), "GF", fill='black', font=get_font(30), anchor="mm")
        draw.text((400, 280), "OTHER", fill='black', font=get_font(30), anchor="mm")
        draw.text((650, 380), "YOU", fill='black', font=get_font(30), anchor="mm")
        
    elif template_name == "change-my-mind":
        # Table with sign
        draw.rectangle([0, 0, width, height], fill='#D3D3D3', outline='black', width=3)
        draw.rectangle([150, 200, 600, 400], fill='#FFFFFF', outline='black', width=5)
        draw.text((350, 150), "🪑 CHANGE MY MIND", fill='black', font=get_font(35), anchor="mm")
        
    elif template_name == "galaxy-brain":
        # Four levels of brain expansion
        colors = ['#FFB6C1', '#FF69B4', '#FF1493', '#8B008B']
        sizes = [80, 100, 120, 140]
        for i, (x, y) in enumerate(config["levels"]):
            draw.ellipse([x-sizes[i], y-30, x+sizes[i], y+30], fill=colors[i], outline='black', width=2)
            
    elif template_name == "woman-yelling-cat":
        # Two-panel split
        draw.rectangle([0, 0, 400, height], fill='#FFF5E1', outline='black', width=3)
        draw.rectangle([400, 0, width, height], fill='#F0F8FF', outline='black', width=3)
        draw.text((200, 150), "😠👉", fill='black', font=get_font(80), anchor="mm")
        draw.text((600, 150), "😼❓", fill='black', font=get_font(80), anchor="mm")
    
    return img

def add_text_to_image(img, text, position, font_size=40, max_width=None, color='black', stroke=True):
    """Add text to image with optional wrapping and stroke"""
    draw = ImageDraw.Draw(img)
    font = get_font(font_size)
    
    if max_width:
        # Wrap text to fit width
        lines = textwrap.wrap(text, width=max_width//font_size*2)
    else:
        lines = [text]
    
    y_offset = 0
    for line in lines:
        if stroke:
            # Add black stroke for better readability
            for adj in [(0,-2), (0,2), (-2,0), (2,0), (-1,-1), (1,-1), (-1,1), (1,1)]:
                draw.text((position[0]+adj[0], position[1]+y_offset+adj[1]), line, 
                         font=font, fill='black', anchor="mm")
        
        draw.text((position[0], position[1]+y_offset), line, font=font, fill=color, anchor="mm")
        y_offset += font_size + 5
    
    return img

def generate_meme(template_name, top_text="", bottom_text="", output="meme_output.png"):
    """Generate a meme using the specified template"""
    if template_name not in TEMPLATES:
        print(f"Error: Template '{template_name}' not found.")
        print(f"Available templates: {', '.join(TEMPLATES.keys())}")
        return None
    
    config = TEMPLATES[template_name]
    template_path = Path(__file__).parent / "templates" / config["file"]
    
    # Load or create template
    if template_path.exists():
        img = Image.open(template_path)
    else:
        print(f"Template file not found, creating placeholder...")
        img = create_blank_template(template_name)
    
    # Add text based on template type
    if template_name == "drake":
        if top_text:
            add_text_to_image(img, top_text, (450, 150), font_size=35, max_width=250)
        if bottom_text:
            add_text_to_image(img, bottom_text, (450, 450), font_size=35, max_width=250)
            
    elif template_name == "change-my-mind":
        if top_text:
            add_text_to_image(img, top_text, (375, 300), font_size=30, max_width=350, color='black', stroke=False)
            
    elif template_name == "woman-yelling-cat":
        if top_text:
            add_text_to_image(img, top_text, (200, 340), font_size=30, max_width=280)
        if bottom_text:
            add_text_to_image(img, bottom_text, (600, 340), font_size=30, max_width=280)
            
    elif template_name == "galaxy-brain":
        # For galaxy brain, split text by lines for each level
        texts = [top_text, bottom_text] if bottom_text else [top_text]
        for i, text in enumerate(texts[:4]):
            if text and i < len(config["levels"]):
                x, y = config["levels"][i]
                add_text_to_image(img, text, (x+180, y), font_size=28, max_width=200)
    
    else:  # Default: top and bottom text
        if top_text:
            add_text_to_image(img, top_text, (config["width"]//2, 50), font_size=40, max_width=config["width"]-100)
        if bottom_text:
            add_text_to_image(img, bottom_text, (config["width"]//2, config["height"]-50), font_size=40, max_width=config["width"]-100)
    
    # Save output
    img.save(output)
    print(f"✅ Meme generated: {output}")
    return output

def generate_ai_meme(description, output="meme_output.png"):
    """Generate an AI meme using OpenAI (requires API key)"""
    try:
        import openai
        import requests
        from io import BytesIO
    except ImportError:
        print("Error: OpenAI library not installed. Run: pip install openai")
        return None
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        return None
    
    try:
        client = openai.OpenAI(api_key=api_key)
        
        # Generate meme-style image
        prompt = f"Create a meme-style image: {description}. Make it funny, relatable, and suitable for social media sharing."
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        
        # Download and save
        img_response = requests.get(image_url)
        img = Image.open(BytesIO(img_response.content))
        img.save(output)
        
        print(f"✅ AI meme generated: {output}")
        return output
        
    except Exception as e:
        print(f"Error generating AI meme: {e}")
        return None

def list_templates():
    """List all available meme templates"""
    print("\n📋 Available Meme Templates:\n")
    for name, config in TEMPLATES.items():
        print(f"  • {name:25} - {config['description']}")
    print()

def main():
    parser = argparse.ArgumentParser(description="OpenClaw Meme Generator")
    parser.add_argument("--template", "-t", help="Meme template name")
    parser.add_argument("--top", help="Top text")
    parser.add_argument("--bottom", help="Bottom text")
    parser.add_argument("--ai", help="AI-generated meme description")
    parser.add_argument("--list", "-l", action="store_true", help="List available templates")
    parser.add_argument("--output", "-o", default="meme_output.png", help="Output file path")
    
    args = parser.parse_args()
    
    if args.list:
        list_templates()
        return 0
    
    if args.ai:
        generate_ai_meme(args.ai, args.output)
    elif args.template:
        if not args.top and not args.bottom:
            print("Error: Please provide --top and/or --bottom text")
            return 1
        generate_meme(args.template, args.top or "", args.bottom or "", args.output)
    else:
        parser.print_help()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

# Meme Templates Directory

This directory is for storing meme template images. The meme generator will use these images if present, otherwise it will generate placeholder templates programmatically.

## Template Image Specifications

### Drake (`drake_template.png`)
- Dimensions: 600x600 pixels
- Format: PNG
- Layout: 2x2 grid (left: Drake gestures, right: text areas)

### Distracted Boyfriend (`distracted_boyfriend_template.png`)
- Dimensions: 800x450 pixels
- Format: PNG
- Layout: Boyfriend looking away from girlfriend at another woman

### Change My Mind (`change_my_mind_template.png`)
- Dimensions: 700x500 pixels
- Format: PNG
- Layout: Person sitting at table with sign

### Galaxy Brain (`galaxy_brain_template.png`)
- Dimensions: 600x800 pixels
- Format: PNG
- Layout: 4 levels of brain expansion (vertical)

### Woman Yelling at Cat (`woman_yelling_cat_template.png`)
- Dimensions: 800x400 pixels
- Format: PNG
- Layout: Split view (left: woman pointing, right: confused cat)

## Adding Your Own Templates

1. Place your template image in this directory
2. Use the naming convention: `template_name_template.png`
3. Configure in `meme_generator.py` TEMPLATES dict
4. Specify text regions and positioning

## Using Placeholder Templates

If no template image exists, the generator will create a programmatic placeholder with:
- Colored regions
- Emoji placeholders
- Layout indicators

This allows the skill to work immediately without requiring template downloads.

## Copyright Notice

If adding meme template images:
- Ensure you have rights to use the image
- Many popular meme templates are public domain or fair use
- Attribution requirements vary by source
- This skill is for educational and entertainment purposes

## Recommended Sources

- knowyourmeme.com (for meme background research)
- imgflip.com (many templates are freely available)
- Create your own original templates
- Use Creative Commons licensed images

---

**Note**: The skill works perfectly fine without any images in this directory - it generates placeholder templates automatically!

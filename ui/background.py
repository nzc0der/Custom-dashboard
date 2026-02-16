from PIL import Image, ImageDraw

def create_gradient(width, height, color1, color2):
    """Creates a vertical gradient image."""
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

if __name__ == "__main__":
    # Test generation
    img = create_gradient(1280, 800, (15, 15, 27), (30, 30, 50))
    img.save("background.png")
    print("Gradient saved to background.png")

from PIL import Image

# Load the WebP file
with Image.open('/home/yvonneg/Downloads/new_wave.webp') as img:
    # Save the image in PNG format
    img.save('text_dall6.png', 'PNG')

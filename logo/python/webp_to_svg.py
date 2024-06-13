from PIL import Image
import svgwrite

def webp_to_svg(webp_path, svg_path):
    # Open the WebP image file
    with Image.open(webp_path) as img:
        # Convert image to RGBA (if not already in that mode)
        img = img.convert('RGBA')
        
        # Create a new SVG drawing
        dwg = svgwrite.Drawing(svg_path, profile='tiny', size=(img.width, img.height))
        
        # Create a group for storing image data
        image_group = svgwrite.container.Group(id='image_group')
        dwg.add(image_group)
        
        # Process each pixel in the image
        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = img.getpixel((x, y))
                # Set the pixel as a rectangle in SVG (if it's not fully transparent)
                if a != 0:
                    color = svgwrite.rgb(r, g, b, 'RGB')
                    image_group.add(dwg.rect(insert=(x, y), size=(1, 1), fill=color, stroke=color))
        
        # Save the drawing
        dwg.save()

# Example usage
webp_to_svg('/home/yvonneg/Downloads/text_dall1.webp', 'text_dall1.svg')

from PIL import Image

def make_transparent(input_image_path, output_image_path, target_color, tolerance=60):
    # Open an image file
    with Image.open(input_image_path) as img:
        # Convert the image to RGBA (if not already in this mode)
        img = img.convert("RGBA")
        
        # Get data for all pixels
        data = img.getdata()
        
        # Create a new data array to store modified pixel data
        new_data = []
        
        # Define the range for color comparison
        r_min, r_max = max(target_color[0] - tolerance, 0), min(target_color[0] + tolerance, 255)
        g_min, g_max = max(target_color[1] - tolerance, 0), min(target_color[1] + tolerance, 255)
        b_min, b_max = max(target_color[2] - tolerance, 0), min(target_color[2] + tolerance, 255)
        
        # Process each pixel
        for item in data:
            # Change pixels that are close to the target color to transparent
            if r_min <= item[0] <= r_max and g_min <= item[1] <= g_max and b_min <= item[2] <= b_max:
#                new_data.append((255, 255, 255, 0))  # This makes the pixel fully transparent
#                new_data.append((27,184,196))#blue
                new_data.append((255,255,255))
            else:
                new_data.append(item)
        
        # Update the image data
        img.putdata(new_data)
        
        # Save the new image
        img.save(output_image_path, "PNG")

# Usage example
make_transparent("wave_logo_blue.png", "wave_logo_white.png", (22,94,83), tolerance=100)
#make_transparent("wave_logo.png", "wave_logo_blue.png", (217,247,232), tolerance=100)

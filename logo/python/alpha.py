from PIL import Image


with Image.open("/home/yvonneg/logo_norkyst/wave_logo.png") as img:
    # Convert the image to RGBA (if not already in this mode)
    img = img.convert("RGBA")

    # Get data of the image
    data = img.getdata()

    # List to hold new image data
    new_data = []
    
    # Threshold for the alpha value
    threshold = 240 #240

    # Go through each item in image data
    for item in data:
        # change all white (also shades of whites)
        # pixels to transparent
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    
    # Update image data
    img.putdata(new_data)
    # Save the new image
    img.save("/home/yvonneg/logo_norkyst/wave_logo_transparent.png")


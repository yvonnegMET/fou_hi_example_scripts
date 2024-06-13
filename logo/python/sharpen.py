from PIL import Image, ImageEnhance

# Load the image
image = Image.open("inbeded.png")

# Enhance the sharpness
enhancer = ImageEnhance.Sharpness(image)
sharpened_image = enhancer.enhance(2)  # Increase the factor to increase sharpness

# Save the sharpened image
sharpened_image.save("inbeded_sharpened.png")

# Optionally, display the sharpened image
sharpened_image.show()

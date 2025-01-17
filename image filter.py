from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import numpy as np
import cv2

def apply_grayscale(image):
    """Convert image to grayscale."""
    return image.convert("L")

def apply_gaussian_blur(image):
    """Apply Gaussian Blur to the image."""
    return image.filter(ImageFilter.GaussianBlur(radius=5))

def apply_edge_detection(image):
    """Apply edge detection filter to the image."""
    image_cv = np.array(image)
    edges = cv2.Canny(image_cv, 100, 200)
    return Image.fromarray(edges)

def apply_sepia(image):
    """Apply sepia filter to the image."""
    width, height = image.size
    pixels = image.load()  # Create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = image.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            # Apply the sepia effect
            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb)

    return image

def adjust_brightness_contrast(image, brightness=1.0, contrast=1.0):
    """Adjust brightness and contrast of the image."""
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)
    
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    return image

def sharpen_image(image):
    """Apply sharpening to the image."""
    return image.filter(ImageFilter.SHARPEN)

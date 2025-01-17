def compress_image_lossy(image, quality=85):
    """Compress image using lossy compression (JPEG)."""
    output = "compressed_image.jpg"
    image.save(output, "JPEG", quality=quality)
    return output

  
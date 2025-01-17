import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
from PIL import Image, ImageFilter

# ...existing code...

def apply_grayscale(image):
    """Convert image to grayscale."""
    return image.convert("L")

def apply_gaussian_blur(image):
    """Apply Gaussian blur to the image."""
    return image.filter(ImageFilter.GaussianBlur(5))

def apply_sepia(image):
    """Apply sepia effect to the image."""
    width, height = image.size
    pixels = image.load()  # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = image.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb)

    return image

class ImageEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Filters and Compression")

        self.image_path = None
        self.image = None

        self.create_widgets()

    def create_widgets(self):
        # Button for loading an image
        self.load_button = tk.Button(self.master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        # Button for applying grayscale
        self.grayscale_button = tk.Button(self.master, text="Grayscale", command=self.apply_grayscale)
        self.grayscale_button.pack()

        # Button for applying Gaussian Blur
        self.blur_button = tk.Button(self.master, text="Gaussian Blur", command=self.apply_gaussian_blur)
        self.blur_button.pack()

        # Button for applying sepia effect
        self.sepia_button = tk.Button(self.master, text="Sepia Effect", command=self.apply_sepia)
        self.sepia_button.pack()

        # Button for saving the image
        self.save_button = tk.Button(self.master, text="Save Image", command=self.save_image)
        self.save_button.pack()

    def load_image(self):
        """Load an image."""
        self.image_path = filedialog.askopenfilename(title="Select an image")
        self.image = Image.open(self.image_path)
        messagebox.showinfo("Image Loaded", f"Loaded image from {self.image_path}")

    def apply_grayscale(self):
        """Apply grayscale effect."""
        if self.image:
            self.image = apply_grayscale(self.image)
            self.update_image_display()

    def apply_gaussian_blur(self):
        """Apply Gaussian blur."""
        if self.image:
            self.image = apply_gaussian_blur(self.image)
            self.update_image_display()

    def apply_sepia(self):
        """Apply sepia effect."""
        if self.image:
            self.image = apply_sepia(self.image)
            self.update_image_display()

    def save_image(self):
        """Save the image."""
        if self.image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            self.image.save(save_path)
            messagebox.showinfo("Image Saved", f"Image saved to {save_path}")

    def update_image_display(self):
        """Update the display of the image in the GUI."""
        self.tk_image = ImageTk.PhotoImage(self.image)
        label = tk.Label(self.master, image=self.tk_image)
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()

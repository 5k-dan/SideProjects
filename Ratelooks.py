import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import random


class FaceAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Attractiveness Analyzer")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.rate_button = tk.Button(root, text="Rate Attractiveness", command=self.rate_attractiveness)
        self.rate_button.pack()

        self.rating_label = tk.Label(root, text="")
        self.rating_label.pack()

        self.image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image(self.image)
            # Clear previous rating when uploading a new image
            self.rating_label.config(text="")

    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.image_label.config(image=image)
        self.image_label.image = image

    def rate_attractiveness(self):
        if self.image is None:
            return

        attractiveness_rating = random.randint(1, 10)
        attractiveness_category = self.get_attractiveness_category(attractiveness_rating)

        self.rating_label.config(text=f"Attractiveness Rating: {attractiveness_rating} - {attractiveness_category}")

    def get_attractiveness_category(self, rating):
        if rating <= 4:
            return "CHOPPED"
        elif rating <= 7:
            return "MID"
        else:
            return "BAE"


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceAnalyzerApp(root)
    root.mainloop()

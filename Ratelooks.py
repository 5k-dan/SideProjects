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
            self.resize_image()
            self.display_image(self.image)
            # Clear previous rating when uploading a new image
            self.rating_label.config(text="")

    def resize_image(self):
        max_width = 800
        max_height = 600

        height, width, _ = self.image.shape
        if width > max_width or height > max_height:
            scale = min(max_width / width, max_height / height)
            self.image = cv2.resize(self.image, (int(width * scale), int(height * scale)))

    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.image_label.config(image=image)
        self.image_label.image = image

    def calculate_attractiveness(self):
        # Load pre-trained face detector
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Convert image to grayscale for face detection
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) == 0:
            return None  # No face detected

        # For simplicity, let's assume the first detected face is the only face
        face = faces[0]
        x, y, w, h = face

        # Normalize width and height
        normalized_width = w / self.image.shape[1]
        normalized_height = h / self.image.shape[0]

        # Example: Calculate attractiveness based on normalized face width and height
        attractiveness_score = max(min((normalized_width / normalized_height) * 5, 10), 1)
        return attractiveness_score

    def rate_attractiveness(self):
        if self.image is None:
            return

        attractiveness_score = self.calculate_attractiveness()

        if attractiveness_score is not None:
            attractiveness_category = self.get_attractiveness_category(attractiveness_score)
            self.rating_label.config(
                text=f"Attractiveness Rating: {attractiveness_score:.2f} - {attractiveness_category}")
        else:
            self.rating_label.config(text="No face detected.")

    def get_attractiveness_category(self, score):
        if score <= 4.99:
            return "CHOPPED"
        elif score <= 6.99:
            return "MID"
        else:
            return "BAE"


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceAnalyzerApp(root)
    root.mainloop()


import tkinter as tk

current_label = None  # Variable to keep track of the current label
image_sequence = []  # List to store the images
current_index = 0

def on_smash_click():
    global current_label, current_index
    destroy_current_label()
    current_index = (current_index + 1) % len(image_sequence)
    current_label = tk.Label(root, image=image_sequence[current_index])
    current_label.place(x=150, y=50)

def on_pass_click():
    global current_label, current_index
    destroy_current_label()
    current_index = (current_index + 1) % len(image_sequence)
    current_label = tk.Label(root, image=image_sequence[current_index])
    current_label.place(x=150, y=50)

def destroy_current_label():
    # Destroy the current label
    if current_label is not None:
        current_label.destroy()

# Create the main window
root = tk.Tk()
root.title("Smash or Pass?")
root.geometry("500x450")

# Load people images
dan_image = tk.PhotoImage(file="dan.png")
dan_image = dan_image.subsample(6, 5)  # Set the factors to make it very tiny because its big
duke_image = tk.PhotoImage(file="duke.png")
duke_image = duke_image.subsample(1, 1)
glorilla_image = tk.PhotoImage(file="glorilla.png")
sexxyred_image = tk.PhotoImage(file="sexxyred.png")
sza_image = tk.PhotoImage(file="sza.png")
beyonce_image = tk.PhotoImage(file="beyonce.png")

# Populate the image_sequence list
image_sequence = [dan_image, sza_image, glorilla_image, sexxyred_image, duke_image, beyonce_image]

# Show Smash or Pass buttons
smash_button = tk.Button(root, text="Smash", width=10, height=2, command=on_smash_click)
smash_button.place(x=160, y=355)

pass_button = tk.Button(root, text="Pass", width=10, height=2, command=on_pass_click)
pass_button.place(x=260, y=355)

# Show the initial image (Dan)
current_label = tk.Label(root, image=image_sequence[0])
current_label.place(x=150, y=50)

root.mainloop()

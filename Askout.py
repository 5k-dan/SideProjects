import tkinter as tk
import random

def on_yes_click():
    # Change the bunny image here
    bunny_label.config(image=yes_image)

    # Remove the "Yes" and "No" buttons
    yes_button.destroy()
    no_button.destroy()

def on_no_click():
    move_no_button()

def move_no_button():
    # Move the "No" button to a random position
    new_x = random.randint(50, 400)
    new_y = random.randint(50, 300)
    no_button.place(x=new_x, y=new_y)

# Create the main window
root = tk.Tk()
root.title("Will You Go Out With Me?")
root.geometry("500x450")  # Set the initial size of the window

# Load bunny images
bunny_image = tk.PhotoImage(file="bunnyhap.png")
yes_image = tk.PhotoImage(file="bunnyind.png")

# Create a label for the bunny image
bunny_label = tk.Label(root, image=bunny_image)
bunny_label.pack()

# Create a text box
text_box = tk.Entry(root, width=22)  # Set the width of the text box
text_box.insert(tk.END, "Will you go out with me?")
text_box.pack()

# Create "Yes" button
yes_button = tk.Button(root, text="Yes", command=on_yes_click)
yes_button.pack()

# Create "No" button
no_button = tk.Button(root, text="No", command=on_no_click)
no_button.place(x=235, y=300)  # Adjusted position

# Run the Tkinter event loop
root.mainloop()

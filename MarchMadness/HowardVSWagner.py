import csv
import pandas as pd
from sklearn.linear_model import LogisticRegression
import tkinter as tk

# Step 1: Create the CSV file with updated data including star player stats
data = [
    ["Team Name", "Win-Loss Record", "Points Per Game", "Points Allowed Per Game", "Field Goal Percentage", "Star PPG", "Star APG", "Star RPG"],
    ["Howard", 0.5729, 75.1, 74.4, 45.1, 16.6, 1.7, 7.6],
    ["Wagner", 0.51, 63.5, 62.1, 39.2, 14.6, 3.4, 5.7]
]

filename = "team_stats.csv"

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

# Step 2: Load and process the updated dataset
data = pd.read_csv('team_stats.csv')

# Display the first few rows to check the updated structure
print(data.head())

# Check for missing values in the updated dataset
print(data.isnull().sum())

# Select features, now including the star player stats
features = data.drop('Team Name', axis=1)

# Step 3: Train the model with the updated features
model = LogisticRegression()

# Assuming Howard wins (1) and Wagner loses (0) for demonstration
model.fit(features, [1, 0])

# Predict the outcome with the updated model
predicted_outcome = model.predict(features)

# Get the prediction probabilities
prediction_probabilities = model.predict_proba(features)

# Assuming the first row in your dataset is Howard and the second row is Wagner
howard_win_probability = prediction_probabilities[0, 1] * 100  # Howard's win probability
wagner_win_probability = 100 - howard_win_probability  # Wagner's win probability

# Display the updated prediction with probabilities in the console
if predicted_outcome[0] == 1:
    console_message = f"Howard has a {howard_win_probability:.2f}% chance of winning! 💙❤️"
    bg_color = "#0000FF"  # Blue
    text_color = "#FF0000"  # Red
else:
    console_message = f"Wagner has a {wagner_win_probability:.2f}% chance of winning! 💚🤍"
    bg_color = "#008000"  # Green
    text_color = "#FFFFFF"  # White
print(console_message)

# Step 4: Add a Tkinter GUI to display the prediction with colors
def show_prediction():
    popup = tk.Toplevel()
    popup.title("Prediction Result")
    message_label = tk.Label(popup, text=console_message, font=("Helvetica", 16), bg=bg_color, fg=text_color)
    message_label.pack(padx=20, pady=20)
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=20)

root = tk.Tk()
root.title("Game Prediction")

# Button to display the prediction
predict_button = tk.Button(root, text="Show Prediction", command=show_prediction)
predict_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()

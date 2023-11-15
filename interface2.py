import tkinter as tk
from subprocess import run
from PIL import Image, ImageTk

def run_game(difficulty):
    if difficulty == "easy":
        run(["python", "Easy.py"])
    elif difficulty == "medium":
        run(["python", "Medium.py"])
        pass
    elif difficulty == "hard":
        run(["python", "Hard.py"])

def open_regles():
    window.destroy()
    run(["python", "interface1.py"])

def quit_game():
    window.destroy()

def on_button_click(difficulty):
    
    run_game(difficulty)

# Create the main window
window = tk.Tk()
window.title("Checkers Game")

# Set the window to full screen
window.attributes("-fullscreen", True)

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

bg_image_path = "assets\\bg.jpg"
bg_image = Image.open(bg_image_path)

# Resize the image to match the screen size using ANTIALIAS filter
bg_image = bg_image.resize((screen_width, screen_height))

bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Define a custom font
custom_font = ("Gagalin", 25, "italic bold")

# Set the background color for the buttons to dark brown
button_color = "#E6C8B4"  # Dark brown color code

# Set the text color for the buttons to white
text_color = "black"

# Add buttons for each difficulty level on top of the background
button_easy = tk.Button(window, text="Facile", command=lambda: on_button_click("easy"), font=custom_font, bg=button_color, fg=text_color, bd=0, highlightthickness=0)
button_easy.place(x=620, y=220)

button_medium = tk.Button(window, text="Moyen", command=lambda: on_button_click("medium"), font=custom_font, bg=button_color, fg=text_color, bd=0, highlightthickness=0)
button_medium.place(x=620, y=350)

button_hard = tk.Button(window, text="Difficile", command=lambda: on_button_click("hard"), font=custom_font, bg=button_color, fg=text_color, bd=0, highlightthickness=0)
button_hard.place(x=620, y=475)

# Add "Regles" button
button_regles = tk.Button(window, text="Regles", command=open_regles, font=custom_font, bg=button_color, fg=text_color, bd=0, highlightthickness=0)
button_regles.place(x=1120, y=690)

# Add "Quitter" button
button_quitter = tk.Button(window, text="Quitter", command=quit_game, font=custom_font, bg=button_color, fg=text_color, bd=0, highlightthickness=0)
button_quitter.place(x=120, y=690)

# Start the main event loop
window.mainloop()

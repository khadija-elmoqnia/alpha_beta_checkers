import tkinter as tk
from PIL import Image, ImageTk
from subprocess import run


def back_to_main():
    window.destroy()
    run(["python", "interface2.py"])

# Créer la fenêtre des règles
window = tk.Tk()
window.title("Règles du Jeu")

# Mettre la fenêtre en mode plein écran
window.attributes("-fullscreen", True)
window.geometry("1366x768")
# Définir la taille de la fenêtre
window_width = 1366
window_height = 768

# Centrer la fenêtre sur l'écran
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Ajouter l'image de fond
bg_image_path = "assets/regle.jpg"  # Assurez-vous que le fichier regle.jpg est dans le même répertoire que interface1.py
bg_image = Image.open(bg_image_path)
# Resize the image to match the screen size using ANTIALIAS filter
bg_image = bg_image.resize((screen_width, screen_height))

bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)


# Définir la police de caractères
custom_font = ("Gagalin", 25, "italic bold")

# Couleur des boutons
button_color = "#E6C8B4"  # Code couleur 
text_color = "black"  # Couleur du texte

# Ajouter le bouton "ALLER "
button_ALLER  = tk.Button(window, text="ALLER ", command=back_to_main, font=custom_font, bg=button_color, fg=text_color, bd=0, highlightthickness=0)
button_ALLER .place(x=70, y=690)

# Lancer la boucle principale
window.mainloop()

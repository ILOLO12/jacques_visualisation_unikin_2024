import tkinter as tk
from tkinter import messagebox, font
import random

class PuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle Game")
        self.root.geometry("260x320")
        
        self.seconds = 0
        self.grid_size = 5
        self.liste_nombre = [i for i in range(self.grid_size ** 2)]
        random.shuffle(self.liste_nombre)

        self.buttons = {}  # Dictionnaire pour garder les boutons par position
        self.bold_font = font.Font(weight="bold")

        self.timer_button = tk.Button(self.root, text="0 Sec", width=8, height=2,
                                      bg="blue", fg="white", font=self.bold_font)
        self.timer_button.place(x=90, y=265)

        self.affichage()
        self.root.after(1000, self.update_timer)

    def est_triee(self):
        # Vérifie si la liste est triée (0 en dernière position)
        return self.liste_nombre[:-1] == list(range(1, self.grid_size ** 2)) and self.liste_nombre[-1] == 0

    def update_timer(self):
        self.seconds += 1
        self.timer_button.config(text=f"{self.seconds} Sec")
        self.root.after(1000, self.update_timer)

    def on_button_click(self, index):
        zero_index = self.liste_nombre.index(0)

        # Déplacement si index adjacent au 0 (haut, bas, gauche, droite)
        if index == zero_index - 1 and index % self.grid_size != self.grid_size - 1 or \
           index == zero_index + 1 and zero_index % self.grid_size != self.grid_size - 1 or \
           index == zero_index - self.grid_size or \
           index == zero_index + self.grid_size:
            self.liste_nombre[zero_index], self.liste_nombre[index] = self.liste_nombre[index], 0
            self.affichage()

            if self.est_triee():
                messagebox.showinfo("Victoire", f"Vous avez gagné en {self.seconds} secondes !")
                random.shuffle(self.liste_nombre)
                self.seconds = 0
                self.affichage()

    def affichage(self):
        # Supprimer les anciens boutons
        for btn in self.buttons.values():
            btn.destroy()
        self.buttons.clear()

        for idx, val in enumerate(self.liste_nombre):
            row, col = divmod(idx, self.grid_size)
            bg_color = "blue" if val == 0 else "white"
            fg_color = "blue" if val != 0 else "blue"
            text = "" if val == 0 else str(val)

            btn = tk.Button(self.root, text=text, width=4, height=2,
                            command=lambda i=idx: self.on_button_click(i),
                            bg=bg_color, fg=fg_color, font=self.bold_font)
            btn.place(x=col * 50, y=row * 50)
            self.buttons[idx] = btn


if __name__ == "__main__":
    root = tk.Tk()
    game = PuzzleGame(root)
    root.mainloop()

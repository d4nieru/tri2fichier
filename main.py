import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileSorter:
    def __init__(self, master):
        self.master = master
        master.title("Trieur de fichiers")

        # Agrandir la fenêtre
        master.geometry("400x150")

        self.label = tk.Label(master, text="Sélectionnez le répertoire à trier:")
        self.label.pack()

        self.directory = tk.StringVar()
        self.directory.set(os.getcwd())

        self.directory_entry = tk.Entry(master, textvariable=self.directory)
        self.directory_entry.pack()

        self.browse_button = tk.Button(master, text="Parcourir...", command=self.select_directory)
        self.browse_button.pack()

        self.sort_button = tk.Button(master, text="Trier", command=self.sort_files_with_confirmation)
        self.sort_button.pack()

    def select_directory(self):
        self.directory.set(filedialog.askdirectory())

    def sort_files(self):
        directory = self.directory.get()

        # Vérifier si le répertoire contient le fichier main.py
        if "main.py" in os.listdir(directory):
            messagebox.showerror("Erreur", "Le répertoire sélectionné contient le fichier main.py.")
            return

        # Vérifier si le répertoire ne contient pas de fichiers à trier
        if not any(os.path.isfile(os.path.join(directory, filename)) for filename in os.listdir(directory)):
            messagebox.showerror("Erreur", "Le répertoire sélectionné ne contient pas de fichiers à trier.")
            return

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            if os.path.isfile(filepath):
                extension = os.path.splitext(filename)[1]

                if not os.path.exists(os.path.join(directory, extension[1:])):
                    os.makedirs(os.path.join(directory, extension[1:]))

                shutil.move(filepath, os.path.join(directory, extension[1:], filename))

        tk.messagebox.showinfo("Terminé", "Les fichiers ont été triés avec succès !")

    def sort_files_with_confirmation(self):
        if messagebox.askyesno("Confirmation", "Êtes-vous sûr(e) de vouloir trier les fichiers ?"):
            self.sort_files()

root = tk.Tk()
my_gui = FileSorter(root)
root.mainloop()
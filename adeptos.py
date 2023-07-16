import tkinter as tk
from PIL import Image, ImageTk

def create_gui():
    root = tk.Tk()
    root.title("Estádio com Adeptos")

    # Carregar a imagem dos adeptos
    image = Image.open("adeptos_imagem.jpg")  # Insira o caminho da imagem dos adeptos
    photo = ImageTk.PhotoImage(image)

    # Criar um rótulo para exibir a imagem
    label = tk.Label(root, image=photo)
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()

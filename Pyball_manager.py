#Pyball_manager \o/

#AndreiaMa
#BitZeus
#pfragoso77

#Ficheiro `app.py`:
import tkinter as tk
import random

class SimuladorFutebol(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Simulador de Equipa")
        self.equipa = {"nome": "Minha Equipa", "jogadores": [], "saldo": 1000}
        tk.Label(self, text=self.equipa["nome"]).pack()
        tk.Label(self, text=f"Saldo: {self.equipa['saldo']}").pack()
        tk.Button(self, text="Simular Jogo", command=self.simular_jogo).pack()
    def simular_jogo(self):
        resultado = random.choice(['Vitória', 'Derrota', 'Empate'])
        tk.Label(self, text=f"Resultado do jogo: {resultado}").pack()
    def criar_equipe():
        nome_equipe = entry_nome.get()
    # Salvar o nome da equipe no banco de dados ou em uma variável global para uso posterior
        print("Equipe criada: ", nome_equipe)
    # Criar a janela principal
    window = tk.Tk()

# Criar um rótulo e um campo de entrada para o nome da equipe
    label_nome = tk.Label(window, text="Nome da Equipe:")
    label_nome.pack()

    entry_nome = tk.Entry(window)
    entry_nome.pack()

# Criar um botão para criar a equipe
    btn_criar_equipe = tk.Button(window, text="Criar Equipe", command=criar_equipe)
    btn_criar_equipe.pack()

# Iniciar o loop principal da janela
    window.mainloop()


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Inicialização de jogo")
    window.geometry("500x300")

    label_nome = tk.Label(window, text="Nome da Equipe:")
    label_nome.pack()

    entry_nome = tk.Entry(window)
    entry_nome.pack()

    label_nome_treinador = tk.Label(window, text="O teu nome:")
    label_nome_treinador.pack()
    entry_nome_treinador = tk.Entry(window)
    entry_nome_treinador.pack()

    btn_criar_equipe = tk.Button(window, text="Criar Equipe", command=criar_equipe)
    btn_criar_equipe.pack()

    label_nome = tk.Label(window, text="Equipamento:")
    label_nome.place(x=70, y=120)
    radio_var = tk.StringVar(value="op1")
    #image_path = "camisa_verm.jpg"
    logo = tk.PhotoImage(file="camisa_verm.gif")
    tk.Label(window, image=logo).place(x=70, y=150)
    logo2 = tk.PhotoImage(file="camisa_azul.gif")
    tk.Label(window, image=logo2).place(x=210, y=150)
    logo3 = tk.PhotoImage(file="camisa_verde.gif")
    tk.Label(window, image=logo3).place(x=350, y=150)
    radio_1 = tk.Radiobutton(window, text="Opção 1", variable=radio_var, value="op1")
    radio_1.place(x=70, y=240)
    radio_2 = tk.Radiobutton(window, text="Opção 2", variable=radio_var, value="op2")
    radio_2.place(x=215, y=240)
    radio_3 = tk.Radiobutton(window, text="Opção 3", variable=radio_var, value="op3")
    radio_3.place(x=360, y=240)

    window.mainloop()
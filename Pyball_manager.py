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
    app = SimuladorFutebol()
    app.mainloop()       

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
if __name__ == '__main__':
    app = SimuladorFutebol()
    app.mainloop()       

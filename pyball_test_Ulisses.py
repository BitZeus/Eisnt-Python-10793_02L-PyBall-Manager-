#Pyball_manager \o/

#AndreiaMa
#BitZeus
#pfragoso77

#Ficheiro `app.py`:
import tkinter as tk
from tkinter import messagebox
import random

class SimuladorFutebol(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.jogo=0
        self.equipas=["Metallica", "Iron maiden", "Megadeth", "AC/DC"]
        #self.lista_jogadores=["um","dois","tres","quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze"]
        self.jogador = {}
        self.mercado_jogadores = {}
        
        self.formations = {
            "4-4-2": ["GR", "DD", "CD1", "CD2", "DE", "MD1", "MC1", "MC2", "ME", "AC1", "AC2"],
            "4-3-3": ["GR", "DD", "CD1", "CD2", "DE", "MC1", "MC2", "MC3", "AC1", "AC2", "AC3"],
            "3-5-2": ["GR", "CD1", "CD2", "CD3", "MD1", "MD2", "MC1", "MC2", "ME", "AC1", "AC2"],
            # Adicione mais formações aqui se desejar
            }
        
        self.players = {
            "GR": ["Thibaut Courtois", "Ederson", "Jan Oblak"],
            "DD": ["Trent Alexander-Arnold", "Kyle Walker", "Reece James"],
            "CD1": ["Virgil Van Dijk", "Marquinhos", "Ruben Dias"],
            "CD2": ["Sergio Ramos", "Kalidou Koulibaly", "Giorgio Chiellini"],
            "DE": ["João Cancelo", "Jordi Alba", "Alphonso Davies"],
            "MD1": ["Marco Verratti", "Marco Reus", "Bernardo Silva"],
            "MC1": ["Kevin De Bruyne", "Luka Modrić", "Casemiro"],
            "MC2": ["Frenkie de Jong", "Paul Pogba", "Saul Niguez"],
            "ME": ["Bruno Fernandes", "Sergej Milinković-Savić", "Memphis Depay"],
            "AC1": ["Cristiano Ronaldo", "Lionel Messi", "Robert Lewandowski"],
            "AC2": ["Erling Haaland", "Harry Kane", "Romelu Lukaku"],
            "AC3": ["Neymar Jr.", "Mohamed Salah", "Kylian Mbappé"],
                }
        
        for i in range(12):
            jogador = random.choice(self.players["AC1"])
            valor = random.choice([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])
            self.jogador[jogador] = valor
        print(self.jogador)
        for i in range (20):
            jogador = f"jogador_mercado{i}"
            valor = random.choice([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])
            self.mercado_jogadores[jogador] = valor

    
        self.historico={}
        
        self.title("Simulador de Equipa")
        
        self.logo = tk.PhotoImage(file="adeptos_imagem.jpg")

        tk.Label(self, image=self.logo).pack(side="right")
        
        label_nome = tk.Label(self, text="Nome da Equipe:")
        label_nome.pack()
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()
               
               
        # Criar um botão para criar a equipe
        btn_criar_equipe = tk.Button(self, text="Criar Equipe", command=self.criar_equipe)
        btn_criar_equipe.pack()
        
        
        
        tk.Button(self, text="Simular Jogo", command=self.simular_jogo).pack()
                
     
                      
        
    def simular_jogo(self):
        self.jogo+=1
        equipa_adversaria= random.choice(self.equipas)
        confronto=f"{self.nome_equipe} vs {equipa_adversaria}"
        tk.Label(self, text=f"{self.nome_equipe} vs {equipa_adversaria}").pack()
        resultado = random.choice(['Vitória', 'Derrota', 'Empate'])
        #tk.Label(self, text=f"Resultado do jogo nº {self.jogo}: {resultado}").pack()
        messagebox.showinfo("Resultado: ", f"{self.nome_equipe} vs {equipa_adversaria}:\n\n{resultado}")
        self.historico[confronto]= resultado
        print(self.historico)
        
    def criar_equipe(self):
        self.nome_equipe = self.entry_nome.get()
        print("Equipe criada: ", self.nome_equipe)
        
        
        self.equipa = {"nome": self.nome_equipe, "jogadores": [], "saldo": 1000}
        tk.Label(self, text=self.equipa["nome"]).pack()
        tk.Label(self, text=f"Saldo: {self.equipa['saldo']}").pack()
        tk.Button(self, text="Ver jogadores", command=self.ver_jogadores).pack()
        tk.Button(self, text="Ver mercado", command=self.comprar_jogador).pack()
        
        
    def ver_jogadores(self):
        nomes_jogadores = "\n".join(self.jogador.keys())
        messagebox.showinfo("Nomes dos Jogadores", nomes_jogadores)
        
    
    def comprar_jogador(self):
        nomes_jogadores = "\n".join(self.mercado_jogadores.keys())
        messagebox.showinfo("Nomes dos Jogadores", nomes_jogadores)
        
        
        #for jogador in self.mercado_jogadores:
            #count+=1
            #listbox.insert(count, jogador)

        #listbox.pack()
        
        
           
        
        
    class Equipa():
        def __init__(self, nome_equipa, jogadores, treinador):
            self.nome_equipa = nome_equipa
            self.jogadores = jogadores
            self.treinador = treinador
            
       
    
      
        
        
    



if __name__ == '__main__':
    app = SimuladorFutebol()
    app.mainloop() 
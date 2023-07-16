#Pyball_manager \o/

#AndreiaMa
#BitZeus
#pfragoso77

#Ficheiro `app.py`:
import tkinter as tk
import random

class SimuladorFutebol(tk.Tk):
    def __init__(self, nome_minha_equipa, treinador):
        super().__init__()
        self.title("Pyball Football Manager")
        self.geometry("500x300")

        self.lista_nomes_equipas = ["Diamante", "Esmeralda", "Rubi", "Safira", "Água-marinha", "Topázio", "Opala", "Ametista", "Turmalina", "Jade"]
        self.dic_equipas_jogadores = {}
        self.dic_jogadores={}
        self.historico={}
        self.jogo=0

        # Exemplo de uso
        self.lista_jogadores = self.gerar_lista_jogadores()
        self.lista_dic_jogadores = self.criar_lista_jogadores(self.lista_jogadores)

        for i in range(10):
            if i == 9:
                jogadores = self.lista_jogadores[i*25: (i+1)*25]
                self.dic_equipas_jogadores[nome_minha_equipa] = jogadores
            else:
                nome_equipa = self.lista_nomes_equipas[i]
                jogadores = self.lista_jogadores[i*25: (i+1)*25]
                self.dic_equipas_jogadores[nome_equipa] = jogadores

        self.minha_equipa = Equipa(nome_minha_equipa, self.dic_equipas_jogadores[nome_minha_equipa], 1000, treinador)

        self.label_nome_equipa = tk.Label(self, text=self.minha_equipa.nome)
        self.label_nome_equipa.place(x=20, y=20)

        self.label_saldo = tk.Label(self, text=f"Saldo: {self.minha_equipa.saldo}")
        self.label_saldo.place(x=20, y=40)

        self.label_treinador = tk.Label(self, text=f"Treinador: {self.minha_equipa.treinador}")
        self.label_treinador.place(x=20, y=60)

        self.botao_ver_minha_equipa = tk.Button(self, text="Ver Minha Equipa", command=self.ver_jogadores_minha_equipa)
        self.botao_ver_minha_equipa.place(x=20, y=100)

        self.label_proximo_jogo = tk.Label(self, text="")
        self.label_proximo_jogo.place(x=180, y=200)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.place(x=180, y=220)

        self.botao_simular = tk.Button(self, text="Próximo Jogo", command=self.proximo_jogo)
        self.botao_simular.place(x=220, y=250)
        
        self.classificacao = {}  # Dicionário para armazenar a classificação das equipas

    def gerar_lista_jogadores(self):
        nomes_proprios = [
            "João", "Maria", "Pedro", "Ana", "Carlos", "Mariana", "Rafael", "Julia",
            "Gustavo", "Camila", "Luiz", "Isabella", "Fernando", "Laura", "Lucas"
        ]

        apelidos = [
            "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Almeida",
            "Ferreira", "Pereira", "Costa", "Gomes", "Martins", "Ribeiro",
            "Carvalho", "Cavalcanti", "Lima"
        ]

        celebridades = [
    "Brad Pitt",
    "Angelina Jolie",
    "Leonardo DiCaprio",
    "Jennifer Aniston",
    "Tom Hanks",
    "Meryl Streep",
    "Robert Downey Jr.",
    "Scarlett Johansson",
    "Johnny Depp",
    "Natalie Portman",
    "Dwayne Johnson",
    "Emma Stone",
    "Ryan Reynolds",
    "Jennifer Lawrence",
    "Will Smith",
    "Charlize Theron",
    "Chris Hemsworth",
    "Gal Gadot",
    "Hugh Jackman",
    "Cate Blanchett",
    "Chris Evans",
    "Margot Robbie",
    "Keanu Reeves",
    "Anne Hathaway",
    "George Clooney",
    "Sandra Bullock",
    "Matt Damon",
    "Kate Winslet",
    "Mark Wahlberg",
    "Julia Roberts",
    "Chris Pratt",
    "Halle Berry",
    "Christian Bale",
    "Amy Adams",
    "Idris Elba",
    "Saoirse Ronan",
    "Daniel Craig",
    "Emma Watson",
    "Ben Affleck",
    "Zoe Saldana",
    "Tom Cruise",
    "Viola Davis",
    "Michael B. Jordan",
    "Kristen Stewart",
    "Samuel L. Jackson",
    "Amanda Seyfried",
    "Robert Pattinson",
    "Reese Witherspoon",
    "Joaquin Phoenix",
    "Gwyneth Paltrow",
    "Nicole Kidman",
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Neymar Jr.",
    "Luka Modric",
    "Virgil van Dijk",
    "Kylian Mbappé",
    "Mohamed Salah",
    "Sergio Ramos",
    "Harry Kane",
    "Antoine Griezmann"
]



        lista_jogadores = []

        for _ in range(189):
            nome_proprio = random.choice(nomes_proprios)
            apelido = random.choice(apelidos)
            nome_completo = nome_proprio + " " + apelido
            lista_jogadores.append(nome_completo)

        lista_jogadores.extend(celebridades)
        print(len(lista_jogadores), "www")

        random.shuffle(lista_jogadores)

        return lista_jogadores


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
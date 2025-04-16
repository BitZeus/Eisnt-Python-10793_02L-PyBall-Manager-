import tkinter as tk
from tkinter import messagebox
import random
import unittest

#Pyball_manager \o/

#AndreiaMa
#BitZeus
#pfragoso77

#Classe principal que contêm a janela principal de jogo
class SimuladorFutebol(tk.Tk):
    #definições de inicialização da classe- janela, variáveis, metodos e funçoes
    def __init__(self, nome_minha_equipa, treinador):
        super().__init__()
        self.title("Pyball Football Manager")
        self.geometry("500x300")
        self.logo = tk.PhotoImage(file="campo490x290.gif")
        tk.Label(self, image=self.logo).place(x=5, y=5)

        self.jornada=0
        self.jogos_jornada=[]
        self.minha_equipa = Equipa(nome_minha_equipa, [], 1000, treinador)
        self.formacao_minha_equipa="0"
        self.formacao_titulares = None
        self.resultados_minha_equipa=[]
        self.nome_equipa_adversaria=""
        self.formacao_equipa_adversaria=""
        
        self.equipas = ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'Swift', 'Go', 'Rust', nome_minha_equipa]

        self.lista_nomes = ["António", "Manuel", "João", "Miguel", "Sofia", "Carolina", "William", "Emily", "James", "Olivia",
                                  "Étienne", "Amélie", "Julien", "Javier", "Isabella", "Diego" ]
    

        self.lista_apelidos = ["Silva", "Santos", "Fernandes", "Pereira", "Ribeiro", "Costa","Smith", "Johnson", "Brown", "Davis",
                                     "Dubois", "Lefèvre", "Martin", "García", "Rodríguez", "López" ]
                
        #definição de lables e butoes da janela principal do jogo

        self.label_nome_equipa = tk.Label(self, text=f"Minha Equipa: {self.minha_equipa.nome}", bg="orange", fg="black", font=("Arial", 10, "bold"))
        self.label_nome_equipa.place(x=20, y=20)


        self.label_saldo = tk.Label(self, text=f"Saldo: {self.minha_equipa.saldo}").place(x=25, y=50)

        self.label_treinador = tk.Label(self, text=f"Treinador: {self.minha_equipa.treinador}").place(x=25, y=70)

        self.botao_ver_minha_equipa = tk.Button(self, text="       Ver Minha Equipa     ", command=self.ver_jogadores_minha_equipa).place(x=20, y=100)
        self.botao_formacao_minha_equipa = tk.Button(self, text="Formação Minha Equipa", command=self.definir_formacao_minha_equipa).place(x=20, y=130)

        self.label_proximo_jogo = tk.Label(self, text="")
        self.label_proximo_jogo.place(x=180, y=200)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.place(x=180, y=220)
        
        self.botao_simular = tk.Button(self, text="Iniciar Liga", command=self.criar_liga, bg="light green", fg="black", font=("Arial", 10, "bold"))
        self.botao_simular.place(x=220, y=250)
        
        #inicialização dos metodos/funçoes para criar as listas/dicionario/plantel das equipas e jogadores
        self.jogadores = self.criar_lista_jogadores()
        self.dicionario_jogadores = self.criar_dicionario_jogadores(self.equipas, self.jogadores)
        self.plantel = self.criar_plantel_equipas(self.jogadores, self.equipas)
        
       #definição da subclasse minha_equipa 
        self.minha_equipa = Equipa(nome_minha_equipa, self.plantel[nome_minha_equipa], 1000, treinador)
        
   #funçao que junta o nome e o apelido de cada jogador a partir da lista nome e da lista apelidos     
    def gerar_jogador(self, nome, apelido):
            nome_escolhido = random.choice(nome)
            apelido_escolhido= random.choice(apelido)
            
            return f"{nome_escolhido} {apelido_escolhido}"          
   #funçao que cria uma lista global dos jogadores tendo em conta as quantidades maximas para cada posiçao     
    def criar_lista_jogadores(self):
        lista_jogadores = {}
        quantidade_jogadores = {
            "defesa": 80,
            "medio": 80,
            "avancados": 40,
            "guarda-redes": 30
        }

        for tipo_jogador, quantidade in quantidade_jogadores.items():
            lista_jogadores[tipo_jogador] = [self.gerar_jogador(self.lista_nomes,self.lista_apelidos) for _ in range(quantidade)]

        return lista_jogadores
    #funçao que cria os diversos plantéis das equipas apartir da lista global de jogadores
    def criar_plantel_equipas(self, jogadores, equipas):
        plantel = {}
        quantidade_jogadores_por_equipa = {
            "Defesa": 8,
            "Médio": 8,
            "Avançado": 4,
            "Guarda-Redes": 3
        }

        jogadores_disponiveis = {
            "Defesa": jogadores["defesa"].copy(),
            "Médio": jogadores["medio"].copy(),
            "Avançado": jogadores["avancados"].copy(),
            "Guarda-Redes": jogadores["guarda-redes"].copy()
        }

        for equipa in equipas:
            plantel[equipa] = []

            for tipo_jogador, quantidade in quantidade_jogadores_por_equipa.items():
                jogadores_selecionados = random.sample(jogadores_disponiveis[tipo_jogador], quantidade)
                plantel[equipa].extend([(tipo_jogador, jogador) for jogador in jogadores_selecionados])
                jogadores_disponiveis[tipo_jogador] = jogadores_disponiveis[tipo_jogador][quantidade:]
        
        
        return plantel
    #funcao que gera a formaçao da equipa:titulares, suplentes, tendo em conta a formaçao escolhida
    def criar_jogadores_titulares(self, plantel, equipa):
        jogadores_titulares_equipa = {}
        jogadores_suplentes_equipa = {}
        formacao = []

        defesas = [jogador[1] for jogador in plantel[equipa][:8]]
        medios = [jogador[1] for jogador in plantel[equipa][8:16]]
        avancados = [jogador[1] for jogador in plantel[equipa][16:20]]
        grs = [jogador[1] for jogador in plantel[equipa][20:]]

        random.shuffle(defesas)
        random.shuffle(medios)
        random.shuffle(avancados)
        random.shuffle(grs)

        formacoes = {
            "1": (4, 4, 2),
            "2": (4, 3, 3),
            "3": (4, 2, 4),
            "4": (4, 5, 1),
            "5": (3, 5, 2),
            "0": (4, 4, 2)  # padrão
        }

        defesas_tit, medios_tit, avs_tit = formacoes.get(self.formacao_minha_equipa, (4, 4, 2))

        titulares = defesas[:defesas_tit] + medios[:medios_tit] + avancados[:avs_tit] + grs[:1]
        suplentes = defesas[defesas_tit:] + medios[medios_tit:] + avancados[avs_tit:] + grs[1:]

        jogadores_titulares_equipa[equipa] = titulares
        jogadores_suplentes_equipa[equipa] = suplentes

        formacao.append(jogadores_titulares_equipa)
        formacao.append(jogadores_suplentes_equipa)

        return formacao

    #funçao que cria dicionario de jogadores por equipa tendo em conta a quantidade por posiçao
    def criar_dicionario_jogadores(self, equipas, jogadores):
        dicionario_jogadores = {}
        quantidade_jogadores_por_equipa = {
            "Defesa": 8,
            "Médio": 8,
            "Avançado": 4,
            "Guarda-Redes": 3
        }

        jogadores_disponiveis = {
            "Defesa": jogadores["defesa"].copy(),
            "Médio": jogadores["medio"].copy(),
            "Avançado": jogadores["avancados"].copy(),
            "Guarda-Redes": jogadores["guarda-redes"].copy()
        }

        for equipa in equipas:
            dicionario_jogadores[equipa] = []

            for tipo_jogador, quantidade in quantidade_jogadores_por_equipa.items():
                jogadores_selecionados = random.sample(jogadores_disponiveis[tipo_jogador], quantidade)
                dicionario_jogadores[equipa].extend([self.criar_jogador_dict(jogador, tipo_jogador, equipa) for jogador in jogadores_selecionados])
                jogadores_disponiveis[tipo_jogador] = jogadores_disponiveis[tipo_jogador][quantidade:]

        return dicionario_jogadores

    #funçao que cria um dicionario para cada jogador tendo em conta os diversos atributos
    def criar_jogador_dict(self, nome_completo, posicao, equipa):
        nome, apelido = nome_completo.split(" ")
        jogador_dict = {
            "nome": nome,
            "sobrenome": apelido,
            "idade": random.randint(18, 35),
            "valor": random.randint(50, 500),
            "posicao": posicao,
            "equipa": equipa,
            "golos": 0
        }
        return jogador_dict

    #funcao que exibe os jogadores da minha_equipa consoante a formaçao escolhida
    def ver_jogadores_minha_equipa(self):
        self.formacao_titulares = self.criar_jogadores_titulares(self.plantel, self.minha_equipa.nome)

        jogadores_texto = "Titulares\n"
        for i, jogador in enumerate(self.formacao_titulares[0][self.minha_equipa.nome]):
            jogadores_texto += f"\n{i + 1}. {jogador}"

        jogadores_texto += "\n\nSuplentes\n"
        for i, jogador in enumerate(self.formacao_titulares[1][self.minha_equipa.nome]):
            jogadores_texto += f"\n{i + 12}. {jogador}"

        janela = tk.Toplevel(self)
        janela.title("Jogadores da Minha Equipa")
        janela.geometry("200x450")
        tk.Label(janela, text=jogadores_texto, anchor="w", justify="left").place(x=20, y=10)
        
    #funcao que define a formaçao da minha_equipa
    def definir_formacao_minha_equipa(self):
        self.escolha_formacao_minha_equipa = tk.StringVar(value=self.formacao_minha_equipa)

        janela = tk.Toplevel(self)
        janela.title("Jogadores da Minha Equipa")
        janela.geometry("200x200")
        formacao_1 = tk.Radiobutton(janela, text="4-4-2", variable=self.escolha_formacao_minha_equipa, value="1")
        formacao_1.place(x=20, y=30)
        formacao_2 = tk.Radiobutton(janela, text="4-3-3", variable=self.escolha_formacao_minha_equipa, value="2")
        formacao_2.place(x=20, y=60)
        formacao_3 = tk.Radiobutton(janela, text="4-2-4", variable=self.escolha_formacao_minha_equipa, value="3")
        formacao_3.place(x=20, y=90)
        formacao_4 = tk.Radiobutton(janela, text="4-5-1", variable=self.escolha_formacao_minha_equipa, value="4")
        formacao_4.place(x=20, y=120)
        formacao_5 = tk.Radiobutton(janela, text="3-5-2", variable=self.escolha_formacao_minha_equipa, value="5")
        formacao_5.place(x=20, y=150)

        confirmar_button = tk.Button(janela, text="Confirmar", command=self.obter_formacao_minha_equipa)
        confirmar_button.place(x=100, y=90)
    #funçao que retorna/atualizada a formação da equipa
    def obter_formacao_minha_equipa(self):
        self.formacao_minha_equipa = self.escolha_formacao_minha_equipa.get()

    #funcao que exibe os jogadores da equipa adversaria
    def ver_jogadores_equipa_adversaria(self):
        if not self.formacao_equipa_adversaria:
            self.formacao_equipa_adversaria = self.criar_jogadores_titulares(self.plantel, self.equipa_adversaria.nome)

        jogadores_texto = "Titulares\n"
        for i, jogador in enumerate(self.formacao_equipa_adversaria[0][self.nome_equipa_adversaria]):
            jogadores_texto += f"\n{i + 1}. {jogador}"

        jogadores_texto += "\n\nSuplentes\n"
        for i, jogador in enumerate(self.formacao_equipa_adversaria[1][self.nome_equipa_adversaria]):
            jogadores_texto += f"\n{i + 12}. {jogador}"

        janela = tk.Toplevel(self)
        janela.geometry("200x450")
        tk.Label(janela, text=jogadores_texto, anchor="w", justify="left").pack()


    #funcao que inicializa a competiçao da liga entre as 10 equipas e em 10 jogos
    def criar_liga(self):
        num_jornadas = 10
        if self.jornada == 0:
            self.tabela = {equipa: {'pontos': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0, 'golos':0} for equipa in self.equipas}

        for jornada in range(1, num_jornadas):
            self.jogos = []
            equipes_disponiveis = self.equipas.copy()

            while len(equipes_disponiveis) >= 2:
                equipa_a, equipa_b = random.sample(equipes_disponiveis, 2)
                equipes_disponiveis.remove(equipa_a)
                equipes_disponiveis.remove(equipa_b)
                self.jogos.append((equipa_a, equipa_b))

            self.jogos_jornada.append(self.jogos)

            for meu_jogo in self.jogos_jornada[0]:
                if self.minha_equipa.nome == meu_jogo[0]:
                    self.nome_equipa_adversaria = meu_jogo[1]
                    self.proximo_jogo=[self.minha_equipa.nome,self.nome_equipa_adversaria]
                    break
                elif self.minha_equipa.nome == meu_jogo[1]:
                    self.nome_equipa_adversaria = meu_jogo[0]
                    self.proximo_jogo=[self.nome_equipa_adversaria,self.nome_equipa_adversaria]
                    break

        self.equipa_adversaria = Equipa(self.nome_equipa_adversaria, self.plantel[self.nome_equipa_adversaria] , 1000, "")
        self.ver_equipa_adversaria = tk.Button(self, text="Ver Equipa Adversaria", command=self.ver_jogadores_equipa_adversaria).place(x=20, y=200)
        self.label_proximo_jogo.configure(text=f"Meu Proximo jogo: {self.proximo_jogo[0]} vs {self.proximo_jogo[1]}", bg="light green", fg="black", font=("Arial",9, "bold"))
        self.botao_simular.configure(text="Simular Jogo", command=self.simular_jogo)
        self.botao_vertabela = tk.Button(self, text="Ver Tabela", command=self.ver_tabela).place(x=350, y=250)
        
    
    #funcao que simula o proximo jogo e retorna o resultado da jornada
    def simular_jogo(self):
        equipe_campea = None
        pontos_campea = -1
        self.jornada += 1

        if self.jornada<10:
            for jogo in self.jogos_jornada[self.jornada-1]:
                equipa_a, equipa_b = jogo
                gols_a = random.randint(0, 5)
                gols_b = random.randint(0, 5)

                resultado = f"{equipa_a} {gols_a} - {gols_b} {equipa_b}"

                if equipa_a == self.minha_equipa.nome or equipa_b == self.minha_equipa.nome:
                    self.resultados_minha_equipa.append(resultado)

                if gols_a > gols_b:
                    self.tabela[equipa_a]['pontos'] += 3
                    self.tabela[equipa_a]['vitorias'] += 1
                    self.tabela[equipa_b]['derrotas'] += 1
                    self.tabela[equipa_a]['golos']+=gols_a
                    self.tabela[equipa_b]['golos']+=gols_b             
                elif gols_a < gols_b:
                    self.tabela[equipa_b]['pontos'] += 3
                    self.tabela[equipa_b]['vitorias'] += 1
                    self.tabela[equipa_a]['derrotas'] += 1
                    self.tabela[equipa_a]['golos']+=gols_a
                    self.tabela[equipa_b]['golos']+=gols_b
                else:
                    self.tabela[equipa_a]['pontos'] += 1
                    self.tabela[equipa_a]['empates'] += 1
                    self.tabela[equipa_b]['pontos'] += 1
                    self.tabela[equipa_b]['empates'] += 1
                    self.tabela[equipa_a]['golos']+=gols_a
                    self.tabela[equipa_b]['golos']+=gols_b
        else:
            for equipa, dados in sorted(self.tabela.items(), key=lambda x: (x[1]['pontos'], x[1]['golos']), reverse=True):
                if equipe_campea is None or dados['pontos'] > pontos_campea:
                    equipe_campea = equipa
                    pontos_campea = dados['pontos']


            print("Equipe Campeã:", equipe_campea)
            messagebox.showinfo("Fim", f"Terminou a liga\nEquipe Campeã:\n\n{equipe_campea}")

        if self.jornada<10:
            meu_jogo = self.resultados_minha_equipa[self.jornada - 1]
            if self.jornada < len(self.resultados_minha_equipa):
                meu_jogo = self.resultados_minha_equipa[self.jornada - 1]

            if self.jornada + 1 < len(self.jogos_jornada):
                proxima_jornada = self.jogos_jornada[self.jornada]
                for jogo in proxima_jornada:
                    self.proximo_jogo=jogo
                    equipa_a, equipa_b = self.proximo_jogo
                    if equipa_a == self.minha_equipa.nome or equipa_b == self.minha_equipa.nome:
                        self.label_proximo_jogo.configure(text=f"Meu Proximo jogo: {self.proximo_jogo[0]} vs {self.proximo_jogo[1]}", bg="light green", fg="black", font=("Arial", 10, "bold"))
                        self.label_resultado.configure(text=f"{meu_jogo}, jornada: {self.jornada + 1}")
                        messagebox.showinfo("Resultado meu jogo:", f"{meu_jogo}" )
            self.formacao_equipa_adversaria=""
    #funcao que exibe a tabela de classificaçao das equipas        
    def ver_tabela(self):
        tabela = tk.Toplevel(self)
        tabela.title("Tabela de Classificação")  
        tabela.geometry("500x300")
    
        scrollbar = tk.Scrollbar(tabela)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
        text_area = tk.Text(tabela, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        text_area.pack(expand=True, fill=tk.BOTH)
    
        for i, (equipa, dados) in enumerate(
            sorted(self.tabela.items(), key=lambda x: (x[1]['pontos'], x[1]['golos']), reverse=True), start=1
        ):
            linha = f"{i}. {equipa}: {dados['pontos']:02} Pts | Vitórias={dados['vitorias']}, Empates={dados['empates']}, Derrotas={dados['derrotas']}, Golos={dados['golos']:02}\n"
            text_area.insert(tk.END, linha)
    
        scrollbar.config(command=text_area.yview)

        
        
 #classe do teste unitario de soma       
class TestSoma(unittest.TestCase):
    def test_juntar_palavras_com_espaço(self):
        app = SimuladorFutebol("", "")
        self.assertEqual(app.gerar_jogador(["a"], ["b"]), "a b")

#subclasse equipa
class Equipa:
    def __init__(self, nome, jogadores, saldo, treinador):
        self.nome = nome
        self.jogadores = jogadores
        self.saldo = saldo
        self.treinador = treinador
        self.pontos = 0 
        self.golos = 0
#funcao que cria o nome da equipa na janela de inicializaçao
def criar_equipe():
    nome_minha_equipa = entry_nome.get()
    treinador = entry_nome_treinador.get()
    window.destroy()

    app = SimuladorFutebol(nome_minha_equipa, treinador)
    app.mainloop()
       

if __name__ == '__main__':
 #inicializao da janela de inicializao do jogo (nome de equipa, treinador, escolha de equipamento)   
    window = tk.Tk()
    window.title("Inicialização de jogo")
    window.geometry("500x300")
    label_titulo = tk.Label(window, text="Bem-vindo ao PyBall Football Manager", bg="orange", fg="black", font=("Arial", 10, "bold")).pack()
    label_nome = tk.Label(window, text="Nome da Equipa:")
    label_nome.pack()

    entry_nome = tk.Entry(window)
    entry_nome.pack()

    label_nome_treinador = tk.Label(window, text="O teu nome:")
    label_nome_treinador.pack()
    entry_nome_treinador = tk.Entry(window)
    entry_nome_treinador.pack()

    btn_criar_equipe = tk.Button(window, text="Criar Equipa", command=criar_equipe)
    btn_criar_equipe.pack()

    label_nome = tk.Label(window, text="Equipamento:")
    label_nome.place(x=70, y=120)
    radio_var = tk.StringVar(value="op1")
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
    #execuçao do teste unitario à funçao gerar_jogadores
    print("\nResultado Teste Unitario")
    unittest.main()


class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 20
        self.saude = 80
        self.idade = 1
    def AlterarNome(self, novoNome):
        self.nome = novoNome
    def AlterarFome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0
    def AlterarSaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0
    def AlterarIdade(self):
        self.idade += 1
    def RetornarNome(self):
        return self.nome
    def RetornarFome(self):
        return self.fome
    def RetornarSaude(self):
        return self.saude
    def RetornarIdade(self):
        return self.idade
    def RetornarHumor(self):
        humor = self.saude + self.fome
        return humor

nomeB = input('Qual o nome que deseja colocar no seu novo companheiro?') 
Bichinho = BichinhoVirtual(nome = nomeB)
while (Bichinho.saude > 0) and (Bichinho.fome < 100):
    Bichinho.AlterarFome(+2)
    Bichinho.AlterarSaude(-2)
    Bichinho.AlterarIdade()
    resposta = input(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \nOlá meu nome é {Bichinho.nome}. Qual aventura vamos ter agora? \n1- Alimentar (-10 defome)\n2- Dormir (+10 de saúde)\n3- Alterar Nome\n4- Visualizar Humor\n5- Visualizar Idade\n6- Visualizar fome\n7- Visualizar Saúde\nResposta: """)
    print('\n')  
    if resposta == '1':
         Bichinho.AlterarFome(-10)
         print("-10 de fome! Estava uma delicia, obrigado.")
    elif resposta == '2':
        Bichinho.AlterarSaude(+10)
        print("+10 de saúde, Amei o exercicio de hoje!")
    elif resposta == '3':
        nome2 = input('Legal, vou ser renomeado, cometemos algum crime criador? \n')
        Bichinho.AlterarNome(nome2)
    elif resposta == '4':
        print("Humor: ", Bichinho.RetornarHumor())
    elif resposta == '5':
        print("Idade: ", Bichinho.RetornarIdade())
    elif resposta == '6':
        print("Fome: ", Bichinho.RetornarFome())
    elif resposta == '7':
        print("Saúde: ",Bichinho.RetornarSaude())
    else:
        print('Escolha um número válido!')
else: print("""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\nVocê me deixou morrer, ó vida cruel!\n""")        

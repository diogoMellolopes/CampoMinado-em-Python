import random
from os import system, name
class CampoMinado:

    def __init__(self, bombas = 1, coluna = 3, linha = 3):
        self.__bombas = bombas
        self.__coluna = coluna
        self.__linha = linha
        self.__campo = []
        self.__campoBombas = []
        self.__colunaJogada = 0
        self.__linhaJogada = 0
        self.__bandeira = bombas
        self.__casasSemBomba = 0

    def criarCampo(self):
        self.__campo = [["■" for i in range(0, self.__coluna)] for j in range(0, self.__linha)]
    
    def criarCampoBombas(self):
        self.__campoBombas = [["■" for i in range(0, self.__coluna)] for j in range(0, self.__linha)]
            
    def printarCampoBombas(self):
        campo = ""
        temp = 1
        cont = 0
        for i in range(0, self.__linha):
            if cont < 10: campo += " "
            campo += str(cont) + "  "
            for j in range(0, self.__coluna):
                campo += "".join(self.__campoBombas[i][j])
                campo += "  "
            if temp != i: campo += "\n"
            temp += 1
            cont += 1
        cima = " #  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z"
        print(cima[:self.__coluna * 3 + 2])
        print(campo)

    def printarCampo(self):
        campo = ""
        temp = 1
        cont = 0
        for i in range(0, self.__linha):
            if cont < 10: campo += " "
            campo += str(cont) + "  "
            for j in range(0, self.__coluna):
                campo += "".join(self.__campo[i][j])
                campo += "  "
            if temp != i: campo += "\n"
            temp += 1
            cont += 1
        cima = " #  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z"
        print(cima[:self.__coluna * 3 + 2])
        print(campo)

    def colocarBombas(self):
        for i in range(0, self.__bombas):
            while True:
                try:
                    while True:
                        coluna = random.randint(0, self.__coluna)
                        linha = random.randint(0, self.__linha)
                        if "X" in self.__campoBombas[linha][coluna]: pass
                        elif self.__bombas <= 0: break
                        else:
                            self.__campoBombas[linha][coluna] = "X"
                            self.__bombas -= 1
                except IndexError:
                    pass
                else:
                    break

    def colocarNumeros(self):
        for i in range(0, self.__linha):
            for j in range(0, self.__coluna):
                try:
                    if "X" in self.__campoBombas[i][j]:
                        continue
                    else:
                        try:
                            bombas = 0
                            for m in range(-1, 2):
                                for n in range(-1, 2):
                                    if i + m == -1 or j + n == -1: continue
                                    elif i + m == self.__linha or j + n == self.__coluna: continue
                                    elif "X" in self.__campoBombas[i + m][j + n]:
                                        bombas += 1
                                        self.__campoBombas[i][j] = str(bombas)
                        except IndexError:
                            pass
                except IndexError:
                    pass
        
    def validarPosicao(self, posicao = "A1"):
        numero = posicao[1:3]
        numero = int(numero)
        letra = posicao[0]
        letra = ord(letra) - 65
        if letra >= self.__coluna or letra < 0:
            input("Por favor, digite uma letra válida")
            return False
        else: self.__colunaJogada = letra
        if numero < 0 or numero >= self.__linha:
            input("Por favor, digite um número válido")
            return False
        else: self.__linhaJogada = numero
        if self.__campo[self.__linhaJogada][self.__colunaJogada] != "■":
            input("Por favor digite uma coordenada ainda não revelada")
            return False
        return True
    
    def getLinhaJogada(self):
        return self.__linhaJogada   
    
    def getColunaJogada(self):
        return self.__colunaJogada
    
    def getBandeira(self):
        return self.__bandeira
    
    def jogar(self, linha, coluna):
        if self.__campoBombas[linha][coluna] == "X":
            self.limparTela()
            print("\nQue pena, você PERDEU!!\n")
            return False
        elif self.__campoBombas[linha][coluna] == "■":
            self.__revelarAdjacentes(linha, coluna)
            return True
        else:
            self.__campo[linha][coluna] = self.__campoBombas[linha][coluna]
            return True
            
    def __revelarAdjacentes(self, linha, coluna):
        visited = set() 
        queue = [(linha, coluna)] 
        while queue:
            linha, coluna = queue.pop(0)
            if (linha, coluna) not in visited:
                visited.add((linha, coluna))
                self.__campo[linha][coluna] = self.__campoBombas[linha][coluna]  
                if self.__campoBombas[linha][coluna] == "■":  
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if i == 0 and j == 0: self.__campo[linha + i][coluna + j] = " "
                            else:
                                novaLinha = linha + i
                                novaColuna = coluna + j
                                if 0 <= novaLinha < self.__linha and 0 <= novaColuna < self.__coluna:
                                    if self.__campo[novaLinha][novaColuna] == "■": 
                                        queue.append((novaLinha, novaColuna))

    def colocarBandeira(self, linha, coluna):
        self.__campo[linha][coluna] = "P"
        self.__bandeira -= 1

    def criarCondicaoVitoria(self):
        for i in range(0, self.__linha):
            for j in range(0, self.__coluna):
                if "■" in self.__campoBombas[i][j]:
                    self.__casasSemBomba += 1
                elif "X" in self.__campoBombas[i][j]:
                   pass
                else:
                    self.__casasSemBomba += 1

    def validarVitoria(self):
        bombas = self.__casasSemBomba
        for i in range(0, self.__linha):
            for j in range(0, self.__coluna):
                if " " in self.__campo[i][j]:
                    bombas -= 1
                elif "■" in self.__campo[i][j]:
                    pass
                else:
                    bombas -= 1
        if bombas == 0:
            return True
        return False
                
    def printarCampoVitoria(self):
        campo = [[" " for i in range(0, self.__coluna)] for j in range(0, self.__linha)]
        for i in range(0, self.__linha):
            for j in range(0, self.__coluna):
                if "X" in self.__campoBombas[i][j]:
                    campo[i][j] = "P"
                elif "■" in self.__campoBombas[i][j]:
                    campo[i][j] = " "
                elif "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" in self.__campoBombas[i][j]:
                    campo[i][j] = self.__campoBombas[i][j]
        campo2 = ""
        temp = 1
        cont = 0
        for i in range(0, self.__linha):
            if cont < 10: campo2 += " "
            campo2 += str(cont) + "  "
            for j in range(0, self.__coluna):
                campo2 += "".join(campo[i][j])
                campo2 += "  "
            if temp != i: campo2 += "\n"
            temp += 1
            cont += 1
        cima = " #  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z"
        print(cima[:self.__coluna * 3 + 2])
        print(campo2)

    def printarCampoDerrota(self):
        campo = [[" " for i in range(0, self.__coluna)] for j in range(0, self.__linha)]
        for i in range(0, self.__linha):
            for j in range(0, self.__coluna):
                if "X" in self.__campoBombas[i][j]:
                    campo[i][j] = "X"
                elif "■" in self.__campoBombas[i][j]:
                    campo[i][j] = " "
                elif "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" in self.__campoBombas[i][j]:
                    campo[i][j] = self.__campoBombas[i][j]
        campo2 = ""
        temp = 1
        cont = 0
        for i in range(0, self.__linha):
            if cont < 10: campo2 += " "
            campo2 += str(cont) + "  "
            for j in range(0, self.__coluna):
                campo2 += "".join(campo[i][j])
                campo2 += "  "
            if temp != i: campo2 += "\n"
            temp += 1
            cont += 1
        cima = " #  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z"
        print(cima[:self.__coluna * 3 + 2])
        print(campo2)
        
    def limparTela(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

while True:
    setColuna = int(input("Digite quantos colunas gostaria que o mapa tenha: "))
    if setColuna > 26 or setColuna <= 0:
        print("Insira um valor entre 1 e 26")
        continue
    break
while True:
    setLinha = int(input("Digite quantas linhas gostaria que o mapa tenha: "))
    if setLinha > 26 or setLinha <= 0:
        print("Insira um valor entre 1 e 26")
        continue
    break
while True:
    setBombas = int(input("Digite quantas bombas gostaria que o mapa tenha: "))
    if setBombas < 0 or setBombas >= setLinha * setColuna:
        print("Insira um valor entre 0 e", setLinha * setColuna - 1)
        continue
    break
jogo = CampoMinado(setBombas, setColuna, setLinha)
jogo.limparTela()
começo = True
jogo.criarCampo()
jogo.criarCampoBombas()
jogo.colocarBombas()
jogo.colocarNumeros()
jogo.criarCondicaoVitoria()
print("========== Bem-vindo ao Campo Minado ===========\n")
jogo.printarCampo()
print("Número de bandeiras: ", jogo.getBandeira(), "\n")
posicao = input("Digite uma posição para jogar Ex.: A1\n...: ").upper()
if jogo.validarPosicao(posicao):
    linha = jogo.getLinhaJogada()
    coluna = jogo.getColunaJogada()
    if jogo.jogar(linha, coluna):
        if jogo.validarVitoria():
            print("\nParabéns você conseguiu marcar todas as posições sem bombas!\n")
            jogo.printarCampoVitoria()
            começo = False
    else:
        jogo.printarCampoDerrota()
        começo = False
jogo.limparTela()
while começo == True:
    jogo.printarCampo()
    print("Número de bandeiras: ", jogo.getBandeira(), "\n")
    escolha = input("Gostaria de colocar uma bandeira ou realizar uma jogada? \n(Jogar - 1 / Bandeira - 2): ")
    if escolha == "2":
        posicao = input("\nDigite uma posição para colocar a bandeira Ex.: A1\n...: ").upper()
        if jogo.validarPosicao(posicao):
            linha = jogo.getLinhaJogada()
            coluna = jogo.getColunaJogada()
            jogo.colocarBandeira(linha, coluna)
        else:
            jogo.limparTela()
    elif escolha == "1":
        posicao = input("\nDigite uma posição para jogar Ex.: A1\n...: ").upper()
        if jogo.validarPosicao(posicao):
            linha = jogo.getLinhaJogada()
            coluna = jogo.getColunaJogada()
            if jogo.jogar(linha, coluna):
                if jogo.validarVitoria():
                    print("\nParabéns você conseguiu marcar todas as posições sem bombas!\n")
                    jogo.printarCampoVitoria()
                    break
            else:
                jogo.printarCampoDerrota()
                break
        else:
            jogo.limparTela()
    elif escolha != "1" or escolha != "2":
        input("Digite uma opção válida!")
    jogo.limparTela()
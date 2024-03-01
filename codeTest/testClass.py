class Predador:
    def __init__(self, genero, idade, posicao):
        self.genero = genero
        self.idade = idade
        self.posicao = posicao

    def apresentar(self):
        print("genero: ", self.genero, "\nidade: ", self.idade, "\nposicao: ", self.posicao)

P1 = Predador("M", 4, [1,1])
P1.apresentar()
    
        

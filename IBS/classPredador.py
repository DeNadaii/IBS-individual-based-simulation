class Predador:
    def __init__(self, genero, idade, coordenada, on_prey):
        self.genero = genero
        self.idade = idade
        self.coordenada = coordenada
        self.procriar = False
        self.morte = False
        self.move = True
        self.on_prey = on_prey
    def crescimento_predador(self):
        if self.idade <= 20:
            self.idade += 1
    def apto_a_procriar(self):
        if 10 <= self.idade <= 12:
            self.procriar = True
    def idade_de_morte(self):
        if self.idade > 20:
            self.morte = True
    def can_move(self):
        if self.on_prey or self.idade < 5:
            self.move = False
    def already_copulate(self):
        return 0
        
    
        
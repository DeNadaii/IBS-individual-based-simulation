class Predador:
    def __init__(self, genero, idade, coordenada):
        self.genero = genero
        self.idade = idade
        self.coordenada = coordenada
    def crescimento_predador(self):
        if self.idade < 4:
            self.idade += 1
    def apto_a_procriar(self):
        if self.idade == 4:
            return True
        else:
            return False
    @property
    def coordenada(self):
        return self.coordenada
    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, genero):
        self._genero = genero
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade):
        self._idade = idade
    @property
    def coordenada(self):
        return self._coordenada
    @coordenada.setter
    def coordenada(self, nova_coordenada):
        self._coordenada = nova_coordenada
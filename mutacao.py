import numpy as np
import random

class mutacao:

    def __init__(self, individuo, limiar):
        self.individuo = individuo
        self.limiar = limiar

    def bit_a_bit(self):
        # percorre cada gene (bit) do individuo e altera de 0 para 1 ou de 1 para 0
        for x in range(0, len(self.individuo)):
            limiar_rand = round(random.random(), 3)
            if limiar_rand <= self.limiar:
                if self.individuo[x] == 1:
                    self.individuo[x] = 0
                else:
                    self.individuo[x] = 1

        return self.individuo

    def random_bit(self):
        # seleciona um bit dos 36 e altera o valor de 0 para 1 ou de 1 para 0
        limiar_rand = round(random.random(), 3)

        if limiar_rand <= self.limiar:
            gene = random.randint(0,35)
            if self.individuo[gene] == 1:
                self.individuo[gene] = 0
            else:
                self.individuo[gene] = 1

        return self.individuo

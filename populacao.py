import numpy as np
import random

class populacao:

    def __init__(self, n_individuos, n_cromossomos, n_genes):
        self.n_individuos = n_individuos
        self.n_cromossomos = n_cromossomos
        self.n_genes = n_genes

    def new_pop(self):
        populacao = []
        for x in range(0, self.n_individuos):
            individuo = self.new_individuo()

            np_individuo = np.append(np.array(individuo).flatten(), 0)
            populacao.append(np_individuo)

        return populacao

    def new_individuo(self):
        individuo = []
        for y in range(0, self.n_cromossomos):
            cromossomo = []

            for z in range(0, self.n_genes):
                cromossomo.append(random.randint(0, 1))

            individuo.append(cromossomo)

        return individuo
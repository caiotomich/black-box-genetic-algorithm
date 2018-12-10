import numpy as np
import random
import mutacao as mut

class cruzamento:

    def __init__(self, populacao, tipo_cruzamento, limiar_cruzamento, tipo_mutacao, limiar_mutacao):
        self.populacao = populacao
        self.tipo_cruzamento = tipo_cruzamento
        self.limiar_cruzamento = limiar_cruzamento
        self.limiar_mutacao = limiar_mutacao
        self.tipo_mutacao = tipo_mutacao

    def init(self):
        if self.tipo_cruzamento == 'ponto_de_corte':
            return self.ponto_de_corte()
        elif self.tipo_cruzamento == 'uniforme':
            return self.uniforme()

    def ponto_de_corte(self):
        new_pop = []
        len_pop = len(self.populacao)
        for x in range(0, len_pop, 2):
            individuo_0 = self.populacao[x]
            individuo_1 = self.populacao[x+1]

            # probabilidade de cruzamento
            limiar_rand = round(random.random(), 2)
            if limiar_rand <= self.limiar_cruzamento:
                # ponto_de_corte = random.randint(0, 36) # performance ruim!
                ponto_de_corte = 18 # corte fixo, melhor performance
                filho_0 = np.concatenate((individuo_1[ponto_de_corte:36], individuo_0[:ponto_de_corte]), axis=None)
                filho_1 = np.concatenate((individuo_0[ponto_de_corte:36], individuo_1[:ponto_de_corte]), axis=None)

                if self.tipo_mutacao == 'bit_a_bit':
                    filho_0 = mut.mutacao(filho_0, self.limiar_mutacao).bit_a_bit()
                    filho_1 = mut.mutacao(filho_1, self.limiar_mutacao).bit_a_bit()
                elif self.tipo_mutacao == 'random_bit':
                    filho_0 = mut.mutacao(filho_0, self.limiar_mutacao).random_bit()
                    filho_1 = mut.mutacao(filho_1, self.limiar_mutacao).random_bit()

                filho_0 = np.append(filho_0, 0)
                filho_1 = np.append(filho_1, 0)

                new_pop.append(filho_0)
                new_pop.append(filho_1)

            new_pop.append(individuo_0)
            new_pop.append(individuo_1)

        return new_pop

    def uniforme(self):
        new_pop = []
        n_populacao = len(self.populacao)-1
        for x in range(0, n_populacao):
            y = 0
            individuo_0 = self.populacao[x]
            while True:
                y = random.randint(0, n_populacao)
                individuo_1 = self.populacao[y]

                if x != y:
                    break

            # gera mascara de bits
            len_individuo = len(individuo_0)-1
            bits_mascara = self.mascara_de_bits(len_individuo)

            # probabilidade de cruzamento
            limiar_rand = round(random.random(), 2)
            if limiar_rand <= self.limiar_cruzamento:
                filho_0 = []
                filho_1 = []

                for z in range(len_individuo):
                    if bits_mascara[z] == 1:
                        filho_0.append(individuo_1[z])
                        filho_1.append(individuo_0[z])
                    elif bits_mascara[z] == 0:
                        filho_0.append(individuo_0[z])
                        filho_1.append(individuo_1[z])

                if self.tipo_mutacao == 'bit_a_bit':
                    filho_0 = mut.mutacao(filho_0, self.limiar_mutacao).bit_a_bit()
                    filho_1 = mut.mutacao(filho_1, self.limiar_mutacao).bit_a_bit()
                elif self.tipo_mutacao == 'random_bit':
                    filho_0 = mut.mutacao(filho_0, self.limiar_mutacao).random_bit()
                    filho_1 = mut.mutacao(filho_1, self.limiar_mutacao).random_bit()

                filho_0 = np.append(filho_0, 0)
                filho_1 = np.append(filho_1, 0)

                new_pop.append(filho_0)
                new_pop.append(filho_1)

            new_pop.append(individuo_0)
            new_pop.append(individuo_1)

        return new_pop

    def mascara_de_bits(self, length):
        mascara = []
        for x in range(length):
            mascara.append(random.randint(0, 1))

        return mascara

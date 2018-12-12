import random

class selecao:

    def __init__(self, populacao, n_populacao, limiar_selecao):
        self.populacao = sorted(populacao, key=lambda x: x[36], reverse=True)
        self.n_populacao = n_populacao
        self.limiar_selecao = limiar_selecao

    def selecao(self, tipo_selecao):
        if tipo_selecao == 'torneio':
            return self.torneio()
        elif tipo_selecao == 'roleta':
            return self.roleta()

    def torneio(self):
        len_populacao = (len(self.populacao)-1)

        new_pop = []
        while True:
            x = random.randint(0, len_populacao)
            y = 0
            while x == y or y == 0:
                y = random.randint(0, len_populacao)

            individuo_0 = self.populacao[x]
            individuo_1 = self.populacao[y]

            if individuo_0[36] > individuo_1[36]:
                new_pop.append(individuo_0)
            elif individuo_1[36] > individuo_0[36]:
                new_pop.append(individuo_1)
            elif individuo_0[36] == individuo_1[36]:
                new_pop.append(individuo_0)

            if len(new_pop) == self.n_populacao:
                break

        return new_pop

    def roleta(self):
        i = 0
        new_pop = []
        while True:
            limiar_rand = round(random.random(), 2)
            if limiar_rand <= self.limiar_selecao:
                new_pop.append(self.populacao[i])
                self.populacao.pop(i)

            i = i + 1

            if (len(new_pop) == self.n_populacao):
                break
            elif i > len(self.populacao)-1:
                i = 0

        return new_pop
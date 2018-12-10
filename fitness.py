import matplotlib.pyplot as plt
import numpy as np

class fitness:

    def __init__(self, populacao):
        self.populacao = populacao

    def calc(self):
        pop_fitness = []
        for x in range(0, len(self.populacao)):
            individuo = self.populacao[x]

            individuo[36] = (
                9 + (individuo[1] * individuo[4]) - (individuo[22] * individuo[13])
                 + (individuo[23] * individuo[3]) - (individuo[20] * individuo[9])
                 + (individuo[35] * individuo[14]) - (individuo[10] * individuo[25])
                 + (individuo[15] * individuo[16]) + (individuo[2] * individuo[32])
                 + (individuo[27] * individuo[18]) + (individuo[11] * individuo[33])
                 - (individuo[30] * individuo[31]) - (individuo[21] * individuo[24])
                 + (individuo[34] * individuo[26]) - (individuo[28] * individuo[6])
                 + (individuo[7] * individuo[12]) - (individuo[5] * individuo[8])
                 + (individuo[17] * individuo[19]) - (individuo[0] * individuo[29])
                 + (individuo[22] * individuo[3]) + (individuo[20] * individuo[14])
                 + (individuo[25] * individuo[15]) + (individuo[30] * individuo[11])
                 + (individuo[24] * individuo[18]) + (individuo[6] * individuo[7])
                 + (individuo[8] * individuo[17]) + (individuo[0] * individuo[32])
            )

            pop_fitness.append(individuo)

        return pop_fitness

    def get_global(self):
        fitness = []
        for x in range(len(self.populacao)):
            individuo = self.populacao[x]

            fitness.append(individuo[36])

        return {'fitness': fitness, 'max': max(fitness), 'min': min(fitness), 'med': np.median(fitness)}

    def grafico(self, max_fitness, min_fitness, med_fitness):
        data = [max_fitness, min_fitness, med_fitness]
        data = np.array(data).T

        fig, ax = plt.subplots()
        lines = ax.plot(data)
        ax.legend(lines, ['Fitness Máximo', 'Fitness Mínimo', 'Fitness Médio'])

        plt.show()
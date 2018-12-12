import numpy as np
import populacao as pop
import cruzamento as crz
import fitness as fit
import selecao as sel

print("\nFaculdade de Ciência e Tecnologia de Montes Claros - FACIT")
print("Engenharia de Computação\n")
print("Disciplina: Otimização")
print("Prof.: Hugo Andrei Mendes da Silva")
print("Objetivo: Resolução do problema da Caixa Preta com Algoritmos Genéticos\n")
print("Equipe: Caio Tomich, Celio Xavier, João César Fróes\n")

print('Inicio da execução...\nAguarde...')

N_GERACOES = 300
N_POPULACAO = 250
N_CROMOSSOMOS = 9
N_GENES = 4

fitness = []
max_fitness = []
min_fitness = []
med_fitness = []

# melhores combinações encontradas para solução do problema
# - ponto_de_corte, bit_a_bit e torneio
# - uniforme, random_bit e roleta
tipo_cruzamento = (['ponto_de_corte', 'uniforme'])[1]
tipo_mutacao = (['bit_a_bit', 'random_bit'])[1]
tipo_selecao = (['torneio', 'roleta'])[0]

limiar_cruzamento = 0.80
limiar_mutacao = 0.005
limiar_selecao = 0.50

# gera população inicial
populacao_inicial = pop.populacao(N_POPULACAO, N_CROMOSSOMOS, N_GENES).new_pop()

# calcula fitness
pop_fitness = fit.fitness(populacao_inicial).calc()

x = 1
while True:
    # seleção
    populacao = sel.selecao(pop_fitness, N_POPULACAO, limiar_selecao).selecao(tipo_selecao)

    # cruzamento/mutação
    pop_cruzamento = crz.cruzamento(populacao, tipo_cruzamento, limiar_cruzamento, tipo_mutacao, limiar_mutacao).init()

    # calcula fitness
    pop_fitness = fit.fitness(pop_cruzamento).calc()

    # captura fitness da população atual
    global_fitness = fit.fitness(populacao).get_global()

    # salva dados de fitness de todas as gerações
    fitness.append(global_fitness['fitness'])
    max_fitness.append(global_fitness['max'])
    min_fitness.append(global_fitness['min'])
    med_fitness.append(global_fitness['med'])

    # critérios de parada
    if x == N_GERACOES or max_fitness[-1] == 27:
        break

    x = x + 1

# plota gráficos
fit.fitness([]).grafico(max_fitness, min_fitness, med_fitness)
print("Processo Concluído!\n")

# exibe resultados finais obtidos
print("Parâmetros Selecionados:\n")

print("Método de cruzamento", tipo_cruzamento, "com probabilidade de", limiar_cruzamento * 100, "%")
print("Método de mutação", tipo_mutacao, "com probabilidade de", limiar_mutacao * 100, "%")
print("Método de seleção por ", tipo_selecao, "com probabilidade de", limiar_selecao * 100, "%\n")

print("Resultados:")
print("Maior Fitness: ", sorted(max_fitness, reverse=True))
print("Menor Fitness: ", sorted(min_fitness, reverse=True))
print("Média Fitness: ", sorted(med_fitness, reverse=True))

print("Fitness Máximo: ", np.max(fitness))
print("Fitness Mínimo: ", np.min(fitness))
print("Fitness Médio: ", np.mean(fitness))
print("Desvio Padrão: ", np.std(fitness), "\n")

print("Número de Gerações: ", x)

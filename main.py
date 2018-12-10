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

tipo_cruzamento = (['ponto_de_corte', 'uniforme'])[1]
tipo_mutacao = (['bit_a_bit', 'random_bit'])[1]
tipo_selecao = (['torneio', 'roleta'])[0]

limiar_cruzamento = 0.80
limiar_mutacao = 0.005
limiar_selecao = 0.50

populacao = pop.populacao(N_POPULACAO, N_CROMOSSOMOS, N_GENES).new_pop()

x = 1
print(x, end='\r')
while True:
    # cruzamento/mutacao
    pop_cruzamento = crz.cruzamento(populacao, tipo_cruzamento, limiar_cruzamento, tipo_mutacao, limiar_mutacao).init()

    # calcula_fitness
    pop_fitness = fit.fitness(pop_cruzamento).calc()

    # seleção
    populacao = sel.selecao(pop_fitness, N_POPULACAO, limiar_selecao).selecao(tipo_selecao)

    # captura fitness da população
    global_fitness = fit.fitness(populacao).get_global()

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

print("Resultados: \n")

print("Maior Fitness: ", sorted(max_fitness, reverse=True), "\n")
print("Menor Fitness: ", sorted(min_fitness, reverse=True), "\n")
print("Média Fitness: ", sorted(med_fitness, reverse=True), "\n")

print("Fitness Máximo: ", np.max(fitness))
print("Fitness Mínimo: ", np.min(fitness))
print("Fitness Médio: ", np.mean(fitness))
print("Desvio Padrão: ", np.std(fitness), "\n")

print("Número de Gerações: ", x)

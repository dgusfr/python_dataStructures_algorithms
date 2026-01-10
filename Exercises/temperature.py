temperaturas = (22, 25, 28, 30, 24, 21, 19)

meio_da_semana = temperaturas[2:5]
temperatura_trinta = 30 in temperaturas

# Tuplas são imutáveis, o que significa que seus valores não podem ser alterados após a criação. Portanto, tentar atribuir um novo valor a um índice específico resultará em um erro.

print("Sub-tupla extraída:", meio_da_semana)

if temperatura_trinta == True:
    print("A temperatura 30 está presente na tupla original")
else:
    print("A temperatura 30 não está presente na tupla original")

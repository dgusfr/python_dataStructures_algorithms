"""
Crie uma lista chamada computadores contendo os nomes: "Dell", "HP" e "Apple". Em seguida, utilize a função print() para exibir no console apenas o nome "HP", acessando-o diretamente pelo seu índice na lista.
Adicione o nome "Lenovo" ao final da lista computadores e, depois, exiba a lista completa no console para confirmar que o novo nome foi incluído.
"""

computadores = ["Dell", "HP", "Apple"]

print(computadores[1])

computadores.append("lenovo")

print(computadores)

computadores.insert(1, "Asus")

from stack import Stack

# 1. Instanciando
pilha_de_roupa = Stack()

# 2. Empilhando (Push)
pilha_de_roupa.push("Camisa Azul")
pilha_de_roupa.push("Calça Jeans")
pilha_de_roupa.push("Casaco")

# 3. Visualizando a Pilha
print(pilha_de_roupa)

# 4. Espiando o topo (Peek)
print(f"No topo está: {pilha_de_roupa.peek()}")  # Saída: Casaco

# 5. Desempilhando (Pop)
removido = pilha_de_roupa.pop()
print(f"Removi o {removido}")  # Saída: Casaco

# 6. Verificando tamanho final usando len()
print(f"Restam {len(pilha_de_roupa)} itens.")  # Saída: 2

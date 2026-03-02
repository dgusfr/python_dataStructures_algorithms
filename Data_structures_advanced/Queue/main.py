class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("pop from empty queue")
        return self.items.pop(0)

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("peek from empty queue")
        return self.items[0]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def main():
    print("=== Testando a estrutura Queue ===")

    # 1. Instanciando
    minha_fila = Queue()

    # 2. Testando push (Inserção)
    print("\nAdicionando itens na fila...")
    minha_fila.push(10)
    minha_fila.push(20)
    minha_fila.push(30)
    print(f"Estado atual da fila: {minha_fila}")
    print(f"Tamanho: {len(minha_fila)}")

    # 3. Testando peek (Observar)
    print("\nEspiando o primeiro da fila...")
    print(f"Próximo elemento: {minha_fila.peek()}")

    # 4. Testando pop (Remoção)
    print("\nRemovendo itens da fila...")
    print(f"Removido: {minha_fila.pop()}")
    print(f"Removido: {minha_fila.pop()}")
    print(f"Estado atual da fila: {minha_fila}")

    # 5. Testando fila vazia (Tratamento de Exceção)
    print("\nLimpando a fila e testando erro...")
    print(f"Removido o último: {minha_fila.pop()}")

    try:
        minha_fila.pop()  # Vai tentar remover de uma fila já vazia
    except IndexError as e:
        print(f"Exceção capturada com sucesso: {e}")


if __name__ == "__main__":
    main()

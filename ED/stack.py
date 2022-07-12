from datetime import date

class Produto:
    def __init__(self, nome: str, categoria: str, data_de_vencimento: date):
        self.nome = nome
        self.categoria = categoria
        self.data_de_vencimento = data_de_vencimento

    def __str__(self):
        data_de_vencimento_formatada = self.data_de_vencimento.strftime("%d/%m/%Y")
        return f"{self.nome} - {self.categoria} - {data_de_vencimento_formatada}"

class PilhasDeProdutos:
    _categorias = {}

    def add(self, produto: Produto):
        pilha = self._categorias.get(produto.categoria, None)
        pilha_temporaria = []

        if pilha is None:
            print("Empilhe o produto: ", produto)
            self._categorias[produto.categoria] = [produto]
            return True

        for i in reversed(range(len(pilha))):
            if produto.data_de_vencimento > pilha[i].data_de_vencimento:
                print("Remova o produto: ", pilha[i])
                pilha_temporaria.append(pilha.pop(i))

        print("Empilhe o produto: ", produto)
        pilha.append(produto)
        self._categorias[produto.categoria] = pilha + pilha_temporaria

        for produto in reversed(pilha_temporaria):
            print("Empilhe o produto: ", produto)
            pilha.append(produto)
            self._categorias[produto.categoria] = pilha

        return True

    def remove(self, categoria):
        pilha = self._categorias.get(categoria, [])
        if len(pilha) == 0:
            return None
        return pilha.pop()

    def show(self):
        for categoria, produtos in self._categorias.items():
            print("\n---------------------------------------\n")
            print("Categoria: {}".format(categoria))
            for produto in reversed(produtos):
                print("    {}".format(produto))
            print("\n")
        print("---------------------------------------\n")


def menu():
    print("""
---------------------------------------

1 - Cadastrar produto
2 - Listar produtos
3 - Tirar produto do estoque
0 - Sair
 
---------------------------------------
    """)
    return input("Digite a opção desejada: ")
    
def main():
    print("Bem vindo ao sistema de controle de estoque")

    pilha = PilhasDeProdutos()

    while True:
        opcao = menu()

        if opcao == "1":
            print("\n--------- Cadastrando Produto ---------\n")

            nome = input("Nome: ")
            categoria = input("Categoria: ").lower()
            [dia, mes, ano] = input("Data de validade (dd/mm/YYYY): ").split("/")
            produto = Produto(nome, categoria, date(int(ano), int(mes), int(dia)))
            pilha.add(produto)
            print("\n---------------------------------------\n")

        elif opcao == "2":
            pilha.show()

        elif opcao == "3":
            categoria = input()
            produto = pilha.remove(categoria)
            if produto:
                print(produto)
            else:
                print("Essa categoria não tem produtos")

        elif opcao == "0":
            return

if __name__ == "__main__":
    main()
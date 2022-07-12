from datetime import date

class Produto:
    def __init__(self, name: str, category: str, expiration: date):
        self.name = name
        self.category = category
        self.expiration = expiration

    def __str__(self):
        formated_expiration = self.expiration.strftime("%d/%m/%Y")
        return f"{self.name} - {self.category} - {formated_expiration}"

class PilhasDeProdutos:
    _pilhas = {}

    def add(self, product: Produto):
        pilha = self._pilhas.get(product.category, None)
        temp_stack = []

        if pilha is None:
            print("Empilhe o produto: ", product)
            self._pilhas[product.category] = [product]
            return True

        for i in reversed(range(len(pilha))):
            if product.expiration > pilha[i].expiration:
                print("Remova o produto: ", pilha[i])
                temp_stack.append(pilha.pop(i))

        print("Empilhe o produto: ", product)
        pilha.append(product)
        self._pilhas[product.category] = pilha + temp_stack

        for product in reversed(temp_stack):
            print("Empilhe o produto: ", product)
            pilha.append(product)
            self._pilhas[product.category] = pilha

        return True

    def remove(self, category):
        pilha = self._pilhas.get(category, [])
        if len(pilha) == 0:
            return None
        return pilha.pop()

    def show(self):
        for category, products in self._pilhas.items():
            print("\n---------------------------------------\n")
            print("Categoria: {}".format(category))
            for product in reversed(products):
                print("    {}".format(product))
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

    # produto1 = Produto("Produto 1", "arroz", date(2020, 1, 1))
    # produto2 = Produto("Produto 2", "arroz", date(2020, 1, 2))
    # produto3 = Produto("Produto 3", "arroz", date(2020, 1, 3))
    # produto4 = Produto("Produto 4", "arroz", date(2020, 1, 4))

    # pilha.add(produto3)
    # pilha.add(produto2)
    # pilha.add(produto1)
    # pilha.add(produto4)

    # pilha.show()
    # return
    while True:
        option = menu()

        if option == "1":
            print("\n--------- Cadastrando Produto ---------\n")

            name = input("Nome: ")
            category = input("Categoria: ").lower()
            [day, month, year] = input("Data de validade (dd/mm/YYYY): ").split("/")
            product = Produto(name, category, date(int(year), int(month), int(day)))
            pilha.add(product)
            print("\n---------------------------------------\n")

        elif option == "2":
            pilha.show()

        elif option == "3":
            category = input()
            produto = pilha.remove(category)
            if produto:
                print(produto)
            else:
                print("Essa categoria não tem produtos")

        elif option == "0":
            return

if __name__ == "__main__":
    main()
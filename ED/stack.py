from datetime import date


class Product:
    def __init__(self, name: str, category: str, expiration: date):
        self.name = name
        self.category = category
        self.expiration = expiration
    def __str__(self):
        return f"{self.name} - {self.category} - {self.expiration}"

class ProductStack:
    _products = {}

    def add(self, product: Product):
        stack = self._products.get(product.category, None)

        if stack is None:
            self._products[product.category] = [product]
            return True

        for i in reversed(range(len(stack))):
            if product.expiration < stack[i].expiration:
                print("Inserir produto: ", product)
                stack.append(product)
                return True
            else:
                print("Remover produto: ", stack[i])

    def remove(self):
        return self._products.pop()

    def show(self):
        for category, products in self._products.items():
            print(f"{category}:")
            for product in products:
                print(product)
            print("\n")


def menu():
    print("""
    1 - Cadastrar produto
    2 - Listar produtos
    3 - Alterar produto
    4 - Excluir produto
    5 - Sair
    """)
    return input("Digite a opção desejada: ")
    
print("Bem vindo ao sistema de controle de estoque")

stack = ProductStack()

product1 = Product("Produto 1", "arroz", date(2020, 1, 1))
product2 = Product("Produto 2", "arroz", date(2020, 1, 2))
product3 = Product("Produto 3", "arroz", date(2020, 1, 3))
product4 = Product("Produto 4", "arroz", date(2020, 1, 4))

stack.add(product3)
stack.add(product2)
stack.add(product1)
# stack.add(product4)

stack.show()

# while True:
#   option = menu()

#   if option == "1":
#     print("Cadastrar produto")
#     name = input("Nome: ")
#     category = input("Categoria: ")
#     expiration = input("Data de validade: ")
#     product = Product(name, category, expiration)
#     stack.add(product)
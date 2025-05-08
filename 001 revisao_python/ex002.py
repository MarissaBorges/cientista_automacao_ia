#Manipulação de Dicionário: Crie um dicionário representando um catálogo de produtos (nome do produto como chave, preço como valor). Escreva funções para:
#   Adicione um novo produto ao catálogo.
#   Atualizar o preço de um produto existente.
#   Remover um produto do catálogo.

def novo_produto(produtos, novo_produto = '<produto>', preco = 0.0):
    try:
        produtos[novo_produto] = preco
        print(f'Produto adicionado com sucesso, {novo_produto}: {preco}')
        return produtos
    except Exception as erro:
        print(f'Ocorreu um erro ao adidiconar um novo produto')
        print(f'Classe de erro: {erro.__class__}')

def atualizar_preco(produtos, produto = '<produto>', novo_preco = 0.0):
    try:
        produtos[produto] = novo_preco
        print(f'Preço atualizado com sucesso, {produto}: {novo_preco}')
        return produtos
    except Exception as erro:
        print(f'Ocorreu um erro ao atualizar o preço')
        print(f'Classe de erro: {erro.__class__}')

def remover_produto(produtos, produto = '<produto>'):
    try:
        del produtos[produto]
        print(f'Produto {produto} removido com sucesso')
        return produtos
    except Exception as erro:
        print(f'Ocorreu um erro ao remover o produto {produto}')
        print(f'Classe de erro: {erro.__class__}')

produtos = {"Computador": 1200.00, "Controle PS4": 100, "Xbox 360": 500, "Play Station 5": 5000.00, "Headset": 250, "Notebook": 4000}
print(produtos)
# output: {'Computador': 1200.0, 'Controle PS4': 100, 'Xbox 360': 500, 'Play Station 5': 5000.0, 'Headset': 250, 'Notebook': 4000}

adicionar_produto = novo_produto(produtos, "Cabo USB", 12.99)
print(adicionar_produto)
# output: Produto adicionado com sucesso, Cabo USB: 12.99

preco_atualizado = atualizar_preco(produtos, "Computador", 1500)
print(preco_atualizado)
# output: Preço atualizado com sucesso, Computador: 1500

produto_removido = remover_produto(produtos, "Xbox 360")
print(produto_removido)
# output: Produto Xbox 360 removido com sucesso


# Sugestão da IA | Inclue validação de entrada, tratamento especifico de erro, retorno de valores booleanos e ajuste no nome de parâmetros
def novo_produto(produtos, nome_produto, preco):
    """
    Adiciona um novo produto ao catálogo.

    Args:
        produtos (dict): O dicionário representando o catálogo de produtos.
        nome_produto (str): O nome do produto a ser adicionado.
        preco (float): O preço do produto.

    Returns:
        bool: True se o produto foi adicionado com sucesso, False caso contrário.
    """
    if not isinstance(nome_produto, str) or not nome_produto:
        print("Erro: Nome do produto inválido.")
        return False
    if not isinstance(preco, (int, float)) or preco <= 0:
        print("Erro: Preço inválido.")
        return False
    try:
        produtos[nome_produto] = preco
        print(f'Produto adicionado com sucesso, {nome_produto}: {preco}')
        return True
    except Exception as erro:
        print(f'Ocorreu um erro ao adicionar o produto {nome_produto}: {erro}')
        return False

def atualizar_preco(produtos, nome_produto, novo_preco):
    """
    Atualiza o preço de um produto existente no catálogo.

    Args:
        produtos (dict): O dicionário representando o catálogo de produtos.
        nome_produto (str): O nome do produto a ser atualizado.
        novo_preco (float): O novo preço do produto.

    Returns:
        bool: True se o preço foi atualizado com sucesso, False caso contrário.
    """
    if not isinstance(nome_produto, str) or not nome_produto:
        print("Erro: Nome do produto inválido.")
        return False
    if not isinstance(novo_preco, (int, float)) or novo_preco <= 0:
        print("Erro: Preço inválido.")
        return False
    try:
        produtos[nome_produto] = novo_preco
        print(f'Preço atualizado com sucesso, {nome_produto}: {novo_preco}')
        return True
    except KeyError:
        print(f'Erro: Produto {nome_produto} não encontrado.')
        return False
    except Exception as erro:
        print(f'Ocorreu um erro ao atualizar o preço do produto {nome_produto}: {erro}')
        return False

def remover_produto(produtos, nome_produto):
    """
    Remove um produto do catálogo.

    Args:
        produtos (dict): O dicionário representando o catálogo de produtos.
        nome_produto (str): O nome do produto a ser removido.

    Returns:
        bool: True se o produto foi removido com sucesso, False caso contrário.
    """
    if not isinstance(nome_produto, str) or not nome_produto:
        print("Erro: Nome do produto inválido.")
        return False
    try:
        del produtos[nome_produto]
        print(f'Produto {nome_produto} removido com sucesso')
        return True
    except KeyError:
        print(f'Erro: Produto {nome_produto} não encontrado.')
        return False
    except Exception as erro:
        print(f'Ocorreu um erro ao remover o produto {nome_produto}: {erro}')
        return False

# Exemplo de uso:
produtos = {"Computador": 1200.00, "Controle PS4": 100, "Xbox 360": 500, "Play Station 5": 5000.00, "Headset": 250, "Notebook": 4000}
print("Catálogo inicial:", produtos)

if novo_produto(produtos, "Cabo USB", 12.99):
    print("Catálogo após adicionar produto:", produtos)

if atualizar_preco(produtos, "Computador", 1500):
    print("Catálogo após atualizar preço:", produtos)

if remover_produto(produtos, "Xbox 360"):
    print("Catálogo após remover produto:", produtos)
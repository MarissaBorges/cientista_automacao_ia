#Tratamento de erros: modifique o script de processamento de arquivos do Exercício 3 para tratar possíveis erros, como arquivo não encontrado ou dados inválidos no arquivo CSV.

def definir_caminho(nome):
    import os
    # Obtém o caminho absoluto da pasta onde este arquivo está localizado
    pasta_base = os.path.dirname(os.path.abspath(__file__))
    # Junta o caminho da pasta 'arquivo' com o nome do arquivo
    caminho = os.path.join(pasta_base, nome)
    return caminho

def arquivo_existe(nome):
    arquivo = definir_caminho(nome)
    try:
        arquivo = open(arquivo, 'r')
        return definir_caminho(nome)
    except FileNotFoundError:
        print(f'O arquivo {nome} não foi encontrado, verifique o nome')

def abrir_arquivo(nome):
    arquivo = arquivo_existe(nome)
    try:
        with open(arquivo, "r") as file:
            conteudo = file.readlines()
            return conteudo
    except Exception as erro:
        print(f'Não foi possível abrir o arquivo {nome}')
        print(erro.__class__)

def extrair_email(nome_arquivo, novo_arquivo):
    try:
        conteudo = abrir_arquivo(nome_arquivo)
        try:
            with open(definir_caminho(novo_arquivo), "w") as new_file:
                for linha in conteudo:
                    dados = linha.split(';')
                    new_file.write(f'{dados[1]}\n')
                print("Arquivo de Emails criado com sucesso")
        except:
            print(f'Não foi possivel criar o arquivo {novo_arquivo}')
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado, verifique o nome')

# PROGRAMA PRINCIPAL
dados = extrair_email('ex004.csv', 'ex004_emails.csv')
arquivo = abrir_arquivo('ex004_emails.csv')
print(arquivo)

# output: Arquivo de Emails criado com sucesso
# ['e-mail\n', 'eduardo@gmail.com\n', 'maria@hotmail.com\n', 'luiz@outlook.com\n', 'fernanda@gmail.com\n', 'manuela@gmail.com\n']

# Sugestão da IA | mais tratamentos de erros e otimização do código
import os

def definir_caminho(nome):
    """
    Define o caminho completo para um arquivo.
    """
    pasta_base = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta_base, nome)
    return caminho

def arquivo_existe(nome):
    """
    Verifica se um arquivo existe no caminho especificado.
    Retorna True se o arquivo existe, False caso contrário.
    """
    caminho_completo = definir_caminho(nome)
    return os.path.exists(caminho_completo)

def extrair_email(nome_arquivo, novo_arquivo):
    """
    Extrai os endereços de e-mail de um arquivo e os salva em um novo arquivo.
    """
    caminho_arquivo_entrada = definir_caminho(nome_arquivo)
    caminho_arquivo_saida = definir_caminho(novo_arquivo)

    if not arquivo_existe(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    try:
        with open(caminho_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada, \
                open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:

            for linha in arquivo_entrada:
                dados = linha.strip().split(';')  # Remove espaços e divide a linha
                if len(dados) > 1:  # Garante que a linha tenha pelo menos duas colunas
                    email = dados[1].strip()  # Extrai o e-mail e remove espaços
                    arquivo_saida.write(email + '\n')  # Escreve o e-mail no novo arquivo
                else:
                    print(f"Aviso: Linha incompleta encontrada no arquivo: {linha.strip()}")

        print("Arquivo de e-mails criado com sucesso.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except PermissionError:
        print(f"Erro: Sem permissão para abrir o arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo '{nome_arquivo}': {e}")

# PROGRAMA PRINCIPAL
extrair_email('ex004.csv', 'ex004_emails.csv')
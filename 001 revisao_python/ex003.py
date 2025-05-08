#Processamento de arquivos: escreva um script que leia um arquivo CSV contendo dados do cliente (nome, e-mail, número de telefone) e extraia todos os endereços de e-mail em um novo arquivo

def definir_caminho(nome):
    import os
    # Obtém o caminho absoluto da pasta onde este arquivo está localizado
    pasta_base = os.path.dirname(os.path.abspath(__file__))
    # Junta o caminho da pasta 'arquivo' com o nome do arquivo
    caminho = os.path.join(pasta_base, nome)
    return caminho

with open(definir_caminho('ex003.csv'), "r") as file:
    conteudo = file.readlines()
    with open(definir_caminho('ex003_emails.csv'), "w") as new_file:
        for linha in conteudo:
            dados = linha.split(';')
            new_file.write(f'{dados[1]}\n')
        print("Arquivo de Emails criado com sucesso")

# output: Arquivo de Emails criado com sucesso

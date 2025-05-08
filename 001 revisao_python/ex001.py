# Conversão de Tipo de Dados: Escreva uma função que receba uma lista de tipos de dados mistos (inteiros, floats, strings) e converta todos os elementos para floats. Lide com possíveis erros (por exemplo, se uma string não puder ser convertida para float, substitua-a por None).

def converter_lista(lista):
    for p, i in enumerate(lista):
        try: 
            lista[p] = float(i)
        except:
            lista[p] = None
    return lista

lista =[2006, "Maria", "Jose", 85, 9.4, "752", "Pedro", 75, "Joao", "Mateus", 0.4, 455, "7.5", "5220"]
nova_lista = converter_lista(lista)
print(nova_lista)

# output: [2006.0, None, None, 85.0, 9.4, 752.0, None, 75.0, None, None, 0.4, 455.0, 7.5, 5220.0]


# Sugestão da IA | Criando uma nova lista para os dados alterados e incluindo uma função separada para conversão
def converter_para_float(elemento):
    """
    Tenta converter um elemento para float. Retorna None se a conversão falhar.
    """
    try:
        return float(elemento)
    except ValueError:
        return None

def converter_lista(lista_original):
    """
    Recebe uma lista de tipos de dados mistos e retorna uma nova lista com todos os
    elementos convertidos para float ou None em caso de falha.
    """
    nova_lista = []
    for elemento in lista_original:
        nova_lista.append(converter_para_float(elemento))
    return nova_lista

# Exemplo de uso:
lista_original = [2006, "Maria", "Jose", 85, 9.4, "752", "Pedro", 75, "Joao", "Mateus", 0.4, 455, "7.5", "5220"]
nova_lista = converter_lista(lista_original)
print(nova_lista)
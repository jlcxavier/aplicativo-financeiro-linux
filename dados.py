import json
import os

ARQUIVO_DADOS = "transacoes.json"


def carregar_dados():
    """
    Carrega as transações salvas em um arquivo JSON.
    :return: Lista de transações.
    """
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as arquivo:
            return json.load(arquivo)
            print('Dados carregados do JSON: ', dados)
            return dados
    return []


def salvar_dados(transacoes):
    """
    Salva a lista de transações em um arquivo JSON.
    :param transacoes: Lista de transações.
    """
    with open(ARQUIVO_DADOS, "w") as arquivo:
        json.dump(transacoes, arquivo, indent=4)


def adicionar_transacao(tipo, valor, data, descricao):
    """
    Adiciona uma nova transação ao arquivo JSON.
    :param tipo: Tipo da transação (Entrada ou Saída).
    :param valor: Valor da transação.
    :param data: Data da transação.
    :param descricao: Descrição da transação.
    """
    transacoes = carregar_dados()
    nova_transacao = {
        "tipo": tipo,
        "valor": valor,
        "data": data,
        "descricao": descricao
    }
    transacoes.append(nova_transacao)
    salvar_dados(transacoes)

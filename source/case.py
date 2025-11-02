# Importar biblioteca para ler o arquivo .json
import json

# Lê os dados dos clientes do JSON externo.
def ler_json_clientes():
    try:
        with open("source/exemplos.json", "r", encoding="utf-8") as arquivo:
            data_json = json.load(arquivo)
        return data_json
    # Caso o arquivo não seja válido, a função retornará nada, e o relatório final será um json vazio
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return None

# Calcula listas para o futuro somatório de numerador e denominador do risco antes e depois da nova ordem.
def numerador_denominador(nova_ordem: dict, carteira: list[dict]):
    # Listas pré nova ordem
    pre_numerador = [ativo["risco"] * ativo["valor_investido"] for ativo in carteira]
    pre_denominador = [ativo["valor_investido"] for ativo in carteira]
    # Listas pós nova ordem
    pos_numerador = pre_numerador + [(nova_ordem["risco"] * nova_ordem["valor_ordem"])]
    pos_denominador = pre_denominador + [nova_ordem["valor_ordem"]]

    return pre_numerador, pre_denominador, pos_numerador, pos_denominador

# Com base no return da função numerador_denominador(), cálcula o risco da carteira antes e depois da nova ordem.
def calcular_risco_carteira(nova_ordem: dict, carteira: list[dict]):
    pre_numerador, pre_denominador, pos_numerador, pos_denominador = numerador_denominador(nova_ordem, carteira)
    risco_atual = round(sum(pre_numerador) / sum(pre_denominador), 2)
    risco_pos = round(sum(pos_numerador) / sum(pos_denominador), 2)

    return risco_atual, risco_pos

# Com base no score_max_risco de cada cliente, define o status da nova ordem: Aprovado, Alerta, Rejeitado (Critérios no README)
def validacao(risco_atual, risco_pos, i, score_max):

    valid_aprov = score_max * 1.1
    valid_leve = score_max * 1.4

    # Caso onde o risco pós nova ordem é menor ou igual que o limite de 110% do score_max_risco do cliente
    if risco_pos < valid_aprov:
        saida = {
                "cliente": i,
                "status": "Aprovado",
                "risco_projetado": risco_pos,
                "mensagem": "Ordem executada. Carteira em conformidade"
            }
        return saida
    # Caso onde o risco pós nova ordem ultrapassa o limite de 110% do score_max_risco do cliente, entretanto
    # é possível prosseguir com a assinatura do termo de ciência
    elif risco_pos <= valid_leve:
        saida = {
                "cliente": i,
                "status": "Alerta",
                "risco_projetado": risco_pos,
                "mensagem": f"Atenção: O risco da carteira ultrapassará o limite de {round((score_max * 1.1), 2)}. É necessário termo de ciência."
            }
        return saida
    # Caso onde o risco pós nova ordem está muito acima do limite de 110% do score_max_risco do cliente
    elif risco_pos > valid_leve:
        saida = {
                "cliente": i,
                "status": "Rejeitado",
                "risco_projetado": risco_pos,
                "mensagem": "Risco excessivo. A operação viola a política de Suitability."
            }
        return saida

# Gera a lista de informações necessárias para o relatório final
def saida() -> list:
    data_json = ler_json_clientes()
    saida = []
    if not data_json:
        print("Nenhum dado para processar. Por favor verifique se o arquivo selecionado é o correto.")
        return saida
    else:
        # Iteração sobre os clientes, cálculo do risco e arquivamento de cada validação na lista saida
        for i, cliente in enumerate(data_json):
            risco_atual, risco_pos = calcular_risco_carteira(cliente["nova_ordem"], cliente["carteira"])
            info_valid = validacao(risco_atual, risco_pos, i, cliente["score_max_risco"])
            saida.append(info_valid)

    return saida

# Gera o relatório final em formato json com as validações feitas de cada cliente
def gerar_relatorio_json():
    relatorio = saida()
    with open(r"source/relatorio_case.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent = 4, ensure_ascii=False)

    return relatorio

def main():
    gerar_relatorio_json()
    print("Case Finalizado!")

# Em caso de outro arquivo .py precisar usar alguma função desse "case.py", somente a função importada será aplicada lá (além de facilitar testes unitários)
if __name__ == "__main__":
    main()
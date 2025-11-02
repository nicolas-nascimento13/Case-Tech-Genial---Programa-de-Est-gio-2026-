# Importar biblioteca para ler o arquivo .json
import json

# Função para 
def numerador_denominador(nova_ordem: dict, carteira: list[dict]) -> float:
    pre_numerador = [ativo["risco"] * ativo["valor_investido"] for ativo in carteira]
    pre_denominador = [ativo["valor_investido"] for ativo in carteira]
    pos_numerador = pre_numerador + [(nova_ordem["risco"] * nova_ordem["valor_ordem"])]
    pos_denominador = pre_denominador + [nova_ordem["valor_ordem"]]
    return pre_numerador, pre_denominador, pos_numerador, pos_denominador

def calcular_risco_carteira(nova_ordem: dict, carteira: list[dict]) -> float:
    pre_numerador, pre_denominador, pos_numerador, pos_denominador = numerador_denominador(nova_ordem, carteira)
    risco_atual = round(sum(pre_numerador) / sum(pre_denominador), 2)
    risco_pos = round(sum(pos_numerador) / sum(pos_denominador), 2)
    return risco_atual, risco_pos

def validacao(risco_atual, risco_pos, i, score_max):

    valid_aprov = score_max * 1.1
    valid_leve = score_max * 1.5

    if risco_pos <= valid_aprov:
        saida = {
                "cliente": i,
                "status": "Aprovado",
                "risco_projetado": risco_pos,
                "mensagem": "Ordem executada. Carteira em conformidade"
            }
        return saida
    elif risco_pos <= valid_leve:
        saida = {
                "cliente": i,
                "status": "Alerta",
                "risco_projetado": risco_pos,
                "mensagem": f"Atenção: O risco da carteira ultrapassará o limite de {round((score_max * 1.1), 2)}. É necessário termo de ciência."
            }
        return saida
    elif risco_pos > valid_leve:
        saida = {
                "cliente": i,
                "status": "Rejeitado",
                "risco_projetado": risco_pos,
                "mensagem": "Risco excessivo. A operação viola a política de Suitability."
            }
        return saida

def saida_relatorio(data_json) -> str:
    # Iteração sobre os clientes e cálculo do risco
    relatorio = []
    for i, cliente in enumerate(data_json):
        risco_atual, risco_pos = calcular_risco_carteira(cliente["nova_ordem"], cliente["carteira"])
        saida = validacao(risco_atual, risco_pos, i, cliente["score_max_risco"])
        relatorio.append(saida)

    with open(r"source/relatorio_case.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent = 4, ensure_ascii=False)

    return relatorio

def main():
    # Leitura do arquivo JSON
    try:
        with open("source/exemplos1.json", "r", encoding="utf-8") as arquivo:
            data_json = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao ler o arquivo JSON: {e}")
        return
    saida_relatorio(data_json)
    print("Case Finalizado!")


# Em caso de outro arquivo .py precisar usar alguma função desse "case.py", somente a função importada será aplicada lá (além de facilitar testes unitários)
if __name__ == "__main__":
    main()
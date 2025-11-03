# Case Tech | Genial Investimentos - Programa de Estágio de Férias 2026

Este repositório contém o projeto Motor de Validação de Suitability de Carteira (CVM 30) desenvolvido utilizando Python. Neste arquivo README você encontrará o que esse motor de validação faz, considerando suas especifidades

---
## Estrutura do json dos clientes
```
[
    {
        "perfil": "Moderado",
        "score_max_risco": 3.0,
        "carteira": [
            { "ativo": "FII Residencial", "risco": 2.4, "valor_investido": 10000 },
            { "ativo": "ETF Setorial", "risco": 2.7, "valor_investido": 9000 }
        ],
        "nova_ordem": { "ativo": "Debênture Verde", "risco": 3.1, "valor_ordem": 4800 }
    },
  .
  .
  .
]
```
## Cálculo do Risco da Carteira (Média Ponderada)

$$R_C = \frac{\sum_{i=1}^{n} \left( Risco_i \times ValorInvestido_i \right)}{\sum_{i=1}^{n} ValorInvestido_i}$$

## Regras de validação

| Status | Quando acontece |
|--------|-----------------|
| **Aprovado** | Risco ≤ Score máximo * 1.1 |
| **Alerta** | Score máximo < Score máximo × 1.1 < Risco |
| **Rejeitado** | Score máximo × 1.4 < Risco |

obs: regras de verificação com base no pdf do case

## Funcionalidade

Com base nas informações de cada cliente (estrutura json dos clientes), o motor verifica se o pedido de aquisição de novo ativo (nova_ordem), para a carteira já existente, infrigirá as Regras de Validação

## Estrutura de Saída após rodar a aplicação

```
[
    {
        "cliente": 0,
        "status": "Aprovado",
        "risco_projetado": 2.65,
        "mensagem": "Ordem executada. Carteira em conformidade"
    },
    .
    .
    .
]
```

Considerações: 
- Os arquivos "exemplos.json, exemplos_test0.json e exemplos_test1.json" foram gerados por inteligência artificial
- Para testar o seu próprio arquivo .json de clientes, você deve garantir que este obedeça à estrutura aqui especificada, renomear seu arquivo com o nome "exemplos.json" e, por fim, colocá-lo na pasta source

---

## Desenvolvido por

**Nicolas de Souza Fonseca Nascimento**

Case Técnico - Programa de Estágio de Férias Genial Investimentos 2026

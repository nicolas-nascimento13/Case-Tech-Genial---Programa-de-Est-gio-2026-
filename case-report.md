# Relatório (Visão de Negócio)

## 1. Regulação vs. Negócio

Se o cliente, ao receber o Alerta, insistir em prosseguir com a compra (permitido pela CVM com Termo de Ciência), as principais implicações tecnológicas e de compliance que a Genial deve prever são:

- **Registro Eletrônico do Termo de Ciência:** O aceite do cliente deve ser armazenado de forma íntegra e rastreável, vinculado à movimentação e ao próprio cliente.
- **Log de Auditoria:** Cada aceite deve ser logado com data/hora, cliente, canal e natureza do aviso — garantindo histórico confiável para fiscalizações.
- **Execução Condicional:** A ordem só deve ser executada após o registro formal do Termo; o sistema deve bloquear pedidos sem termo aceito.
- **Proteção de Dados:** Logs e termos precisam ser protegidos contra edição/remoção, assegurando atendimento às normas da CVM e LGPD.
- **Rastreabilidade:** Os registros devem ser facilmente localizáveis por identificador de cliente, ordem, motivo e data, a fim de responder prontamente em auditorias.

## 2. Desenquadramento Passivo

Para monitorar o desenquadramento passivo (quando o risco da carteira aumenta apenas por movimento de mercado), o sistema da Genial deve:

- **Monitoramento Automático:** Analisar as carteiras periodicamente, recalculando o risco global sem depender de novas ordens.
- **Alertas Automatizados:** Detectar qualquer desenquadramento causado por volatilidade e acionar logs automáticos do evento.
- **Notificação Multicanal:**
    - **App:** Notificações push rápidas.
    - **E-mail:** Comunicação formal, rastreável e fácil de consultar.
    - **Assessor:** Intervenção proativa nos clientes sensíveis, feita por equipe especializada.
- **Registro de Comunicação:** Todo envio de alerta deve ser registrado com data, canal, destinatário e motivo para garantir rastreabilidade e compliance.

---

> *Este relatório responde diretamente aos tópicos exigidos no desafio de Suitability, com foco regulatório, tecnológico e de comunicação eficiente.*

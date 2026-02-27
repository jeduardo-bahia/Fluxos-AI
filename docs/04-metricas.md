# 📈 Avaliação e Métricas: Fluxos AI

Este guia orienta como validar a eficácia do agente, garantindo que a inteligência artificial e o motor de cálculo estejam sincronizados.

---

## 🧐 Como Avaliar o Agente
A avaliação do Fluxos AI é realizada através de duas frentes complementares:

1.  **Testes Estruturados:** Validação técnica se a resposta da LLM corresponde exatamente aos cálculos do `FinancialAnalyzer` baseados no `transacoes.csv`.
2.  **Feedback Real:** Testes de usabilidade via interface Streamlit para avaliar a experiência do usuário e clareza das respostas.

---

## 📊 Métricas de Qualidade

| Métrica | O que avalia | Exemplo Aplicado |
| :--- | :--- | :--- |
| **Assertividade** | O agente respondeu exatamente o que foi perguntado? | Perguntar "Qual meu saldo?" e receber o valor exato do CSV. |
| **Segurança** | O agente evitou inventar informações (Anti-Alucinação)? | Ao perguntar sobre o tempo, o agente reforça que só entende de finanças. |
| **Coerência** | A resposta faz sentido com o contexto dos dados? | Se o saldo é negativo, o agente não deve dizer que a saúde financeira está ótima. |
| **Consistência** | Os valores batem com os cálculos determinísticos? | Conferir se `Entradas - Saídas = Saldo` exibido no chat. |

> [!TIP]
> **Dica de Validação:** Peça para 3-5 pessoas testarem o agente via Streamlit e darem nota de 1 a 5 para cada métrica acima. Certifique-se de que eles saibam que os dados vêm do arquivo `data/transacoes.csv`.

---

## 🧪 Cenários de Teste (Checklist)

### Teste 1: Consulta de Saldo
* **Pergunta:** "Qual meu saldo?"
* **Resposta esperada:** Valor exato retornado pela função `saldo()`.
* **Resultado:** `[ ] Correto` | `[ ] Incorreto`

### Teste 2: Total de Saídas
* **Pergunta:** "Quanto eu gastei?"
* **Resposta esperada:** Valor exato retornado por `total_saidas()`.
* **Resultado:** `[ ] Correto` | `[ ] Incorreto`

### Teste 3: Maior Categoria de Gasto
* **Pergunta:** "Qual categoria com maior gasto?"
* **Resposta esperada:** Categoria retornada por `percentual_categoria()` com valor e % corretos.
* **Resultado:** `[ ] Correto` | `[ ] Incorreto`

### Teste 4: Pergunta Fora do Escopo
* **Pergunta:** "Qual a previsão do tempo para amanhã?"
* **Resposta esperada:** Agente informa educadamente que é especializado apenas em análise financeira.
* **Resultado:** `[ ] Correto` | `[ ] Incorreto`

### Teste 5: Informação Inexistente
* **Pergunta:** "Quanto rendeu meu investimento em ações?"
* **Resposta esperada:** Agente informa que não possui esses dados no fluxo de caixa atual.
* **Resultado:** `[ ] Correto` | `[ ] Incorreto`

---

## 📝 Registro de Resultados

### ✅ O que funcionou bem
* Cálculos determinísticos garantem precisão numérica absoluta.
* A arquitetura Híbrida (LLM para intenção + Python para cálculo) eliminou alucinações matemáticas.
* Respostas objetivas e tom de voz alinhado ao microempreendedor.

### 🛠️ O que pode melhorar
* **Interpretação:** Refinar a compreensão de perguntas complexas (ex: gastos por mês específico).
* **UX/UI:** Implementar visualização de gráficos (barras/pizza) diretamente no Streamlit.
* **Performance:** Implementar cache para reduzir latência e consumo da API do Gemini.

---

## ⚙️ Métricas Técnicas (Roadmap)
Para a evolução do projeto, considere monitorar:
* **Latência:** Tempo médio de resposta da API.
* **Consumo de Tokens:** Controle de custos por sessão.
* **Logs de Intenção:** Mapear quais perguntas a LLM não conseguiu classificar corretamente.
* **Fallback Local:** Criar uma camada de Regex/Palavras-chave para quando a API estiver offline.
![Status](https://img.shields.io/badge/status-completo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-Llama3-black?logo=ollama)
![License](https://img.shields.io/badge/licença-educacional-lightgrey)
![Bootcamp](https://img.shields.io/badge/Bootcamp-Bradesco-blue)
![IA Local](https://img.shields.io/badge/IA-local-purple?logo=ai)
![Pandas](https://img.shields.io/badge/Pandas-data-150458?logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-charts-3F4F75?logo=plotly)

![Banner](assets/banner_fluxosai.png)

# Fluxos AI

> Assistente inteligente de análise de fluxo de caixa com IA local (Ollama/Llama3).  
> Projeto desenvolvido no **Bootcamp GenAI & Dados – Bradesco**.

---

## 📌 Sobre o Projeto

O **Fluxos AI** é uma aplicação web construída com **Streamlit** que permite ao usuário fazer upload de um arquivo CSV financeiro e obter análises automáticas, visualizações gráficas e respostas inteligentes baseadas nos próprios dados — tudo isso usando um modelo de linguagem local via **Ollama**, sem custos de API externa.

---

## ✨ Funcionalidades

- 📂 Upload de arquivo CSV financeiro
- 📊 Cálculo automático de entradas, saídas e saldo
- 📈 Visualização gráfica por categoria (gráfico de barras interativo)
- 🤖 Assistente com IA para responder perguntas sobre os dados
- 🔒 Processamento 100% local — nenhum dado sai da sua máquina

---

## 💬 Perguntas Suportadas pelo Assistente

- Qual é o meu saldo?
- Qual categoria teve maior saída?
- Qual categoria teve maior entrada?
- Quanto gastei com logística?
- Qual foi minha maior despesa?

---

## 📁 Estrutura do Projeto

```
fluxos-ai/
├── app/
│   └── streamlit_app.py       # Interface principal (Streamlit)
├── core/
│   └── financial_analyzer.py  # Processamento e análise do CSV
├── data/
│   └── fluxo_caixa_teste.csv  # Arquivo de exemplo para testes
├── docs/                       # Documentação técnica
├── services/
│   ├── llm_service.py         # Integração com Ollama
│   └── report_generator.py    # Geração de relatório financeiro
├── assets/
│   └── banner.png             # Banner do projeto
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.11+ | Linguagem principal |
| Streamlit | Interface web |
| Pandas | Processamento de dados |
| Plotly | Visualização gráfica |
| Ollama + Llama3 | Modelo de linguagem local |
| Requests | Comunicação com a API do Ollama |

---

## ▶️ Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/jeduardo-bahia/fluxos-ai.git
cd fluxos-ai
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Instale o Ollama e baixe o modelo**

Acesse [https://ollama.com](https://ollama.com), instale e execute:
```bash
ollama pull llama3
```

**5. Execute a aplicação**
```bash
streamlit run app/streamlit_app.py
```

> ⚠️ Certifique-se de usar `streamlit run` e não `python streamlit_app.py` diretamente.

---

## 📦 Dependências

```txt
streamlit
pandas
plotly
requests
ollama
```

> Ou instale tudo de uma vez: `pip install -r requirements.txt`

---

## 🎯 Arquitetura

```
CSV Upload
    ↓
FinancialAnalyzer  →  Métricas + Gráficos
    ↓
Contexto Estruturado
    ↓
LLMService (Ollama/Llama3)
    ↓
Resposta ao Usuário
```

O usuário envia um CSV → o sistema processa e calcula métricas → monta um contexto estruturado → a LLM interpreta a pergunta e responde com base exclusivamente nos dados fornecidos.

---

## 🚀 Possíveis Evoluções

- [ ] Exportação de relatórios em PDF
- [ ] Deploy em nuvem (Streamlit Cloud / Railway)
- [ ] Autenticação de usuários
- [ ] Dashboard executivo
- [ ] Banco de dados persistente
- [ ] Implementação de RAG completo
- [ ] Fine-tuning de prompts

---

## 👨‍💻 Autor

Desenvolvido por **Jhonanthan Bahia**  
Bootcamp GenAI & Dados – Bradesco

---

## 📄 Licença

Projeto desenvolvido para fins educacionais e demonstração técnica.

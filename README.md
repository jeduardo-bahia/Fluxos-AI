# 💰 Fluxos AI

Assistente inteligente para análise de fluxo de caixa com IA local (Ollama)  
Projeto desenvolvido para o Bootcamp GenAI & Dados – Bradesco

## 🚀 Visão Geral

O Fluxos AI é uma aplicação web desenvolvida com Streamlit que permite:  
📂 Upload de arquivo CSV financeiro  
📊 Análise automática de entradas, saídas e saldo  
📈 Visualização gráfica por categoria  
🤖 Interpretação inteligente de perguntas usando LLM (Ollama)  
🧠 Respostas baseadas exclusivamente nos dados enviados  

A aplicação utiliza um modelo local via Ollama (Llama3), eliminando custos com API externa e problemas de cota.

## 🏗️ Arquitetura do Projeto

<img width="487" height="734" alt="image" src="https://github.com/user-attachments/assets/36ee85ba-bb0f-4aea-889c-af89165f2533" />



## 🧠 Como Funciona

O usuário envia um CSV com colunas como:  
data, tipo (entrada/saida), categoria, valor  

O sistema:  
- Processa os dados  
- Calcula métricas financeiras  
- Gera gráficos interativos  
- Monta um contexto estruturado  

A LLM:  
- Interpreta a intenção da pergunta  
- Consulta o contexto  
- Retorna resposta baseada nos dados

## 🛠️ Tecnologias Utilizadas

Python 3.11+, Streamlit, Plotly, Pandas, Ollama, Llama3

## ⚙️ Instalação

1️⃣ Clone o repositório  
`git clone https://github.com/jeduardo-bahia/fluxos-ai.git`  
`cd fluxos-ai`  

2️⃣ Crie o ambiente virtual  
`python -m venv venv`  
`venv\Scripts\activate  # Windows`  

3️⃣ Instale as dependências  
`pip install -r requirements.txt`  

Caso não tenha requirements.txt, instale manualmente:  
`pip install streamlit pandas plotly ollama`  

4️⃣ Instale o Ollama  
Baixe em: https://ollama.com  
Depois rode:  
`ollama pull llama3`  

5️⃣ Execute o projeto  
`streamlit run app/streamlit_app.py`

## 📊 Exemplo de Uso

Perguntas que podem ser feitas:  
- Qual meu saldo?  
- Qual categoria teve maior saída?  
- Qual categoria teve maior entrada?  
- Quanto gastei com logística?  
- Qual foi minha maior despesa?  

## 🎯 Diferenciais

✔ Uso de LLM local (sem custo de API)  
✔ Análise contextual baseada em dados reais  
✔ Interface profissional  
✔ Estrutura modular e escalável  
✔ Separação clara entre Core, Services e App  

## 📈 Possíveis Evoluções

Exportação de relatórios PDF, Deploy em nuvem, Autenticação de usuários, Dashboard executivo, Banco de dados persistente, Fine-tuning de prompts, Implementação de RAG completo

## 👑 Autor

Desenvolvido por Jhonanthan Bahia  
Bootcamp GenAI & Dados – Bradesco

## 📜 Licença

Projeto para fins educacionais e demonstração técnica

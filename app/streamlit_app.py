import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import plotly.express as px
from core.financial_analyzer import FinancialAnalyzer
from services.llm_service import LLMService

# ================= CONFIG =================
st.set_page_config(
    page_title="Fluxos AI",
    page_icon="💹",
    layout="wide"
)

# ================= CSS PROFISSIONAL =================
st.markdown("""
<style>

/* Fundo geral */
body {
    background: linear-gradient(135deg, #0E1117 0%, #111827 100%);
}

/* Centraliza conteúdo */
.block-container {
    max-width: 1100px;
    margin: auto;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Título central */
h1 {
    text-align: center;
    font-weight: 700;
}

/* Cards métricas */
div[data-testid="metric-container"] {
    background-color: #161B22;
    padding: 25px;
    border-radius: 14px;
    border: 1px solid #30363D;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}

/* Upload box */
section[data-testid="stFileUploader"] {
    background-color: #161B22;
    padding: 25px;
    border-radius: 14px;
    border: 1px solid #30363D;
}

/* Form pergunta */
div[data-testid="stForm"] {
    background-color: #161B22;
    padding: 25px;
    border-radius: 14px;
    border: 1px solid #30363D;
}

/* Botão */
button[kind="primary"] {
    border-radius: 8px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ================= FUNÇÃO MOEDA =================
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ================= HEADER =================
st.title("💹 Fluxos AI")
st.caption("Plataforma inteligente de análise financeira baseada em IA")

st.divider()

# ================= UPLOAD =================
uploaded_file = st.file_uploader("📂 Envie seu arquivo CSV", type=["csv"])

if uploaded_file:

    analyzer = FinancialAnalyzer(uploaded_file)
    resumo = analyzer.get_resumo()
    llm = LLMService()

    # ===== RESUMO =====
    st.subheader("📊 Resumo Financeiro")

    col1, col2, col3 = st.columns(3)

    col1.metric("Entradas", formatar_moeda(resumo["total_entradas"]))
    col2.metric("Saídas", formatar_moeda(resumo["total_saidas"]))
    col3.metric("Saldo", formatar_moeda(resumo["saldo"]))

    st.divider()

    # ===== GRÁFICO =====
    st.subheader("📊 Distribuição por Categoria")

    categoria = analyzer.df.groupby(
        ["tipo", "categoria"]
    )["valor"].sum().reset_index()

    fig = px.bar(
        categoria,
        x="valor",
        y="categoria",
        color="tipo",
        orientation="h",
        template="seaborn"
    )

    fig.update_layout(
        plot_bgcolor="#161B22",
        paper_bgcolor="#161B22",
        font=dict(color="white", size=14),
        xaxis=dict(
            title_font=dict(color="white"),
            tickfont=dict(color="white")
        ),
        yaxis=dict(
            title_font=dict(color="white"),
            tickfont=dict(color="white")
        ),
        legend=dict(font=dict(color="white"))
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ===== CONTEXTO PARA IA =====
    resumo_categorias = analyzer.df.groupby(
        ["tipo", "categoria"]
    )["valor"].sum().reset_index()

    resumo_categorias["valor"] = resumo_categorias["valor"].apply(formatar_moeda)

    contexto = f"""
Resumo Geral:
Total de Entradas: {formatar_moeda(resumo["total_entradas"])}
Total de Saídas: {formatar_moeda(resumo["total_saidas"])}
Saldo: {formatar_moeda(resumo["saldo"])}

Distribuição por Categoria:
{resumo_categorias.to_string(index=False)}
"""

    # ===== PERGUNTA =====
    st.subheader("🤖 Pergunte ao Assistente")

    with st.form("form_pergunta", clear_on_submit=True):
        pergunta = st.text_input("Digite sua pergunta")
        submitted = st.form_submit_button("Consultar")

    if submitted and pergunta:
        with st.spinner("Consultando IA..."):
            resposta = llm.responder_contextual(pergunta, contexto)

        st.success(resposta)

else:
    st.info("Envie um arquivo CSV para começar.")
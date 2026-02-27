class ReportGenerator:

    @staticmethod
    def gerar_relatorio(resumo):
        entradas = resumo["total_entradas"]
        saidas = resumo["total_saidas"]
        saldo = resumo["saldo"]
        maior_categoria = resumo.get("maior_categoria", "N/A")
        valor_maior = resumo.get("valor_maior_categoria", 0)

        status = "positivo ✅" if saldo >= 0 else "negativo ⚠️"

        relatorio = f"""
===== RELATÓRIO FINANCEIRO =====

Total de Entradas: R$ {entradas:.2f}
Total de Saídas:   R$ {saidas:.2f}
Saldo Final:       R$ {saldo:.2f} ({status})

Categoria com maior impacto nas despesas:
- {maior_categoria} → R$ {valor_maior:.2f}

Análise:
Seu saldo está {status}.
A categoria que mais impacta seu orçamento é '{maior_categoria}'.
Recomenda-se revisar despesas relacionadas a essa categoria para otimizar seu fluxo de caixa.

=================================
"""

        return relatorio
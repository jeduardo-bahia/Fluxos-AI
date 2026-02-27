import pandas as pd

class FinancialAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df.columns = self.df.columns.str.lower()
        self.df["valor"] = pd.to_numeric(self.df["valor"], errors="coerce").fillna(0)

        self.df["tipo"] = self.df["tipo"].str.lower().str.strip()
        self.df["categoria"] = self.df["categoria"].str.lower().str.strip()

    def total_entradas(self):
        return self.df[self.df["tipo"] == "entrada"]["valor"].sum()

    def total_saidas(self):
        return self.df[self.df["tipo"] == "saida"]["valor"].sum()

    def saldo(self):
        return self.total_entradas() - self.total_saidas()

    def resumo_categorias(self):
        despesas = self.df[self.df["tipo"] == "saida"]

        if despesas.empty:
            return None, 0, None, 0

        categoria = despesas.groupby("categoria")["valor"].sum()

        maior_categoria = categoria.idxmax()
        valor_maior = categoria.max()

        menor_categoria = categoria.idxmin()
        valor_menor = categoria.min()

        return maior_categoria, valor_maior, menor_categoria, valor_menor

    def total_por_categoria(self, categoria_nome, tipo):
        categoria_nome = categoria_nome.lower().strip()
        tipo = tipo.lower().strip()

        df_cat = self.df[
            (self.df["tipo"] == tipo) &
            (self.df["categoria"] == categoria_nome)
        ]

        return df_cat["valor"].sum()

    def get_resumo(self):
        maior_cat, valor_maior, menor_cat, valor_menor = self.resumo_categorias()

        return {
            "total_entradas": self.total_entradas(),
            "total_saidas": self.total_saidas(),
            "saldo": self.saldo(),
            "maior_categoria": maior_cat,
            "valor_maior_categoria": valor_maior,
            "menor_categoria": menor_cat,
            "valor_menor_categoria": valor_menor
        }

    def menor_categoria(self):
        despesas = self.df[self.df["tipo"] == "saida"]

        if despesas.empty:
            return "Nenhuma", 0

        categoria = despesas.groupby("categoria")["valor"].sum()
        menor_categoria = categoria.idxmin()
        valor = categoria.min()

        return menor_categoria, valor
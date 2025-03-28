import pandas as pd
import streamlit as st


class BaseComponent:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def handle_melt(self, prefix: str, var_name: str, value_name: str) -> pd.DataFrame:
        return self.df.melt(
            id_vars=["curso"],
            value_vars=[col for col in self.df.columns if col.startswith(prefix)],
            var_name=var_name,
            value_name=value_name,
        )  # Converte as colunas de dummies em formato empilhado

    def order(
        self,
        data: pd.DataFrame,
        x: str,
        y: str,
        sort_by: str = None,
        ascending: bool = False,
    ) -> pd.DataFrame:
        if sort_by is None:
            sort_by = y

        return (
            data.groupby(x, as_index=False)[y]
            .sum()
            .sort_values(by=sort_by, ascending=ascending)
        )

    def plot(self, fig) -> None:
        st.plotly_chart(fig, use_container_width=True)

    def divider(self) -> None:
        st.markdown("---")

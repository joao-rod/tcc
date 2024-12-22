import pandas as pd
import streamlit as st


class BaseComponent:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def handle_melt(self, prefix: str, var_name: str, value_name: str):
        return self.df.melt(
            id_vars=["curso"],
            value_vars=[col for col in self.df.columns if col.startswith(prefix)],
            var_name=var_name,
            value_name=value_name,
        )  # Converte as colunas de dummies em formato empilhado

    def plot(self, fig):
        st.plotly_chart(fig, use_container_width=True)

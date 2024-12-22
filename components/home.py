import streamlit as st
import pandas as pd
import plotly.express as px
from components.sidebar import SidebarComponent
from components.base import BaseComponent


class HomeComponent(BaseComponent):
    def __init__(self, df: pd.DataFrame) -> None:
        super().__init__(df)
        self.select_curses = SidebarComponent(options=df["curso"].unique())

        st.title("Página Inicial")
        st.write("Bem-vindo à página inicial!")

    def histogram(self):
        df_melted = self.handle_melt("atv_cultural_", "atividade", "participacao")

        selected_curso = self.select_curses.selectboxes()

        df_filter = df_melted[df_melted["curso"] == selected_curso]

        figure = px.histogram(
            df_filter,
            x="atividade",
            y="participacao",
            title=f"Atividades culturais - {selected_curso}",
            labels={
                "atividade": "Atividades Culturais",
                "participacao": "Participação",
            },
        )

        return self.plot(figure)

    # Apenas para teste da navegação do menu na sidebar
    def line(self):
        df_melted = self.handle_melt("hab_musical_", "habilidade", "participacao")

        selected_curso = self.select_curses.selectboxes()

        df_filter = df_melted[df_melted["curso"] == selected_curso]

        figure = px.line(
            df_filter,
            x="habilidade",
            y="participacao",
            title=f"Habilidades musicaal - {selected_curso}",
            labels={
                "habilidade": "Habilidades musicais",
                "participacao": "Participação",
            },
        )

        return self.plot(figure)

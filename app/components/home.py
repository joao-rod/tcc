import streamlit as st
import pandas as pd
import plotly.express as px
from components.sidebar import SidebarComponent
from components.base import BaseComponent


class HomeComponent(BaseComponent):
    def __init__(self, df: pd.DataFrame) -> None:
        super().__init__(df)
        self.select_curses = SidebarComponent(options=df["curso"].unique())
        self.selected_curso = self.select_curses.selectboxes()

        st.title("Página Inicial")
        st.write("Bem-vindo à página inicial!")

    def histogram(self):
        df_melted = self.handle_melt("atv_cultural_", "atividade", "participacao")

        df_filter = df_melted[df_melted["curso"] == self.selected_curso]

        data = self.order(data=df_filter, x="atividade", y="participacao")

        figure = px.bar(
            data,
            x="atividade",
            y="participacao",
            title=f"Atividades culturais - {self.selected_curso}",
            labels={
                "atividade": "Atividades Culturais",
                "participacao": "Participação",
            },
        )

        return self.plot(figure)

    def histogram2(self):
        df_melted = self.handle_melt(
            "melhoria_alimentacao_", "alimentacao", "participacao"
        )

        df_filter = df_melted[df_melted["curso"] == self.selected_curso]

        data = self.order(data=df_filter, x="alimentacao", y="participacao")

        figure = px.bar(
            data,
            x="alimentacao",
            y="participacao",
            title=f"Atividades culturais - {self.selected_curso}",
            labels={
                "alimentacao": "Atividades Culturais",
                "participacao": "Participação",
            },
        )

        return self.plot(figure)

    def heatmap(self):
        heatmap_data = pd.crosstab(
            self.df["curso"],
            self.df["serie"],
        )

        fig = px.imshow(
            heatmap_data,
            labels=dict(x="Série", y="Curso", color="Distribuição"),
            x=heatmap_data.columns,
            y=heatmap_data.index,
            color_continuous_scale="Purples",
            title="Correlação entre Cursos e Serie",
        )

        return self.plot(fig)

    # def wordcloud(self):
    #     text = " ".join(self.df["melhoria_alimentacao"])

    #     wordcloud = WordCloud(
    #         width=800, height=400, background_color="white", max_font_size=32, collocations=False
    #     ).generate(text)

    #     fig, ax = plt.subplots(figsize=(4, 4))
    #     ax.imshow(wordcloud, interpolation="bilinear")
    #     ax.axis("off")

    #     st.pyplot(fig)

    # Apenas para teste da navegação do menu na sidebar
    def line(self):
        df_melted = self.handle_melt("hab_musical_", "habilidade", "participacao")

        df_filter = df_melted[df_melted["curso"] == self.selected_curso]

        figure = px.line(
            df_filter,
            x="habilidade",
            y="participacao",
            title=f"Habilidades musicaal - {self.selected_curso}",
            labels={
                "habilidade": "Habilidades musicais",
                "participacao": "Participação",
            },
        )

        return self.plot(figure)

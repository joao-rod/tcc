import streamlit as st


class SidebarComponent:
    def __init__(self, title="Filtros", options=None) -> None:
        self.title = title
        self.options = [] if options is None else options

    def navigation(self) -> str:
        st.sidebar.title(self.title)
        selected_option = st.sidebar.radio("Navegação", self.options)
        return selected_option

    def selectboxes(self) -> str:
        st.sidebar.title(self.title)
        selected_option = st.sidebar.selectbox("Selecione o curso:", self.options)

        return selected_option

    def sidebar_footer(self) -> None:
        st.sidebar.markdown("---")
        st.sidebar.write(
            "Desenvolvido por [Joao Rodrigues](https://github.com/joao-rod)"
        )

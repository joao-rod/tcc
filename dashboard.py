import streamlit as st
import pandas as pd
from components.sidebar import SidebarComponent
from components.home import HomeComponent

df = pd.read_csv("data.csv")

st.set_page_config(
    page_title="Dashboard - Censo Cultural",
    page_icon="📊",
    layout="wide",
)

sidebar = SidebarComponent(title="Páginas", options=["🏠️ Home", "📄 Pag2"])
navigator = sidebar.navigation()

if navigator == "🏠️ Home":
    component = HomeComponent(df)
    component.histogram()

elif navigator == "📄 Pag2":
    component = HomeComponent(df)
    component.line()

sidebar.sidebar_footer()

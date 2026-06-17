import streamlit as st
from streamlit_option_menu import option_menu
from pages.init_page import init_page
from pages.data_page import data_page

selected = option_menu(
    menu_title=None,
    options=["Home", "Analise de Dados"],
    icons=['house', 'bar-chart'],
    orientation="horizontal"
)

if selected == "Home":
    init_page()

elif selected == "Analise de Dados":
    data_page()
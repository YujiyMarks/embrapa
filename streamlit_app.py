import streamlit as st
from streamlit.logger import get_logger
import sqlite3

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(page_title="EMBRAPA",page_icon=":gear:",)
    st.title("Embrapa Agricultura Digital")
    st.sidebar.success("HOME")

    #dados = sqlite3.connect('bd_app.db')
    #cursor = dados.cursor()

if __name__ == "__main__":
    run()


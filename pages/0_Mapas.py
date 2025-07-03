import streamlit as st #biblioteca para a parte visual
import io

#conexão com o banco de dados
import sqlite3

#dados = sqlite3.connect('bd_app.db')
#cursor = dados.cursor()

def main():
    # configurações iniciais
    st.set_page_config(page_title="Mapas Oidio",page_icon="page_facing_up:",)
    st.sidebar.header("Mapas")

    st.title("Mapas Projeto OIDIO")

    observacao = st.text_input(f"Digite a observação do item:")

    lista = [1,2,3]
    itens = []
    item = st.selectbox(f"Escolha o item:",lista)
    itens.append(item)

    data = st.date_input("Data de elaboração:")
    img = st.file_uploader("Imagem geral:")
    if img is not None:
        st.image(img, use_column_width='always')

    st.header("ITENS")
    st.subheader(f"Item 1")
    # botão para escolha da quantidade de itens
    num_items = st.number_input("Número de itens:", min_value=1, step=1, value=1)

    analise = st.radio(f"Análise do item:",["C","NC","NA","PA"],horizontal=True)

    # botão para geração do relatório
    if st.button("Botão"):
        if 1:
            st.warning("Erro ao gerar o PDF.")


if __name__ == "__main__":
    main()

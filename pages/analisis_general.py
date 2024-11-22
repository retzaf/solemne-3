import pandas as pd
import streamlit as st


def show():
    # Cargar los datos
    try:
        book = pd.read_csv('books_of_the_decade.csv')
        user_reviews = pd.read_csv('user_reviews_dataset.csv')
        st.success('📊 ¡Datos cargados correctamente!')
    except FileNotFoundError as e:
        st.error(f"⚠️ Error al cargar los datos: {e}")
        st.stop()

    # Fusionar datasets
    books = pd.merge(user_reviews, book, left_on='bookIndex', right_on='Index', how='inner')

    # Mostrar los 10 mejores libros
    st.markdown("<h2>📊 Análisis General</h2>", unsafe_allow_html=True)
    st.subheader('Top 10 Libros de la Década por Puntaje')

    # Usar columnas para mostrar la tabla y la descripción
    col1, col2 = st.columns([2, 1])
    with col1:
        top_ten_books = book.sort_values(by='Score', ascending=False).head(10)
        st.dataframe(top_ten_books)

    with col2:
        st.markdown("""
        <div style='padding: 10px; background-color: #eef; border-radius: 8px;'>
        Aquí se muestran los 10 libros mejor rankeados de la década en base al puntaje total otorgado por los lectores.
        </div>
        """, unsafe_allow_html=True)

    st.divider()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def show():
    # Cargar los datos
    try:
        book = pd.read_csv('books_of_the_decade.csv')
        user_reviews = pd.read_csv('user_reviews_dataset.csv')
        st.success('📚 ¡Datos cargados correctamente!')
    except FileNotFoundError as e:
        st.error(f"⚠️ Error al cargar los datos: {e}")
        st.stop()

    # Fusionar datasets
    books = pd.merge(user_reviews, book, left_on='bookIndex', right_on='Index', how='inner')
    # Asegurarse de que 'Rating' sea numérico
    books['Rating'] = pd.to_numeric(books['Rating'], errors='coerce')

    # Eliminar filas donde 'Rating' no es un número
    books = books.dropna(subset=['Rating'])

    # Título de la sección
    st.markdown("<h2>✍️ Análisis por Autor</h2>", unsafe_allow_html=True)

    # Filtrar por autor
    author_list = books['Author'].dropna().unique()
    selected_author = st.selectbox('Selecciona un Autor:', sorted(author_list))

    # Datos del autor seleccionado
    author_books = books[books['Author'] == selected_author].drop_duplicates(
        subset=['Book Name', 'Score', 'Rating', 'Number of Votes'])

    if not author_books.empty:
        st.markdown(f"<h3>Libros de {selected_author}</h3>", unsafe_allow_html=True)
        st.dataframe(author_books[['Book Name', 'Score', 'Rating', 'Number of Votes']])

        # Estadísticas del autor
        author_stats = (
            author_books.groupby('Author')
            .agg(
                number_of_books=('Book Name', 'count'),
                total_score=('Score', 'sum'),
                average_rating=('Rating', 'mean')
            )
            .reset_index()
        )

        st.write('**Estadísticas del Autor:**')
        st.write(author_stats[['number_of_books', 'total_score', 'average_rating']])

        # Gráfico de calificaciones del autor seleccionado
        st.markdown(f"<h4>Distribución de Calificaciones para {selected_author}</h4>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(author_books['Rating'], kde=True, color='#0078D4', bins=10, ax=ax)
        ax.set_title(f'Distribución de Calificaciones para {selected_author}', fontsize=16)
        ax.set_xlabel('Calificación', fontsize=14)
        ax.set_ylabel('Frecuencia', fontsize=14)
        st.pyplot(fig)

        # Mostrar gráfico de los libros del autor por puntuación
        st.markdown(f"<h4>Top 10 Libros de {selected_author} por Puntuación</h4>", unsafe_allow_html=True)
        top_books_by_score = author_books.sort_values(by='Score', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(y=top_books_by_score['Book Name'], x=top_books_by_score['Score'], palette='viridis', ax=ax)
        ax.set_title(f'Top 10 Libros de {selected_author}', fontsize=16)
        ax.set_xlabel('Puntuación', fontsize=14)
        ax.set_ylabel('Nombre del Libro', fontsize=14)
        st.pyplot(fig)
    else:
        st.warning('⚠️ No se encontraron libros para este autor.')

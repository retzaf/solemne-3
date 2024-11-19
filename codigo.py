import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Configuración de la página de Streamlit
st.set_page_config(page_title='Análisis de Libros', layout='wide')
st.title('Análisis de los Mejores Libros de la Década 2330')

# Introducción
st.markdown("""
### Base de datos: Mejores Libros de la Década 2330
Esta aplicación se basa en una encuesta realizada a **600,000 lectores** para rankear los libros más destacados de la década.
""")

# Cargar archivos CSV con manejo de errores
try:
    book = pd.read_csv('books_of_the_decade.csv')
    user_reviews = pd.read_csv('user_reviews_dataset.csv')
    st.success('¡Datos cargados correctamente!')
except FileNotFoundError as e:
    st.error(f"Error al cargar los datos: {e}")
    st.stop()

# Fusionar datasets
books = pd.merge(user_reviews, book, left_on='bookIndex', right_on='Index', how='inner')

# Mostrar los 10 mejores libros
st.subheader('Top 10 Libros de la Década por Puntaje')
top_ten_books = book.sort_values(by='Score', ascending=False).head(10)
st.dataframe(top_ten_books)

# Añadir opciones de búsqueda por autor o por libro
st.sidebar.title('Búsqueda de Libros y Autores')
search_option = st.sidebar.radio('Buscar por:', ('Autor', 'Libro'))

if search_option == 'Autor':
    author_name = st.sidebar.text_input('Ingrese el nombre del autor')
    if author_name:
        filtered_books = books[books['Author'].str.contains(author_name, case=False, na=False)]
        st.subheader(f'Resultados de búsqueda para el autor: {author_name}')
        st.dataframe(filtered_books)
else:
    book_name = st.sidebar.text_input('Ingrese el nombre del libro')
    if book_name:
        filtered_books = books[books['Book Name'].str.contains(book_name, case=False, na=False)]
        st.subheader(f'Resultados de búsqueda para el libro: {book_name}')
        st.dataframe(filtered_books)

# Limpieza de datos
books['Rating'] = pd.to_numeric(books['Rating'], errors='coerce')
books['Number of Votes'] = pd.to_numeric(books['Number of Votes'], errors='coerce')
median_rating = books['Rating'].median()
books['Rating'].fillna(median_rating, inplace=True)
books['Number of Votes'].fillna(0, inplace=True)

# Parámetros de visualización interactivos
st.sidebar.title('Configuraciones de Visualización')
bins = st.sidebar.slider('Número de Bins para la Distribución de Calificaciones', min_value=5, max_value=50, value=10, step=1)
color_palette = st.sidebar.selectbox('Selecciona una Paleta de Colores', ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'Greens', 'Purples'])

# Estadísticas de autores
author_stats = (
    books.groupby('Author')
    .agg(
        number_of_books=('Book Name', 'count'),
        total_score=('Score', 'sum')
    )
    .reset_index()
)

# Mejores autores por puntaje total
top_authors = author_stats.sort_values(by='total_score', ascending=False)
st.subheader('Autores Más Vendidos por Puntaje Total')
st.dataframe(top_authors[['Author', 'number_of_books', 'total_score']].head(10))

# Gráfico interactivo de los mejores autores por puntaje total
st.subheader('Gráfico de los 10 Mejores Autores por Puntaje Total')
top_auth = top_authors['Author'].head(10)
top_scr = top_authors['total_score'].head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_scr.values, y=top_auth.values, palette=color_palette, ax=ax)
ax.set_title('Top 10 Autores por Puntaje Total')
ax.set_xlabel('Puntaje Total')
ax.set_ylabel('Autor')
st.pyplot(fig)

# Distribución de calificaciones
st.subheader('Distribución de Calificaciones de Libros')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(books['Rating'], bins=bins, kde=True, color='blue', ax=ax)
ax.set_title('Distribución de Calificaciones')
ax.set_xlabel('Calificación')
st.pyplot(fig)
color_input_1 = st.sidebar.color_picker("selecciona un color para el primer gráfico", '#00f900')
# Matriz de correlación
st.subheader('Matriz de Correlación')
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(books[['Rating', 'Number of Votes', 'Score']].corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Matriz de Correlación')
st.pyplot(fig)

# Gráfico de torta interactivo para autores
st.subheader('Distribución de los 10 Autores Principales por Cantidad de Libros')
fig, ax = plt.subplots(figsize=(8, 8))
author_counts = books['Author'].value_counts().head(10)
ax.pie(author_counts, labels=author_counts.index, autopct='%1.1f%%', startangle=140)
ax.set_title('Distribución de los 10 Autores Principales por Cantidad de Libros')
st.pyplot(fig)

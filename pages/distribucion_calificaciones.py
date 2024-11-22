import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def show():
    # Cargar los datos
    try:
        book = pd.read_csv('books_of_the_decade.csv')
        user_reviews = pd.read_csv('user_reviews_dataset.csv')
        st.success('📈 ¡Datos cargados correctamente!')
    except FileNotFoundError as e:
        st.error(f"⚠️ Error al cargar los datos: {e}")
        st.stop()

    # Fusionar datasets
    books = pd.merge(user_reviews, book, left_on='bookIndex', right_on='Index', how='inner')

    # Parámetros de visualización interactivos
    st.markdown("<h2>📈 Distribución de Calificaciones</h2>", unsafe_allow_html=True)
    bins = st.sidebar.slider('📊 Número de Bins para la Distribución de Calificaciones', min_value=5, max_value=50,
                             value=10, step=1)

    # Gráfico interactivo de distribución de calificaciones
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.set_style("whitegrid")
    sns.histplot(books['Rating'], bins=bins, kde=True, color='#4CAF50', ax=ax)
    ax.set_title('Distribución de Calificaciones', fontsize=18)
    ax.set_xlabel('Calificación', fontsize=16)
    ax.set_ylabel('Frecuencia', fontsize=16)

    # Ajustar rotación de las etiquetas del eje x
    ax.tick_params(axis='x', rotation=45)

    # Ajustar límites de los ticks del eje x
    ax.set_xticks(ax.get_xticks()[::5])  # Mostrar solo la mitad de los ticks para evitar solapamiento

    st.pyplot(fig)

import streamlit as st


def show():
    # Título principal estilizado
    st.markdown("<h1>🌟 Análisis de los Mejores Libros de la Década 2330 🌟</h1>", unsafe_allow_html=True)

    # Descripción introductoria
    st.markdown("""
    <div style='background-color:#f9f9f9; padding: 20px; border-radius: 10px;'>
    <h2>📚 Bienvenido a la Aplicación de Análisis de Libros 📚</h2>
    <p>
    Esta aplicación utiliza una base de datos de los <b>mejores libros de la década 2330</b>, basada en una encuesta a
    <b>600,000 lectores</b> para evaluar y rankear los libros más destacados.
    </p>
    <p>
    Utiliza el menú de la izquierda para navegar por las diferentes secciones:
    </p>
    <ul>
        <li><b>Análisis General:</b> Información sobre los mejores libros y autores.</li>
        <li><b>Distribución de Calificaciones:</b> Visualización interactiva de la distribución de calificaciones.</li>
        <li><b>Análisis por Autor:</b> Información detallada sobre los autores y sus puntuaciones.</li>
        <li><b>Búsqueda:</b> Encuentra libros o autores específicos en la base de datos.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Imagen decorativa
    st.image("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
             caption="Explora el mundo de la literatura", use_column_width=True)

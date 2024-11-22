import streamlit as st

# Configuración de la página principal de Streamlit
st.set_page_config(
    page_title='Análisis de Libros 📚',
    page_icon='📖',
    layout='wide'
)

# Agregar estilo personalizado con CSS
st.markdown(
    """
    <style>
    .css-18e3th9 {padding-top: 2rem;}  /* Ajustar el padding superior */
    .css-1offfwp {background-color: #f4f4f4;} /* Fondo claro para los controles */
    .css-h5rgaw {padding-bottom: 1rem;} /* Padding inferior */
    .css-1aumxhk {color: #6c757d;} /* Color del texto de la barra lateral */
    h1 {
        color: #ff6347;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    h2 {
        color: #0078D4;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Crear el menú de navegación
st.sidebar.title('🔍 Navegación')
menu = st.sidebar.radio(
    'Selecciona una página:',
    ['Inicio 🏠', 'Análisis General 📊', 'Distribución de Calificaciones 📈', 'Análisis por Autor ✍️', 'Búsqueda 🔎']
)

# Redirigir a la página correspondiente según el menú seleccionado
if menu == 'Inicio 🏠':
    from pages import inicio
    inicio.show()
elif menu == 'Análisis General 📊':
    from pages import analisis_general
    analisis_general.show()
elif menu == 'Distribución de Calificaciones 📈':
    from pages import distribucion_calificaciones
    distribucion_calificaciones.show()
elif menu == 'Análisis por Autor ✍️':
    from pages import analisis_autor
    analisis_autor.show()
elif menu == 'Búsqueda 🔎':
    from pages import busqueda
    busqueda.show()

import streamlit as st

st.markdown("<h1> Reconocimiento Facial 👤</h1>",unsafe_allow_html=True)
st.markdown("<h2>Descripción del Reconocimiento Facial</h2>",unsafe_allow_html=True)
st.markdown("""
            Como parte de nuestro proyecto final, hemos desarrollado un sistema de reconocimiento facial diseñado para identificar a una persona a partir de una imagen. Para lograrlo, utilizamos la biblioteca OpenCV en combinación con un modelo GPT, que proporciona una descripción detallada de la persona identificada, permitiendo obtener resultados precisos y enriquecidos.            
            """)

st.markdown("<h2>Subir imagen para hacer reconocimiento facial</h2>",unsafe_allow_html=True)
st.markdown("""
            Para realizar el reconocimiento facial, sube una imagen de una persona y presiona el botón de 'Analizar imagen'. Una vez que se haya procesado la imagen, se mostrará la imagen con un recuadro alrededor de la cara identificada y una descripción de la persona.            
            """)
st.file_uploader("Subir imagen para hacer reconocimiento facial", type=["jpg", "png", "jpeg"])

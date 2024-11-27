import streamlit as st
import openai
from PIL import Image

import os
import sys
import subprocess

# Instalar openai si no está instalado
try:
    import openai
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    import openai


OpenAI.api_key = st.secrets["OPENAI_API_KEY"]

st.markdown("<h1> Reconocimiento Facial 👤</h1>", unsafe_allow_html=True)
st.markdown("<h2>Descripción del Reconocimiento Facial</h2>", unsafe_allow_html=True)
st.markdown("""
            Como parte de nuestro proyecto final, hemos desarrollado un sistema de reconocimiento facial diseñado para identificar a una persona a partir de una imagen. Para lograrlo, utilizamos la biblioteca OpenCV en combinación con un modelo GPT, que proporciona una descripción detallada de la persona identificada, permitiendo obtener resultados precisos y enriquecidos.            
            """)

st.markdown("<h2>Subir imagen para hacer reconocimiento facial</h2>", unsafe_allow_html=True)
st.markdown("""
            Para realizar el reconocimiento facial, sube una imagen de una persona y presiona el botón de 'Analizar imagen'. Una vez que se haya procesado la imagen, se mostrará la imagen con un recuadro alrededor de la cara identificada y una descripción de la persona.            
            """)
uploaded_file = st.file_uploader("Subir imagen para hacer reconocimiento facial", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagen subida', use_column_width=True)
    except Exception as e:
        st.error("Por favor, sube un archivo válido.")
        st.stop()
    
    st.markdown("<h2>Descripción de la persona identificada</h2>", unsafe_allow_html=True)

    response = OpenAI.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user", 
                "content": (
                    f"Describe the person in the image, including their race, eye color, facial features, "
                    "and any other distinguishing characteristics."
                )
            }
        ]
    )

    description = response['choices'][0]['message']['content']
    st.markdown(description)
else:
    st.info("Por favor, sube una imagen para continuar.")


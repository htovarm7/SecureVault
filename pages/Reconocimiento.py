import streamlit as st
import secrets as sc
import OpenAi as openai
import os

from PIL import Image

openai.api_key = st.secrets("OPENAI_API_KEY")

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

try:
    image = Image.open(uploaded_file)
except Exception as e:
    st.error("Por favor, sube un archivo válido.")
    st.stop()

# Función para generar una descripción detallada usando la API de OpenAI
def generate_description(description):
    # Corregir el error tipográfico "rasgoz" -> "rasgos"
    prompt = "Describe la imagen de la persona basándote en sus rasgos físicos como posible nacionalidad, género, color de pelo, color de ojos, etc."
    
    try:
        # Llamada a la API de OpenAI para generar la respuesta
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150,  # Aumenté los tokens para obtener una respuesta más detallada
            temperature=0.7   # Temperatura moderada para obtener respuestas variadas pero coherentes
        )
        
        # Retornar solo el texto generado por la API
        return response.choices[0].text.strip()
    
    except Exception as e:
        return f"Error al generar la descripción: {e}"

# Interfaz de Streamlit
st.markdown("<h2>Descripción de la persona identificada</h2>", unsafe_allow_html=True)

# Obtener la descripción generada por la IA
response = generate_description(description)

# Mostrar la respuesta en Streamlit
st.write(response)  # Usamos st.write para mostrar la respuesta generada
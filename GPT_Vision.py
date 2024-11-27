import streamlit as st
import openai
from PIL import Image

# Configuración de la clave API de OpenAI
client = openai.OpenAI(api_key=st.secrets["OPEN_AI_KEY"])

# Título y descripción
st.markdown("<h2>Descripción del Reconocimiento Facial 👤</h2>", unsafe_allow_html=True)
st.markdown("""
            Como parte de nuestro proyecto final, hemos desarrollado un sistema de reconocimiento facial diseñado para identificar a una persona a partir de una imagen. Para lograrlo, utilizamos la biblioteca OpenCV en combinación con un modelo GPT, que proporciona una descripción detallada de la persona identificada, permitiendo obtener resultados precisos y enriquecidos.            
            """)

st.markdown("<h2>¿Cómo funciona el Reconocimiento Facial? ❓</h2>", unsafe_allow_html=True)
st.markdown("""
            El reconocimiento facial es una tecnología que permite identificar o verificar a una persona a partir de una imagen o un video. Para lograrlo, se utilizan algoritmos de visión por computadora que analizan las características faciales de una persona, como la forma de la cara, los ojos, la nariz, la boca, entre otros. Estas características se comparan con una base de datos de rostros previamente almacenados para determinar la identidad de la persona.
            """)

st.markdown("<h2>¿Por qué es importante el Reconocimiento Facial? 📍</h2>", unsafe_allow_html=True)
st.markdown("""
            El reconocimiento facial tiene diversas aplicaciones en la actualidad, desde la seguridad y la vigilancia hasta la autenticación biométrica y el marketing personalizado. Algunos de los usos más comunes del reconocimiento facial incluyen el desbloqueo de dispositivos móviles, el acceso a edificios y eventos, la identificación de sospechosos en investigaciones criminales, la personalización de anuncios y recomendaciones en línea, entre otros.
            """)
st.image("Imagenes/SeBusca.jpg", caption="Imagen de una persona buscada",  use_container_width = True)

st.markdown("<h2>Subir imagen para hacer reconocimiento facial 📷</h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Sube una imagen para hacer reconocimiento facial", type=["jpg", "png", "jpeg"])

# Procesar la imagen cargada y mostrar los resultados
if uploaded_file:
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=False)
        except Exception as e:
            st.error("Por favor, sube un archivo válido.")
            st.stop()
        
        st.markdown("<h2>Descripción de la persona identificada</h2>", unsafe_allow_html=True)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
            {
                "role": "user", 
                "content": (
                "Describe a la persona en la imagen, incluyendo su raza, color de ojos, características faciales "
                "y cualquier otra característica distintiva."
                )
            }
            ],
            max_tokens = 400,
            temperature = 0.7,
        )

        description = response.choices[0].message.content
        st.markdown(description)
else:
    st.info("Por favor, sube una imagen para continuar.")
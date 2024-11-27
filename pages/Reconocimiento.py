import streamlit as st
from openai import OpenAI
from PIL import Image

client = OpenAI(api_key = st.secrets["OPEN_AI_KEY"]) 

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

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user", 
                "content": (
                    f"Describe the person in the image, including their race, eye color, facial features, "
                    "and any other distinguishing characteristics."
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


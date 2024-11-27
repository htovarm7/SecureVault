import streamlit as st
import cv2
import numpy as np
from PIL import Image
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPEN_AI_KEY"])

st.markdown("<h1>Reconocimiento Facial 👤</h1>", unsafe_allow_html=True)

# Descripción del proyecto
st.markdown("""
    Como parte de nuestro proyecto final, hemos desarrollado un sistema de reconocimiento facial diseñado para identificar a una persona a partir de una imagen.
""")

# Subir imagen
uploaded_file = st.file_uploader("Sube una imagen para hacer reconocimiento facial", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagen subida", use_column_width=True)
        
        # Convertir imagen a un formato adecuado para OpenCV
        open_cv_image = np.array(image.convert('RGB'))
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)
        
        # Cargar el clasificador en cascada de OpenCV para detección facial
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Detectar caras en la imagen
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Dibujar un rectángulo alrededor de la cara detectada
        for (x, y, w, h) in faces:
            cv2.rectangle(open_cv_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Mostrar la imagen con el rectángulo
        image_with_box = Image.fromarray(open_cv_image)
        st.image(image_with_box, caption="Imagen con cara detectada", use_column_width=True)

        # Descripción de la persona
        st.markdown("<h2>Descripción de la persona identificada</h2>", unsafe_allow_html=True)
        
        # Generar descripción con GPT
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": "Describe a la persona en la imagen basándote en características generales como raza, color de ojos, y otros rasgos distintivos."
            }],
            max_tokens=400,
            temperature=0.7,
        )
        
        description = response.choices[0].message.content
        st.markdown(description)

    except Exception as e:
        st.error("Hubo un error procesando la imagen.")
        st.stop()
else:
    st.info("Por favor, sube una imagen para continuar.")

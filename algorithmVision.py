import streamlit as st
import cv2
import numpy as np
from PIL import Image
from openai import OpenAI
import base64
from deepface import DeepFace

client = OpenAI(api_key = st.secrets["OPEN_AI_KEY"]) 

st.markdown("<h1> Reconocimiento Facial 👤</h1>", unsafe_allow_html=True)
st.markdown("<h2>Descripción del Reconocimiento Facial</h2>", unsafe_allow_html=True)
st.markdown("""
            Como parte de nuestro proyecto final, hemos desarrollado un sistema de reconocimiento facial diseñado para identificar a una persona a partir de una imagen. Para lograrlo, utilizamos la biblioteca OpenCV en combinación con un modelo GPT, que proporciona una descripción detallada de la persona identificada, permitiendo obtener resultados precisos y enriquecidos.            
            """)

st.markdown("<h2>¿Cómo funciona el Reconocimiento Facial?</h2>", unsafe_allow_html=True)
st.markdown("""
            El reconocimiento facial es una tecnología que permite identificar o verificar a una persona a partir de una imagen o un video. Para lograrlo, se utilizan algoritmos de visión por computadora que analizan las características faciales de una persona, como la forma de la cara, los ojos, la nariz, la boca, entre otros. Estas características se comparan con una base de datos de rostros previamente almacenados para determinar la identidad de la persona.
            """)

st.markdown("<h2>¿Por qué es importante el Reconocimiento Facial?</h2>", unsafe_allow_html=True)
st.markdown("""
            El reconocimiento facial tiene diversas aplicaciones en la actualidad, desde la seguridad y la vigilancia hasta la autenticación biométrica y el marketing personalizado. Algunos de los usos más comunes del reconocimiento facial incluyen el desbloqueo de dispositivos móviles, el acceso a edificios y eventos, la identificación de sospechosos en investigaciones criminales, la personalización de anuncios y recomendaciones en línea, entre otros.
            """)
st.image("Imagenes/SeBusca.jpg", caption="Imagen de una persona buscada", use_column_width=True)

st.markdown("<h2>Subir imagen para hacer reconocimiento facial</h2>", unsafe_allow_html=True)
st.markdown("""
            Para realizar el reconocimiento facial, sube una imagen de una persona y presiona el botón de 'Analizar imagen'. Una vez que se haya procesado la imagen, se mostrará la imagen con un recuadro alrededor de la cara identificada y una descripción de la persona.            
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

        # Analizar la imagen con DeepFace para obtener más información (edad, género, emoción, etc.)
        analysis = DeepFace.analyze(np.array(image), actions=['age', 'gender', 'emotion'])

        # Extraer las características analizadas
        age = analysis['age']
        gender = analysis['gender']
        emotion = analysis['dominant_emotion']

        # Descripción de la persona con la información analizada
        st.markdown("<h2>Descripción de la persona identificada</h2>", unsafe_allow_html=True)
        description = f"La persona en la imagen tiene aproximadamente {age} años, su género es {gender} y la emoción predominante es {emotion}."
        st.markdown(description)

        # Generar una descripción más elaborada con GPT
        gpt_description = f"Describe a la persona en la imagen basándote en las siguientes características: edad aproximada: {age} años, género: {gender}, emoción predominante: {emotion}."
        
        response = client.chat_completions.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": gpt_description
            }],
            max_tokens=400,
            temperature=0.7,
        )
        
        gpt_text = response.choices[0].message['content']
        st.markdown(f"Descripción generada por GPT: {gpt_text}")

    except Exception as e:
        st.error(f"Hubo un error procesando la imagen: {str(e)}")
        st.stop()
else:
    st.info("Por favor, sube una imagen para continuar.")



import streamlit as st
import cv2
import base64
import numpy as np
from PIL import Image
import openai
import io as BytesIO

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
st.image("Imagenes/SeBusca.jpg", caption="Imagen de una persona buscada")

st.markdown("<h2>Subir imagen para hacer reconocimiento facial 📷</h2>", unsafe_allow_html=True)
st.markdown("""
            Para realizar el reconocimiento facial, sube una imagen de una persona y presiona el botón de 'Analizar imagen'. Una vez que se haya procesado la imagen, se mostrará la imagen con un recuadro alrededor de la cara identificada y una descripción de la persona.            
            """)

uploaded_file = st.file_uploader("Sube una imagen para hacer reconocimiento facial", type=["jpg", "png", "jpeg"])

def detect_face(image):
    # Convertir la imagen en formato de OpenCV
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Cargar el clasificador de rostro de OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    # Detectar rostros en la imagen
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    return faces, img

# Procesar la imagen cargada y mostrar los resultados
if uploaded_file:
    # Abrir la imagen usando PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    # Detectar rostros en la imagen
    faces, img = detect_face(image)

    # Dibujar un recuadro alrededor de cada rostro detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Convertir la imagen a formato PIL para mostrarla en Streamlit
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Si se detecta al menos un rostro, enviar el análisis a OpenAI
    if len(faces) > 0:
        # Convertir la imagen a base64 para enviarla a la API de OpenAI
        buffered = BytesIO()
        img_pil.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        # Crear el payload para la API de OpenAI
        payload = {
            "model": "text-davinci-003",
            "prompt": f"Describe físicamente a la persona en la imagen: {img_base64}",
            "max_tokens": 150
        }

        # Realizar la solicitud a la API de OpenAI
        response = client.Completion.create(**payload)

        # Obtener la descripción generada por la API
        description = response.choices[0].text.strip()

        # Mostrar la descripción en la aplicación
        st.markdown(f"**Descripción generada por la IA:** {description}")
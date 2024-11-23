import streamlit as st
import secrets as sc
import openai
import cv2
import numpy as np
import os


from PIL import Image

openai.api_key = os.getenv("OPENAI_API_KEY")

# sc.CLIENT_ID

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


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida.', use_column_width=True)
    
    # Convert the image to an OpenCV format
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Load a pre-trained face detection model
    net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel")
    
    # Detect faces in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    face_descriptions = []
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_descriptions.append(f"Posición de la cara: ({x}, {y}), tamaño: {w}x{h} píxeles.") 
    
    # Convert the image back to RGB format for displaying in Streamlit
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, caption='Imagen con reconocimiento facial.', use_column_width=True)
    
    # Generate a description of the detected faces
    face_descriptions = []
    for (x, y, w, h) in faces:
        face_descriptions.append(f"Una persona con una cara de {w} píxeles de ancho y {h} píxeles de alto.")
    
    description = " ".join(face_descriptions)
    
    # Use GPT model to generate a detailed description
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a human."},
            {"role": "user", "content": f"Describe the following person: {description}"}
        ]
    )
    st.markdown(response['choices'][0]['message']['content'])
except Exception as e:
    st.error("Ocurrió un error al procesar la solicitud con OpenAI.")
    st.markdown(response['choices'][0]['message']['content'])
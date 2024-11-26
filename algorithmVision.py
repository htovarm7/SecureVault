import streamlit as st
import openai

# Configura tu clave API de OpenAI
openai.api_key = st.secrets["OPEN_AI_KEY"]  # Usa Streamlit Secrets

# Realiza la solicitud a la API de OpenAI
completion = openai.ChatCompletion.create(
    model="gpt-4",  # Asegúrate de usar el nombre correcto del modelo
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

# Muestra la respuesta de la API
st.write(completion['choices'][0]['message']['content'])

import streamlit as st
from openai import OpenAI

# Configura tu clave API de OpenAI
client = OpenAI(api_key = st.secrets["OPEN_AI_KEY"])  # Usa Streamlit Secrets

# Realiza la solicitud a la API de OpenAI
completion = client.chat.completions.create(
    model="gpt-4",  # Asegúrate de usar el nombre correcto del modelo
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ],
    max_tokens = 100,
    temperature = 0.7
)

print(completion.choices[0].message.content)

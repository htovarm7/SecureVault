import streamlit as st
from openai import OpenAI

OpenAI.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Prueba de OpenAI API")

if st.button("Probar conexión"):
    try:
        response = OpenAI.Completion.create(
            engine="text-davinci-003",
            prompt="Hola, ¿puedes responder a esta prueba?",
            max_tokens=50,
            temperature=0.7
        )
        st.success("Conexión exitosa: " + response.choices[0].text.strip())
    except Exception as e:
        st.error(f"Error: {e}")

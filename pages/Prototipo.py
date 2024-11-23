import streamlit as st

st.markdown("<h1> Prototipo 🚀</h1>",unsafe_allow_html=True)
st.divider()

st.markdown("<h2>Descripción del Prototipo</h2>",unsafe_allow_html=True)
st.write("")

st.markdown("<h2>Metodologia</h2>", unsafe_allow_html=True)
st.write("")

st.markdown("<b>SecureVault</b> utiliza una combinación de técnicas y herramientas de ingeniería que abarcan hardware, software y diseño de sistemas avanzados para garantizar un sistema de seguridad robusto y eficiente.", unsafe_allow_html=True)
st.write("")
st.markdown("<h3><b>Control de Accesso Multifactorial</b></h3>", unsafe_allow_html=True)
st.markdown("""
    - Uso de reconocimiento facial mediante una camara ESP32 para validar la identidad de usuarios autorizados.
    - Lector RFID (MFRC522) para verificar credenciales físicas, como tarjetas de acceso.
    - Códigos dinámicos ingresados mediante un teclado numérico para añadir una capa adicional de seguridad.
""")

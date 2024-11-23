import streamlit as st

st.markdown("<h1> Prototipo 🚀</h1>",unsafe_allow_html=True)
st.divider()

st.markdown("<h2>Descripción del Prototipo</h2>",unsafe_allow_html=True)
st.video("https://youtu.be/G_iDkolIcTk")
st.write("""El prototipo fue realizado con madera MDF de 5mm para garantizar la resistencia y durabilidad, 
         además de ser un material económico y fácil de trabajar. 
         El diseño del prototipo se basa en la simulación de un banco realizado con, con un sistema de control de acceso multifactorial que incluye reconocimiento facial,
         lectura de credenciales RFID y códigos dinámicos.)
         """)
st.divider()

st.markdown("<h2 style='text-align: center;'><b>Materiales</b></h2>",unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
col1.image("Imagenes/CamESP32.jpg",caption="Camara ESP32", width=100)
col2.image("Imagenes/TecladoNumerico.png",caption="Teclado Numérico", width=100)
col3.image("Imagenes/RFID.jpg",caption="Lector RFID", width=100)
col4.image("Imagenes/Boton.jpeg",caption="Boton de Emergencia", width=100)
col5.image("Imagenes/Acelerometro.jpg",caption="Detector de forzado de boveda", width=100)
st.divider()

st.markdown("<h2><b>Metodologia</b></h2>", unsafe_allow_html=True)
st.write("")

st.markdown("<b>SecureVault</b> utiliza una combinación de técnicas y herramientas de ingeniería que abarcan hardware, software y diseño de sistemas avanzados para garantizar un sistema de seguridad robusto y eficiente.", unsafe_allow_html=True)
st.write("")
st.markdown("<h3><b>Control de Accesso Multifactorial</b></h3>", unsafe_allow_html=True)
st.markdown("""
    - Uso de reconocimiento facial mediante una camara ESP32 para validar la identidad de usuarios autorizados.
    - Lector RFID (MFRC522) para verificar credenciales físicas, como tarjetas de acceso.
    - Códigos dinámicos ingresados mediante un teclado numérico para añadir una capa adicional de seguridad.
""")

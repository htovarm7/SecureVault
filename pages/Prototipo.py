import streamlit as st
import pandas as pd
import numpy as np

st.markdown("<h1> Prototipo 🚀</h1>",unsafe_allow_html=True)
st.divider()

st.markdown("<h2 >Descripción del Prototipo</h2>",unsafe_allow_html=True)
st.video("https://youtu.be/G_iDkolIcTk")
st.caption("Video del Prototipo")
st.markdown("<h2>Características del Prototipo</h2>",unsafe_allow_html=True)
st.write("El prototipo fue realizado con madera MDF de 5mm para garantizar la resistencia y durabilidad, además de ser un material económico y fácil de trabajar.")
st.write("El diseño del prototipo se basa en la simulación de un banco realizado con el software SolidWorks. Este prototipo incluye  un sistema de control de acceso multifactorial que incluye reconocimiento facial, lectura de tarjetas RFID y códigos dinámicos.)")

st.markdown("<h2>Divisiones del prototipo</h2>",unsafe_allow_html=True)
st.write("El prototipo se divide en tres secciones principales: ")
st.markdown("""
            - La primera es el lobby para los clientes, donde se encuentran las ventanillas y los empleados. 
            - La segunda zona es donde están los archiveros. 
            - La tercera y última zona es donde se encuentra la bóveda.
            """)
st.markdown("<h2>¿Brinda una solución?</h2>",unsafe_allow_html=True)
st.write("Concluimos que el prototipo brinda efectivamente la solución a la problemática que es brindarle seguridad a las instituciones financieras.  Gracias a nuestra implementacion de sensores y actuadores, junto con registro de datos de estos mismos en tiempo real, podemos analizar los datos y utilizar para prevenir y reforzar aun mas la seguridad.")
st.divider()

st.markdown("<h2 style='text-align: center;'><b>Materiales</b></h2>",unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
col1.image("Imagenes/Madera.jpeg",caption="Madera MDF 5mm", width=75)
col2.image("Imagenes/NodeMCU.jpeg",caption="NodeMCU", width=75)
col3.image("Imagenes/CamESP32.jpg",caption="Camara ESP32", width=75)
col4.image("Imagenes/TecladoNumerico.png",caption="Teclado Numérico", width=75)
col5.image("Imagenes/Pantalla.jpeg",caption="Pantalla LCD", width=75)
col6.image("Imagenes/RFID.jpg",caption="Lector RFID", width=75)
col7.image("Imagenes/Boton.jpeg",caption="Boton de Emergencia", width=75)
col8.image("Imagenes/Acelerometro.jpg",caption="Detector de forzado de boveda", width=75)

st.markdown("<h2 style='text-align: center;'><b>Costos</b></h2>", unsafe_allow_html=True)

data = {
    "Material": ["Madera MDF 5mm", "NodeMCU", "Cámara ESP32", "Teclado Numérico", "Pantalla LCD", "Lector RFID", "Botón de Emergencia", "Acelerómetro"],
    "Lugar": ["Home Depot", "MercadoLibre", "MercadoLibre", "MercadoLibre", "MercadoLibre", "MercadoLibre", "Steren", "MercadoLibre"],
    "Costo": ["$299", "$150", "$199", "$60", "$69", "$100", "$20", "$65"]
}

df = pd.DataFrame(data)
st.dataframe(df)
st.divider()

st.markdown("<h2><b>Costo total del prototipo es de $1152.00 MXN.</b></h2>", unsafe_allow_html=True) 
st.markdown("El costo total del <b>material fisico fue de $952.00 MXN + $200 MXN de diseño</b>.", unsafe_allow_html=True)
st.divider()

st.markdown("<h2><b>Metodologia</b></h2>", unsafe_allow_html=True)
st.markdown("<b>SecureVault</b> utiliza una combinación de técnicas y herramientas de ingeniería que abarcan hardware, software y diseño de sistemas avanzados para garantizar un sistema de seguridad robusto y eficiente.", unsafe_allow_html=True)

st.write("")
st.markdown("<h3><b>Control de Accesso Multifactorial</b></h3>", unsafe_allow_html=True)
st.markdown("""
    - Uso de reconocimiento facial mediante una camara ESP32 para validar la identidad de usuarios autorizados.
    - Lector RFID (MFRC522) para verificar credenciales físicas, como tarjetas de acceso.
    - Códigos dinámicos ingresados mediante un teclado numérico para añadir una capa adicional de seguridad.
""")

st.write("")
st.markdown("<h3><b>Redes IoT y Comunicaciones</b></h3>", unsafe_allow_html=True)
st.markdown("""
            - Uso del NodeMCU con capacidad de Wi-Fi para transmitir datos en tiempo real a una aplicación de monitoreo.
            - Enlace seguro mediante uso de una IP para proteger la comunicación entre dispositivos y servidores.
""")

st.write("")
st.markdown("<h3><b>Sistemas de Alerta en Tiempo Real</b></h3>", unsafe_allow_html=True)
st.markdown("""
            - Pantalla LCD para notificaciones locales, como denegación o autorización de acceso.
            - Envío de alertas al personal de seguridad mediante notificaciones push en la aplicación móvil.
            """)
st.divider()

st.markdown("<h2><b>Resultados 🏆</b></h2>", unsafe_allow_html=True) 
st.markdown("<h3><b>Datos en tiempo real</b></h3>", unsafe_allow_html=True)
st.markdown("""
            - El sistema transmite información actualizada al instante mediante conectividad Wi-Fi, permitiendo monitoreo remoto desde cualquier dispositivo móvil o computadora.
            - Generación de alertas en tiempo real ante intentos de acceso no autorizado, mejorando significativamente la capacidad de respuesta ante incidentes de seguridad.
            """)
st.markdown("<h3><b>Seguridad Solida</b></h3>", unsafe_allow_html=True)
st.markdown("""- Integración de control de acceso multifactorial, incluyendo reconocimiento facial, lector RFID y teclado numérico, lo que garantiza protección robusta contra intentos de acceso no autorizado.""")
st.markdown("<h3><b>Indicadores con visualización</b></h3>", unsafe_allow_html=True)
st.markdown("""
            - Creación de indicadores con visualización de graficas. 
            - Se logró un buen analisis de datos en donde se miden los indicadores de los empleados, lugares y sensores
            """)   
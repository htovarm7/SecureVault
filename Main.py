import streamlit as st

pages = {
    ""
    "Secure Vault 🔒": [
        st.Page("pages/Sobre_Nosotros.py", title="Sobre Nosotros 👥"),
        st.Page("pages/Prototipo.py", title="Prototipo 🚀"),
        st.Page("pages/Dashboard.py", title="Dashboard 📊"),
        #st.Page("pages/Reconocimiento.py", title="Reconocimiento Facial👤"),
        st.Page("pages/Contacto.py", title="Contactanos 📩"),
    ],
}

pg = st.navigation(pages)
pg.run()


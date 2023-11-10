import streamlit as st
import random

# Título de la aplicación
st.title("Selector de Portero de Fútbol")

# Área de entrada de texto para los nombres de porteros
nombres_input = st.text_input("Ingresa los nombres de los porteros separados por coma:")

# Botón para seleccionar un portero aleatorio
if st.button("Seleccionar Portero Aleatorio"):
    porteros = nombres_input.split(",")
    porteros = [portero.strip() for portero in porteros if portero.strip() != ""]
    
    if porteros:
        portero_aleatorio = random.choice(porteros)
        st.success(f"Portero seleccionado al azar: {portero_aleatorio}")
    else:
        st.warning("Por favor, ingresa al menos un nombre de portero.")

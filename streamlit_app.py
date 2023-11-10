import streamlit as st
import random
import time

# Lista de nombres de porteros iniciales
nombres_iniciales = {
    "MARTIN BARREIROS": False,
    "DAVID": False,
    "ALEX": False,
    "ARIANA": False,
    "ISMAEL": False,
    "MARTIN DOSIL": False,
    "HUGO": False,
    "RODRI": False,
    "MATEO": False,
    "ANXO": False,
    "VICTOR": False
}

# Configuración de página
st.set_page_config(
    page_title="Porteiro Miudos",
    page_icon="⚽",
    layout="wide"  # Asegura que los elementos se muestren en una sola columna
)

# Título de la aplicación
st.title("A ver a quen lle toca quedar")

# Imagen del escudo del club
st.image("escudo.jfif", width=200)  # Reemplaza la ruta de la imagen

# Entrada de texto para agregar un nuevo nombre
nuevo_nombre = st.text_input("Agregar un nuevo nombre de portero:")

# Función para agregar un nombre a la lista inicial
def agregar_nombre(nombre):
    if nombre.strip() != "":
        nombres_iniciales[nombre] = False
        st.success(f"Se agregó '{nombre}' a la lista de porteros.")

# Botón para agregar un nombre a la lista
if st.button("Agregar Nombre"):
    agregar_nombre(nuevo_nombre)
    nuevo_nombre = ""

# Función para seleccionar un portero aleatorio
def seleccionar_portero_aleatorio():
    with st.spinner("Seleccionando portero aleatorio..."):
        time.sleep(2)  # Simula un proceso que tarda 2 segundos
        if nombres_seleccionados:
            portero_aleatorio = random.choice(nombres_seleccionados)
            st.success(f"Tocoulle a : {portero_aleatorio}")
        else:
            st.warning("Por favor, selecciona al menos un portero para participar en el sorteo.")

# Ordena los nombres alfabéticamente
nombres_iniciales = {nombre: seleccionado for nombre, seleccionado in sorted(nombres_iniciales.items())}

# Actualiza la selección de nombres usando botones y permite deseleccionar
for nombre in nombres_iniciales:
    nombres_iniciales[nombre] = st.checkbox(nombre, nombres_iniciales[nombre])

# Filtra los nombres seleccionados para el sorteo
nombres_seleccionados = [nombre for nombre, seleccionado in nombres_iniciales.items() if seleccionado]

# Botón para seleccionar un portero aleatorio
if st.button("Seleccionar Portero Aleatorio"):
    seleccionar_portero_aleatorio()

# Icono de guantes de portero
st.write("⚽️ Diviértete seleccionando un portero al azar!")

# Efecto visual divertido
if st.button("¡Fiesta de la victoria!"):
    st.balloons()

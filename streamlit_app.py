import streamlit as st
import random
import time

# Configuración de página
st.set_page_config(
    page_title="Porteiro Miudos",
    page_icon="⚽",
    layout="wide"
)

# Inicializar el estado de la sesión con todos los nombres seleccionados
if 'nombres_iniciales' not in st.session_state:
    st.session_state['nombres_iniciales'] = {
        "MARTIN BARREIROS": True,
        "DAVID": True,
        "ALEX": True,
        "ARIANA": True,
        "ISMAEL": True,
        "MARTIN DOSIL": True,
        "HUGO": True,
        "RODRI": True,
        "MATEO": True,
        "ANXO": True,
        "VICTOR": True
    }

# Título de la aplicación y imagen del escudo del club
st.title("A ver a quen lle toca quedar")
st.image("escudo.jfif", width=200)

# Expander para añadir o eliminar nombres, y reemplazar equipo
with st.expander("Gestionar nombres"):
    # Sección para agregar un nuevo nombre
    nuevo_nombre = st.text_input("Agregar un nuevo nombre de porteiro:")

    def agregar_nombre():
        nombre = nuevo_nombre.strip()
        if nombre and nombre not in st.session_state.nombres_iniciales:
            st.session_state.nombres_iniciales[nombre] = True
            st.success(f"Se agregó '{nombre}' a la lista de porteiros.")
        elif nombre:
            st.error("El nombre ya está en la lista.")

    if st.button("Agregar Nombre"):
        agregar_nombre()

    # Sección para eliminar un nombre (ordenada)
    if st.session_state.nombres_iniciales:
        nombres_ordenados_para_eliminar = sorted(st.session_state.nombres_iniciales)
        nombre_a_eliminar = st.selectbox("Selecciona un nombre para eliminar:", nombres_ordenados_para_eliminar)

        def eliminar_nombre():
            del st.session_state.nombres_iniciales[nombre_a_eliminar]
            st.success(f"Se eliminó '{nombre_a_eliminar}' de la lista de porteiros.")

        if st.button("Eliminar Nombre"):
            eliminar_nombre()

    # Sección para reemplazar el equipo actual
    nuevo_equipo = st.text_area("Introduce los nombres del nuevo equipo, separados por comas:")

    def reemplazar_equipo():
        nombres_nuevos = [nombre.strip() for nombre in nuevo_equipo.split(',') if nombre.strip()]
        st.session_state.nombres_iniciales = {nombre: True for nombre in nombres_nuevos}
        st.success("El equipo ha sido reemplazado exitosamente.")

    if st.button("Reemplazar Equipo"):
        reemplazar_equipo()

# Seleccionar porteiro aleatorio
def seleccionar_porteiro_aleatorio():
    with st.spinner("Seleccionando porteiro aleatorio..."):
        time.sleep(2)
        nombres_seleccionados = [nombre for nombre, seleccionado in st.session_state.nombres_iniciales.items() if seleccionado]
        if nombres_seleccionados:
            porteiro_aleatorio = random.choice(nombres_seleccionados)
            st.success(f"Tocoulle a : {porteiro_aleatorio}")
        else:
            st.warning("Por favor, selecciona un porteiro polo menos.")

# Ordenar y mostrar checkboxes
nombres_ordenados = sorted(st.session_state.nombres_iniciales.items())
for nombre, seleccionado in nombres_ordenados:
    st.session_state.nombres_iniciales[nombre] = st.checkbox(nombre, seleccionado)

st.write("⚽️ selecciona un porteiro ó azar!")
if st.button("Sortea"):
    seleccionar_porteiro_aleatorio()
if st.button("¡Por si ganamos hoxe!"):
    st.balloons()

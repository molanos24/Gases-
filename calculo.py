import streamlit as st

# Constante universal de los gases (L·atm/mol·K)
R = 0.0821

# Título principal
st.set_page_config(page_title="Calculadora de Gases Ideales", layout="centered")
st.title("💨 Calculadora de la Ecuación de los Gases Ideales")
st.markdown("Resuelve la ecuación PV = nRT")

# Selección de la variable a calcular
opcion = st.selectbox(
    "Selecciona la variable que deseas calcular:",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

st.markdown("### Ingresa los valores conocidos:")

# Variables de entrada
if opcion == "Presión (P)":
    volumen = st.number_input("Volumen (L)", min_value=0.001, format="%.3f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.001, format="%.2f")
    moles = st.number_input("Número de moles (mol)", min_value=0.001, format="%.3f")
    if st.button("Calcular Presión"):
        presion = (moles * R * temperatura) / volumen
        st.success(f"La presión es: **{presion:.3f} atm**")

elif opcion == "Volumen (V)":
    presion = st.number_input("Presión (atm)", min_value=0.001, format="%.3f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.001, format="%.2f")
    moles = st.number_input("Número de moles (mol)", min_value=0.001, format="%.3f")
    if st.button("Calcular Volumen"):
        volumen = (moles * R * temperatura) / presion
        st.success(f"El volumen es: **{volumen:.3f} L**")

elif opcion == "Temperatura (T)":
    presion = st.number_input("Presión (atm)", min_value=0.001, format="%.3f")
    volumen = st.number_input("Volumen (L)", min_value=0.001, format="%.3f")

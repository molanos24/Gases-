import streamlit as st

R = 0.0821  # Constante de los gases ideales: L·atm/mol·K

st.title("Calculadora de la Ecuación de los Gases Ideales")

opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

st.markdown("### Introduce los valores conocidos:")

presion = volumen = temperatura = moles = None

if opcion == "Presión (P)":
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.3f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.3f")
    if volumen > 0 and temperatura > 0:
        presion = (moles * R * temperatura) / volumen
        st.success(f"La presión es: {presion:.3f} atm")

elif opcion == "Volumen (V)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.3f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="

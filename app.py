import streamlit as st

# Ejemplo valores (si no los defines dentro del script dará error)
p_control = 0.482
p_test = 0.541
p_value = 3.465351712919813e-50

st.title("A/B Test Vanguard")

st.metric("Tasa Control", f"{round(p_control*100,2)} %")
st.metric("Tasa Test", f"{round(p_test*100,2)} %")
st.metric("Lift (pp)", f"{round((p_test-p_control)*100,2)}")

if p_value < 0.05:
    st.success("Resultado estadísticamente significativo")
else:
    st.warning("No significativo")

# streamlit run app.py -> en la terminal
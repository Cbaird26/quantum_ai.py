import streamlit as st
from quantum_ai import run_quantum_circuit, run_qiskit_circuit

st.title("Quantum AI on Streamlit")

st.write("### Pennylane Quantum Circuit")

params = st.slider('Choose parameters', 0.0, 3.14, (0.54, 0.12))
result = run_quantum_circuit(params)
st.write("Pennylane Quantum Circuit Result: ", result)

st.write("### Qiskit Quantum Circuit")

if st.button('Run Qiskit Circuit'):
    qiskit_result = run_qiskit_circuit()
    st.write("Qiskit Quantum Circuit Result: ", qiskit_result)

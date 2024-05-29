# app.py
import streamlit as st
import pennylane as qml
from pennylane import numpy as np

def run_quantum_circuit():
    dev = qml.device("default.qubit", wires=2)

    @qml.qnode(dev)
    def circuit(weights):
        qml.RX(weights[0], wires=0)
        qml.RY(weights[1], wires=1)
        qml.CNOT(wires=[0, 1])
        qml.RX(weights[2], wires=1)
        return qml.expval(qml.PauliZ(1))

    weights = np.array([0.1, 0.2, 0.3], requires_grad=True)
    return circuit(weights)

st.title("Quantum Circuit Runner")
if st.button("Run Circuit"):
    result = run_quantum_circuit()
    st.write("Circuit Result:", result)

import pennylane as qml
from pennylane import numpy as np

def run_quantum_circuit(params):
    dev = qml.device('default.qubit', wires=2)

    @qml.qnode(dev)
    def circuit(params):
        qml.RX(params[0], wires=0)
        qml.RY(params[1], wires=1)
        qml.CNOT(wires=[0, 1])
        return qml.expval(qml.PauliZ(0)), qml.expval(qml.PauliZ(1))

    return circuit(params)

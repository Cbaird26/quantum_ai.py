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

from qiskit import IBMQ, Aer, execute, QuantumCircuit

def run_qiskit_circuit():
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    backend = provider.get_backend('ibmq_qasm_simulator')

    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])

    job = execute(circuit, backend)
    result = job.result()
    counts = result.get_counts()

    return counts

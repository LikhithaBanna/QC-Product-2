from qiskit import QuantumCircuit
from math import pi


def qft_circuit(n=3):
    """
    Create an n-qubit Quantum Fourier Transform circuit.
    """

    if n < 1:
        raise ValueError("Number of qubits must be at least 1.")

    qc = QuantumCircuit(n)

    # Apply QFT
    for target in range(n):
        qc.h(target)

        for control in range(target + 1, n):
            angle = pi / (2 ** (control - target))
            qc.cp(angle, control, target)

    # Reverse the order of qubits
    for i in range(n // 2):
        qc.swap(i, n - i - 1)

    return qc


def inverse_qft_circuit(n=3):
    """
    Create the inverse Quantum Fourier Transform circuit.
    """

    return qft_circuit(n).inverse()


if __name__ == "__main__":
    n = 3

    circuit = qft_circuit(n)

    print("\nQuantum Fourier Transform (QFT) Circuit\n")
    print(circuit)
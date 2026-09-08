from qiskit import QuantumCircuit


def bernstein_vazirani_circuit(secret_string="1011"):
    """
    Create a Bernstein-Vazirani quantum circuit.

    The algorithm determines a hidden binary string
    using a single query to the oracle.

    Parameters
    ----------
    secret_string : str
        Hidden binary string, e.g. "1011".

    Returns
    -------
    QuantumCircuit
        Bernstein-Vazirani circuit.
    """

    if not secret_string:
        raise ValueError("Secret string cannot be empty.")

    if any(bit not in "01" for bit in secret_string):
        raise ValueError("Secret string must contain only 0 and 1.")

    n = len(secret_string)

    # n input qubits + 1 ancilla
    qc = QuantumCircuit(n + 1, n)

    # Prepare ancilla in |1>
    qc.x(n)
    qc.h(n)

    # Put input qubits into superposition
    for qubit in range(n):
        qc.h(qubit)

    # Oracle
    # Apply CNOT according to the secret string
    for qubit, bit in enumerate(reversed(secret_string)):
        if bit == "1":
            qc.cx(qubit, n)

    # Apply Hadamard to input qubits
    for qubit in range(n):
        qc.h(qubit)

    # Measure input qubits
    qc.measure(range(n), range(n))

    return qc


if __name__ == "__main__":
    secret = "1011"

    circuit = bernstein_vazirani_circuit(secret)

    print("\nBernstein-Vazirani Circuit\n")
    print(circuit)
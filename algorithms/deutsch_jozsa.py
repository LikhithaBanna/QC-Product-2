from qiskit import QuantumCircuit


def deutsch_jozsa_circuit(n=3, oracle_type="balanced"):
    """
    Create a Deutsch-Jozsa quantum circuit.

    Parameters
    ----------
    n : int
        Number of input qubits.
    oracle_type : str
        "constant" or "balanced".

    Returns
    -------
    QuantumCircuit
        Deutsch-Jozsa circuit.
    """

    if n < 1:
        raise ValueError("Number of qubits must be at least 1.")

    if oracle_type not in ["constant", "balanced"]:
        raise ValueError(
            "oracle_type must be 'constant' or 'balanced'."
        )

    # n input qubits + 1 ancilla qubit
    qc = QuantumCircuit(n + 1, n)

    # Step 1: Prepare ancilla |1>
    qc.x(n)

    # Step 2: Create superposition
    qc.h(n)

    for qubit in range(n):
        qc.h(qubit)

    # Step 3: Oracle
    if oracle_type == "balanced":
        for qubit in range(n):
            qc.cx(qubit, n)

    # Constant oracle does nothing

    # Step 4: Apply Hadamard gates to input qubits
    for qubit in range(n):
        qc.h(qubit)

    # Step 5: Measure input qubits
    qc.measure(range(n), range(n))

    return qc


if __name__ == "__main__":
    circuit = deutsch_jozsa_circuit(
        n=3,
        oracle_type="balanced"
    )

    print("\nDeutsch-Jozsa Circuit\n")
    print(circuit)
from qiskit import QuantumCircuit


def grover_circuit(target="101"):
    """
    Create a Grover search circuit for a target state.

    Parameters
    ----------
    target : str
        Binary target state, e.g. "101".

    Returns
    -------
    QuantumCircuit
        Grover search circuit.
    """

    if not target:
        raise ValueError("Target cannot be empty.")

    if any(bit not in "01" for bit in target):
        raise ValueError("Target must contain only 0 and 1.")

    n = len(target)

    qc = QuantumCircuit(n, n)

    # --------------------------------------------------
    # Step 1: Create equal superposition
    # --------------------------------------------------

    for qubit in range(n):
        qc.h(qubit)

    # Number of Grover iterations
    iterations = max(
        1,
        int((3.14159 / 4) * (2 ** (n / 2)))
    )

    for _ in range(iterations):

        # --------------------------------------------------
        # Oracle
        # Mark the target state with a phase flip.
        # --------------------------------------------------

        for qubit, bit in enumerate(reversed(target)):
            if bit == "0":
                qc.x(qubit)

        qc.h(n - 1)

        if n == 1:
            qc.z(0)
        else:
            qc.mcx(
                list(range(n - 1)),
                n - 1
            )

        qc.h(n - 1)

        for qubit, bit in enumerate(reversed(target)):
            if bit == "0":
                qc.x(qubit)

        # --------------------------------------------------
        # Diffusion operator
        # --------------------------------------------------

        for qubit in range(n):
            qc.h(qubit)
            qc.x(qubit)

        qc.h(n - 1)

        if n == 1:
            qc.z(0)
        else:
            qc.mcx(
                list(range(n - 1)),
                n - 1
            )

        qc.h(n - 1)

        for qubit in range(n):
            qc.x(qubit)
            qc.h(qubit)

    # --------------------------------------------------
    # Measurement
    # --------------------------------------------------

    qc.measure(range(n), range(n))

    return qc


if __name__ == "__main__":
    target = "101"

    circuit = grover_circuit(target)

    print("\nGrover's Search Circuit\n")
    print(circuit)
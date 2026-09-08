from qiskit import transpile


def transpile_circuit(circuit, optimization_level=1):
    """
    Transpile a quantum circuit using Qiskit's transpiler.
    """

    if circuit is None:
        raise ValueError("Circuit cannot be None.")

    if optimization_level not in [0, 1, 2, 3]:
        raise ValueError("Optimization level must be between 0 and 3.")

    return transpile(
        circuit,
        optimization_level=optimization_level
    )
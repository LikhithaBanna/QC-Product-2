from qiskit import transpile
from qiskit_aer import AerSimulator


def run_circuit(circuit, shots=1024):
    """
    Execute a quantum circuit using Qiskit AerSimulator.

    Parameters
    ----------
    circuit : QuantumCircuit
        Circuit to simulate.
    shots : int
        Number of measurements.

    Returns
    -------
    dict
        Measurement counts.
    """

    simulator = AerSimulator()

    # Transpile the circuit for the simulator
    compiled_circuit = transpile(circuit, simulator)

    # Execute the circuit
    result = simulator.run(
        compiled_circuit,
        shots=shots
    ).result()

    # Return measurement counts
    counts = result.get_counts()

    return counts
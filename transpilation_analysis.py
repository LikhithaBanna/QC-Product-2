from algorithms.deutsch_jozsa import deutsch_jozsa_circuit
from algorithms.bernstein_vazirani import bernstein_vazirani_circuit
from algorithms.simon import simon_circuit
from algorithms.grover import grover_circuit
from algorithms.qft import qft_circuit

from utils.transpiler import transpile_circuit


def analyze(name, circuit):
    """Display original and transpiled circuit statistics."""

    transpiled = transpile_circuit(circuit, optimization_level=1)

    print()
    print("=" * 70)
    print(name)
    print("=" * 70)

    print("Original circuit:")
    print(f"  Qubits      : {circuit.num_qubits}")
    print(f"  Depth       : {circuit.depth()}")
    print(f"  Gates       : {len(circuit.data)}")
    print(f"  Operations  : {dict(circuit.count_ops())}")

    print()
    print("Transpiled circuit:")
    print(f"  Qubits      : {transpiled.num_qubits}")
    print(f"  Depth       : {transpiled.depth()}")
    print(f"  Gates       : {len(transpiled.data)}")
    print(f"  Operations  : {dict(transpiled.count_ops())}")


# Create circuits
dj = deutsch_jozsa_circuit(3, "balanced")
bv = bernstein_vazirani_circuit("1011")
simon = simon_circuit("101")
grover = grover_circuit("101")
qft = qft_circuit(3)


# Analyze all algorithms
analyze("Deutsch-Jozsa Algorithm", dj)
analyze("Bernstein-Vazirani Algorithm", bv)
analyze("Simon's Algorithm", simon)
analyze("Grover's Algorithm", grover)
analyze("Quantum Fourier Transform (QFT)", qft)


print()
print("=" * 70)
print("TRANSPILATION ANALYSIS COMPLETE")
print("=" * 70)
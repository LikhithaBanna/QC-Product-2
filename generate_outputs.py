import os
import matplotlib.pyplot as plt

from algorithms.deutsch_jozsa import deutsch_jozsa_circuit
from algorithms.bernstein_vazirani import bernstein_vazirani_circuit
from algorithms.simon import simon_circuit
from algorithms.grover import grover_circuit
from algorithms.qft import qft_circuit

from utils.simulator import run_circuit
from utils.visualization import plot_measurement_distribution


os.makedirs("outputs/circuits", exist_ok=True)
os.makedirs("outputs/plots", exist_ok=True)


def save_circuit(circuit, filename):
    fig = circuit.draw("mpl")
    fig.savefig(
        f"outputs/circuits/{filename}.png",
        bbox_inches="tight",
        dpi=200
    )
    plt.close(fig)


def save_results(counts, filename, title):
    fig = plot_measurement_distribution(counts)

    fig.axes[0].set_title(title)

    fig.savefig(
        f"outputs/plots/{filename}.png",
        bbox_inches="tight",
        dpi=200
    )

    plt.close(fig)


# Deutsch-Jozsa
print("Generating Deutsch-Jozsa...")

dj = deutsch_jozsa_circuit(3, "balanced")
dj_counts = run_circuit(dj)

save_circuit(dj, "deutsch_jozsa")
save_results(
    dj_counts,
    "deutsch_jozsa_results",
    "Deutsch-Jozsa Measurement Results"
)


# Bernstein-Vazirani
print("Generating Bernstein-Vazirani...")

bv = bernstein_vazirani_circuit("1011")
bv_counts = run_circuit(bv)

save_circuit(bv, "bernstein_vazirani")
save_results(
    bv_counts,
    "bernstein_vazirani_results",
    "Bernstein-Vazirani Measurement Results"
)


# Simon
print("Generating Simon...")

simon = simon_circuit("101")
simon_counts = run_circuit(simon)

save_circuit(simon, "simon")
save_results(
    simon_counts,
    "simon_results",
    "Simon Algorithm Measurement Results"
)


# Grover
print("Generating Grover...")

grover = grover_circuit("101")
grover_counts = run_circuit(grover)

save_circuit(grover, "grover")
save_results(
    grover_counts,
    "grover_results",
    "Grover Search Measurement Results"
)


# QFT
print("Generating QFT...")

qft = qft_circuit(3)

qft_measure = qft.copy()
qft_measure.measure_all()

qft_counts = run_circuit(qft_measure)

save_circuit(qft, "qft")
save_results(
    qft_counts,
    "qft_results",
    "Quantum Fourier Transform Measurement Results"
)


print()
print("=" * 60)
print("OUTPUT GENERATION COMPLETE")
print("=" * 60)
print("Circuit diagrams saved in: outputs/circuits/")
print("Result plots saved in:     outputs/plots/")
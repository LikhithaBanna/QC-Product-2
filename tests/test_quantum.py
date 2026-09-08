import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from algorithms.qft import qft_circuit
from algorithms.deutsch_jozsa import deutsch_jozsa_circuit
from algorithms.bernstein_vazirani import bernstein_vazirani_circuit
from algorithms.simon import simon_circuit
from algorithms.grover import grover_circuit


def test_qft():
    qc = qft_circuit(3)
    assert qc.num_qubits == 3


def test_deutsch_jozsa():
    qc = deutsch_jozsa_circuit(3, "balanced")
    assert qc.num_qubits == 4
    assert qc.num_clbits == 3


def test_bernstein_vazirani():
    qc = bernstein_vazirani_circuit("1011")
    assert qc.num_qubits == 5
    assert qc.num_clbits == 4


def test_simon():
    qc = simon_circuit("101")
    assert qc.num_qubits == 6
    assert qc.num_clbits == 3


def test_grover():
    qc = grover_circuit("101")
    assert qc.num_qubits == 3
    assert qc.num_clbits == 3
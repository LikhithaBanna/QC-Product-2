import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms.deutsch_jozsa import deutsch_jozsa_circuit
from algorithms.bernstein_vazirani import bernstein_vazirani_circuit
from algorithms.simon import simon_circuit, valid_measurement, recover_secret
from algorithms.grover import grover_circuit
from algorithms.qft import qft_circuit
from utils.simulator import run_circuit
import pytest

SHOTS = 1024


def test_deutsch_jozsa_balanced():
    counts = run_circuit(deutsch_jozsa_circuit(3, "balanced"))

    assert sum(counts.values()) == SHOTS
    assert max(counts, key=counts.get) == "111"


def test_deutsch_jozsa_constant():
    counts = run_circuit(deutsch_jozsa_circuit(3, "constant"))

    assert sum(counts.values()) == SHOTS
    assert max(counts, key=counts.get) == "000"


def test_bernstein_vazirani():
    counts = run_circuit(
        bernstein_vazirani_circuit("1011")
    )

    assert sum(counts.values()) == SHOTS
    assert counts.get("1011", 0) >= 0.95 * SHOTS


def test_simon_valid_measurements():
    secret = "101"

    counts = run_circuit(
        simon_circuit(secret)
    )

    assert sum(counts.values()) == SHOTS

    for measurement in counts:
        assert valid_measurement(measurement, secret)


def test_simon_recover_secret():
    secret = "101"

    measurements = [
        "010",
        "101"
    ]

    recovered = recover_secret(measurements, 3)

    assert recovered == secret


def test_grover():
    target = "101"

    counts = run_circuit(
        grover_circuit(target)
    )

    assert sum(counts.values()) == SHOTS
    assert counts.get(target, 0) >= 0.80 * SHOTS


def test_qft_structure():
    circuit = qft_circuit(3)

    assert circuit.num_qubits == 3
    assert circuit.depth() > 0


@pytest.mark.parametrize(
    "bad_input",
    ["102", "abc", ""]
)
def test_bernstein_vazirani_invalid_input(bad_input):

    with pytest.raises(ValueError):
        bernstein_vazirani_circuit(bad_input)
from qiskit import QuantumCircuit


def _is_independent(vectors, candidate):
    """Check linear independence over GF(2)."""

    vectors = [v[:] for v in vectors]
    vectors.append(candidate[:])

    rank = 0
    n = len(candidate)

    for col in range(n):
        pivot = None

        for row in range(rank, len(vectors)):
            if vectors[row][col] == 1:
                pivot = row
                break

        if pivot is not None:
            vectors[rank], vectors[pivot] = vectors[pivot], vectors[rank]

            for row in range(len(vectors)):
                if row != rank and vectors[row][col] == 1:
                    for j in range(col, n):
                        vectors[row][j] ^= vectors[rank][j]

            rank += 1

    return rank == len(vectors)


def _orthogonal_basis(secret):
    """
    Find n-1 independent vectors y satisfying:

        y · secret = 0 (mod 2)
    """

    n = len(secret)
    basis = []

    for number in range(1, 2 ** n):
        candidate = [
            (number >> (n - 1 - i)) & 1
            for i in range(n)
        ]

        dot_product = sum(
            candidate[i] * int(secret[i])
            for i in range(n)
        ) % 2

        if dot_product == 0 and _is_independent(
            basis, candidate
        ):
            basis.append(candidate)

        if len(basis) == n - 1:
            break

    return basis


def simon_circuit(secret="101"):
    """
    Create a Simon's Algorithm circuit.

    The oracle implements a 2-to-1 linear function
    satisfying:

        f(x) = f(x XOR secret)
    """

    if not secret:
        raise ValueError("Secret string cannot be empty.")

    if any(bit not in "01" for bit in secret):
        raise ValueError("Secret string must contain only 0 and 1.")

    if "1" not in secret:
        raise ValueError(
            "Secret string must contain at least one 1."
        )

    n = len(secret)

    qc = QuantumCircuit(2 * n, n)

    # Step 1: Superposition
    for qubit in range(n):
        qc.h(qubit)

    # Step 2: Simon oracle
    basis = _orthogonal_basis(secret)

    for output_index, row in enumerate(basis):
        output_qubit = n + output_index

        for input_index, coefficient in enumerate(row):
            if coefficient == 1:
                qc.cx(input_index, output_qubit)

    # Step 3: Hadamard
    for qubit in range(n):
        qc.h(qubit)

    # Step 4: Measurement
    qc.measure(range(n), range(n))

    return qc


def valid_measurement(y, secret):
    """
    Check:

        y · secret = 0 (mod 2)
    """

    return sum(
        int(a) * int(b)
        for a, b in zip(y, secret)
    ) % 2 == 0


def recover_secret(measurements, n):
    """
    Recover the non-zero Simon secret by searching for the
    binary string orthogonal to all measured equations.

    Parameters
    ----------
    measurements : list
        Measured bit strings.
    n : int
        Number of input qubits.

    Returns
    -------
    str
        Recovered secret.
    """

    candidates = []

    for number in range(1, 2 ** n):

        candidate = format(number, f"0{n}b")

        if all(
            valid_measurement(y, candidate)
            for y in measurements
        ):
            candidates.append(candidate)

    if len(candidates) == 1:
        return candidates[0]

    return candidates


if __name__ == "__main__":
    secret = "101"

    circuit = simon_circuit(secret)

    print("\nSimon's Algorithm Circuit\n")
    print(circuit)

    print("\nHidden secret:", secret)
    print("Expected condition: y · s = 0 (mod 2)")
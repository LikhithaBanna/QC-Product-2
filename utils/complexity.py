def get_complexity():
    """
    Return time-complexity information for the
    quantum algorithms in the demonstrator.
    """

    return {
        "QFT": {
            "classical": "O(n²)",
            "quantum": "O(n²)",
            "description": "Quantum Fourier Transform uses Hadamard and controlled-phase gates."
        },

        "Grover's Algorithm": {
            "classical": "O(N)",
            "quantum": "O(√N)",
            "description": "Grover's algorithm provides a quadratic speedup for unstructured search."
        },

        "Deutsch-Jozsa": {
            "classical": "O(2ⁿ)",
            "quantum": "O(1)",
            "description": "Determines whether a Boolean function is constant or balanced with one quantum query."
        },

        "Bernstein-Vazirani": {
            "classical": "O(n)",
            "quantum": "O(1)",
            "description": "Identifies a hidden binary string using a single quantum query."
        },

        "Simon's Algorithm": {
            "classical": "O(2ⁿ)",
            "quantum": "O(n)",
            "description": "Finds a hidden XOR period using quantum interference."
        }
    }


def print_complexity_table():
    """
    Print algorithm complexity information.
    """

    complexities = get_complexity()

    print("\nQuantum Algorithm Complexity Comparison")
    print("=" * 70)

    for algorithm, data in complexities.items():
        print(f"\n{algorithm}")
        print(f"  Classical: {data['classical']}")
        print(f"  Quantum:   {data['quantum']}")
        print(f"  {data['description']}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    print_complexity_table()
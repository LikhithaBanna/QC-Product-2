import matplotlib.pyplot as plt


def plot_measurement_distribution(results):
    """
    Create a bar chart from quantum measurement results.
    """

    if not results:
        raise ValueError("Measurement results cannot be empty.")

    states = list(results.keys())
    counts = list(results.values())

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(states, counts)

    ax.set_xlabel("Quantum State")
    ax.set_ylabel("Measurement Count")
    ax.set_title("Quantum Measurement Distribution")

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig
import streamlit as st
import pandas as pd

from algorithms.qft import qft_circuit
from algorithms.deutsch_jozsa import deutsch_jozsa_circuit
from algorithms.bernstein_vazirani import bernstein_vazirani_circuit
from algorithms.simon import simon_circuit
from algorithms.grover import grover_circuit

from utils.simulator import run_circuit
from utils.complexity import get_complexity
from utils.visualization import plot_measurement_distribution
from utils.transpiler import transpile_circuit


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Quantum Algorithm Demonstrator",
    page_icon="⚛️",
    layout="wide"
)


# ==================================================
# MAIN TITLE
# ==================================================

st.title("⚛️ Quantum Algorithm Demonstrator")

st.write(
    "An interactive educational application for exploring "
    "quantum algorithms, quantum circuits, simulation results, "
    "transpilation, and computational complexity."
)

st.divider()


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("🔬 Algorithm Selection")

algorithm = st.sidebar.selectbox(
    "Choose an algorithm",
    [
        "Quantum Fourier Transform (QFT)",
        "Deutsch-Jozsa Algorithm",
        "Bernstein-Vazirani Algorithm",
        "Simon's Algorithm",
        "Grover's Algorithm",
        "Complexity Comparison"
    ]
)


# ==================================================
# HELPER FUNCTION
# ==================================================

def display_circuit_tools(qc, run_simulation=True):
    """
    Display circuit, transpilation, simulation,
    measurement results, and visualization.
    """

    # --------------------------------------------------
    # Original Circuit
    # --------------------------------------------------

    st.subheader("🔗 Quantum Circuit")

    st.code(
        qc.draw(output="text"),
        language="text"
    )

    # --------------------------------------------------
    # Circuit Statistics
    # --------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Qubits",
            qc.num_qubits
        )

    with col2:
        st.metric(
            "Circuit Depth",
            qc.depth()
        )

    with col3:
        st.metric(
            "Gate Count",
            len(qc.data)
        )

    # --------------------------------------------------
    # Transpilation
    # --------------------------------------------------

    st.subheader("⚙️ Circuit Transpilation")

    optimization_level = st.select_slider(
        "Optimization level",
        options=[0, 1, 2, 3],
        value=1,
        help=(
            "Higher levels attempt to optimize the "
            "quantum circuit more aggressively."
        )
    )

    if st.button(
        "⚙️ Transpile Circuit",
        key="transpile_button"
    ):

        try:

            transpiled_qc = transpile_circuit(
                qc,
                optimization_level
            )

            st.success(
                "Circuit transpiled successfully!"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Original Depth",
                    qc.depth()
                )

                st.metric(
                    "Original Gate Count",
                    len(qc.data)
                )

            with col2:

                st.metric(
                    "Transpiled Depth",
                    transpiled_qc.depth()
                )

                st.metric(
                    "Transpiled Gate Count",
                    len(transpiled_qc.data)
                )

            st.write("### Transpiled Circuit")

            st.code(
                transpiled_qc.draw(output="text"),
                language="text"
            )

        except Exception as e:

            st.error(
                f"Transpilation failed: {e}"
            )

    # --------------------------------------------------
    # Simulation
    # --------------------------------------------------

    if run_simulation:

        st.subheader("🧪 Quantum Simulation")

        if st.button(
            "▶ Run Simulation",
            key="simulation_button"
        ):

            try:

                # Create a copy so the original circuit
                # remains unchanged.
                measured_circuit = qc.copy()

                # QFT and other circuits without classical
                # bits need measurement added.
                if measured_circuit.num_clbits == 0:

                    measured_circuit.measure_all()

                results = run_circuit(
                    measured_circuit
                )

                st.success(
                    "Simulation completed successfully!"
                )

                # --------------------------------------
                # Measurement Results
                # --------------------------------------

                st.write("### 📋 Measurement Results")

                results_df = pd.DataFrame(
                    list(results.items()),
                    columns=["State", "Count"]
                )

                results_df = results_df.sort_values(
                    by="State"
                )

                st.dataframe(
                    results_df,
                    width="stretch",
                    hide_index=True
                )

                # --------------------------------------
                # Visualization
                # --------------------------------------

                st.write(
                    "### 📊 Measurement Distribution"
                )

                fig = plot_measurement_distribution(
                    results
                )

                st.pyplot(
                    fig,
                    width="stretch"
                )

            except Exception as e:

                st.error(
                    f"Simulation failed: {e}"
                )


# ==================================================
# QFT
# ==================================================

if algorithm == "Quantum Fourier Transform (QFT)":

    st.header("🔬 Quantum Fourier Transform")

    st.write(
        "The Quantum Fourier Transform (QFT) is a fundamental "
        "quantum transformation used in important quantum "
        "algorithms such as Shor's algorithm."
    )

    st.subheader("Circuit Configuration")

    n = st.slider(
        "Number of qubits",
        min_value=1,
        max_value=5,
        value=3
    )

    qc = qft_circuit(n)

    display_circuit_tools(qc)


# ==================================================
# DEUTSCH-JOZSA
# ==================================================

elif algorithm == "Deutsch-Jozsa Algorithm":

    st.header("🔍 Deutsch-Jozsa Algorithm")

    st.write(
        "The Deutsch-Jozsa algorithm determines whether a "
        "Boolean function is constant or balanced using "
        "quantum parallelism."
    )

    st.subheader("Circuit Configuration")

    n = st.slider(
        "Number of input qubits",
        min_value=1,
        max_value=5,
        value=3
    )

    oracle_type = st.selectbox(
        "Oracle Type",
        [
            "constant",
            "balanced"
        ]
    )

    qc = deutsch_jozsa_circuit(
        n=n,
        oracle_type=oracle_type
    )

    display_circuit_tools(qc)


# ==================================================
# BERNSTEIN-VAZIRANI
# ==================================================

elif algorithm == "Bernstein-Vazirani Algorithm":

    st.header("🔐 Bernstein-Vazirani Algorithm")

    st.write(
        "The Bernstein-Vazirani algorithm identifies a hidden "
        "binary string using a single query to a quantum oracle."
    )

    st.subheader("Circuit Configuration")

    secret_string = st.text_input(
        "Secret binary string",
        value="1011",
        help="Enter a binary string containing only 0 and 1."
    )

    if secret_string and all(
        bit in "01" for bit in secret_string
    ):

        qc = bernstein_vazirani_circuit(
            secret_string
        )

        display_circuit_tools(qc)

    else:

        st.warning(
            "Please enter a valid binary string."
        )


# ==================================================
# SIMON
# ==================================================

elif algorithm == "Simon's Algorithm":

    st.header("🔑 Simon's Algorithm")

    st.write(
        "Simon's algorithm finds a hidden non-zero binary "
        "string by exploiting quantum interference."
    )

    st.subheader("Circuit Configuration")

    secret = st.text_input(
        "Hidden secret string",
        value="101",
        help=(
            "Enter a non-zero binary string. "
            "For example: 101"
        )
    )

    if (
        secret
        and all(bit in "01" for bit in secret)
        and "1" in secret
    ):

        qc = simon_circuit(
            secret
        )

        display_circuit_tools(qc)

    else:

        st.warning(
            "Secret must contain only 0 and 1 "
            "and must contain at least one 1."
        )


# ==================================================
# GROVER
# ==================================================

elif algorithm == "Grover's Algorithm":

    st.header("🎯 Grover's Search Algorithm")

    st.write(
        "Grover's algorithm provides a quadratic speedup "
        "for searching an unstructured database."
    )

    st.subheader("Search Configuration")

    target = st.text_input(
        "Target binary state",
        value="101",
        help="Enter the state you want Grover's algorithm to find."
    )

    if target and all(
        bit in "01" for bit in target
    ):

        qc = grover_circuit(
            target
        )

        display_circuit_tools(qc)

    else:

        st.warning(
            "Please enter a valid binary target."
        )


# ==================================================
# COMPLEXITY
# ==================================================

elif algorithm == "Complexity Comparison":

    st.header(
        "📊 Quantum Algorithm Complexity Comparison"
    )

    st.write(
        "Compare the classical and quantum computational "
        "complexities of the algorithms included in the "
        "demonstrator."
    )

    complexities = get_complexity()

    rows = []

    for algorithm_name, data in complexities.items():

        rows.append(
            {
                "Algorithm": algorithm_name,
                "Classical Complexity": data["classical"],
                "Quantum Complexity": data["quantum"],
                "Description": data["description"]
            }
        )

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

    st.subheader("Why Quantum Algorithms Matter")

    st.info(
        "Quantum algorithms can provide significant speedups "
        "for specific computational problems. For example, "
        "Grover's algorithm provides a quadratic speedup for "
        "unstructured search."
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Quantum Algorithm Demonstrator • "
    "Educational Quantum Computing Project"
)
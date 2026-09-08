# Quantum Algorithm Demonstrator

An interactive educational application for exploring fundamental quantum algorithms through circuit visualization, simulation, measurement results, transpilation analysis, and classical-versus-quantum complexity comparison.

## Project Overview

The **Quantum Algorithm Demonstrator** is a Qiskit-based educational application developed using Python and Streamlit.

The application allows users to select different quantum algorithms, configure their inputs, generate and visualize quantum circuits, simulate their execution, view measurement results, analyze circuit complexity, transpile circuits using different optimization levels, and compare classical and quantum computational complexity.

The project is designed to provide an interactive and beginner-friendly way to understand the principles and practical implementation of quantum algorithms.

## Objectives

* Understand fundamental quantum algorithms.
* Visualize quantum circuits interactively.
* Implement quantum algorithms using Qiskit.
* Simulate quantum circuits using Qiskit Aer.
* Analyze measurement results.
* Visualize measurement distributions.
* Demonstrate quantum circuit transpilation.
* Compare classical and quantum computational complexity.
* Provide an easy-to-use educational interface for learning quantum computing.
* Validate implementations through automated testing.

## Algorithms Implemented

### 1. Quantum Fourier Transform (QFT)

The Quantum Fourier Transform is a fundamental quantum transformation used in several quantum algorithms, including Shor's algorithm.

**Features:**

* Configurable number of qubits.
* Hadamard gates.
* Controlled phase rotations.
* Qubit swap operations.
* Circuit visualization.
* Circuit simulation.
* Measurement distribution.

### 2. Deutsch-Jozsa Algorithm

The Deutsch-Jozsa algorithm determines whether a Boolean function is constant or balanced using quantum parallelism.

**Features:**

* Configurable number of input qubits.
* Constant oracle.
* Balanced oracle.
* Quantum circuit construction.
* Circuit visualization.
* Simulation and measurement results.

### 3. Bernstein-Vazirani Algorithm

The Bernstein-Vazirani algorithm identifies a hidden binary string using a single query to a quantum oracle.

**Features:**

* User-defined secret binary string.
* Oracle construction.
* Quantum circuit visualization.
* Circuit simulation.
* Measurement results.

### 4. Simon's Algorithm

Simon's algorithm finds a hidden non-zero binary string by exploiting quantum interference.

**Features:**

* User-defined hidden secret.
* Simon oracle construction.
* Quantum circuit visualization.
* Circuit simulation.
* Measurement validation.
* Secret-string recovery.

### 5. Grover's Search Algorithm

Grover's algorithm provides a quadratic quantum speedup for searching an unstructured database.

**Features:**

* User-defined target state.
* Oracle construction.
* Diffusion operator.
* Configurable target input.
* Circuit visualization.
* Simulation and measurement results.

## Application Features

* Interactive Streamlit interface.
* Quantum circuit visualization.
* Quantum circuit simulation.
* Measurement result tables.
* Measurement distribution charts.
* Circuit depth analysis.
* Gate count analysis.
* Circuit transpilation.
* Transpiler optimization levels 0-3.
* Classical-versus-quantum complexity comparison.
* Input validation.
* Automated unit testing.
* Generated circuit diagrams.
* Generated result plots.

## System Architecture

```text
                    User
                     |
                     v
           Streamlit Web Interface
                     |
                     v
             Algorithm Selection
                     |
          +----------+----------+
          |          |          |
          v          v          v
         QFT       DJ / BV   Simon / Grover
          |          |          |
          +----------+----------+
                     |
                     v
               Qiskit Circuit
                     |
          +----------+----------+
          |                     |
          v                     v
     Transpilation         Qiskit Aer
                              Simulator
          |                     |
          +----------+----------+
                     |
                     v
             Measurement Results
                     |
          +----------+----------+
          |                     |
          v                     v
      Result Table       Distribution Plot
```

## Technologies Used

* Python
* Qiskit
* Qiskit Aer
* Streamlit
* NumPy
* Pandas
* Matplotlib
* Pytest
* pylatexenc

## Project Structure

```text
Quantum-Algorithm-Demonstrator/
|
+-- algorithms/
|   +-- __init__.py
|   +-- deutsch_jozsa.py
|   +-- bernstein_vazirani.py
|   +-- simon.py
|   +-- grover.py
|   +-- qft.py
|
+-- utils/
|   +-- __init__.py
|   +-- simulator.py
|   +-- complexity.py
|   +-- visualization.py
|   +-- transpiler.py
|
+-- tests/
|   +-- test_quantum.py
|
+-- notebooks/
|   +-- Quantum_Algorithm_Demonstrator.ipynb
|
+-- outputs/
|   +-- circuits/
|   +-- plots/
|
+-- report/
|
+-- app.py
+-- generate_outputs.py
+-- transpilation_analysis.py
+-- requirements.txt
+-- README.md
+-- .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/LikhithaBanna/QC-Product-2.git
cd QC-Product-2
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```cmd
pip install -r requirements.txt
```

## Running the Streamlit Application

After activating the virtual environment, run:

```cmd
streamlit run app.py
```

The application opens in a web browser.

The interface provides access to:

* Quantum Fourier Transform
* Deutsch-Jozsa Algorithm
* Bernstein-Vazirani Algorithm
* Simon's Algorithm
* Grover's Search Algorithm
* Complexity Comparison

Each algorithm can be configured and simulated through the interface.

## Running the Jupyter Notebook

Launch Jupyter Notebook using:

```cmd
jupyter notebook
```

Open:

```text
notebooks/Quantum_Algorithm_Demonstrator.ipynb
```

The notebook demonstrates the algorithms, circuits, simulation results, visualization, complexity analysis, and transpilation analysis.

## Running Automated Tests

Run the complete test suite using:

```cmd
pytest
```

The project includes tests for:

* Deutsch-Jozsa
* Bernstein-Vazirani
* Simon's Algorithm
* Grover's Algorithm
* QFT circuit structure
* Input validation
* Simon secret recovery

The implemented test suite contains 10 automated tests.

Expected result:

```text
10 passed
```

## Generating Circuit Diagrams and Result Plots

Run:

```cmd
python generate_outputs.py
```

Generated circuit diagrams are saved in:

```text
outputs/circuits/
```

Generated measurement distribution plots are saved in:

```text
outputs/plots/
```

## Transpilation Analysis

To compare original and transpiled circuits, run:

```cmd
python transpilation_analysis.py
```

The analysis reports:

* Number of qubits.
* Original circuit depth.
* Transpiled circuit depth.
* Original gate count.
* Transpiled gate count.
* Gate operation statistics.

### Example Transpilation Results

| Algorithm          | Original Depth | Transpiled Depth | Original Gates | Transpiled Gates |
| ------------------ | -------------: | ---------------: | -------------: | ---------------: |
| Deutsch-Jozsa      |              7 |                6 |             14 |               13 |
| Bernstein-Vazirani |              7 |                6 |             17 |               14 |
| Simon's Algorithm  |              5 |                5 |             12 |               12 |
| Grover's Algorithm |             22 |               10 |             46 |               21 |
| QFT                |              6 |                6 |              7 |                7 |

Grover's circuit showed the largest reduction in both circuit depth and gate count in the implemented analysis.

## Complexity Comparison

The demonstrator provides a theoretical comparison of classical and quantum approaches.

| Algorithm          | Classical Complexity | Quantum Complexity   |
| ------------------ | -------------------- | -------------------- |
| Deutsch-Jozsa      | O(2^n) queries       | O(1) query           |
| Bernstein-Vazirani | O(n) queries         | O(1) query           |
| Simon's Algorithm  | O(2^n)               | O(n)                 |
| Grover's Search    | O(N)                 | O(sqrt(N))           |
| QFT                | O(n^2) circuit gates | O(n^2) circuit gates |

**Note:** Complexity comparisons should be interpreted carefully. For Deutsch-Jozsa and Bernstein-Vazirani, the commonly quoted quantum advantage refers to oracle query complexity, while the complete circuit still requires gates that scale with the number of qubits.

## Simulation

Quantum circuits are simulated using **Qiskit Aer**.

The default simulation configuration uses:

```text
Shots: 1024
Simulator seed: 42
```

Measurement results are presented as state-count distributions and visualized using Matplotlib.

## Generated Outputs

The project generates:

```text
outputs/
|
+-- circuits/
|   +-- deutsch_jozsa.png
|   +-- bernstein_vazirani.png
|   +-- simon.png
|   +-- grover.png
|   +-- qft.png
|
+-- plots/
    +-- deutsch_jozsa_results.png
    +-- bernstein_vazirani_results.png
    +-- simon_results.png
    +-- grover_results.png
    +-- qft_results.png
```

These outputs are useful for analysis, documentation, presentations, and demonstrations.

## Testing Results

The automated test suite has been executed successfully.

```text
10 passed
```

The tests verify:

* Circuit construction.
* Simulation behavior.
* Expected measurement results.
* Simon secret recovery.
* QFT structure.
* Invalid-input handling.

## Challenges and Limitations

* Quantum simulation is performed on a classical computer.
* Simulation cost increases as the number of qubits grows.
* The current application focuses on fundamental educational algorithms.
* The implemented circuits are not intended for production-scale quantum workloads.
* Results from quantum simulations can be probabilistic depending on the algorithm and circuit.
* The current implementation does not include direct IBM Quantum hardware execution.

## Future Enhancements

Possible future improvements include:

* Noisy quantum circuit simulation.
* IBM Quantum hardware execution.
* Additional quantum algorithms.
* Interactive circuit editing.
* More advanced visualization.
* Bloch sphere visualization.
* Statevector visualization.
* Runtime benchmarking.
* Hardware-specific transpilation.
* Larger algorithm configurations.
* Exporting simulation results.
* Improved educational explanations.

## Educational Value

The project demonstrates how theoretical quantum computing concepts can be converted into executable Qiskit circuits and explored through an interactive interface.

It provides practical exposure to:

* Qubits.
* Superposition.
* Quantum interference.
* Quantum measurement.
* Quantum oracles.
* Quantum search.
* Quantum Fourier Transform.
* Circuit optimization.
* Quantum simulation.
* Algorithmic complexity.

## References

1. Qiskit Documentation - IBM Quantum.
2. Qiskit Aer Documentation.
3. Nielsen, M. A. and Chuang, I. L., *Quantum Computation and Quantum Information*.
4. IBM Quantum Learning resources.
5. Research literature on Deutsch-Jozsa, Bernstein-Vazirani, Simon's, Grover's, and Quantum Fourier Transform algorithms.

## Project Information

**Project:** Quantum Algorithm Demonstrator

**Platform:** Python + Qiskit + Streamlit

**Purpose:** Educational demonstration and comparison of fundamental quantum algorithms.

**Repository:** QC-Product-2

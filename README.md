\# ⚛️ Quantum Algorithm Demonstrator



An interactive educational application for exploring fundamental quantum algorithms through circuit visualization, simulation, transpilation, measurement results, and complexity comparison.



\## 📌 Project Overview



The \*\*Quantum Algorithm Demonstrator\*\* is a Qiskit-based educational application developed using Python and Streamlit.



The application allows users to select different quantum algorithms, configure their inputs, visualize the corresponding quantum circuits, simulate their execution, view measurement distributions, transpile circuits, and compare computational complexity.



\## 🎯 Objectives



\- Understand fundamental quantum algorithms.

\- Visualize quantum circuits interactively.

\- Simulate quantum algorithms using Qiskit.

\- Analyze measurement results.

\- Demonstrate quantum circuit transpilation.

\- Compare classical and quantum computational complexity.

\- Provide an easy-to-use educational interface for learning quantum computing.



\## 🧠 Algorithms Implemented



\### 1. Quantum Fourier Transform (QFT)



QFT is a fundamental quantum transformation used in several quantum algorithms, including Shor's algorithm.



\*\*Features:\*\*

\- Configurable number of qubits.

\- QFT circuit generation.

\- Circuit visualization.

\- Circuit simulation.

\- Measurement distribution.



\### 2. Deutsch-Jozsa Algorithm



Determines whether a Boolean function is constant or balanced using quantum parallelism.



\*\*Features:\*\*

\- Configurable input qubits.

\- Constant oracle.

\- Balanced oracle.

\- Circuit visualization.

\- Simulation.



\### 3. Bernstein-Vazirani Algorithm



Identifies a hidden binary string using a single query to a quantum oracle.



\*\*Features:\*\*

\- User-defined secret binary string.

\- Oracle construction.

\- Circuit visualization.

\- Simulation.



\### 4. Simon's Algorithm



Finds a hidden non-zero binary string by exploiting quantum interference.



\*\*Features:\*\*

\- User-defined hidden secret.

\- Simon oracle construction.

\- Circuit visualization.

\- Simulation.



\### 5. Grover's Search Algorithm



Provides a quadratic speedup for searching an unstructured database.



\*\*Features:\*\*

\- User-defined target state.

\- Oracle construction.

\- Diffusion operator.

\- Circuit visualization.

\- Simulation.



\## 🖥️ Application Features



\- Interactive Streamlit interface

\- Quantum circuit visualization

\- Quantum circuit simulation

\- Measurement result tables

\- Measurement distribution charts

\- Circuit depth analysis

\- Gate count analysis

\- Circuit transpilation

\- Optimization levels 0–3

\- Classical vs quantum complexity comparison

\- Input validation



\## 🛠️ Technologies Used



\- \*\*Python\*\*

\- \*\*Qiskit\*\*

\- \*\*Streamlit\*\*

\- \*\*NumPy\*\*

\- \*\*Pandas\*\*

\- \*\*Matplotlib\*\*

\- \*\*Pytest\*\*



\## 📂 Project Structure



```text

Quantum-Algorithm-Demonstrator/

│

├── algorithms/

│   ├── \_\_init\_\_.py

│   ├── deutsch\_jozsa.py

│   ├── bernstein\_vazirani.py

│   ├── simon.py

│   ├── grover.py

│   └── qft.py

│

├── utils/

│   ├── simulator.py

│   ├── complexity.py

│   ├── visualization.py

│   └── transpiler.py

│

├── tests/

│   └── test\_quantum.py

│

├── app.py

├── requirements.txt

└── README.md


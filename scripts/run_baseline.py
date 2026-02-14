import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from qiskit_aer import AerSimulator
from qiskit import transpile
from src.circuits.benchmark_circuits import bell_circuit

qc = bell_circuit()

sim = AerSimulator()
tqc = transpile(qc, sim)

result = sim.run(tqc, shots=1000).result()
print("Ideal Counts:", result.get_counts())

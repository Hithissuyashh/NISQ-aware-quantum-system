import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel
from qiskit import transpile
from src.circuits.benchmark_circuits import bell_circuit

qc = bell_circuit()

# build basic noise model from simulator defaults
noise_model = NoiseModel.from_backend(AerSimulator())

sim = AerSimulator(noise_model=noise_model)

tqc = transpile(qc, sim)

result = sim.run(tqc, shots=1000).result()
counts = result.get_counts()
print("Noisy Counts:", counts)

with open("noisy_output_final.txt", "w") as f:
    f.write(f"Noisy Counts: {counts}\n")

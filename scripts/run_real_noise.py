import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
print("START REAL NOISE TEST")
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel
from qiskit import transpile
from circuits.benchmark_circuits import bell_circuit
service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.backend("ibm_fez")
print("Backend:", backend.name)
noise_model = NoiseModel.from_backend(backend)
qc = bell_circuit()
sim = AerSimulator(noise_model=noise_model)
tqc = transpile(qc, sim)
result = sim.run(tqc, shots=1000).result()
print("Counts:", result.get_counts())

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel
from qiskit_ibm_runtime import QiskitRuntimeService
from circuits.benchmark_circuits import bell_circuit
from backend.noise_profile import best_connected_pair
service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.backend("ibm_fez")
noise_model = NoiseModel.from_backend(backend)
sim = AerSimulator(noise_model=noise_model)
qc = bell_circuit()
# -------- default mapping --------
t_default = transpile(qc, backend)
r_default = sim.run(t_default, shots=2000).result().get_counts()
# -------- optimizer mapping --------
pair, _ = best_connected_pair("ibm_fez")
t_opt = transpile(qc, backend, initial_layout=list(pair))
r_opt = sim.run(t_opt, shots=2000).result().get_counts()
print("Default counts:", r_default)
print("Optimized counts:", r_opt)
def bell_error(counts):
    good = counts.get("00",0) + counts.get("11",0)
    total = sum(counts.values())
    return 1 - good/total
print("Default error rate:", bell_error(r_default))
print("Optimized error rate:", bell_error(r_opt))

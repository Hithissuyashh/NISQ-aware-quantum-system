import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService
from circuits.benchmark_circuits import bell_circuit
from backend.noise_profile import get_qubit_error_scores
service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.backend("ibm_fez")
qc = bell_circuit()
# default mapping
t_default = transpile(qc, backend)
# noise-aware mapping
scores = get_qubit_error_scores("ibm_fez")
best2 = [scores[0][0], scores[1][0]]
t_noise_aware = transpile(
    qc,
    backend,
    initial_layout=best2
)
print("Default layout:", t_default.layout)
print("Noise-aware layout:", t_noise_aware.layout)
print("Default depth:", t_default.depth())
print("Noise-aware depth:", t_noise_aware.depth())

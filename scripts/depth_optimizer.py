import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService
from circuits.benchmark_circuits import bell_circuit
from backend.noise_profile import best_connected_pair, get_qubit_error_scores
service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.backend("ibm_fez")
qc = bell_circuit()
scores = get_qubit_error_scores("ibm_fez")
top = [q for q, *_ in scores[:8]]
best = None
best_depth = 10**9
for a in top:
    for b in top:
        if a == b:
            continue
        try:
            t = transpile(qc, backend, initial_layout=[a,b])
            d = t.depth()
            if d < best_depth:
                best_depth = d
                best = (a,b)
        except:
            pass
print("Depth-optimal pair:", best)
print("Depth:", best_depth)

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService
from circuits.benchmark_circuits import bell_circuit
from backend.noise_profile import get_qubit_error_scores
service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.backend("ibm_fez")
qc = bell_circuit()
scores = get_qubit_error_scores("ibm_fez")
top = scores[:6]
best = None
best_metric = -1
for (q1, s1, *_ ) in top:
    for (q2, s2, *_ ) in top:
        if q1 == q2:
            continue
        try:
            t = transpile(qc, backend, initial_layout=[q1,q2])
            depth = t.depth()
            fidelity_score = s1 + s2
            metric = fidelity_score / depth   # ? hybrid metric
            if metric > best_metric:
                best_metric = metric
                best = (q1, q2, depth, metric)
        except:
            pass
print("Decision Engine Winner:", best)

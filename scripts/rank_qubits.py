import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from backend.noise_profile import get_qubit_error_scores
scores = get_qubit_error_scores()
print("Top 10 best qubits:")
for q, score, t1, t2, ro in scores[:10]:
    print(f"Q{q} score={score:.2e} readout_err={ro:.4f}")

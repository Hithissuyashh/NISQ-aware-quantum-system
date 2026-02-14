import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
print("VIS TEST START")
import numpy as np
import matplotlib.pyplot as plt
from qiskit import transpile
from qiskit.quantum_info import Statevector, state_fidelity, DensityMatrix
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel
from qiskit_ibm_runtime import QiskitRuntimeService
from circuits.benchmark_circuits import bell_circuit
# ---------- IDEAL CIRCUIT ----------
ideal_qc = bell_circuit()
ideal_qc.remove_final_measurements()
ideal_state = Statevector.from_instruction(ideal_qc)
# ---------- NOISY CIRCUIT ----------
noisy_qc = bell_circuit()
noisy_qc.remove_final_measurements()
noisy_qc.save_density_matrix()
service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.backend("ibm_fez")
noise_model = NoiseModel.from_backend(backend)
sim = AerSimulator(noise_model=noise_model, method="density_matrix")
tqc = transpile(noisy_qc, sim)
result = sim.run(tqc).result()
dm = DensityMatrix(result.data(0)["density_matrix"])
fid = state_fidelity(dm, ideal_state)
print("Fidelity:", fid)
plt.imshow(np.abs(dm.data))
plt.title("Noisy Density Matrix")
plt.colorbar()
plt.show()

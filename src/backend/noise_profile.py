from qiskit_ibm_runtime import QiskitRuntimeService
def get_qubit_error_scores(backend_name="ibm_fez"):
    service = QiskitRuntimeService(channel="ibm_quantum_platform")
    backend = service.backend(backend_name)
    props = backend.properties()
    scores = []
    for q in range(len(props.qubits)):
        t1 = props.t1(q)
        t2 = props.t2(q)
        readout_err = props.readout_error(q)
        score = (t1 + t2) / (1 + readout_err)
        scores.append((q, score, t1, t2, readout_err))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores
from qiskit_ibm_runtime import QiskitRuntimeService
def best_connected_pair(backend_name="ibm_fez"):
    service = QiskitRuntimeService(channel="ibm_quantum_platform")
    backend = service.backend(backend_name)
    props = backend.properties()
    cmap = backend.configuration().coupling_map
    scores = {}
    for q in range(len(props.qubits)):
        t1 = props.t1(q)
        t2 = props.t2(q)
        ro = props.readout_error(q)
        scores[q] = (t1 + t2) / (1 + ro)
    best_pair = None
    best_score = -1
    for a, b in cmap:
        pair_score = scores[a] + scores[b]
        if pair_score > best_score:
            best_score = pair_score
            best_pair = (a, b)
    return best_pair, best_score

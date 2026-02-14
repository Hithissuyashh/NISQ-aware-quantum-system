from qiskit_ibm_runtime import QiskitRuntimeService

def get_backend(name="ibm_brisbane"):
    service = QiskitRuntimeService(channel="ibm_quantum")
    backend = service.backend(name)
    return backend


def print_backend_noise(backend):
    props = backend.properties()

    print("\nQubit T1/T2:")
    for q in range(min(5, len(props.qubits))):
        t1 = props.t1(q)
        t2 = props.t2(q)
        print(f"Q{q}: T1={t1:.2e}, T2={t2:.2e}")

    print("\nSample gate errors:")
    for g in props.gates[:5]:
        print(g.gate, g.qubits, g.parameters)

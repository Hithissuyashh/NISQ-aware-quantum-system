from qiskit_ibm_runtime import QiskitRuntimeService
try:
    QiskitRuntimeService.save_account(
        channel="ibm_quantum",
        token="7KylyNEonF1LzR2mQnCf3qUhvBP-eFHRrFzLtweLWGD6",
        overwrite=True
    )
    print("SUCCESS")
except Exception as e:
    print(f"FAILED: {e}")

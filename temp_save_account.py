from qiskit_ibm_runtime import QiskitRuntimeService
import traceback

try:
    QiskitRuntimeService.save_account(
        channel="ibm_quantum",
        token="7KylyNEonF1LzR2mQnCf3qUhvBP-eFHRrFzLtweLWGD6",
        overwrite=True
    )
    print("Account saved successfully.")
except Exception as e:
    print(f"Error saving account: {e}")
    traceback.print_exc()

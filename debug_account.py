from qiskit_ibm_runtime import QiskitRuntimeService
import traceback
import sys

token = "7KylyNEonF1LzR2mQnCf3qUhvBP-eFHRrFzLtweLWGD6"

print("Python version:", sys.version)

try:
    print("Attempting to save account with channel='ibm_quantum'...")
    QiskitRuntimeService.save_account(
        channel="ibm_quantum",
        token=token,
        overwrite=True
    )
    print("Account saved successfully with channel='ibm_quantum'.")
except Exception as e:
    print(f"Error saving with channel='ibm_quantum': {e}")
    traceback.print_exc()

try:
    print("\nChecking saved accounts...")
    accounts = QiskitRuntimeService.saved_accounts()
    print("Saved accounts:", accounts)
except Exception as e:
    print(f"Error checking saved accounts: {e}")

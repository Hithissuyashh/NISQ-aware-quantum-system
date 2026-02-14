from qiskit_ibm_runtime import QiskitRuntimeService
import os

token = "7KylyNEonF1LzR2mQnCf3qUhvBP-eFHRrFzLtweLWGD6"
log_file = "account_log.txt"

with open(log_file, "w") as f:
    f.write("Starting account save process...\n")
    try:
        # Save as ibm_quantum
        QiskitRuntimeService.save_account(channel="ibm_quantum", token=token, overwrite=True)
        f.write("Saved as ibm_quantum\n")
    except Exception as e:
        f.write(f"Error saving as ibm_quantum: {e}\n")

    try:
        # Save as ibm_quantum_platform
        QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token=token, overwrite=True)
        f.write("Saved as ibm_quantum_platform\n")
    except Exception as e:
        f.write(f"Error saving as ibm_quantum_platform: {e}\n")

    try:
        accounts = QiskitRuntimeService.saved_accounts()
        f.write(f"Saved accounts: {list(accounts.keys())}\n")
    except Exception as e:
        f.write(f"Error listing accounts: {e}\n")

print("Done")

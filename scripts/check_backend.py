import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.backend.backend_info import get_backend, print_backend_noise

try:
    backend = get_backend()
    print("Backend:", backend.name)
    print_backend_noise(backend)
except Exception as e:
    print(f"Error: {e}")
    print("Please ensure you have saved your IBM Quantum account token.")

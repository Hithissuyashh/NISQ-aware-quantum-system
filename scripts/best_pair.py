import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from backend.noise_profile import best_connected_pair
pair, score = best_connected_pair()
print("Best connected pair:", pair)
print("Pair score:", score)

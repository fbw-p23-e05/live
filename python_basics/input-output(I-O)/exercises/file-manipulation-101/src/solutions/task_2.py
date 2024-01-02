"""Obtaining the current path."""
import os 

ROOT = os.getcwd()
DATA_ROOT = os.path.join(ROOT, 'src/data/initial')
DATA_ROOT = os.path.join(ROOT, 'src', 'data', 'initial')

print(ROOT)
print(DATA_ROOT)

import os
import sys

# Obtener el directorio padre del directorio actual (tests)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
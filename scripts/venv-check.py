# This script checks if the current Python interpreter is running inside a virtual environment.
import sys
print(sys.prefix != sys.base_prefix)

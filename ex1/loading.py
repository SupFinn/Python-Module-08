import sys
from importlib import util, metadata

def main():
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    packages = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
        "numpy": "Numerical computation ready"
    }

    for package, message in packages.items():
        if util.find_spec(package) is not None:
            print(f"[OK] {package} ({metadata.version(package)}) - {message}")
        else:
            print(f"[MISSING] {package} - Please install it with pip or Poetry")

    print()
    missing_packages = [pkg for pkg in packages if util.find_spec(pkg) is None]
    if missing_packages:
        print("Some packages are missing:", ", ".join(missing_packages))
        print("Please install them with pip or Poetry")
        sys.exit(1)

    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np



if __name__ == "__main__":
    main()

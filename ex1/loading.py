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

    print()
    print("Analyzing Matrix data...")
    data_points = 1000
    print(f"Processing {data_points} data points...")
    data = np.random.randn(data_points)
    df = pd.DataFrame({
        'agent_id': range(data_points),
        'signal_strength': data
    })

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.plot(df['agent_id'], df['signal_strength'], linewidth=0.5, alpha=0.7)
    plt.title('Matrix Signal Analysis')
    plt.xlabel('Agent ID')
    plt.ylabel('Signal Strength')
    plt.grid(True, alpha=0.3)

    plt.savefig('matrix_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()

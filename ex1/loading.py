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
    }

    for package, message in packages.items():
        if util.find_spec(package) is not None:
            print(f"[OK] {package} ({metadata.version(package)}) - {message}")
        else:
            print(f"[MISSING] {package} - "
                  "Please install it with pip or Poetry")

    print()
    missing_packages = [pkg for pkg in packages if util.find_spec(pkg) is None]
    if missing_packages:
        print("Some packages are missing:", ", ".join(missing_packages))
        print("For installation:\n")
        print("--: Using pip:\n")
        print("pip install -r requirements.txt\n")
        print("--: Using poetry:\n")
        print("poetry install")
        return

    print("\nAnalyzing Matrix data...")
    import pandas
    import matplotlib.pyplot as plt
    import requests

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code >= 404:
        print("HTTP error.")
        return

    request_data: list[dict] = response.json()
    print("Processing 1000 data points...")
    pandas_format = pandas.DataFrame(request_data)
    print("Generating visualization...\n")

    numberical_columns = pandas_format[["id", "userId"]]

    numberical_columns.plot()
    print("Analysis complete!")
    plt.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()

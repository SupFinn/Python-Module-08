import sys
import os
import site


def print_site_packages() -> None:
    """Safely print the site-packages installation path."""
    try:
        paths = site.getsitepackages()
        if paths:
            print(paths[0])
        else:
            print("Unable to determine site-packages location.")
    except Exception as error:
        print(f"Could not retrieve site-packages path: {error}")


def main():
    if sys.prefix != sys.base_prefix:
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print()

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()

        print("Package installation path:")
        print_site_packages()

    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: Not detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()

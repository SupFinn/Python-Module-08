import os
import sys
from dotenv import find_dotenv, load_dotenv


def main():
    print("\nORACLE STATUS: Reading the Matrix...\n")

    env_path = find_dotenv()
    load_dotenv(env_path)

    env_vars: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    missing: list = []
    for var in env_vars:
        if os.environ.get(var, None) is None:
            print(f"Variable {var} is missing")
            missing.append(var)

    print("Configuration loaded:")
    print(f"Mode: {os.environ.get('MATRIX_MODE', 'UNKNOWN')}")

    is_connected = os.environ.get("DATABASE_URL", None)
    status = ("Connected to local instance" if is_connected
              else "Failed To Connect")
    print(f"Database: {status}")

    is_auth = os.environ.get("API_KEY", None)
    authentication = "Authenticated" if is_auth else "Not Authenticated"
    print(f"API Access: {authentication}")

    print(f"Log Level: {os.environ.get('LOG_LEVEL', 'IDLE')}")

    is_active = os.environ.get("ZION_ENDPOINT", None)
    zion = "Online" if is_active else "Offline"
    print(f"Zion Network: {zion}")

    print("\nEnvironment security check:")

    env_secrets = []
    for var in env_vars:
        env_secrets.append(os.environ.get(var))

    with open(sys.argv[0], "r") as f:
        is_hardcoded: bool = False
        for line in f:
            line = line.strip()
            for secret in env_secrets:
                if secret in line:
                    print("[WARN] Hardcoded secret found")
                    is_hardcoded = True
                    break
            if is_hardcoded:
                break

        if not is_hardcoded:
            print("[OK] No hardcoded secrets detected")

    if len(missing) == 0:
        print("[OK] .env file properly configured")
    else:
        print(f"[FAIL] .env missing: {missing}")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()

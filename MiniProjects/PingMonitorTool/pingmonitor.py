import subprocess
import platform

# Determine ping command based on operating system
param = "-n" if platform.system().lower() == "windows" else "-c"

def ping_host(host):
    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"{host} -> ONLINE ✅")
        else:
            print(f"{host} -> OFFLINE ❌")

    except Exception as e:
        print(f"Error checking {host}: {e}")

def main():
    try:
        with open("hosts.txt", "r") as file:
            hosts = [line.strip() for line in file if line.strip()]

        print("\n📡 Ping Monitor Started...\n")

        for host in hosts:
            ping_host(host)

    except FileNotFoundError:
        print("hosts.txt file not found.")

if __name__ == "__main__":
    main()
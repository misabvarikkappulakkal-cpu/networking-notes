import socket
import subprocess
import platform


def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", param, "4", host]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"\n✅ {host} is reachable")
        else:
            print(f"\n❌ {host} is unreachable")

    except Exception as e:
        print(f"Error: {e}")


def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n🌐 {domain} → {ip}")

    except socket.gaierror:
        print("Domain could not be resolved.")


while True:
    print("\n===== CONNECTIVITY CHECKER =====")
    print("1. Ping Host")
    print("2. Resolve Domain")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        host = input("Enter host/IP: ")
        ping_host(host)

    elif choice == "2":
        domain = input("Enter domain: ")
        resolve_domain(domain)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
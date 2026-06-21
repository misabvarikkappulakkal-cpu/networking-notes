import socket

print("=== DNS Lookup Tool ===")

while True:
    domain = input("\nEnter a domain name (or 'exit'): ")

    if domain.lower() == "exit":
        print("Goodbye!")
        break

    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP Address: {ip_address}")

    except socket.gaierror:
        print("Invalid domain or unable to resolve.")
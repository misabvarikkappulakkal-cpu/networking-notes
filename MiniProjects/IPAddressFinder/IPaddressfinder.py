import socket

def get_ip_info():
    print("\n===== IP ADDRESS FINDER =====")

    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)

        print(f"Hostname   : {hostname}")
        print(f"IP Address : {ip_address}")

    except socket.error:
        print("Unable to retrieve IP address.")

get_ip_info()
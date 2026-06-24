from scapy.all import sniff, IP
from datetime import datetime

LOG_FILE = "traffic_log.txt"

def log_packet(packet):
    if packet.haslayer(IP):

        timestamp = datetime.now()

        log = (
            f"{timestamp} | "
            f"{packet[IP].src} -> "
            f"{packet[IP].dst}\n"
        )

        with open(LOG_FILE, "a") as file:
            file.write(log)

        print(log.strip())

print("Logging packets...")
sniff(prn=log_packet, store=False)
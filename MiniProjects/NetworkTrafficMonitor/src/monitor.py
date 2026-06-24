from scapy.all import sniff, IP

tcp_count = 0
udp_count = 0
icmp_count = 0

def packet_callback(packet):
    global tcp_count, udp_count, icmp_count

    if packet.haslayer(IP):
        protocol = packet[IP].proto

        if protocol == 6:
            tcp_count += 1
            proto_name = "TCP"

        elif protocol == 17:
            udp_count += 1
            proto_name = "UDP"

        elif protocol == 1:
            icmp_count += 1
            proto_name = "ICMP"

        else:
            proto_name = f"OTHER({protocol})"

        print(
            f"[{proto_name}] "
            f"{packet[IP].src} -> {packet[IP].dst}"
        )

def show_stats():
    print("\n=== Traffic Statistics ===")
    print(f"TCP  : {tcp_count}")
    print(f"UDP  : {udp_count}")
    print(f"ICMP : {icmp_count}")

try:
    print("Monitoring network traffic...")
    sniff(prn=packet_callback, store=False)

except KeyboardInterrupt:
    show_stats() 
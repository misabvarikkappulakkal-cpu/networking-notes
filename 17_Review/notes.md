# Networking Review Notes

## Overview

Networking enables devices to communicate and share resources across local and global networks. Modern networking relies on protocols, addressing schemes, routing mechanisms, and security controls to ensure reliable communication.

---

# 1. Networking Basics

Networking is the connection of two or more devices to exchange data.

### Key Components

* Hosts (Computers, Servers, Phones)
* Switches
* Routers
* Network Interface Cards (NIC)
* Transmission Media

### Benefits

* Resource Sharing
* Communication
* Centralized Management
* Internet Access

---

# 2. Types of Networks

### PAN

Personal Area Network

Example:

* Bluetooth devices

### LAN

Local Area Network

Example:

* Home WiFi
* Office Network

### MAN

Metropolitan Area Network

Example:

* City-wide networks

### WAN

Wide Area Network

Example:

* Internet

---

# 3. IPv4 Addressing

IPv4 addresses uniquely identify devices.

Example:

192.168.1.10

### Structure

* 32-bit address
* 4 octets
* Range: 0-255 per octet

### Types

* Public IP
* Private IP

Private ranges:

* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16

---

# 4. Subnetting Basics

Subnetting divides large networks into smaller networks.

### Benefits

* Better organization
* Reduced broadcast traffic
* Improved security

Example:

192.168.1.0/24

Where:

* Network bits = 24
* Host bits = 8

Hosts:

2^8 - 2 = 254

---

# 5. MAC Address & ARP

### MAC Address

Physical address assigned to a network interface.

Example:

00:1A:2B:3C:4D:5E

### ARP

Address Resolution Protocol maps:

IP Address → MAC Address

Process:

1. ARP Request
2. ARP Reply
3. Communication begins

---

# 6. DNS

Domain Name System translates domain names into IP addresses.

Example:

google.com → 142.x.x.x

### Benefits

* Easy to remember names
* Faster navigation

Popular DNS:

* 8.8.8.8
* 1.1.1.1

---

# 7. DHCP

Dynamic Host Configuration Protocol automatically assigns:

* IP Address
* Subnet Mask
* Gateway
* DNS Server

Advantages:

* Reduces manual work
* Prevents IP conflicts

---

# 8. OSI Model

| Layer | Name         |
| ----- | ------------ |
| 7     | Application  |
| 6     | Presentation |
| 5     | Session      |
| 4     | Transport    |
| 3     | Network      |
| 2     | Data Link    |
| 1     | Physical     |

### Memory Trick

Please Do Not Throw Sausage Pizza Away

---

# 9. Common Protocols

### HTTP

Port 80

Transfers web pages.

### HTTPS

Port 443

Encrypted HTTP.

### FTP

Ports 20/21

File transfer protocol.

### SSH

Port 22

Secure remote administration.

---

# 10. TCP/IP Model

| Layer          | Purpose                |
| -------------- | ---------------------- |
| Application    | User Services          |
| Transport      | End-to-End Delivery    |
| Internet       | Routing                |
| Network Access | Physical Communication |

### Comparison

OSI = 7 Layers

TCP/IP = 4 Layers

---

# 11. Ports & Services

Ports identify applications on a device.

### Common Ports

| Port  | Service |
| ----- | ------- |
| 22    | SSH     |
| 53    | DNS     |
| 80    | HTTP    |
| 443   | HTTPS   |
| 20/21 | FTP     |

### Types

* Well-known Ports (0-1023)
* Registered Ports (1024-49151)
* Dynamic Ports (49152-65535)

---

# 12. Routing Basics

Routing determines the path packets take between networks.

### Router Functions

* Forward packets
* Maintain routing tables
* Connect networks

### Default Gateway

Used when destination is outside local network.

---

# 13. Firewalls & Security Basics

Firewalls monitor and filter network traffic.

### Types

* Hardware Firewall
* Software Firewall

### Security Practices

* Strong passwords
* Disable unused services
* Keep systems updated
* Use SSH instead of Telnet

---

# 14. Linux Networking Commands

### View IP Address

```bash
ip addr
```

### View Routing Table

```bash
ip route
```

### Test Connectivity

```bash
ping google.com
```

### DNS Lookup

```bash
nslookup google.com
```

or

```bash
dig google.com
```

### Open Ports

```bash
ss -tuln
```

### Network Interfaces

```bash
ip link
```

---

# 15. Troubleshooting Basics

### Step 1

Check physical connection.

### Step 2

Verify IP configuration.

### Step 3

Check gateway.

### Step 4

Test connectivity using ping.

### Step 5

Verify DNS resolution.

### Step 6

Inspect firewall settings.

### Step 7

Analyze routing information.

---

# 16. Mini Project Summary

The networking mini project demonstrates practical understanding of:

* IP configuration
* Network diagnostics
* Connectivity testing
* Service inspection
* Linux networking commands

Skills Applied:

✅ IP Addressing

✅ Routing

✅ DNS

✅ DHCP Concepts

✅ Troubleshooting

✅ Linux Networking

---

# Final Quick Revision

* IP identifies devices.
* MAC identifies network interfaces.
* ARP maps IP to MAC.
* DNS resolves names to IPs.
* DHCP assigns network settings automatically.
* TCP is reliable.
* UDP is faster but less reliable.
* Routers connect networks.
* Firewalls protect networks.
* SSH provides secure remote access.
* Troubleshooting follows a step-by-step process.

## Networking Learning Outcome

After completing this repository, you should be able to:

* Understand network communication.
* Configure and troubleshoot basic networks.
* Interpret IP addressing and subnetting.
* Use Linux networking commands confidently.
* Understand routing, DNS, DHCP, and security fundamentals.
* Build a strong foundation for Cloud, Linux, DevOps, and Cybersecurity learning paths.

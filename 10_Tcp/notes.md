# Day 10 - TCP/IP Model

# TCP/IP Model

The TCP/IP model is the foundation of internet communication.

TCP/IP stands for:
- Transmission Control Protocol
- Internet Protocol

## Layers of TCP/IP Model

### 1. Application Layer
Provides services to applications.

Protocols:
- HTTP
- HTTPS
- FTP
- DNS
- SSH

Examples:
- Web browsing
- Email
- File transfer

---

### 2. Transport Layer
Responsible for end-to-end communication.

Protocols:
- TCP
- UDP

TCP:
- Reliable
- Connection-oriented

UDP:
- Faster
- Connectionless

---

### 3. Internet Layer
Handles logical addressing and routing.

Protocols:
- IP
- ICMP

Functions:
- Packet routing
- IP addressing

---

### 4. Network Access Layer
Handles physical transmission.

Examples:
- Ethernet
- Wi-Fi

Functions:
- MAC addressing
- Data transmission

---

## TCP/IP vs OSI Model

| TCP/IP | OSI |
|---|---|
| 4 Layers | 7 Layers |
| Practical | Conceptual |
| Used in Internet | Used for learning |

---

## Important Commands

### Check IP Address

ip addr

### Ping a Host

ping google.com

### Trace Route

traceroute google.com

### DNS Lookup

nslookup google.com
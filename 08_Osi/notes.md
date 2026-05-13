# Day 8 - OSI Model Notes

## What is OSI Model?

OSI stands for:
Open Systems Interconnection Model

It is a 7-layer networking model used to understand how data travels through a network.

Think of it like a 7-floor data apartment tower 🏢📡

Each layer has its own job.

---

# 7 Layers of OSI Model

| Layer Number | Layer Name | Function |
|---|---|---|
| 7 | Application | User interaction |
| 6 | Presentation | Data formatting & encryption |
| 5 | Session | Connection management |
| 4 | Transport | Reliable delivery |
| 3 | Network | Routing & IP addressing |
| 2 | Data Link | MAC addressing |
| 1 | Physical | Cables & signals |

---

# Layer Details

## 7. Application Layer

Provides services to applications.

Examples:
- HTTP
- HTTPS
- FTP
- DNS

---

## 6. Presentation Layer

Responsible for:
- Encryption
- Compression
- Data translation

Examples:
- SSL/TLS
- JPEG
- ASCII

---

## 5. Session Layer

Manages sessions between devices.

Functions:
- Start session
- Maintain session
- End session

---

## 4. Transport Layer

Provides reliable communication.

Protocols:
- TCP
- UDP

Functions:
- Segmentation
- Error checking
- Flow control

---

## 3. Network Layer

Responsible for routing packets.

Protocols:
- IP
- ICMP

Devices:
- Routers

---

## 2. Data Link Layer

Handles:
- MAC addresses
- Frame delivery

Devices:
- Switches

Protocols:
- Ethernet

---

## 1. Physical Layer

Actual hardware transmission.

Examples:
- Cables
- Fiber optics
- Radio signals

Devices:
- Hubs
- Repeaters

---

# Encapsulation

Data moves down the OSI layers before transmission.

Application Data
↓
Segments
↓
Packets
↓
Frames
↓
Bits

---

# Real World Example

Opening YouTube:

- Application → Browser request
- Transport → TCP communication
- Network → IP routing
- Data Link → MAC delivery
- Physical → Electrical/WiFi signals

---

# Mnemonic

Top to Bottom:

All People Seem To Need Data Processing

Bottom to Top:

Please Do Not Throw Sausage Pizza Away

---

# Why OSI Model Matters

- Helps troubleshoot networks
- Makes protocols easier to understand
- Standardizes networking concepts
- Important for CCNA, RHCSA, cloud, and cybersecurity
## Output

Enter target IP or hostname: scanme.nmap.org 

Scanning scanme.nmap.org... 

Port 22: OPEN 
Port 80: OPEN 

Scan Completed.

# Port Scanner (Basic) - Notes

A Port Scanner is a tool used to check which ports on a target device are open.

Open ports usually indicate that a service is running and accepting connections.

Examples:

| Port | Service |
| ---- | ------- |
| 22   | SSH     |
| 53   | DNS     |
| 80   | HTTP    |
| 443  | HTTPS   |

---

## What is a Port?

A port is a logical communication endpoint used by applications.

Example:

IP Address:
192.168.1.10

Services:

* SSH → Port 22
* HTTP → Port 80
* HTTPS → Port 443

The IP identifies the device.

The port identifies the service.

---

## What is Port Scanning?

Port scanning is the process of checking ports to determine whether they are:

* Open
* Closed
* Filtered

Purpose:

* Network troubleshooting
* Service discovery
* Security auditing

---

## TCP Connection Scanning

This project uses TCP Connect Scanning.

Process:

1. Attempt connection to a port.
2. If connection succeeds → Open.
3. If connection fails → Closed.

---

## Python Socket Module

The socket module enables network communication.

Import:

```python
import socket
```

Create Socket:

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Where:

* AF_INET = IPv4
* SOCK_STREAM = TCP

---

## connect_ex()

Used to test connections.

Example:

```python
result = sock.connect_ex((target, port))
```

Return Values:

* 0 = Open
* Non-zero = Closed

---

## Timeout

Timeout prevents the scanner from waiting too long.

Example:

```python
sock.settimeout(0.5)
```

Meaning:

Wait 0.5 seconds before giving up.

---

## Workflow

1. User enters target host.
2. Program loops through ports.
3. Attempts TCP connection.
4. Displays open ports.
5. Ends scan.

---

## Networking Concepts Used

* IPv4 Addressing
* TCP Protocol
* Ports & Services
* Socket Programming
* Network Troubleshooting

---

## Advantages

* Simple
* Fast to understand
* Practical networking application
* Beginner-friendly cybersecurity project

---

## Limitations

* Slow for large scans
* No service detection
* No multithreading
* Only basic TCP scanning

---

## Key Takeaways

* Ports identify services.
* Open ports indicate active services.
* TCP connections can be used to test ports.
* Python sockets provide networking functionality.
* Port scanning is a fundamental networking skill.

# Day 14 - Networking Commands (Linux)

# What is Networking?

Networking allows computers to communicate with each other.

Linux networking commands help us:

- Check internet connection
- Find IP addresses
- Test servers
- Diagnose network issues

---

# Important Networking Commands

## ping

Tests connectivity to another server.

Example:

ping google.com

Stops with:

CTRL + C

---

## ip a

Shows IP addresses and network interfaces.

Example:

ip a

---

## hostname

Shows system hostname.

Example:

hostname

---

## hostname -I

Shows local IP address.

Example:

hostname -I

---

## ifconfig

Old networking command.

Example:

ifconfig

Install if missing:

sudo apt install net-tools

---

## curl

Fetches data from websites/APIs.

Example:

curl ifconfig.me

Shows public IP.

---

## wget

Downloads files from internet.

Example:

wget https://example.com/file.zip

---

## netstat

Shows network connections.

Example:

netstat -tulnp

Install if missing:

sudo apt install net-tools

---

# Understanding netstat Flags

-t → TCP
-u → UDP
-l → Listening ports
-n → Numerical output
-p → Process info

---

## ss

Modern replacement for netstat.

Example:

ss -tuln

---

## traceroute

Shows path packets travel.

Example:

traceroute google.com

Install if missing:

sudo apt install traceroute

---

## nslookup

Finds DNS information.

Example:

nslookup google.com

---

# Important Concepts

## IP Address

Unique address of a device.

Example:

192.168.1.5

---

## Public IP

Internet-facing address.

---

## Private IP

Internal local network address.

---

## DNS

Converts domain names into IP addresses.

Example:

google.com → IP address

---

## Port

Communication endpoint.

Examples:

80 → HTTP
443 → HTTPS
22 → SSH

---

# Beginner Cybersecurity Connection

Networking commands are heavily used in:

- DevOps
- Cloud Engineering
- System Administration
- Cybersecurity
- Server Troubleshooting

---

# Real World Usage

- Check if server is online
- Diagnose internet issues
- Verify DNS
- Check listening ports
- Troubleshoot websites

Linux networking feels like detective work with terminal coffee ☕
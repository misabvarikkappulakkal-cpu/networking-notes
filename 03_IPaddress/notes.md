# Day 3 - IP Addressing (IPv4)

## What is an IP Address?

IP Address stands for Internet Protocol Address.

It is a unique address assigned to a device in a network.

Example:
```txt
192.168.1.1
```

An IP address helps devices identify and communicate with each other.

Without IP addresses, computers would be like houses without addresses.

---

# IPv4 Basics

IPv4 stands for Internet Protocol Version 4.

It uses:
- 32 bits
- Divided into 4 octets
- Each octet ranges from 0 to 255

Example:
```txt
192.168.1.1
```

Structure:
```txt
192 | 168 | 1 | 1
```

Each section is called an octet.

---

# Binary Representation

Computers understand binary numbers.

Example:
```txt
192.168.1.1
```

Binary:
```txt
11000000.10101000.00000001.00000001
```

Each octet contains 8 bits.

Total:
```txt
8 x 4 = 32 bits
```

---

# Types of IP Addresses

## 1. Public IP Address

- Assigned by ISP
- Used on the internet
- Unique globally

Example:
```txt
49.x.x.x
```

---

## 2. Private IP Address

Used inside local networks.

Common private ranges:

| Class | Range |
|------|------|
| A | 10.0.0.0 - 10.255.255.255 |
| B | 172.16.0.0 - 172.31.255.255 |
| C | 192.168.0.0 - 192.168.255.255 |

Example:
```txt
192.168.1.5
```

Routers usually assign private IP addresses to devices.

---

# Special IP Addresses

## Localhost

```txt
127.0.0.1
```

Used for testing your own computer.

The computer talks to itself.

---

## Broadcast Address

Used to send data to all devices in a network.

Example:
```txt
192.168.1.255
```

---

# IP Address Classes

| Class | First Octet Range | Usage |
|------|------|------|
| A | 1 - 126 | Large networks |
| B | 128 - 191 | Medium networks |
| C | 192 - 223 | Small networks |

Class C is common in homes and small offices.

---

# Subnet Mask

A subnet mask separates:
- Network portion
- Host portion

Example:
```txt
255.255.255.0
```

Usually written as:
```txt
/24
```

Meaning:
- First 24 bits = network
- Remaining bits = hosts

---

# Gateway

A gateway is the router that connects your local network to other networks.

Example:
```txt
192.168.1.1
```

Devices send internet traffic through the gateway.

---

# Important Networking Commands

## Linux

Check IP address:
```bash
ip a
```

Show only IP:
```bash
hostname -I
```

Test connection:
```bash
ping google.com
```

---

## Windows

Check IP:
```cmd
ipconfig
```

Test connection:
```cmd
ping google.com
```

---

# DNS (Domain Name System)

DNS converts domain names into IP addresses.

Example:
```txt
google.com -> 142.250.x.x
```

Humans remember names.
Computers use IP addresses.

---

# Important Terms

| Term | Meaning |
|------|------|
| IP Address | Unique device address |
| IPv4 | 32-bit addressing system |
| Octet | 8-bit section |
| Public IP | Internet-facing IP |
| Private IP | Local network IP |
| Gateway | Router address |
| DNS | Converts names to IPs |
| Subnet Mask | Separates network and host |

---

# Real Life Example

Suppose:
- Your laptop IP = 192.168.1.5
- Router IP = 192.168.1.1

When you open YouTube:
1. Laptop sends request to router
2. Router forwards request to internet
3. Internet sends data back
4. Router delivers it to your laptop

IP addresses make sure data reaches the correct device.

---

# Conclusion

IPv4 is the foundation of modern networking.

Every device connected to a network requires an IP address for communication.
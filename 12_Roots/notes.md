# Day 12 - Routing Basics

# What is Routing?

Routing is the process of forwarding data packets from one network to another.

Routers decide the best path for data travel.

---

# What is a Router?

A router connects different networks together.

Example:
- Home network → Internet
- College network → Cloud servers

---

# How Routing Works

1. Packet arrives
2. Router checks destination IP
3. Router checks routing table
4. Router forwards packet to next network

---

# Routing Table

A routing table stores paths to networks.

Example:

| Destination | Gateway |
|-------------|----------|
| 192.168.1.0 | Local |
| 0.0.0.0     | ISP Router |

---

# Types of Routing

## Static Routing

Routes are manually configured.

Advantages:
- Simple
- Secure

Disadvantages:
- Not scalable

---

## Dynamic Routing

Routers automatically learn routes.

Protocols:
- RIP
- OSPF
- BGP

Advantages:
- Automatic updates
- Scalable

Disadvantages:
- More complex

---

# Default Gateway

The router used when destination network is unknown.

Usually:
```bash
192.168.1.1
```

---

# Common Routing Protocols

## RIP
- Simple
- Small networks

## OSPF
- Faster
- Large enterprise networks

## BGP
- Used on the Internet
- Connects ISPs

---

# Important Commands

## Show Routing Table

Linux:
```bash
ip route
```

Windows:
```powershell
route print
```

---

# Traceroute

Shows path packets take.

Linux:
```bash
traceroute google.com
```

Windows:
```powershell
tracert google.com
```

---

# Real World Example

When opening YouTube:
- Your router forwards request
- ISP routers forward traffic
- Data travels through many routers
- Reaches Google servers

Routing is the traffic management system of the internet.
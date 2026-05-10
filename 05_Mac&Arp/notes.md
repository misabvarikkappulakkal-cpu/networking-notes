# Day 5 - MAC Address & ARP Notes

# 1. What is a MAC Address?

MAC stands for:
Media Access Control

A MAC address is a unique physical address assigned to a network device.

Examples:
- Laptop
- Phone
- Router
- Network Card

It works at:
Layer 2 (Data Link Layer) of the OSI Model.


## MAC Address Format

Example:

00:1A:2B:3C:4D:5E

- 48 bits
- Written in hexadecimal
- Separated using colons or hyphens


# 2. IP Address vs MAC Address

IP Address:
- Logical address
- Can change
- Used for communication across networks

MAC Address:
- Physical hardware address
- Usually fixed
- Used inside local networks


## Simple Analogy

IP Address:
House address 🏠

MAC Address:
Person inside the house 👤


# 3. What is ARP?

ARP stands for:
Address Resolution Protocol

ARP is used to find the MAC address of a device using its IP address.


# 4. How ARP Works

Suppose:

PC1 wants to send data to:
192.168.1.5

But PC1 only knows the IP address.

Steps:

1. PC1 sends ARP Request:
"Who has 192.168.1.5?"

2. All devices receive the request.

3. Correct device replies:
"I am 192.168.1.5, my MAC is AA:BB:CC:DD:EE:FF"

4. PC1 stores this in ARP Cache.


# 5. ARP Cache

ARP cache stores:
IP address ↔ MAC address mappings

This helps devices avoid sending ARP requests repeatedly.


# 6. Important Commands

## Windows

arp -a

Shows ARP table.


ipconfig

Shows IP configuration.


getmac

Shows MAC address.


## Linux

arp -a

ip addr

ifconfig


# 7. Broadcast in ARP

ARP requests are broadcasted.

Meaning:
Every device in the local network receives it.


# 8. Key Points

- MAC works at Layer 2
- IP works at Layer 3
- ARP connects IP addresses to MAC addresses
- ARP works only in local networks


# Real World Importance

ARP is used constantly in:
- home WiFi
- offices
- servers
- cloud networking
- data centers

Without ARP, local communication would become digital hide-and-seek with no referee 📡
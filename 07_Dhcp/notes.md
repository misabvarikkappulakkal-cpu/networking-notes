# Day 7: DHCP Notes

---

## What is DHCP?

DHCP stands for:
Dynamic Host Configuration Protocol

It automatically assigns:
- IP Address
- Subnet Mask
- Default Gateway
- DNS Server

to devices in a network.

---

## Why DHCP is Important

Without DHCP:
- IP addresses must be assigned manually
- Higher chance of IP conflicts
- Difficult network management

With DHCP:
- Automatic configuration
- Faster connectivity
- Easier administration

---

## DHCP Process (DORA)

### 1. Discover
Client searches for DHCP server.

### 2. Offer
Server offers an IP address.

### 3. Request
Client requests the offered IP.

### 4. Acknowledge
Server confirms and assigns IP.

---

## DHCP Port Numbers

- UDP Port 67 → Server
- UDP Port 68 → Client

---

## Lease Time

DHCP gives an IP temporarily.
This duration is called Lease Time.

After expiration:
- Device renews IP
- Or receives a new IP

---

## Advantages

- Reduces manual work
- Prevents IP conflicts
- Centralized management
- Easy scalability

---

## Disadvantages

- DHCP server failure affects network
- Rogue DHCP servers can cause issues

---

## What I Learned

- DHCP automates IP assignment
- DORA process is the heart of DHCP
- DHCP uses UDP ports 67 and 68
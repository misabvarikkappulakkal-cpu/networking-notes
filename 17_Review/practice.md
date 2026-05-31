# Networking Practice Questions

## Level 1: Fundamentals

### Networking Basics

1. What is a computer network?
2. Why are networks important?
3. Name three devices commonly used in networking.
4. What is the difference between a client and a server?
5. What is the Internet?

---

### Types of Networks

1. What does LAN stand for?
2. What does WAN stand for?
3. Which network type is used inside homes and offices?
4. Give one example of a MAN.
5. Which network type covers the largest geographical area?

---

### IPv4 Addressing

1. What is an IP address?
2. How many bits are present in IPv4?
3. How many octets are in an IPv4 address?
4. What is the difference between public and private IP addresses?
5. Name the three private IPv4 ranges.

---

### Subnetting

1. What is subnetting?
2. Why is subnetting used?
3. What does /24 represent?
4. How many usable hosts are available in a /24 network?
5. What is a subnet mask?

---

### MAC Address & ARP

1. What is a MAC address?
2. Is a MAC address physical or logical?
3. What is the purpose of ARP?
4. What information does ARP resolve?
5. Why is ARP needed before communication on a LAN?

---

### DNS

1. What does DNS stand for?
2. What problem does DNS solve?
3. What happens when you type google.com in a browser?
4. Name two public DNS servers.
5. What would happen if DNS stopped working?

---

### DHCP

1. What does DHCP stand for?
2. Why is DHCP useful?
3. Name four settings provided by DHCP.
4. What problem does DHCP prevent?
5. Can a device work without DHCP?

---

## Level 2: Intermediate Concepts

### OSI Model

1. How many layers are in the OSI model?
2. Which layer handles routing?
3. Which layer handles applications?
4. Which layer handles physical transmission?
5. List all seven layers in order.

---

### TCP/IP Model

1. How many layers are in the TCP/IP model?
2. Which OSI layers correspond to the Application layer in TCP/IP?
3. Which layer handles routing?
4. What is the main purpose of the Transport layer?
5. Compare OSI and TCP/IP models.

---

### Protocols

1. What protocol is used for web browsing?
2. What is the secure version of HTTP?
3. Which protocol is used for secure remote login?
4. Which protocol is commonly used for file transfer?
5. Why is HTTPS preferred over HTTP?

---

### Ports & Services

1. What is a port?
2. Which port is used by SSH?
3. Which port is used by DNS?
4. Which port is used by HTTPS?
5. Why are ports needed?

---

### Routing

1. What is routing?
2. What device performs routing?
3. What is a routing table?
4. What is a default gateway?
5. What happens when a packet leaves the local network?

---

### Firewalls & Security

1. What is a firewall?
2. Why are firewalls important?
3. What is the difference between hardware and software firewalls?
4. Why should unused services be disabled?
5. Why is SSH safer than Telnet?

---

## Level 3: Linux Networking Commands

### Identify Purpose

What does each command do?

```bash
ip addr
```

```bash
ip route
```

```bash
ping 8.8.8.8
```

```bash
nslookup google.com
```

```bash
dig google.com
```

```bash
ss -tuln
```

```bash
ip link
```

---

### Practical Tasks

#### Task 1

Find:

* Your IP Address
* Network Interface Name
* Subnet Information

Command:

```bash
ip addr
```

---

#### Task 2

Find:

* Default Gateway
* Routing Table Entries

Command:

```bash
ip route
```

---

#### Task 3

Test connectivity to:

```bash
ping localhost
```

```bash
ping 8.8.8.8
```

```bash
ping google.com
```

Explain the result of each test.

---

#### Task 4

Perform DNS lookup:

```bash
nslookup google.com
```

Record:

* DNS Server
* Returned IP Addresses

---

#### Task 5

List open ports:

```bash
ss -tuln
```

Identify:

* Protocol
* Port Number
* Listening Services

---

## Scenario-Based Questions

### Scenario 1

You can ping 8.8.8.8 but cannot ping google.com.

Question:

What is the most likely problem?

---

### Scenario 2

You have an IP address but cannot access the Internet.

Possible causes?

---

### Scenario 3

Your system cannot obtain an IP address automatically.

Which service should you investigate first?

---

### Scenario 4

SSH connection to a server fails.

List at least four troubleshooting steps.

---

### Scenario 5

Two computers are connected to the same switch but cannot communicate.

List possible causes.

---

## Mini Project Review

1. What networking concepts were used in the project?
2. Which Linux commands were used?
3. What troubleshooting techniques were applied?
4. What challenges were encountered?
5. What improvements can be made?

---

# Self-Assessment Checklist

Tick each item when confident.

* [ ] I understand networking fundamentals.
* [ ] I can identify LAN, WAN, MAN and PAN.
* [ ] I understand IPv4 addressing.
* [ ] I can perform basic subnet calculations.
* [ ] I understand MAC addresses and ARP.
* [ ] I understand DNS resolution.
* [ ] I understand DHCP.
* [ ] I can explain the OSI Model.
* [ ] I can explain the TCP/IP Model.
* [ ] I know common networking protocols.
* [ ] I know common port numbers.
* [ ] I understand routing basics.
* [ ] I understand firewall fundamentals.
* [ ] I can use Linux networking commands.
* [ ] I can troubleshoot common networking issues.

## Goal

Score yourself:

* 90%+ → Ready for Intermediate Networking
* 75%-89% → Strong Foundation
* 60%-74% → Review Weak Areas
* Below 60% → Revisit Notes and Labs

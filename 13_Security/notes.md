# Day 13 - Firewalls & Security Basics

# What is a Firewall?

A firewall is a security system that monitors and controls incoming and outgoing network traffic.

Think of it like a security guard standing at the gate of your network 🛡️

It:
- Allows safe traffic
- Blocks dangerous traffic

---

# Types of Firewalls

## 1. Hardware Firewall
Physical device between internet and network.

Examples:
- Router firewall
- Enterprise firewall appliances

---

## 2. Software Firewall
Installed on operating system.

Examples:
- UFW (Linux)
- Windows Defender Firewall

---

# Why Firewalls Matter

Without firewall:
- Hackers can access ports
- Malware can spread
- Unauthorized access becomes easier

Firewalls reduce attack surface.

---

# What is UFW?

UFW = Uncomplicated Firewall

Popular firewall tool in Ubuntu/Debian Linux.

Easy beginner-friendly firewall management.

---

# Important UFW Commands

Install:

```bash
sudo apt install ufw
```

Enable firewall:

```bash
sudo ufw enable
```

Check status:

```bash
sudo ufw status
```

Disable firewall:

```bash
sudo ufw disable
```

---

# Allow and Block Ports

Allow SSH:

```bash
sudo ufw allow 22
```

Allow HTTP:

```bash
sudo ufw allow 80
```

Allow HTTPS:

```bash
sudo ufw allow 443
```

Block port:

```bash
sudo ufw deny 21
```

Delete rule:

```bash
sudo ufw delete allow 22
```

---

# What is a Port?

A port is a communication endpoint used by applications.

Examples:

| Port | Service |
|---|---|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 21 | FTP |
| 53 | DNS |

---

# Incoming vs Outgoing Traffic

## Incoming
Traffic entering your system.

Example:
- Someone connecting to your SSH server

## Outgoing
Traffic leaving your system.

Example:
- Opening a website

---

# Network Security Basics

## 1. Strong Passwords
Avoid weak passwords.

## 2. Updates
Keep software updated.

## 3. Firewall Rules
Allow only necessary ports.

## 4. Antivirus
Detect malware.

## 5. Least Privilege
Give minimum permissions needed.

---

# Common Security Threats

| Threat | Meaning |
|---|---|
| Malware | Harmful software |
| Phishing | Fake websites/messages |
| Brute Force | Repeated password attempts |
| DDoS | Traffic flooding attack |
| Spyware | Secret monitoring software |

---

# Linux Security Commands

Check open ports:

```bash
ss -tuln
```

Check listening services:

```bash
sudo lsof -i
```

Check logged-in users:

```bash
who
```

System updates:

```bash
sudo apt update && sudo apt upgrade
```

---

# Basic SSH Security

Disable root login.
Use strong passwords or SSH keys.
Change default configurations carefully.

---

# What is Encryption?

Encryption converts readable data into unreadable form.

Used in:
- HTTPS
- VPN
- Password storage

---

# Networking Security in Real Life

Cloud engineers secure:
- Servers
- Databases
- APIs
- Networks
- User access

Security is not one big wall.
It's layers of shields stacked like a fortress 🏰

---

# Best Practices

- Never open unnecessary ports
- Keep backups
- Monitor logs
- Use MFA where possible
- Avoid downloading suspicious files
- Use secure WiFi

---

# Mini Project Ideas

- Simple firewall setup
- Port scanner detection notes
- SSH hardening checklist
- Security monitoring script
- Failed login checker
# Day 11 - Ports and Services in Networking

## What is a Port?

A port is a communication endpoint used by applications and services in networking.

Ports allow multiple services to run on the same device using the same IP address.

Example:
- SSH uses port 22
- HTTP uses port 80
- HTTPS uses port 443

---

## What is a Service?

A service is a background application that performs specific tasks.

Examples:
- Web servers
- SSH servers
- DNS servers
- Database servers

Ports help services communicate over a network.

---

## Common Ports

| Port | Protocol | Service |
|------|------|------|
| 20/21 | TCP | FTP |
| 22 | TCP | SSH |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |

---

## Types of Ports

### Well-Known Ports
- Range: 0 - 1023
- Reserved for common services

### Registered Ports
- Range: 1024 - 49151
- Used by applications

### Dynamic/Private Ports
- Range: 49152 - 65535
- Temporary communication ports

---

## Important Commands

### Check Listening Ports

```bash
ss -tuln
```

---

### Alternative Command

```bash
netstat -tuln
```

---

### Check Process Using Port

```bash
sudo lsof -i :80
```

---

### Check SSH Port

```bash
sudo lsof -i :22
```

---

### Test Local Web Server

```text
http://localhost
```

---

## Command Explanation

### ss
- Shows socket statistics
- Modern replacement for netstat

### lsof
- Lists open files
- Can show which process is using a port

---

## Real World Usage

Ports and services are important for:
- Web hosting
- Remote server management
- Cloud computing
- API communication
- Cybersecurity
- DevOps engineering

---

## Key Concepts Learned

- Ports identify services
- Services listen on ports
- Multiple services can run on one machine
- Port scanning helps identify running services
- Linux tools help monitor network activity
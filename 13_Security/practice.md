## 1. Install UFW

```bash
sudo apt install ufw
```

Check version:

```bash
ufw version
```

---

## 2. Enable Firewall

```bash
sudo ufw enable
```

Check status:

```bash
sudo ufw status verbose
```

---

## 3. Allow Important Ports

Allow:
- SSH
- HTTP
- HTTPS

Commands:

```bash
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
```

---

## 4. Deny a Port

```bash
sudo ufw deny 21
```

Explain why FTP can be risky.

---

## 5. Delete Firewall Rule

```bash
sudo ufw delete allow 22
```

---

# Intermediate Practice

## 6. Check Open Ports

```bash
ss -tuln
```

Identify:
- Port number
- Protocol

---

## 7. View Active Network Connections

```bash
sudo lsof -i
```

---

## 8. Check Logged-in Users

```bash
who
```

---

## 9. Update System Packages

```bash
sudo apt update && sudo apt upgrade
```

Why are updates important for security?

---

# Challenge Tasks 🚀

## 10. Build Your Own Firewall Rules

Create rules for:
- Web server
- SSH server
- Blocking unwanted ports

---

## 11. Security Audit Notes

Write:
- Open ports
- Active services
- Firewall rules
- Security risks found

---

## 12. Research Task

Research:
- VPN
- HTTPS
- SSH
- Encryption

Write short notes.

---

# Self Check Questions

1. What does a firewall do?
2. Difference between hardware and software firewall?
3. What is UFW?
4. What does port 443 do?
5. Why block unused ports?
6. What is encryption?
7. What is brute force attack?
8. Why are updates important?
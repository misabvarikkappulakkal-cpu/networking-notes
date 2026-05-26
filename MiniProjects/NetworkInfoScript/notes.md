# Network Info Script - Notes

# 🎯 Goal

Create a Bash script that automatically displays useful networking information.

Instead of manually typing many commands,
the script gathers everything together.

This is basic network automation.

---

# 🧠 Concepts Used

| Concept | Purpose |
|---|---|
| Bash Script | Automate commands |
| Networking Commands | Collect network info |
| Variables | Store values later |
| Command Output | Display system/network details |

---

# 📦 Important Commands

## hostname

Shows computer hostname.

```bash
hostname
```

---

## hostname -I

Displays local IP address.

```bash
hostname -I
```

---

## ping

Checks internet connectivity.

```bash
ping google.com
```

In script:

```bash
ping -c 2 google.com
```

`-c 2` sends only 2 packets.

---

## ip route

Displays routing table.

```bash
ip route
```

Shows:
- Gateway
- Routes
- Network paths

---

## /etc/resolv.conf

Contains DNS server information.

```bash
cat /etc/resolv.conf
```

---

## ip a

Shows:
- Network interfaces
- IP addresses
- Connection details

```bash
ip a
```

---

# 🌍 Why This Project Matters

This project teaches:
- Network troubleshooting
- System diagnostics
- Automation
- Script building

These skills are useful in:
- Cloud Engineering
- DevOps
- Cybersecurity
- Linux Administration

---

# 🚀 Future Improvements

You can later add:
- Public IP lookup
- Port scanner
- Internet speed test
- WiFi signal strength
- Device discovery
- Logging

Each improvement introduces new networking concepts.

---

# ⚠️ Real-World Use

System admins often use scripts like this to:
- Diagnose network issues
- Monitor servers
- Check connectivity
- Collect troubleshooting info

Automation saves time during emergencies.


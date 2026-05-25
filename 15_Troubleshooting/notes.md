# Day 15 – Troubleshooting Basics

## 🎯 Goal
Learn how to diagnose common networking problems.

Real engineers are not paid because systems never fail.

They are paid because they know how to find the problem calmly.

---

# 🧠 Troubleshooting Mindset

Never panic.

Networking problems usually come from:
- Wrong IP
- DNS issues
- Gateway problems
- Firewall blocks
- No internet connection
- Service downtime

Solve problems step by step.

---

# 🔍 Important Troubleshooting Commands

| Command | Purpose |
|---|---|
| ping | Check connectivity |
| ip a | Show IP address |
| ifconfig | Network interface info |
| traceroute | Track route to destination |
| nslookup | Check DNS |
| netstat | Show connections |
| curl | Test websites/APIs |

---

# 📡 ping

Checks whether another device/server is reachable.

```bash
ping google.com
```

Useful for:
- Internet testing
- Server availability
- DNS checking

Stop using:
```bash
CTRL + C
```

---

# 🌍 ip a

Shows:
- IP address
- Network interfaces
- Connection details

```bash
ip a
```

---

# 🧭 traceroute

Shows the path packets travel.

```bash
traceroute google.com
```

Useful for:
- Slow networks
- Routing issues
- ISP problems

Install if missing:

```bash
sudo apt install traceroute
```

---

# 🔎 nslookup

Checks DNS resolution.

```bash
nslookup google.com
```

If DNS fails:
- Websites may not open
- But pinging IP addresses may still work

Install if missing:

```bash
sudo apt install dnsutils
```

---

# 📊 netstat

Shows:
- Open ports
- Active connections
- Listening services

```bash
netstat -tulnp
```

Install if missing:

```bash
sudo apt install net-tools
```

---

# 🌐 curl

Tests websites and APIs.

```bash
curl https://example.com
```

Useful for:
- API testing
- Website response checking
- Debugging servers

---

# 🛠️ Common Troubleshooting Flow

## Problem:
No internet connection.

## Step-by-step:
1. Check WiFi/cable
2. Run:
   ```bash
   ip a
   ```
3. Ping router
4. Ping Google DNS:
   ```bash
   ping 8.8.8.8
   ```
5. Test DNS:
   ```bash
   nslookup google.com
   ```
6. Test website:
   ```bash
   curl https://google.com
   ```

---

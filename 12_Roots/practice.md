# 1. View IP Address

Linux:
```bash
ip a
```

Windows:
```powershell
ipconfig
```

---

# 2. View Routing Table

Linux:
```bash
ip route
```

Windows:
```powershell
route print
```

Observe:
- Default gateway
- Local routes

---

# 3. Ping Test

```bash
ping google.com
```

Purpose:
- Check connectivity
- Test network reachability

---

# 4. Traceroute

Linux:
```bash
traceroute google.com
```

Windows:
```powershell
tracert google.com
```

Observe:
- Number of hops
- Routers between you and destination

---

# 5. Find Default Gateway

Linux:
```bash
ip route | grep default
```

Windows:
```powershell
ipconfig
```

---

# 6. Understand Packet Travel

Example flow:

Your Laptop
↓
Home Router
↓
ISP Router
↓
Internet Backbone
↓
Google Server

---

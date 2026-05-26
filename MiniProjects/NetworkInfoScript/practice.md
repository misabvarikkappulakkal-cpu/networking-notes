# Network Info Script - Practice

# 🧪 Practice Commands

---

# 1️⃣ Check Hostname

```bash
hostname
```

---

# 2️⃣ Check IP Address

```bash
hostname -I
```

Also try:

```bash
ip a
```

---

# 3️⃣ Test Internet Connectivity

```bash
ping google.com
```

Stop with:

```bash
CTRL + C
```

---

# 4️⃣ Send Limited Ping Requests

```bash
ping -c 3 google.com
```

---

# 5️⃣ View Routing Table

```bash
ip route
```

Observe:
- Default gateway
- Network routes

---

# 6️⃣ Check DNS Servers

```bash
cat /etc/resolv.conf
```

---

# 7️⃣ Create Small Test Script

```bash
nano test_network.sh
```

Paste:

```bash
#!/bin/bash

echo "Testing Network"

hostname -I
```

Run:

```bash
chmod +x test_network.sh

./test_network.sh
```

---

# 8️⃣ Mini Challenge

Create script that shows:
- Hostname
- IP address
- Internet test
- DNS info

WITHOUT copying previous script fully.

---

# 🎯 Bonus Challenge

Upgrade script to:
- Show public IP
- Save output to file
- Add timestamps
- Check multiple websites

Research:
```bash
curl
```

---

# 🧠 Self Check

Can you:
- Use networking commands?
- Read IP information?
- Understand DNS basics?
- Build network scripts?
- Test internet connectivity?


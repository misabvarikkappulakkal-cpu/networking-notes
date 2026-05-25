# 1️⃣ Test Internet Connection

```bash
ping google.com
```

Stop with:
```bash
CTRL + C
```

---

# 2️⃣ Check IP Address

```bash
ip a
```

Also try:

```bash
ifconfig
```

---

# 3️⃣ Test DNS Resolution

```bash
nslookup google.com
```

Try:
- youtube.com
- github.com

---

# 4️⃣ Track Packet Route

```bash
traceroute google.com
```

If missing:

```bash
sudo apt install traceroute
```

---

# 5️⃣ View Active Connections

```bash
netstat -tulnp
```

If missing:

```bash
sudo apt install net-tools
```

---

# 6️⃣ Test Website Response

```bash
curl https://example.com
```

Also try:

```bash
curl https://github.com
```

---

# 7️⃣ DNS Failure Experiment

Try pinging:
```bash
ping 8.8.8.8
```

Then:
```bash
ping google.com
```

Observe:
- If IP works but domain fails → DNS issue

---

# 8️⃣ Troubleshooting Scenario Practice

## Scenario:
Website not opening.

## Try:
```bash
ip a

ping 8.8.8.8

nslookup google.com

curl https://google.com
```

Think:
- Internet issue?
- DNS issue?
- Website issue?

---

# 🎯 Mini Challenge

Create a troubleshooting checklist file.

```bash
nano checklist.txt
```

Write:
- Check internet
- Check IP
- Ping DNS
- Test DNS
- Test website
- Check routes

Save and view using:
```bash
cat checklist.txt
```

---

# 🧠 Self Check

Can you:
- Test connectivity?
- Check IP address?
- Identify DNS problems?
- Inspect connections?
- Debug basic networking issues?

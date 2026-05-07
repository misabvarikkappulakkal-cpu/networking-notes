# 1. Check IP Address

## Linux
```bash
ip a
```

## Windows
```cmd
ipconfig
```

Observe:
- IPv4 Address
- Subnet Mask
- Gateway

---

# 2. Show Only IP Address

```bash
hostname -I
```

---

# 3. Ping Test

```bash
ping google.com
```

Observe:
- packets sent
- packets received
- response time

---

# 4. Test Localhost

```bash
ping 127.0.0.1
```

This checks whether your own network stack is working.

---

# 5. Find Default Gateway

## Linux
```bash
ip route
```

## Windows
```cmd
ipconfig
```

---

# 6. Practice Questions

## Q1:
How many bits are present in IPv4?

Answer:
32 bits

---

## Q2:
What is the localhost IP?

Answer:
127.0.0.1

---

## Q3:
Which IP range is private?

Answer:
192.168.x.x

---

## Q4:
What does DNS do?

Answer:
Converts domain names into IP addresses.

---

# 7. Identify Public or Private

| IP Address | Type |
|------|------|
| 192.168.1.5 | Private |
| 8.8.8.8 | Public |
| 10.0.0.1 | Private |
| 172.20.5.1 | Private |

---

# 8. Mini Task

Find:
- Your IP address
- Your gateway
- Your subnet mask

Write them below:

IP Address:
__________

Gateway:
__________

Subnet Mask:
__________
## Output

===== IP ADDRESS FINDER =====
Hostname   : misabvp
IP Address : 172.xx.xx.x

## 🧠 Concepts Learned

### 1. Socket Module

The `socket` module allows Python programs to interact with networking services and obtain network-related information.

```python
import socket
```

---

### 2. Getting the Hostname

Every device on a network has a hostname.

```python
hostname = socket.gethostname()
```

Example:

```text
DESKTOP-ABC123
```

---

### 3. Getting the IP Address

The hostname can be converted into an IP address.

```python
ip_address = socket.gethostbyname(hostname)
```

Example:

```text
192.xxx.x.x
```

---

## 📖 Key Networking Terms

### IP Address

A unique numerical address assigned to a device on a network.

Example:

```text
192.xxx.x.x
```

---

### Hostname

A human-readable name assigned to a device.

Example:

```text
LAPTOP-MISAB
```

---

### Local IP Address

The IP address assigned by the local network router.

Used for communication between devices within the same network.

---

## 📝 Program Flow

1. Import the socket module.
2. Get the system hostname.
3. Convert the hostname into an IP address.
4. Display the information.

---

## 💡 Sample Output

```text
===== IP ADDRESS FINDER =====

Hostname   : LAPTOP-MISAB
IP Address : 192.xxx.x.x
```

---

## 🚀 Skills Practiced

* Python Networking
* Socket Programming
* Functions
* Error Handling
* Network Fundamentals

---

## 🎯 Learning Outcome

After completing this project, I can:

* Retrieve network information using Python
* Understand hostnames and IP addresses
* Use the socket module
* Build basic networking tools

---

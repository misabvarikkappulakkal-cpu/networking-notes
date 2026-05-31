# Port Scanner (Basic) - Practice Questions

## Theory Questions

### Basics

1. What is a port?

2. Why are ports used?

3. What is port scanning?

4. What is an open port?

5. What is a closed port?

---

### Networking Concepts

1. Which protocol is used in this scanner?

2. What is the purpose of TCP?

3. What service commonly uses port 22?

4. What service commonly uses port 80?

5. What service commonly uses port 443?

---

### Python Concepts

1. Why is the socket module used?

2. What does AF_INET represent?

3. What does SOCK_STREAM represent?

4. What does connect_ex() do?

5. What does a return value of 0 indicate?

---

## Code Understanding

### Question 1

What is the purpose of:

```python
sock.settimeout(0.5)
```

---

### Question 2

What happens if timeout is removed?

---

### Question 3

Why is sock.close() important?

---

### Question 4

Why is a loop used in the scanner?

---

### Question 5

What would happen if we scanned ports 1-65535?

---

## Output Analysis

Example:

```text
Port 22: OPEN
Port 80: OPEN
Port 443: OPEN
```

Questions:

1. Which services are likely running?

2. Which port is used for SSH?

3. Which port is used for HTTPS?

---

## Practical Exercises

### Task 1

Modify the scanner to scan:

Ports 1-100

---

### Task 2

Modify the scanner to scan:

Ports 1-500

---

### Task 3

Add a counter that displays:

Total Open Ports Found

Example:

```text
Open Ports Found: 3
```

---

### Task 4

Display Closed Ports as well.

Example:

```text
Port 25: CLOSED
```

---

### Task 5

Store results inside a text file.

Example:

```text
scan_results.txt
```

---

## Scenario Questions

### Scenario 1

Port 22 is open.

Question:

Which service is most likely running?

Answer:

SSH

---

### Scenario 2

Port 80 is open.

Question:

What service is likely running?

Answer:

HTTP

---

### Scenario 3

All ports appear closed.

Possible reasons:

* Host is offline
* Firewall blocking traffic
* Wrong IP address
* Service not running

---

### Scenario 4

Scan takes too long.

Question:

What feature could improve performance?

Answer:

Multithreading

---

## Challenge Questions

1. What is the difference between TCP and UDP scanning?

2. Why might a firewall hide open ports?

3. How could you detect the service running on an open port?

4. Why is port scanning useful in network troubleshooting?

5. How can port scanning help improve security?

---

## Self Assessment

* [ ] I understand what a port is.
* [ ] I understand port scanning.
* [ ] I understand TCP connections.
* [ ] I understand socket programming basics.
* [ ] I can explain connect_ex().
* [ ] I can identify common port numbers.
* [ ] I can modify the scanner code.
* [ ] I understand how open ports indicate services.

### Score

7-8 checked → Excellent

5-6 checked → Good

3-4 checked → Needs Review

0-2 checked → Revisit Notes

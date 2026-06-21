## Theory Questions

### Easy

1. What does NAT stand for?
2. Why is NAT used?
3. What is a private IP address?
4. What is a public IP address?
5. Which device usually performs NAT?

---

### Intermediate

6. Explain how NAT works.
7. What is the difference between Static NAT and Dynamic NAT?
8. What is PAT?
9. Why is PAT commonly used?
10. List three advantages of NAT.

---

### Advanced

11. Explain NAT with a real-world example.
12. Why does NAT help conserve IPv4 addresses?
13. What are the disadvantages of NAT?
14. Compare Static NAT, Dynamic NAT, and PAT.
15. How does NAT improve security?

---

## Practical Exercises

### Exercise 1

Identify whether the following IP addresses are Private or Public:

* 192.168.1.10
* 8.8.8.8
* 10.0.0.25
* 172.20.5.1
* 142.250.190.78

---

### Exercise 2

A home router has:

Public IP: 203.0.113.5

Devices:

* Laptop → 192.168.1.2
* Phone → 192.168.1.3
* Tablet → 192.168.1.4

Question:

How can all devices access the internet using only one public IP?

---

### Exercise 3

Match the NAT Type:

| Scenario                           | NAT Type |
| ---------------------------------- | -------- |
| One private IP to one public IP    | ?        |
| Many devices sharing one public IP | ?        |
| Public IP selected from a pool     | ?        |

Answers:

* Static NAT
* Dynamic NAT
* PAT

---

## Challenge Questions

1. Why would a company use Static NAT for a web server?
2. What problems would occur if NAT did not exist?
3. Why is IPv6 reducing the dependency on NAT?
4. Explain PAT using port numbers.
5. Draw a diagram showing NAT between a LAN and the Internet.

---

## Mini Lab

Draw the following network:

Internet
↓
Router (Public IP)
↓
Switch
↓
PC1 (Private IP)
↓
PC2 (Private IP)
↓
PC3 (Private IP)

Label:

* Public IP
* Private IPs
* NAT Translation

Explain the flow of data from PC1 to a website.

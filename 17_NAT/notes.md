# NAT (Network Address Translation)

## What is NAT?

NAT (Network Address Translation) is a networking technique used by routers to translate private IP addresses into public IP addresses and vice versa.

It allows multiple devices in a private network to share a single public IP address when accessing the internet.

---

## Why NAT is Needed

* Conserves public IPv4 addresses
* Improves network security by hiding internal IP addresses
* Allows private networks to access the internet
* Reduces the need for multiple public IP addresses

---

## How NAT Works

1. A device inside the network sends a request to the internet.
2. The router replaces the private IP address with its public IP address.
3. The request reaches the destination server.
4. The server sends the response back to the router.
5. The router forwards the response to the correct internal device.

---

## Types of NAT

### 1. Static NAT

* One private IP ↔ One public IP
* Permanent mapping
* Used for servers

Example:

Private IP: 192.168.1.10

Public IP: 203.0.113.10

---

### 2. Dynamic NAT

* Maps private IPs to a pool of public IPs
* Assignment occurs dynamically
* Less common today

---

### 3. PAT (Port Address Translation)

Also called NAT Overload.

* Many private IPs share one public IP
* Uses port numbers to identify devices
* Most commonly used NAT type

Example:

192.168.1.2:5000 → 203.0.113.5:5000

192.168.1.3:5001 → 203.0.113.5:5001

---

## Private IP Address Ranges

### Class A

10.0.0.0 – 10.255.255.255

### Class B

172.16.0.0 – 172.31.255.255

### Class C

192.168.0.0 – 192.168.255.255

---

## Advantages of NAT

* Saves public IPv4 addresses
* Adds a layer of security
* Easy internet sharing
* Simplifies network management

---

## Disadvantages of NAT

* Can increase processing overhead
* Some applications may face compatibility issues
* Makes end-to-end communication more complex

---

## Real-World Example

Suppose three devices are connected to a home Wi-Fi:

* Laptop → 192.168.1.2
* Phone → 192.168.1.3
* Smart TV → 192.168.1.4

The router has one public IP:

203.0.113.5

Using NAT/PAT, all devices can browse the internet through that single public IP address.

---

## Key Terms

| Term       | Meaning                           |
| ---------- | --------------------------------- |
| Private IP | Internal network address          |
| Public IP  | Internet-routable address         |
| NAT        | Translates private and public IPs |
| PAT        | Uses port numbers for translation |
| Router     | Device performing NAT             |

---

## Summary

NAT enables devices using private IP addresses to communicate with the internet using public IP addresses. It conserves IPv4 addresses, enhances privacy, and is widely used in home and enterprise networks.

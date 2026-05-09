# Day 4 - Subnetting Basics

## What is Subnetting?

Subnetting divides a network into smaller networks.

---

## IPv4 Address

Example:

```text
192.168.1.10
```

IPv4 address contains:
- Network portion
- Host portion

---

## Subnet Mask

Example:

```text
255.255.255.0
```

CIDR notation:

```text
/24
```

---

## Common CIDR Ranges

| CIDR | Subnet Mask       | Usable Hosts |
|------|-------------------|--------------|
| /24  | 255.255.255.0     | 254          |
| /25  | 255.255.255.128   | 126          |
| /26  | 255.255.255.192   | 62           |
| /27  | 255.255.255.224   | 30           |

---

## Network Address

First IP address in subnet.

Example:

```text
192.168.1.0/24
```

Network address:

```text
192.168.1.0
```

---

## Broadcast Address

Last IP address in subnet.

Example:

```text
192.168.1.255
```

---

## Usable Host Range

Example:

```text
192.168.1.1 - 192.168.1.254
```

---

## Formula

Usable hosts:

:contentReference[oaicite:0]{index=0}

---

### Important Concepts Learned

- IPv4
- CIDR
- Subnet mask
- Network address
- Broadcast address
- Usable hosts
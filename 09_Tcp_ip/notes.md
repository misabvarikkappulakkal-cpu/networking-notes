# Day 9 - Common Networking Protocols

Protocols are rules used for communication between devices.

---

## HTTP

HyperText Transfer Protocol

Used for:
- Websites
- APIs
- Web communication

Default Port:
80

Example:
http://example.com

---

## HTTPS

Secure version of HTTP.

Uses encryption (SSL/TLS).

Default Port:
443

Example:
https://example.com

Benefits:
- Secure communication
- Data encryption
- Trusted websites

---

## FTP

File Transfer Protocol

Used for:
- Uploading files
- Downloading files

Default Ports:
20 and 21

Problem:
Not encrypted.

Secure Alternative:
SFTP

---

## SSH

Secure Shell

Used for:
- Remote server login
- Secure command execution

Default Port:
22

Example:
ssh user@server-ip

---

## Protocol Comparison

| Protocol | Port | Secure | Purpose |
|---|---|---|---|
| HTTP | 80 | No | Websites |
| HTTPS | 443 | Yes | Secure websites |
| FTP | 21 | No | File transfer |
| SSH | 22 | Yes | Remote access |

---

## Real World Examples

- GitHub uses HTTPS and SSH
- AWS servers are accessed using SSH
- Browsers use HTTP/HTTPS
- Linux admins use SSH daily
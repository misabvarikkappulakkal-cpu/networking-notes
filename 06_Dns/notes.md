# Day 6 - Domain Name System (DNS) Notes

# DNS (Domain Name System)

DNS converts domain names into IP addresses.

Example:
google.com → 142.250.x.x

Humans remember names.
Computers communicate using IP addresses.

DNS acts like the internet's phonebook 📖🌐

## Why DNS is Important

Without DNS:
- We would need to remember IP addresses.
- Websites would be difficult to access.

## DNS Process

1. User enters domain name
2. DNS query is sent
3. DNS server finds matching IP
4. Browser connects to server

## Common DNS Record Types

| Record | Purpose |
|--------|----------|
| A | Maps domain to IPv4 |
| AAAA | Maps domain to IPv6 |
| CNAME | Alias record |
| MX | Mail server record |
| NS | Name server record |

## Important DNS Servers

- Recursive Resolver
- Root Server
- TLD Server
- Authoritative Server

## Common Commands

### Check DNS using ping
ping google.com

### DNS lookup
nslookup google.com

### Detailed DNS info
dig google.com
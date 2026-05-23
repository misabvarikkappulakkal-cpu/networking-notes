## Task 1

Check your hostname.

Command:

hostname

---

## Task 2

Find your local IP address.

Commands:

hostname -I

and

ip a

---

## Task 3

Ping Google.

Command:

ping google.com

Stop after few seconds using:

CTRL + C

---

## Task 4

Find your public IP.

Command:

curl ifconfig.me

---

## Task 5

Check listening ports.

Command:

ss -tuln

---

## Task 6

Install net-tools package.

Command:

sudo apt install net-tools

Then run:

ifconfig

---

## Task 7

Use nslookup.

Command:

nslookup github.com

---

## Task 8

Use traceroute.

Install:

sudo apt install traceroute

Run:

traceroute google.com

---

## Task 9

Download a sample file using wget.

Example:

wget https://speed.hetzner.de/100MB.bin

Cancel anytime with:

CTRL + C

---

## Task 10

Research these ports:

22
80
443
3306

Find what services use them.

---

# Self Check

Can you explain:

- Difference between public IP and private IP?
- What ping does?
- What DNS is?
- What ports are?
- Difference between wget and curl?
- Why ss is replacing netstat?

If yes:
you're starting to think like a cloud engineer 🛰️🐧
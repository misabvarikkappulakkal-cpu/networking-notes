## Step 1 - Check Your IP Address

### Windows

ipconfig

### Linux

ip addr


## Step 2 - Check Your MAC Address

### Windows

getmac

### Linux

ip link


## Step 3 - View ARP Table

### Windows

arp -a

### Linux

arp -a


## Step 4 - Ping Another Device

Example:

ping 192.168.1.1

This creates ARP entries.


## Step 5 - View ARP Table Again

arp -a

Notice:
New IP and MAC mappings may appear.


## Step 6 - Identify Gateway MAC Address

Find:
- Default gateway IP
- Its MAC address from ARP table


## Step 7 - Practice Understanding

Example Data:

IP Address:
192.168.1.10

MAC Address:
00:1A:2B:3C:4D:5E

Questions:
1. Which layer uses MAC?
2. Which protocol maps IP to MAC?
3. Is MAC physical or logical?
4. Does ARP work outside local networks?


## Step 8 - Linux Bonus Practice

Run:

ip neigh

This displays neighbor table information.


## Mini Challenge

1. Find your:
   - IP address
   - MAC address
   - Gateway IP

2. Run:
   arp -a

3. Identify:
   - Router MAC address
   - Another device MAC address

4. Write your findings in a text file:

network_info.txt


## Extra Curiosity Corner 🛰️

Think about this:

Before your laptop opens YouTube or Discord,
it first whispers:

"Who has this IP address?"

ARP is basically devices introducing themselves before talking.
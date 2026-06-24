# VLAN Practice Questions

## Multiple Choice Questions

### 1. What does VLAN stand for?

A. Virtual Local Area Network
B. Variable Local Area Network
C. Virtual Logical Access Network
D. Variable Logical Access Network

**Answer:** A

---

### 2. Which IEEE standard is used for VLAN tagging?

A. 802.3
B. 802.11
C. 802.1Q
D. 802.5

**Answer:** C

---

### 3. What is the default VLAN on most Cisco switches?

A. VLAN 0
B. VLAN 1
C. VLAN 10
D. VLAN 100

**Answer:** B

---

### 4. Which port carries traffic from multiple VLANs?

A. Access Port
B. Console Port
C. Trunk Port
D. AUX Port

**Answer:** C

---

### 5. Devices in different VLANs require what to communicate?

A. Hub
B. Repeater
C. Inter-VLAN Routing
D. Bridge

**Answer:** C

---

## Short Answer Questions

### 1. What is a VLAN?

### 2. Why are VLANs used?

### 3. What is an access port?

### 4. What is a trunk port?

### 5. What is VLAN tagging?

### 6. What is Inter-VLAN Routing?

### 7. What is the purpose of a native VLAN?

### 8. Why should VLAN 1 be avoided for user traffic?

---

## Scenario Questions

### Scenario 1

A company has:

* HR Department
* Finance Department
* IT Department

How would VLANs improve security and management?

---

### Scenario 2

PC-A belongs to VLAN 10.
PC-B belongs to VLAN 20.

Can they communicate directly?
If not, what is required?

---

### Scenario 3

Two switches are connected together.

Should the connecting ports be:

* Access ports?
* Trunk ports?

Explain why.

---

## Cisco CLI Practice

### Task 1

Create VLAN 10 named HR.

```bash
Switch(config)# vlan 10
Switch(config-vlan)# name HR
```

---

### Task 2

Assign FastEthernet 0/1 to VLAN 10.

```bash
Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

---

### Task 3

Configure GigabitEthernet 0/1 as a trunk.

```bash
Switch(config)# interface g0/1
Switch(config-if)# switchport mode trunk
```

---

### Task 4

Display VLAN information.

```bash
Switch# show vlan brief
```

---

### Task 5

Display trunk information.

```bash
Switch# show interfaces trunk
```

---

## Packet Tracer Lab

### Objective

Create three VLANs:

| VLAN ID | Name    |
| ------- | ------- |
| 10      | HR      |
| 20      | Finance |
| 30      | IT      |

### Tasks

1. Create VLANs.
2. Assign PCs to VLANs.
3. Configure trunk links.
4. Verify VLAN membership.
5. Test connectivity.
6. Configure Inter-VLAN Routing.
7. Verify communication between VLANs.

---

## Interview Questions

1. What is the difference between a VLAN and a subnet?
2. What is an access port?
3. What is a trunk port?
4. What is VLAN hopping?
5. What is Router-on-a-Stick?
6. What is a native VLAN?
7. Why are VLANs important?
8. What happens when a broadcast is sent inside a VLAN?
9. What is the purpose of 802.1Q?
10. How do VLANs improve security?

---

## Challenge

Design a network for:

* 50 HR users
* 70 Finance users
* 30 IT users

Requirements:

* Separate departments using VLANs.
* Allow communication between departments.
* Minimize broadcast traffic.
* Improve security.

Draw the topology and explain your VLAN design.

# VLAN (Virtual Local Area Network)

## What is VLAN?

A VLAN (Virtual Local Area Network) is a logical grouping of devices within a network, regardless of their physical location. VLANs allow network administrators to divide a single physical switch into multiple separate broadcast domains.

Think of VLANs as creating multiple virtual switches inside one physical switch.

---

## Why Use VLANs?

### 1. Improved Security

Devices in different VLANs cannot communicate directly without a Layer 3 device (router or Layer 3 switch).

Example:

* HR Department → VLAN 10
* Finance Department → VLAN 20

This prevents unauthorized access between departments.

### 2. Reduced Broadcast Traffic

Broadcasts remain inside their VLAN, reducing unnecessary network traffic.

### 3. Better Network Management

Users can be grouped based on:

* Department
* Function
* Location
* Project

rather than physical connection.

### 4. Scalability

Networks become easier to expand and reorganize.

---

## VLAN Terminology

### Access Port

A switch port assigned to a single VLAN.

Example:

* PC connected to Switch Port Fa0/1
* Port belongs to VLAN 10

The PC is unaware of VLAN tagging.

### Trunk Port

A port that carries traffic from multiple VLANs between networking devices.

Example:

* Switch ↔ Switch
* Switch ↔ Router

Uses VLAN tagging.

---

## VLAN Tagging

Most networks use:

**IEEE 802.1Q (Dot1Q)**

The switch inserts a VLAN ID into Ethernet frames.

Example:

| VLAN    | VLAN ID |
| ------- | ------- |
| HR      | 10      |
| Finance | 20      |
| IT      | 30      |

---

## Default VLAN

By default, all switch ports belong to:

**VLAN 1**

Characteristics:

* Exists by default
* Cannot be deleted on many switches
* Used for management traffic unless changed

Best practice:

* Avoid using VLAN 1 for user devices.

---

## VLAN Types

### Data VLAN

Carries user-generated traffic.

### Voice VLAN

Dedicated for IP phones.

### Management VLAN

Used for switch management (SSH, Telnet, SNMP).

### Native VLAN

Frames on a trunk that are sent untagged.

---

## VLAN Communication

### Same VLAN

Devices communicate directly.

Example:

PC1 (VLAN 10) → PC2 (VLAN 10)

Communication works.

### Different VLANs

Devices require inter-VLAN routing.

Example:

PC1 (VLAN 10) → PC2 (VLAN 20)

Requires:

* Router-on-a-Stick
* Layer 3 Switch

---

## Inter-VLAN Routing

Inter-VLAN Routing allows communication between different VLANs.

Methods:

### Router-on-a-Stick

One router interface configured with multiple subinterfaces.

Example:

Router
├── VLAN 10
├── VLAN 20
└── VLAN 30

### Layer 3 Switch

A switch capable of routing traffic between VLANs.

Advantages:

* Faster
* More scalable
* Common in enterprise networks

---

## Advantages of VLANs

* Better security
* Reduced broadcast domains
* Easier management
* Improved performance
* Greater flexibility
* Supports large networks

---

## Disadvantages of VLANs

* More configuration complexity
* Requires proper planning
* Inter-VLAN communication requires routing
* Troubleshooting can become harder

---

## Example Network

VLAN 10 (HR)

* PC1
* PC2

VLAN 20 (Finance)

* PC3
* PC4

VLAN 30 (IT)

* PC5
* PC6

Switch
│
├── VLAN 10
├── VLAN 20
└── VLAN 30
│
Router / Layer 3 Switch
│
Inter-VLAN Routing

---

## Cisco VLAN Commands

### Create VLAN

```bash
Switch(config)# vlan 10
Switch(config-vlan)# name HR
```

### Assign Port to VLAN

```bash
Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

### Configure Trunk

```bash
Switch(config)# interface g0/1
Switch(config-if)# switchport mode trunk
```

### Show VLANs

```bash
Switch# show vlan brief
```

### Show Trunks

```bash
Switch# show interfaces trunk
```

---

## Quick Summary

* VLAN = Logical network segmentation
* VLANs create separate broadcast domains
* Access ports carry one VLAN
* Trunk ports carry multiple VLANs
* IEEE 802.1Q provides VLAN tagging
* VLAN 1 is the default VLAN
* Different VLANs require routing to communicate
* VLANs improve security, performance, and management

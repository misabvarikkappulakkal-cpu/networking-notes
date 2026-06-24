# Network Traffic Monitor Architecture

## High Level Architecture

┌───────────────┐
│ Network Card  │
└───────┬───────┘
│
▼
┌───────────────┐
│ Packet Capture│
└───────┬───────┘
│
▼
┌───────────────┐
│ Packet Parser │
└───────┬───────┘
│
▼
┌───────────────┐
│ Traffic Logger│
└───────┬───────┘
│
▼
┌───────────────┐
│ Statistics    │
└───────────────┘

---

## Components

### Packet Capture Module

Responsible for collecting packets.

### Parser Module

Extracts:

* Source IP
* Destination IP
* Protocol

### Logger Module

Stores packet information.

### Statistics Module

Calculates traffic metrics.

---

## Data Flow

Packet
↓
Capture
↓
Parse
↓
Classify
↓
Store
↓
Report
 
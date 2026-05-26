#!/bin/bash

echo "=============================="
echo "🖥️  SYSTEM INFORMATION SCRIPT"
echo "=============================="

echo ""

echo "👤 Current User:"
whoami

echo ""

echo "📅 Current Date & Time:"
date

echo ""

echo "💻 Hostname:"
hostname

echo ""

echo "🧠 System Uptime:"
uptime

echo ""

echo "💾 Memory Usage:"
free -h

echo ""

echo "💽 Disk Usage:"
df -h

echo ""

echo "🌐 IP Address:"
hostname -I

echo ""

echo "⚙️ CPU Information:"
lscpu | head

echo ""

echo "✅ Script Completed"
## Output

📡 Ping Monitor Started...

google.com -> ONLINE ✅
8.8.8.8 -> ONLINE ✅
github.com -> ONLINE ✅
1.1.1.1 -> ONLINE ✅
192.168.1.1 -> ONLINE ✅

## 🎯 Objective

The objective of this project is to:

- Check whether a host is online or offline
- Automate connectivity testing
- Learn basic network monitoring techniques
- Practice Python networking concepts

---

## 🛠 Technologies Used

- Python 3
- subprocess module
- File handling

---

## 📚 Concepts Practiced

- ICMP ping requests
- Network troubleshooting
- Reading from files
- Loops and conditionals
- Error handling
- Automation using Python

---

## ⚙️ How It Works

1. The program reads hosts from `hosts.txt`.
2. It sends a ping request to each host.
3. The response is analyzed.
4. The status is displayed as ONLINE or OFFLINE.

---

## 🧪 Sample Hosts

```text
google.com
8.8.8.8
github.com
```

---

## 📥 Example Output

```text
google.com -> ONLINE ✅
8.8.8.8 -> ONLINE ✅
192.168.1.100 -> OFFLINE ❌
```

---

## 🚀 Future Improvements

- Continuous monitoring mode
- Response time measurement
- Logging results to a file
- Email or Telegram notifications
- Graphical dashboard

---

## 💡 What I Learned

Through this project, I learned:

- Basic network diagnostics
- Using Python for networking tasks
- Automating repetitive checks
- Working with external system commands

---

## 🏁 Conclusion

The Ping Monitor Tool demonstrates how Python can be used for basic network monitoring and troubleshooting. It provides practical experience with connectivity testing and automation in networking environments.
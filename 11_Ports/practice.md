## Task 1: Check Listening Ports

```bash
ss -tuln
```

---

## Task 2: Alternative Port Check

```bash
netstat -tuln
```

---

## Task 3: Check SSH Port

```bash
sudo lsof -i :22
```

---

## Task 4: Install Apache

```bash
sudo apt update
sudo apt install apache2
```

---

## Task 5: Start Apache

```bash
sudo systemctl start apache2
```

---

## Task 6: Check Apache Status

```bash
systemctl status apache2
```

---

## Task 7: Check HTTP Port

```bash
sudo lsof -i :80
```

---

## Task 8: View Open Ports Again

```bash
ss -tuln
```

---

## Task 9: Open Local Web Server

Open in browser:

```text
http://localhost
```

---

## Task 10: Check HTTPS Port

```bash
sudo lsof -i :443
```

---

## Task 11: Check Running Services

```bash
systemctl list-units --type=service
```

---

## Task 12: Check SSH Service

```bash
systemctl status ssh
```

---

## Task 13: View Apache Logs

```bash
journalctl -u apache2
```

---

## Task 14: Live Apache Logs

```bash
journalctl -u apache2 -f
```

---

## Task 15: Stop Apache

```bash
sudo systemctl stop apache2
```

---

## Task 16: Restart Apache

```bash
sudo systemctl restart apache2
```

---

## Task 17: Enable Apache at Boot

```bash
sudo systemctl enable apache2
```

---

## Task 18: Disable Apache at Boot

```bash
sudo systemctl disable apache2
```
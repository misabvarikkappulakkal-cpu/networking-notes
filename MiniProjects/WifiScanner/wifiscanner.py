import subprocess

print("=" * 40)
print("      WiFi Network Scanner")
print("=" * 40)

try:
    result = subprocess.check_output(
        ["netsh", "wlan", "show", "networks"],
        text=True
    )

    print(result)

except Exception as e:
    print("Error:", e)
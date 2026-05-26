
config = """
hostname Router1
interface g0/0
shutdown
interface g0/1

ip address 192.168.1.1
"""

if "shutdown" in config:
    print("warning: Interface is shutdown")

if "ip address" not in config:
    print("warning: No IP address configured")

if "hostname" in config:
    print("Hostname detected")

config = """
interface g0/0
shutdown

interface g0/1
no shutdown

interface g0/2
shutdown
"""

interfaces = config.split("interface")

for item in interfaces:

    if "shutdown" in item and "no shutdown" not in item:
        print("Interface is DOWN")

    elif "no shutdown" in item:
        print("Interface is ACTIVE")
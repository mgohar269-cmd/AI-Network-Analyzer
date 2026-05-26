config = """
interface g0/0
shutdown

interface g0/1
no shutdown

interface g0/2
shutdown
"""

interfaces = config.split("interface")

down_count = 0
active_count = 0

for item in interfaces:

    if "g0/" in item:

        interface_name = item.split()[0]

        if "shutdown" in item and "no shutdown" not in item:

            print(interface_name, "= DOWN")
            down_count += 1

        elif "no shutdown" in item:

            print(interface_name, "= ACTIVE")
            active_count += 1


print("\nFINAL REPORT")
print("DOWN Interfaces:", down_count)
print("ACTIVE Interfaces:", active_count)
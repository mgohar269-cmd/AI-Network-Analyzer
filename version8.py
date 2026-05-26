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

report = ""

print("=" * 45)
print("      AI NETWORK ANALYZER V8")
print("=" * 45)

for item in interfaces:

    if "g0/" in item:

        interface_name = item.split()[0]

        if "shutdown" in item and "no shutdown" not in item:

            status = "[DOWN]"
            print(interface_name, status)

            report += interface_name + " " + status + "\n"

            down_count += 1

        elif "no shutdown" in item:

            status = "[ACTIVE]"
            print(interface_name, status)

            report += interface_name + " " + status + "\n"

            active_count += 1


print("\n========== AI DECISION ENGINE ==========")

if down_count >= 2:

    alert = "CRITICAL ALERT"
    action = "Immediate engineer response required"

elif down_count == 1:

    alert = "MEDIUM RISK"
    action = "Monitor the affected interface"

else:

    alert = "LOW RISK"
    action = "Network operating normally"


print("Threat Level:", alert)
print("AI Recommendation:", action)


summary = "\n========== FINAL REPORT ==========\n"
summary += "DOWN Interfaces: " + str(down_count) + "\n"
summary += "ACTIVE Interfaces: " + str(active_count) + "\n"
summary += "Threat Level: " + alert + "\n"
summary += "Recommendation: " + action

print(summary)

report += summary


file = open("network_report_v8.txt", "w")

file.write(report)

file.close()

print("\nAI Report exported successfully!")
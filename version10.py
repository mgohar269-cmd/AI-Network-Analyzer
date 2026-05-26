import time

print("=" * 60)
print("         AI NETWORK ANALYZER V10")
print("      Smart Enterprise Edition")
print("=" * 60)

devices = {
    "Router-1": """
interface g0/0
shutdown

interface g0/1
no shutdown

interface g0/2
shutdown
""",

    "Switch-1": """
interface f0/1
no shutdown

interface f0/2
shutdown

interface f0/3
no shutdown
"""
}

total_down = 0
total_active = 0

report = ""

for device_name, config in devices.items():

    print("\n" + "=" * 60)
    print("Analyzing Device:", device_name)
    print("=" * 60)

    report += "\nDEVICE: " + device_name + "\n"

    interfaces = config.split("interface")

    device_down = 0
    device_active = 0

    for item in interfaces:

        if "g0/" in item or "f0/" in item:

            interface_name = item.split()[0]

            print("\nChecking Interface:", interface_name)
            time.sleep(1)

            if "shutdown" in item and "no shutdown" not in item:

                status = "[DOWN]"

                print("Status:", status)

                print("AI Suggestion:")
                print("interface", interface_name)
                print("no shutdown")

                report += interface_name + " " + status + "\n"

                device_down += 1
                total_down += 1

            elif "no shutdown" in item:

                status = "[ACTIVE]"

                print("Status:", status)

                print("AI Suggestion:")
                print("No action required")

                report += interface_name + " " + status + "\n"

                device_active += 1
                total_active += 1

    print("\n========== DEVICE AI ANALYSIS ==========")

    if device_down >= 2:

        alert = "CRITICAL ALERT"
        action = "Immediate engineer response required"

    elif device_down == 1:

        alert = "MEDIUM RISK"
        action = "Monitor affected interface"

    else:

        alert = "LOW RISK"
        action = "Device operating normally"

    print("Threat Level:", alert)
    print("AI Decision:", action)

    report += "Threat Level: " + alert + "\n"
    report += "Recommendation: " + action + "\n"

summary = "\n" + "=" * 60 + "\n"
summary += "            FINAL ENTERPRISE REPORT\n"
summary += "=" * 60 + "\n"

summary += "Total DOWN Interfaces: " + str(total_down) + "\n"
summary += "Total ACTIVE Interfaces: " + str(total_active) + "\n"

if total_down >= 3:

    final_alert = "NETWORK CRITICAL"

elif total_down >= 1:

    final_alert = "NETWORK WARNING"

else:

    final_alert = "NETWORK STABLE"

summary += "Overall Network Status: " + final_alert + "\n"

print(summary)

report += summary

file = open("enterprise_network_report_v10.txt", "w")

file.write(report)

file.close()

print("AI Enterprise Report exported successfully!")

print("\nSystem Monitoring Complete...")
print("AI Engine Shutdown...")
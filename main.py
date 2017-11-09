import os
import time

battery_path = "/sys/class/power_supply/BAT0/"

# Main loop
while (True):
	# Get battery capacity ("85%", "100%", etc)
	battery_capacity_file = open(battery_path + "capacity")
	battery_capacity = battery_capacity_file.read()
	battery_capacity_file.close()
	# Get battery status ("Charging", "Discharging", etc)
	battery_status_file = open(battery_path + "status")
	battery_status = battery_status_file.read()
	battery_status_file.close()

	if (battery_capacity == "100\n" and battery_status == "Charging\n"):
		print(battery_capacity)
		os.system("aplay beep.wav")
		time.sleep(15*60)
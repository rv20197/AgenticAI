device_status = "active"
current_temperature = 35

if device_status == "active":
    if current_temperature > 35:
        print("Warning: Device is overheating!")
    else:
        print("Device is operating within normal temperature range.")
else:
    print("Device is inactive. Please check the status and try again.")
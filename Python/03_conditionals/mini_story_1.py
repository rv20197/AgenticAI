import time
kettle_boiled = False

if kettle_boiled:
    print("The kettle is boiled. Time to make tea!")
else:
    print("The kettle is not boiled yet. Please wait.")

time.sleep(2)  # Simulating the time it takes to boil the kettle
kettle_boiled = True

if kettle_boiled:
    print("The kettle is now boiled. Time to make tea!")

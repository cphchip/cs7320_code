import datetime
import time

end_time = time.time() + 10  # Set the end time to 10 seconds from now

while time.time() < end_time:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current time
    print("The current time is:", current_time)
    time.sleep(1)  # Wait for 1 second before printing the next time
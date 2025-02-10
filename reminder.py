import time
from plyer import notification

def remind_20_20_20():
    while True:
        notification.notify(
            title="20-20-20 Reminder 👀",
            message="Look at something 20 meters away for 20 seconds!",
            timeout=10 
        )
        time.sleep(20 * 60)  

if __name__ == "__main__":
    remind_20_20_20()

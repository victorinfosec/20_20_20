import time
from plyer import notification

def remind_20_20_20():
    while True:
        notification.notify(
            title="Rappel 20-20-20 👀",
            message="Regarde au loin (20 mètres) pendant 20 secondes !",
            timeout=10 
        )
        time.sleep(20 * 60)  

if __name__ == "__main__":
    remind_20_20_20()

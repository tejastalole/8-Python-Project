from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "*** Drink Water ***",
            message="Drink a 250ML Water",
            app_icon = "icon1.ico",
            timeout = 5)
        time.sleep(30 * 60)   # for 30 Minutes

# # (pythonw desktopnotifier.py)
# # run this command in cmd for background run continuously
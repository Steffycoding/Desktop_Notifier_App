import time
import win32api
import win32con
from datetime import datetime

def desktop_notifier(title, message):
    """Display desktop notification using win32api."""
    win32api.MessageBox(0, message, title, win32con.MB_ICONINFORMATION)

if __name__ == "__main__":
    # Get user input for notification details
    notification_title = input("Enter notification title: ")
    notification_message = input("Enter notification message: ")

    # Get user input for notification date and time
    date_str = input("Enter date (YYYY-MM-DD): ")
    time_str = input("Enter time (HH:MM): ")

    # Parse user input for date and time
    scheduled_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

    # Calculate time difference between current time and scheduled time
    time_difference = (scheduled_time - datetime.now()).total_seconds()

    if time_difference > 0:
        print(f"Notification scheduled for {scheduled_time}.")
        # Wait until the scheduled time
        time.sleep(time_difference)
        # Display the desktop notification
        desktop_notifier(notification_title, notification_message)
    else:
        print("Invalid scheduled time. Please set a future date and time.")

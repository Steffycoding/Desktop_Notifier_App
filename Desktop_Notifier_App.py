import time
from plyer import notification

def desktop_notifier(title, message):
    """Display desktop notification."""
    notification.notify(
        title=title,
        message=message,
        app_name='Desktop Notifier',
        timeout=10,  # Notification timeout in seconds
    )

if __name__ == "__main__":
    # Get user input for notification details
    notification_title = input("Enter notification title: ")
    notification_message = input("Enter notification message: ")

    # Display the desktop notification
    desktop_notifier(notification_title, notification_message)

    # Wait for a moment before exiting
    time.sleep(5)


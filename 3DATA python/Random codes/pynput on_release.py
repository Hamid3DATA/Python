from pynput import keyboard

variable = 0


def on_release(key):
    if key.char == "b":
        global variable
        print("b was released")
        variable += 1


listener = keyboard.Listener(on_release=on_release)
listener.start()

while variable == 0:
    variable = 0

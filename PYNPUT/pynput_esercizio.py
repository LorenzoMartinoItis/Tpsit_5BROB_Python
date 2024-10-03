# Crea un software che stampi il nome del tasto cliccato su tastiera (solo lettere)
# Usa la libreria:
# pynput

import pynput
from pynput import keyboard


def on_press(key):
    try:
        if(key.char.isalpha()):
            print(f'key {format(key.char)} pressed')
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
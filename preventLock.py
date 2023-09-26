import pyautogui
import time
import keyboard
import signal

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)
print('Preventing lock')
print('Ctrl C to quit')

interrupted = False
while True:        
    pyautogui.press('volumedown')
    time.sleep(15)
    pyautogui.press('volumeup')
    time.sleep(15)
    if interrupted:
        print("Prevent stopped")
        break
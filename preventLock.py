import pyautogui
import time
import keyboard

print('Preventing lock')
print('Keep pressed Q to quit')

while True:        
    try:
        pyautogui.press('volumedown')
        time.sleep(1)
        if keyboard.is_pressed('q'):
            break
        pyautogui.press('volumeup')
        time.sleep(5)
        if keyboard.is_pressed('q'):
            break
    except KeyboardInterrupt:
        break

print('Prevent stopped')
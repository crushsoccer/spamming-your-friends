from pynput.keyboard import Key, Controller
import time

message = "面对疾风吧"
keyboard = Controller()
time.sleep(5)
for num in range(1001):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.面对疾风enter)
    time.sleep(1)

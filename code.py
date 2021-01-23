# Import Modules
from pynput.keyboard import Key, Controller
import time

# Inside the "message" variable, you can put what you are going to text to the user
message = "Hi"

keyboard = Controller()
time.sleep(5)
for num in range(1001): # In the for loop, you can decide how many times you would like to spam the "message" to the other user by changing the number
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) 
    
    time.sleep(1) # Wait for 1 second before texting the next text

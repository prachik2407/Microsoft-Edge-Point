import pyautogui as p
import time
import random
from hashlib import sha256

def search(query):
    p.hotkey("ctrl","e")
    time.sleep(.1)
    p.write(query)
    p.press("enter")
    time.sleep(.67)

print("Starting...")
time.sleep(6)
searchOps = "qwertyuiopasdfghjklzxcvbnm1234567890!\"£$%^&*()/-+.|¬`[];'#,/{}:@~<>?"
searchQ = ""

for z in range(32):
    searchQ += searchOps[random.randint(0,len(searchOps)-1)]

for y in range(len(searchQ)):
    search(searchQ[:y])
    time.sleep(6)

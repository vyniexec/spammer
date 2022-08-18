#https://www.github.com/vyniexec
from operator import truediv
from telnetlib import theNULL
from tkinter import END
import pyautogui as spam
import time
#https://www.github.com/vyniexec

limite_msg = input("VYNIEXEC! Enter N de msgs:")
msg = input("VYNIEXEC! Coloque a msg:")

i = 0

time.sleep(1.5)

while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")

i+=1
#https://www.github.com/vyniexec
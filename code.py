from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

YellowLed = LED(4)
BlueLed = LED(17)
RedLed = LED(27)


win = Tk()
win.title("GUI")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def YellowLedToggel():
    if YellowLed.is_lit:
        YellowLed.off()
        YellowLedButton["text"] = "Turn led on"
        
    else:
        YellowLed.on()
        YellowLedButton["text"] = "Turn led off"
        BlueLed.off()
        RedLed.off()
        
def BlueLedToggel():
    if BlueLed.is_lit:
        BlueLed.off()
        BlueLedButton["text"] = "Turn led on"
        
    else:
        BlueLed.on()
        YellowLed.off()
        RedLed.off()
        BlueLedButton["text"] = "Turn led off"
def RedLedToggel():
    if RedLed.is_lit:
        RedLed.off()
        RedLedButton["text"] = "Turn led on"
        
    else:
        RedLed.on()
        YellowLed.off()
        BlueLed.off()
        RedLedButton["text"] = "Turn led off"

def close():
    GPIO.cleanup()
    win.destroy()
    
YellowLedButton = Button(win, text = 'Turn led on', font = myFont, command = YellowLedToggel, bg = 'yellow', height = 1, width = 24)
YellowLedButton.grid(row=0, column=1)

BlueLedButton = Button(win, text = 'Turn led on', font = myFont, command = BlueLedToggel, bg = 'blue', height = 1, width = 24)
BlueLedButton.grid(row=1, column=1)

RedLedButton = Button(win, text = 'Turn led on', font = myFont, command = RedLedToggel, bg = 'red', height = 1, width = 24)
RedLedButton.grid(row=2, column=1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'grey', height = 1, width = 6)
exitButton.grid(row=3, column=1)

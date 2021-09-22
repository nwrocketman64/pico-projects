from machine import Pin
import utime

pins = [
    Pin(16, Pin.OUT), #middle
    Pin(17, Pin.OUT), #top left
    Pin(18, Pin.OUT), #top
    Pin(19, Pin.OUT), #top right
    Pin(13, Pin.OUT), #bottom right
    Pin(14, Pin.OUT), #bottom
    Pin(15, Pin.OUT), #bottom left
    Pin(12, Pin.OUT), #dot
]

chars = [
    [0, 1, 1, 1, 1, 1, 1, 0], #0
    [0, 0, 0, 1, 1, 0, 0, 1], #1
    [1, 0, 1, 1, 0, 1, 1, 0], #2
    [1, 0, 1, 1, 1, 1, 0, 1], #3
    [1, 1, 0, 1, 1, 0, 0, 0], #4
    [1, 1, 1, 0, 1, 1, 0, 1], #5
    [1, 1, 1, 0, 1, 1, 1, 0], #6
    [0, 0, 1, 1, 1, 0, 0, 1], #7
    [1, 1, 1, 1, 1, 1, 1, 0], #8
    [1, 1, 1, 1, 1, 1, 0, 1], #9
]

def clear():
    for i in pins:
        i.value(1)
clear()

while True:
    for i in range(len(chars)):
        for j in range(len(pins)):
            pins[j].value(chars[i][j])
        utime.sleep(1)
from adafruit_circuitplayground import cp
import time

BLACK = (0, 0, 0)
pixel_color = (100, 100, 100)


def pixels_on():
    for i in range(0, 10):
        cp.pixels[i] = (pixel_color)

def pixels_off():
    for i in range(0, 10):
        cp.pixels[i] = (BLACK)


def main():
    if cp.touch_A1:
        pixels_on()
    else:
        pixels_off()

while True:
  
    main()
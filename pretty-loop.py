import board
import time
import neopixel
pixels = neopixel.NeoPixel(board.D18, 150)
	
pixels.fill((0, 0, 0))

while(True):
    for x in range(0, 150):
        pixels[x] = (0, 255, 0)
        time.sleep(0.001)
    for x in reversed(range(0, 150)):
        pixels[x] = (0, 0,255)
        time.sleep(0.001)
    for x in range(0, 150):
        pixels[x] = (255, 0, 0)
        time.sleep(0.001)
    for x in reversed(range(0, 150)):
        pixels[x] = (128, 0, 128)
        time.sleep(0.001)
    

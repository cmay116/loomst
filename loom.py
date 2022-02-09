import board
import time, sys
import neopixel
pixels = neopixel.NeoPixel(board.D18, 150,brightness=0.1)

loomNums = {"1": 0,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "7": 6,
            "8": 7,
            "9": 8,
            "10": 9,
            "11": 10,
            "12": 11,
            "13": 12,
            "14": 13,
            "15": 14,
            "16": 15,
            }

red = (0, 255, 0)
pixels.fill((0, 0, 0))

def lightItUp(row):
    off()
    global splitArray
    lightLin(splitArray[row - 1], loomNums, red)

def lightLin(l, d, c):
      for shaft in l:
       pixels[d[shaft]] = c
def off():
      pixels.fill((0,0,0))


testArray = []

with open('static/numbers.txt') as my_file:
    testArray = my_file.readlines()
splitArray = []
for line in testArray:
      junk = line.strip().split(",")
      splitArray.append(junk)
      
               
         
         
#pixels[loomNums["3"]] = red

# while(True):
#     for x in range(134, 150):
#         pixels[x] = (128, 0, 128)
#         time.sleep(0.2)
#     for x in reversed(range(134, 150)):
#         pixels[x] = (255, 255, 255)
#         time.sleep(0.2)




            
# lightLin(['1', '2', '5'], loomNums, red)
# time.sleep(2)
# off()
# lightLin(['4', '3', '4'], loomNums, red)
# time.sleep(2)
# off()
# lightLin(['1', '2', '5'], loomNums, red)
# time.sleep(2)
# off()
# lightLin(['4', '3', '4'], loomNums, red)
# time.sleep(2)
# off()

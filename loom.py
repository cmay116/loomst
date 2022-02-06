import board
import time, sys
import neopixel
pixels = neopixel.NeoPixel(board.D18, 150,brightness=0.1)

loomNums = {"1": 134,
            "2": 135,
            "3": 136,
            "4": 137,
            "5": 138,
            "6": 139,
            "7": 140,
            "8": 141,
            "9": 142,
            "10": 143,
            "11": 144,
            "12": 145,
            "13": 146,
            "14": 147,
            "15": 148,
            "16": 149,
            }

red = (255, 0, 0)
pixels.fill((0, 0, 0))

def lightItUp(row):
    global splitArray
    lightLin(splitArray[row], loomNums, red)

def lightLin(l, d, c):
      for shaft in l:
       pixels[d[shaft]] = c
def off():
      pixels.fill((0,0,0))


testArray = []

with open('numbers.txt') as my_file:
    testArray = my_file.readlines()
splitArray = []
for line in testArray:
      junk = line.strip().split(",")
      splitArray.append(junk)
      
while(True):
      try:
       for line in splitArray:
                lightLin(line, loomNums, red)
                input(line)
                off()
      except KeyboardInterrupt:
           print("\ngoodbye")
           off()
           sys.exit()
               
         
         
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

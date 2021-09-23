import pyfirmata
import time
import numpy as np
from main import count_vehicles, calculate_delays, controller, logTrafficStats
from data_display import display_data

file = 'data.csv'

displaycount = 1
led_red = 13
led_amber = 12
led_green = 11

led_red_ = 10
led_amber_ = 9
led_green_ = 8
port = 'COM12'
board = 0 ##pyfirmata.Arduino(port)

index = 0

delay_endsAB = np.array([3, 4, 5, 5, 6, 7, 3, 4, 5, 5, 6, 7])
delay_endC = np.array([5, 6, 7, 3, 4, 5, 5, 6, 7, 3, 4, 5])

test_camAB = []
endABcam = 'AB2.mp4'
endCcam = 'C.mp4'

endsABcount = 0
endsCcount = 0


while True:
##    board.digital[led_amber].write(1)
##    time.sleep(1)
##    board.digital[led_amber].write(0)
##    time.sleep(1)
    countAB, countC = controller(board, index, delay_endsAB, delay_endC, endCcam, endABcam)
    delayA, delayB, boon = calculate_delays(countAB, countC, 0.7)
    # delay_endsAB.append(delayA)
    # delay_endC.append(delayB)
    displaycount = display_data(delayA, delayB, countAB, countC, displaycount)
    logTrafficStats(file, countC, countAB, delayB, delayA, boon)
##    print(delayA)
##    board.digital[led_amber].write(1)
##    time.sleep(delayA)
##    board.digital[led_amber].write(0)
##    time.sleep(2)
##    board.digital[led_green].write(1)
##    time.sleep(2)
##    board.digital[led_green].write(0)
##    time.sleep(2)
##    board.digital[led_red].write(1)
##    time.sleep(2)
##    board.digital[led_red].write(0)
    index = index + 1
    if index == 12:
        index = 0
    

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
board = 0#pyfirmata.Arduino(port)

index = 0

delay_endsAB = np.array([8, 9, 5, 5, 6, 7, 7, 4, 5, 5, 6, 7])
delay_endC = np.array([5, 6, 7, 6, 4, 5, 5, 6, 7, 3, 4, 5])

test_camAB = []
endABcam = 'B.mp4'
endCcam = 'C.mp4'

endsABcount = 0
endsCcount = 0


while True:
    countAB, countC = controller(board, index, delay_endsAB, delay_endC, endCcam, endABcam)
    delayA, delayB, boon = calculate_delays(countAB, countC, 3)
    
    displaycount = display_data(delayA, delayB, countAB, countC, displaycount)
    logTrafficStats(file, countC, countAB, delayB, delayA, boon)

    
    # board.digital[led_green].write(0)
    print('green off') 
    # board.digital[led_amber].write(1)
    print('amber on')
    time.sleep(2)
    # board.digital[led_amber].write(0)
    print('amber off') 
    # board.digital[led_red].write(1)
    print('red on')
    time.sleep(1)

    # board.digital[led_red_].write(0)
    print('red_ off')
    time.sleep(1)
    # board.digital[led_green_].write(1)
    print('green_ on')
    time.sleep(round(delayB/10, 1))
    # board.digital[led_green_].write(0)
    print('greeen_ off')
    # board.digital[led_amber_].write(1)
    print('amber_ on')
    time.sleep(2)
    # board.digital[led_amber_].write(0)
    print('amber_ off') 
    # board.digital[led_red_].write(1)
    print('red_ on')
    time.sleep(0.5)
    # board.digital[led_red].write(0)
    print('red off')
    time.sleep(1)
    
    # board.digital[led_red_].write(1)
    # board.digital[led_green].write(1)
    print('green on')
    time.sleep(round(delayA/10, 1))


    index = index + 1
    if index == 12:
        index = 0
    

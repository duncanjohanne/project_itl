import pyfirmata
import time
from main import count_vehicles, calculate_delays
from data_display import display_data

displaycount = 1
led_red = 13
led_amber = 12
led_green = 11

led_red_ = 10
led_amber_ = 9
led_green_ = 8
port = 'COM12'
board = 0 ##pyfirmata.Arduino(port)

delay_endsAB = 1
delay_endC = 0

endABcam = 'A.mp4'
endCcam = 'C.mp4'

endsABcount = 0
endsCcount = 0

def controller(board):
    #high to green
##    board.digital[led_green].write(1)
    terminate = time.localtime().tm_sec + delay_endsAB
    endsCcount = count_vehicles(terminate, endCcam)
    return endsCcount
    #low to green
##    board.digital[led_green].write(0)
##    #high to amber
##    board.digital[led_amber].write(1)
##    time.sleep(2)
##    #low to amber
##    board.digital[led_amber].write(0)
##    #high to red
##    board.digital[led_red].write(1)
    #low to red_
#     board.digital[led_red_].write(0)
#     #high to green_
#     board.digital[led_green_].write(1)
# ##    terminate = time.localtime().tm_sec + delay_endC
# ##    #counting vehicles
# ##    endsABcount = count_vehicles(terminate, endABcam)
#     #low to green_
#     board.digital[led_green_].write(0)
#     #high to amber_
#     board.digital[led_amber_].write(1)
#     time.sleep(5)
#     #low to amber_
#     board.digital[led_amber_].write(0)
#     #high to red_
#     board.digital[led_red_].write(1)
    #low to red
##    board.digital[led_red].write(0)

##    return endsABcount, endsCcount










while True:
##    board.digital[led_amber].write(1)
##    time.sleep(1)
##    board.digital[led_amber].write(0)
##    time.sleep(1)
    count = controller(board)
    delayA, delayB = calculate_delays(count, 0, 0.7)
    displaycount = display_data(delayA, delayB, 0, count, displaycount)
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
    

import time
times = 1
def display_data(delayAB, delayC, countAB, countC, times):
    if times == 1:
        print("Stats Collected : ")
        print(59*"-")
        print("| AB Delay   | C Delay | AB Vehicle Count | C Vehicle Count |")
        print(59*"-")
        print("|    "+str(delayAB)+"         "+str(delayC)+"            "+str(countAB)+"                "+str(countC)+"         |")
        print(59*"-")
    else:
        print("|    "+str(delayAB)+"         "+str(delayC)+"            "+str(countAB)+"                "+str(countC)+"         |")
        print(59*"-")

    times += 1
    return times
        
##while True:
##    times = display_data(1, 0, 0, 0, times)
##    time.sleep(3)

import cv2
import time

# timing based on vehicle volumes
def calculate_delays(countAB, countC, objectPerSecond):
    delayAB = countAB * objectPerSecond
    delayC = countC * objectPerSecond

    if delayAB < 10:
        delayAB = 10
    if delayC < 10:
        delayC = 10
    if delayC == 0:
        delayC = 5
    if delayAB == 0:
        delayAB = 5

    return delayAB, delayC


def count_vehicles(terminate, cam):
    #loading video of traffic
    cap = cv2.VideoCapture(cam)

    #object detector used to extract moving objects
    #history attribute increases precision of object detection
    #varthreshold reduces false positives
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)

    vehicle_counter = 0
    #looping 
    while True:
        #creating object reading the video
        ret, frame = cap.read()

        #extraction of region of interest
        height, width, _ = frame.shape
        region = frame[300:500,50:600]
        #creating mask that shows the objects that are required
        mask = object_detector.apply(frame)

        #cleaning mask, removing shadows
    # _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        
        #extracting boundaries of the moving objects from mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #iterating through the contours
        for cnt in contours:
            #calculating area and eliminating small elements
            area = cv2.contourArea(cnt)
            #drawing contours on objects
            if area > 650:
                #cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
                #extracting values for drawing rectangle on object
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                #middle points
                xMid = int((x + (x+w))/2)
                yMid = int((y + (y+h))/2)
                cv2.circle(frame, (xMid, yMid), 5, (0, 255, 0), 5 )

                if yMid > 400 and yMid < 420:
                    vehicle_counter += 1

        #showing threshold line
        cv2.line(frame, (70,400), (350, 400), (0,0,255), 2)#red line
        #showing vehicle counting 
        cv2.putText(frame, 'Total Vehicles : {}'.format(vehicle_counter), (250, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        #showing frame
        cv2.imshow('Frame', frame)
        
        
        # cv2.imshow('Mask', mask)
        # #showing region of interest
        # cv2.imshow('Region', region)   


        #using a key to break loop eg. esc
        key = cv2.waitKey(30)
        sec = time.localtime().tm_sec
        if sec == terminate:
            sec = time.localtime().tm_sec
            break

    cap.release()
    cv2.destroyAllWindows()

    return vehicle_counter

## term = time.localtime().tm_sec + 30
## val = count_vehicles(term, 'A.mp4')
## print(val)
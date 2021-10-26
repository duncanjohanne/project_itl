from main import count_vehicles
import time

terminate = time.localtime().tm_sec + 20

count = count_vehicles(terminate, 'C.mp4')
print(int((count/3.3)*2.7))
import time
import main as mb

def qwerty():
    x = 0
    y = 1

    return x, y

term = time.localtime().tm_sec + 15
val = mb.count_vehicles(term, 'B.mp4')
print(val)
x, y = qwerty()
print(x, y)
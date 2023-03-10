import time
import threading
import math

def calculate_square_root():
    number = 256
    square_root = math.sqrt(number)
    print("Square root of", number, "is", square_root)

def delayed_square_root(milliseconds):
    time.sleep(milliseconds/1000)
    calculate_square_root()

delay = 2000  # 2 seconds
thread = threading.Timer(delay/1000, delayed_square_root, args=[delay])
thread.start()
print("Waiting for square root to be calculated...")
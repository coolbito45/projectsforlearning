import time
while True:
    for i in range(10):
        print(" "*i + "0")
        time.sleep(0.1)
    for i in reversed(range(10)):
        print(" "*i + "0")
        time.sleep(0.1)
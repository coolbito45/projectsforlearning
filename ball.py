import time
while True:
    for i in range(26):
        print(" "*i + "0")
        time.sleep(0.1)
    for i in reversed(range(26)):
        print(" "*i + "0")
        time.sleep(0.1)
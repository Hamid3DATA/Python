import time
seconds = 5
while True:
    print("Image in:")
    print(f"00:0{seconds}")
    seconds -= 1
    time.sleep(1)
    if seconds == 0:
        break
print("Voila")

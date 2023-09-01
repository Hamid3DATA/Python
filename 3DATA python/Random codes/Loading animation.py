import os
from time import sleep

my_list = ["|", "/", "-", "\\"]
count = 0

# while True: (instead of for x in my_list:)
for x in my_list:
    print(my_list[count])
    sleep(0.5)
    os.system('cls')
    count += 1
    if count == 4:
        count = 0

# works in visual studio code

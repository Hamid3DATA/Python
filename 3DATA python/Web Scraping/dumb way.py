the_sum = 0
bottom = list(range(35, 71))
bottom2 = list(range(35, 70).__reversed__())
count = -1
bottom_count = 0
i = -1
right = list(range(-25, 101))
numbers = [1, 1, 1, 2]
for x in range(101):
    i += 1
    count += 1
    if count == 3:
        count = -1
        print(str(x) + "% {right: " + str(right[i + 1]) + "%; bottom: " + str(bottom[bottom_count]) + "%;}")
        i = i + 1
    else:
        print(str(x) + "% {right: " + str(right[i]) + "%; bottom: " + str(bottom[bottom_count]) + "%;}")
    bottom_count += 1
    if bottom_count == 36:
        break

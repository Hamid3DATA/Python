the_sum = 0
bottom = list(range(35, 71))
bottom2 = list(range(35, 70).__reversed__())
count = -1
count2 = 0
bottom_count = 0
i = -1
right = list(range(-25, 101))
numbers = [1, 1, 1, 2]
while True:
    i += 1
    count += 1
    if count == 3:
        count = -1
        print(str(count2) + "% {right: " + str(right[i + 1]) + "%; bottom: " + str(bottom[bottom_count]) + "%;}")
        i += 1
    else:
        print(str(count2) + "% {right: " + str(right[i]) + "%; bottom: " + str(bottom[bottom_count]) + "%;}")
    count2 += 1
    bottom_count += 1

    if count2 == 99:
        break

    elif bottom_count == 35:
        bottom_count = 0
        count = -1
        for y in range(35):

            i += 1
            count += 1
            if count == 3:
                count = -1
                print(str(count2) + "% {right: " + str(right[i + 1]) + "%; bottom: " + str(bottom2[bottom_count]) + "%;}")
                i += 1
            else:
                print(str(count2) + "% {right: " + str(right[i]) + "%; bottom: " + str(bottom2[bottom_count]) + "%;}")
            count2 += 1
            bottom_count += 1
            if count2 == 99:
                break

            elif bottom_count == 35:
                bottom_count = 0
                count = -1
                for z in range(35):
                    i += 1
                    count += 1
                    if count == 3:
                        count = -1
                        print(str(count2) + "% {right: " + str(right[i + 1]) + "%; bottom: " + str(
                            bottom[bottom_count]) + "%;}")
                        i += 1
                    else:
                        print(str(count2) + "% {right: " + str(right[i]) + "%; bottom: " + str(
                            bottom[bottom_count]) + "%;}")
                    count2 += 1
                    bottom_count += 1
                    if count2 == 99:
                        break

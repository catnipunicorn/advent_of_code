

## open file
doc = open('firstfile.txt', 'r')
data = doc.readlines()
summa = 0
previous = int(data[0])
current = int(data[0])
oldy = int(data[0])
ancient = int(data[0])
iteration = 0

for current in data:
    current_n = int(current)
    prevsum = ancient + oldy + previous
    cursum = oldy + previous + current_n
    #print(prevsum)
    #print(cursum)
    if iteration > 2 and prevsum < cursum:
        summa = summa + 1
    ancient = oldy
    oldy = previous
    previous = current_n
    iteration = iteration + 1
print(summa)
  

# print(summa)


# new_summa = 0
# i = int(data[0])
# new_list = []
# for x in data:





# [sum(data[i]) for i in range(3)]
# print(new_list)




# window = int(new_list[0])
# for window_x in new_list:
#     window_new = int(window_x)
#     if window < window_new:
#         new_summa = new_summa + 1
#     window = window_new

# print(new_summa)

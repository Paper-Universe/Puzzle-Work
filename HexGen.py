import os
import random
from time import time
#puzzle 69
count = 0
spaces = 0
range2 = 18 # Amount of total digits in hex range
file2 = open('list2.txt','a')
#16777215
st = time()
with open('list2.txt', 'r') as file3:
        for line in file3:
            spaces += line.count(' ')
list = []
file = open("list2.txt", 'r') # Make an empty list.txt file before you start program
randomList = file.read()
total = (255)
print(total)
while count in range(total):
    rand = random.randint(0x1ffff00, 0x1ffffff) # currently 6 0's and f's or 44 bit
    hexify = hex(rand)
    stripped = hexify[2:]
    file = open("list2.txt", 'r')
    randomList = file.read()
    if stripped not in randomList or list:
        list.append(stripped)
        if count % 1 == 0: 
            print(f'[+] Completed: {count}', end='\r')
            file2.write(('{} '*len(list)).format(*list))
            list.clear()
        count += 1
        file2.flush()
        os.fsync(file2.fileno())
    elif stripped in list or randomList:
        continue
file2.close()
print(f'[+] Finished Total Keys: {total}\n')
print(f'[+] Completed in {time() - st:.2f} sec')

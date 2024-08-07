import os
import random
from time import time
#puzzle 69
count = 0
spaces = 0
range2 = 18 # Amount of total digits in hex range
total = 268435455 # Max Range in Decimal. Max Range = (end range - start)
#268435455
file2 = open('list2.txt','a')
st = time()

list = []
file = open("list2.txt", 'r') # Make an empty list.txt file before you start program
randomList = file.read()

while count in range(total):
    rand = random.randint(0x10000000, 0x1fffffff) # currently 7 0's and f's or 40 bit
    hexify = hex(rand)
    stripped = hexify[2:]
    count += 1
    if stripped not in list or randomList:
        list.append(stripped)
        file2.flush()
        os.fsync(file2.fileno())
    elif stripped in list or randomList:
        continue
    if count % 1000 == 0: 
        print(f'[+] Completed: {count}', end='\r')
        file2.write(('{} '*len(list)).format(*list))
        list.clear()
file2.close()
print(f'[+] Finished Total Keys: {total}\n')
print(f'[+] Completed in {time() - st:.2f} sec')
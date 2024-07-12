from random import randint
import subprocess
from os.path import exists
import random
#puzzle 69
count = 0
spaces = 0
range2 = 18 # Amount of total digits in hex range
total = 268435455 # Max Range in Decimal. Max Range = (end range - start)

list = []
file = open("list.txt", 'r') # Make an empty list.txt file before you start program
randomList = file.read()
list.append(randomList)

#16,777,215 for 6
#268,435,455 for 7
#4,294,967,295 for 8
#274,877,906,943 for 9
#1,099,511,627,775 for 10

while exists('Found.txt') == False:
    if exists('Found.txt') == True:
        exit()
    rand = random.randint(0x10000000, 0x1fffffff) # currently 7 0's and f's or 40 bit
    hexify = hex(rand)
    stripped = hexify[2:]
    file = open("list.txt", 'r') # add this to rest
    randomList = file.read()
    if stripped not in randomList and list:
        list0 = list.append(hexify)
        list1 = str(stripped)
        if (count % 1) == 0: # saves the Randomly generated hexes to file 
            def count_blank_spaces(file):
                spaces = 0
                with open('list.txt', 'r') as file:
                    for line in file:
                        spaces += line.count(' ')
                return spaces
            percentage = count_blank_spaces(file)
            percent = (percentage / total)
            print("{:.50%}".format(percent))
            with open("list.txt", 'a') as vf:
                vf.write(f"{list1} ")
                vf.close()
        start = str(stripped).ljust(range2, '0')
        end = ':' + str(stripped).ljust(range2, 'f')
        final = start + end
        count += 1
        run = subprocess.run(["cmd","/c","KeyHunt-Cuda.exe -t 0 -g --gpux 2048,128 -m address --coin BTC -o Found.txt --range ",final, '19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG'])
    elif stripped in randomList or list:
        continue


#40 bit seems to be the sweet spot only 15 keys less than 44 bit but marginally more keys than 36 or 32 bit in the same time
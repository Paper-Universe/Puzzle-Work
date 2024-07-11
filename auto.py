from random import randint
import subprocess
import random
from os.path import exists
#puzzle 69
count = 0
spaces = 0
range2 = 18 # Amount of total digits in hex range
total = 68719476480 # Max Range in Decimal. Max Range = (end range - start)

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
    rand = random.randint(0x10000000ff, 0x1fffffff00) # currently 9 0's and f's 
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
        run = subprocess.run(["cmd","/c","BitCrack.exe -b 68 -t 256 -p 128 -c -o Found.txt --keyspace ",final, '19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG'])
    elif stripped in randomList or list:
        continue

#32 bit range = time:1sec
#36 bit range = time:16m 
#40 bit range = time:3.23h 

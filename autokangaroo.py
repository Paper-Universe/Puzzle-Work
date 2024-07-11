from random import randint
import subprocess
from os.path import exists

count = 0
range2 = 33 # Amount of total digits in hex range
total = 151115727451828646838271 # Max Range in Decimal. Max Range = (end range - start)
pubkey = '03633cbe3ec02b9401c5effa144c5b4d22f87940259634858fc7e59b1c09937852'

list = []
file = open("listk.txt", 'r') # Make an empty list.txt file before you start program
randomList = file.read()
list.append(randomList)

while exists('Found.txt') == False:
    if exists('Found.txt') == True:
        exit()
    rand = randint(0x20000000000000000000, 0x3fffffffffffffffffff) #19 f's
    hexify = hex(rand)
    stripped = hexify[2:]
    file = open("listk.txt", 'r')
    randomList = file.read()
    if stripped not in randomList and list:
        list0 = list.append(hexify)
        list0 = str(stripped)
        if (count % 1) == 0: # saves the Randomly generated hexes to file
            with open("listk.txt", 'a') as the_file:
                the_file.write(f"{list0} ")
                the_file.close()
        start = str(stripped).ljust(range2, '0')
        end = str(stripped).ljust(range2, 'f')
        count += 1
        with open("file.txt", 'w') as vf:
            vf.write(f"{start}\n{end}\n{pubkey}\n")
            vf.close()
        word = subprocess.run("kangaroocpu.cmd")
    elif stripped in randomList:
        continue

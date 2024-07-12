from random import randint
import subprocess
from os.path import exists
import random

count = 0
spaces = 0
range2 = 20
total = 528905046081400263933951 

list = []
file = open("list.txt", 'r') 
randomList = file.read()
list.append(randomList)

while exists('Found.txt') == False:
    if exists('Found.txt') == True:
        exit()
    rand = random.randint(0x1000000000, 0x7fffffffff)
    hexify = hex(rand)
    stripped = hexify[2:]
    file = open("list.txt", 'r') 
    randomList = file.read()
    if stripped not in randomList and list:
        list0 = list.append(hexify)
        list1 = str(stripped)
        if (count % 1) == 0:
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
        run = subprocess.run(["cmd","/c","KeyHunt-Cuda.exe -t 0 -g --gpux 2048,128 -m addresses --coin BTC -o Found.txt -i hash160outs.bin --range ",final])
    elif stripped in randomList or list:
        continue

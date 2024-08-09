from os.path import exists
import random
from random import randint
import secp256k1 as ice
#puzzle 66
list = []
count = 0
target = "20d45a6a762535700ce9e0b216e31994335db8a5"
privKey= 0x0000000000000000000000000000000000000000000000020000000000000000

while exists('Found.txt') == False:
    h160 = ice.privatekey_to_h160(0, True, privKey).hex()
    privKey += random.randint(0x1, 0xffffffffffffffff)
    list.append(privKey)
    count += 1
    print(f'[+] Completed: {count}', end='\r')
    if privKey > 0x3ffffffffffffffff:
        privKey = 0x0000000000000000000000000000000000000000000000020000000000000000
    if count % 1000 == 0:
        list.clear()
    if h160 == target:
        HEX = "%064x" % privKey
        caddr = ice.privatekey_to_address(0, True, privKey)
        wifc = ice.btc_pvk_to_wif(HEX)
        privKey = hex(privKey)
        list = ('{} '*len(list)).format(*list)
        list = (list[:-19])
        with open('Found.txt', 'w') as vf:
            vf.write(f"{caddr}\n{privKey}\n{wifc}\n{list}")
            vf.close()
        print('Found')
        exit()
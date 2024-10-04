import subprocess
import binascii
import secp256k1 as ice
# puzzle 69
puzzle = '19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG'
rangestart = '100000000000000000'
rangeend = '1fffffffffffffffff'
i = 0
count = 0
range2 = 0xfffffffffffffffff
list = []
P = '04608c7b8f41eae057b976053cbf001346e353b3b8aab6b7cd1ed689f35889ac7a20bd5531eb7da2dbcd5277a43655add6e69a9c0ffceae396484cb35f6d47eee8'
scrambles = binascii.unhexlify(P)
list.append(scrambles)
print('Expected:', int(range2)
def world():
    publickey_inc = ice.point_increment(list[0])
    list.clear()
    list.append(publickey_inc)
    #publickey_uncompressed = publickey_inc[:65].hex()
    #publickey_back_into_bytes = binascii.unhexlify(publickey_uncompressed)
    match = ice.pubkey_to_address(0, True, publickey_inc)
    if match == puzzle:
        public2 = publickey_inc[:65].hex()
        print(f'\nFOUND: {match}\t {public2}')
        #run kangaroo
        with open("file.txt", 'w') as file:
            file.write(f'{rangestart}\n{rangeend}\n{public2}')
            file.close()
            subprocess.run('kangaroo.cmd')
            exit()
    return (publickey_inc, match)
while i in range(0xfffffffffffffffff):
    try:
        public, match = world()
        i += 1
        count += 1
        #print(match)
        print(f'[+] Completed: {count}', end='\r')
    except(KeyboardInterrupt, SystemExit):
        public = public[:65].hex()
        print(f'{count}')
        print(f"{public}")
        exit('\nSIGINT or CTRL-C detected. Exiting gracefully. BYE')
print('  Program Finished  ')

#start P = 0485672c7d2de0b7da2bd1770d89665868741b3f9af7643397721d74d28134ab837c481b9b5b43b2eb6374049bfa62c2e5e77f17fcc5298f44c8e3094f790313a6

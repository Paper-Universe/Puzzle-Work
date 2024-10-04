import subprocess
import binascii
import secp256k1 as ice
# puzzle 69
puzzle = '19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG'
rangestart = '100000000000000000'
rangeend = '1fffffffffffffffff'
i = 0
count = 0
stride = 0xfffffffffff
range2 = 0xfffffffffffffffff
list = []
P = '04608c7b8f41eae057b976053cbf001346e353b3b8aab6b7cd1ed689f35889ac7a20bd5531eb7da2dbcd5277a43655add6e69a9c0ffceae396484cb35f6d47eee8'
scrambles = binascii.unhexlify(P)
list.append(scrambles)
print('Expected:', int(range2 / stride))
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
        i += stride
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
#adding stride can't check through the public key if it goes over so we will need to check through our i
'''
we just need to add to i what we put into stride so if stride = 10 then i += 1
also add a ctrl exit like in seed puzzle from iceland and make it print out the last public key it hashed so we can save where we ended
'''
#look at icelands and others code to see how they get 3.5 million keys per second
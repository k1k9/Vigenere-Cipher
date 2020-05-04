#!/usr/bin/env python3
from sys import argv, exit
from modules.encrypt import encrypt
from modules.decrypt import decrypt



# CHECK USAGE MESSAGE
def _usage():
    print(
f'''USAGE: {argv[0]} <OPTIONS> <KEY> <TEXT>

    -e <KEY> <TEXT>\t Encrypt text via <KEY>
    -d <KEY> <TEXT>\t Decrypt text via <KEY>
''')
    exit()




# MAIN
if len(argv) < 4: _usage()

elif len(argv) == 4:
    if argv[1].lower()   == '-e': encrypt(argv[2], argv[3])
    elif argv[1].lower() == '-d': decrypt(argv[2], argv[3])
    else:
        _usage()

else: _usage

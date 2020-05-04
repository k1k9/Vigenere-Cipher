#!/usr/bin/env python3
import argparse

from sys import argv, exit
from modules.caesar  import caesar_table
from modules.encrypt import encrypt
from modules.decrypt import decrypt


parser = argparse.ArgumentParser(description='Encrypt and decrypt message using Vigenere Cipher method')
# Options
parser.add_argument('-e', '--encrypt', action='store_false',
                    help='Encrypt your message via your key (default enabled)')
parser.add_argument('-d','--decrypt', action='store_true',
                    help='Decrypt your message via your key')

# Arguments
parser.add_argument('key', metavar='KEY',
                    help='KEY which encrypts/decrypts your message')
parser.add_argument('text', metavar='TXT',
                    help='Message wich you want to encrypt/decrypt message')

args = parser.parse_args()



if args.decrypt:
    encrypt(args.key, args.text, caesar_table())
elif args.encrypt:
    decrypt(args.key, args.text, caesar_table())
    
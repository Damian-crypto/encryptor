import sys

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# simple_key = get_random_bytes(32)
# print(simple_key)

SALT = b'\xa3tt\x8cp\x19\x10\xca\xe1\xda\x91\xb4\x9bM\xe7l\xf85\xc7\xc4^\xd7C\x8e\x02Z_\t\xcd\xa2\x17Y'

# References: https://youtu.be/gyPuAJfOnGk
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Invalid usage: python generator.py <password>')
    elif len(sys.argv) == 2:
        password = sys.argv[1]
        key = PBKDF2(password, SALT, dkLen=32)

        with open('key.bin', 'wb') as file:
            file.write(key)

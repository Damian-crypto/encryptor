import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Invalid usage: python unlocker.py <key-file> <encrypted-file>')
    elif len(sys.argv) == 3:
        key_file = sys.argv[1]
        enc_file = sys.argv[2]

        with open(key_file, 'rb') as file:
            key = file.read()
        
        with open(enc_file, 'rb') as file:
            iv = file.read(16)
            cipher_data = file.read()
        
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        original = unpad(cipher.decrypt(cipher_data), AES.block_size)
        print(original.decode('utf-8'))

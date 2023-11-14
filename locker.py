import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Invalid usage: python locker.py <key-file> <message-file>')
    elif len(sys.argv) == 3:
        key_file = sys.argv[1]
        msg_file = sys.argv[2]

        with open(key_file, 'rb') as file:
            key = file.read()
        
        with open(msg_file, 'r') as file:
            msg = file.read()
        
        cipher = AES.new(key, AES.MODE_CBC)
        cipher_data = cipher.encrypt(pad(msg.encode('utf-8'), AES.block_size))

        with open('encrypted.bin', 'wb') as file:
            file.write(cipher.iv)
            file.write(cipher_data)

import hashlib # test sha256 alg

def encodeUTF8(msg):
    byte = ' '.join(format(ord(char), '08b') for char in msg)
    return byte

usrInput = input("input message to convert\ninput:\t")
Input = encodeUTF8(usrInput)
print(Input)

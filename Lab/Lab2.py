import sys

# python command line
input=sys.argv[1]
output=[" problems but EECS 388 ain't one"]

if input>1:
    output.append(input)
    output.reverse()
    print ''.join(output)


# Caesar cipher
def encrypt(msg,k):
    msg=msg.upper()
    ciphertext=''
    for letter in msg:
        cipher_num=(ord(letter)-ord('A')+k)%26
        cipher_chr=chr(cipher_num+ord('A'))
        ciphertext+=cipher_chr
    print('Ciphertext: '+ciphertext)

encrypt('helloworldtest',5)
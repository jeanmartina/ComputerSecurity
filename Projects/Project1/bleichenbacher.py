import roots
import hashlib
import sys
import math

def hexstr_to_int(hex):
    numbers = '0123456789'
    letters = 'abcdef'
    counter = 0
    sum = 0
    for c in hex[::-1]:
        to_add = 0
        if c in numbers:
            to_add = int(c)*16**counter
        else:
            to_add = (ord(c) - ord('a') + 10)*16**counter
        sum += to_add
        counter += 1
    return sum

def main():
#print(hexstr_to_int('6ab282e'))
    message = sys.argv[1]
    # Your code to forge a signature goes here.
    n=0x00b06004b3528bfd2d187f48e6cb9f3fe79afade6cc3c428dd0577b8bb3e752824b632d100d28b396726a887c5189ded3fe9717d959730dadbf468b2bc76eea3c15091a38b61fdfa46b1510ef885ea3105ae7d7f3007e97c6761bc47e715ba32464c77f7d0cfd2c88c0f53d45404a110d6951d3f4255edc3523921237a86f35fed200c7e45870b822d7652dc896d0de064617dbb48eb9b1d47103f12911b0dab3d91e0fdb847f0b87cf2b20b19d3b951cae86cab611893f6f4cd016c68607e970fc2db800f981d9bb4441fe5d70299693a8ae51f2e9b2656f0c279bf87ecb96a753f231739eb1f9a9d7dd01f15f283dd2da2887e7fdef6aedd61c4ca7b3be1b1cd
    #print(n)
    e = 3

    prefix = "0001FF003031300d060960864801650304020105000420"
    m = hashlib.sha256()
    m.update(message)
    evil_hex = m.hexdigest()
    evil_str = prefix + evil_hex + "00"*(201)
    evil_int = int(evil_str,16)


    evil_forged = roots.integer_nthroot(evil_int, e)
    if (evil_forged[1]):
        new_forged = evil_forged[0]
    else:
        new_forged = evil_forged[0]+1    

    print roots.integer_to_base64(new_forged)


if __name__ == "__main__":
    main()

#update hashlib with the public key
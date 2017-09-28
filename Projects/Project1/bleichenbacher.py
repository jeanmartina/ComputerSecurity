import roots
import hashlib
import sys
import math

def main():
    message = sys.argv[1]
    # Your code to forge a signature goes here.
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
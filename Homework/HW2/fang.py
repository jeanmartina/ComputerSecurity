ciphertext=\
"QEDPZVYSPVPJPZIFHPJANWHDCVPYCIPZTPNXRTVOLRQBCVDRTWFLDZYCSAEPJWRRBEQIJE\
IDFMIXBGPLADSAWJSMILRANDCKEYPATOCXJEFDMVXRHNEBCIOVRLSAEFXGLJGIVWGZWYYC\
SAEPZLREEEPMYTEAOXDGXIQFXOLRWGTKFAUMPSWPVIMFTBJVUEQWMAXOIUTVYLVQGSMIMT\
LGMMASEIVEEVWNJVYMOLVGXAQZGRSSHWJHOYYMWPWUINOMYSSXUPAJVGAUTKCMFOAZEIEF\
ECPVVRTPNHGZVWYFECIHRVGSMCINHJLAVFESNOADPIIEMIIHAINCTTEAMANPVGESFDBJNN\
QRDUJVGMZPZHVPWSCWHLVWSCQZRQWBQBCIPGUHINIAKELDZHHTBYQOAVXUEPZHNXRTBREF\
NHDBNYPLNDBDGXEFEPZSYHSLACMBRRONVQVPLAZVGGMGTWIIEYFPLOSPEECGYMTRVQQZHF\
SYTLVRQVRLANYEMAREZPYANEAJRJLNELJCBYZLSZSSMGSWGQRWJLANMGXVYORMGLUTAWEP\
OGZUZEAHVSIYKVZRYPDQASFTOISSQLZKXYCEGTWILBAQTLTSHOAZERLNXVHINHBMARQWIY\
MRGMTSHLNGMZCRWVYBCIOEPVWACBYESMVHVLNGMVXYINDBVARPYAWGMFLROADPIIEATVXR\
HPZNAIRTBEQIJESAEWAQRWNTLCIOYGEMGPZIJLBNSAAULBYSLSHXIFIBJBFZQMFMGZZNWG\
MPVADRPIJPPVZRFRPVNSHRSZZOYAEGPINXBQVDACMZEAOPVZRRBYWOMBRBQPDWRVELVYXU\
MFLKXMQIAEIGWBYIPVDVOIPZUZWBJVXXJVGEANMGIGQRSMVVLSHCMXSAWGCCXXGLRXIIFL\
EAPFVQVRNEQJRBJVEQOLVRXDIDHVJBWTJAVRTLAAEEEFTKJYYHGSMHIGLBOAJJZCPZUKEA\
MBYBCEGHEXWMXVQRCQNEFYPNMNWSYYPTYIEPLXMYMPEYXIIARPYPAOIRQROADRPIGSWNIJ\
LBVVJAUMZRQQIUMZEPDWZEEVWAXUIVCIKTEIPTIOMBRTZWYWNMQSWGQRWRIKZPYIAEQOLV\
RXLTNSGLNEBCICVBMIWMYMGJQNMAJNGWPVBJUTAWIVRTLKJYAXEJXMEPXVEQJRRVJSWYSR\
WNRZZEGHRLTJJUMFGQNMGMARWIJBSGHPTWBFRNIPWRXUTANXVGXEPJYTLBCQBMAEYWGVZR"


def var(string):
    count=[0]*26
    for i in range(0,len(string)):
        count[ord(string[i].capitalize())-ord('A')]+=1
    assert sum(count)==len(string)
    s=0
    for i in range(0,26):
        s+=(float(count[i])/len(string) - float(1)/26)**2
    return s/26


def kasiski(cipher, length):
    l=[]
    for j in range(0,length):
        l.append("")
    for j in range(0,len(cipher)):
        l[j%length]+=cipher[j]
    s=0
    for k in l:
        s+=var(k)
    return s/length


### Problem 2
p2=open("P4.txt","w")
p2.write("# Problem 2\n")

for i in range(1,10):
    p2.write("key_length=="+str(i)+", variance="+str(kasiski(ciphertext,i))+"\n")
p2.write("Clearly, when key_length==7, we have a large population variance.\n")

vigenere = [""]*7
for i in range(0, len(ciphertext)):
    vigenere[i % 7] += ciphertext[i]

# for i in range(0,7):
#     p2.write(vigenere[i]+"\n")

p2.write("Then apply normal frequency analysis.\n"
         "Assume letter 'e' will occur with top nth frequency "
         "and generate the possible key sets. "
         "In practice, we will make n=3 or n=4, since 3^7=2187, 4^7=16384, "
         "both affordable to use brute-force to try all keys.\n")

# Vigenère decipher, default upper case, lower case when specified
def decrypt(cipher,key,capital=True):
    decipher=""
    if capital:
        for i in range(0,len(cipher)):
            decipher=decipher+chr((ord(cipher[i])-ord(key[i%len(key)]))%26+ord('A'))
    else:
        for i in range(0,len(cipher)):
            decipher=decipher+chr((ord(cipher[i])-ord(key[i%len(key)]))%26+ord('a'))
    return decipher


# find letters of maximum frequency.
# Assume 'e' is at top nth frequency, find the corresponding Caesar ciphers
def freqmax(string,n):
    count=[0]*26
    for i in range(0,len(string)):
        count[ord(string[i].capitalize())-ord('A')]+=1
    count=sorted(range(len(count)), key=lambda x: count[x],reverse=True)
    candidate=[]
    for i in range(0,n):
        candidate.append(chr((count[i]-4)%26+ord('A')))
    return candidate


# generate all the possible keys from the max frequency
def generator(n):
    keypool = []
    for i in range(0, len(vigenere)):
        keypool.append(freqmax(vigenere[i], n))
    keys = []
    for a in keypool[0]:
        for b in keypool[1]:
            for c in keypool[2]:
                for d in keypool[3]:
                    for e in keypool[4]:
                        for f in keypool[5]:
                            for g in keypool[6]:
                                keys.append(a + b + c + d + e + f + g)
    return keys

# select the population variance that is approximately at the normal English text level, and sort them by population variance, descending order
def selector(n,threshold):
    keys=generator(n)
    keylist=[]
    varlist=[]
    for key in keys:
        s=var(decrypt(ciphertext,key))
        if s>threshold:
            keylist.append(key)
            varlist.append(s)
    return [y for x,y in sorted(zip(varlist,keylist),reverse=True)]

finallist=selector(4,0.0009)
p2.write("So the final list of candidates are the following keys:\n")

p2.write(', '.join(finallist)+"\n")

p2.write("Print the decrypted text together with the population variance,\n")
for key in finallist:
    plain=decrypt(ciphertext, key, capital=False)
    p2.write(key+"\t"+str(var(plain))+"\n"+plain+"\n")

p2.write("It turns out that the plaintext decrypted by key 'ANODIZE' makes the most sense.")

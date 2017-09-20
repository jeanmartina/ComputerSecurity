dictionary=\
{ "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }

plaintext=\
"ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletot\
hinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt\
ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolate\
thelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev\
enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpuls\
ioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacya\
ndpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawf\
ullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandab\
useactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisi\
soneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindou\
btwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoft\
echnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"


ciphertext=\
"TUSQIQEGBFQTDHTUSZIXENQGXKGAAFHKMRXRRBJBGSFUWVEHPLVBWPZXHBIUBGETNZOBGI\
DHBHLZMNNBGBGIIEVRZRISSCOTNAEQVLUZRDVBGMDHTUSOWUITUOWBGIHBFVMRSFGVHZZR\
GRFVJNVESCUBGIIEFLLDVSJOVANKRROWBGETGVHGVIRRKLTKMNTHRNZGERJHVSLEGSUZNV\
OSHKMCSOEWIBGIIEADASIRFVHIQXSJSUMRXENRBIRXHRMZIKOEQPHAHHEGVHUAYTNFRLSL\
EUCUADSFECKIMVESIVMCXHRKDGZRDUSVBNSDFKHISMNTOQLSVEZPOQMKIAOIMZVTUOWEZW\
GEWHDNYSGCVMDXHRBOMFSLNGOIHHHVGKIMHSBBKQRIYRGDVCWAAUVWLIWBFGASLAGKHVSW\
OSHLVSLETZRWLYNGWOPDWUSTHZDHHVAVMKJTBPHTDHAAROMFSLNGSIRWEQWQIMHTUSUMRX\
OBRJQLPIGVHLVERSZHNSELYOOWMIHVGNVDISFVRWJENQVHEZWWECWPVMTUVLURILSVHZDM\
SNHKQMKUAVHIQHOSVHAZMDNBHTEAIYZJWTRDRFJZNYNQOQLZHWNFILZVEACWEHXHGVDBGI\
PYIQODHIAPXBHXSRSPMCXOUWPBGETUSGZZKGRRKQRJERHOQJILROGWUIRGVHBGVEFVRTCE\
NQOWWMGENPOQMHNRGVKZQEHDRVGMMRJHVTTOAULUKMGYWQARSNJVRPZHWNZNMCYNNTUIHH\
IAADVXHERDSTZGEFCIBGIWBFOLZVATCUVGEDOFRCFLTGCUKGISSFRUCYNUOUZNAAARQWVL\
EJSQBZLENREMZVIAURVDELBTWIMHEYZDLZRWVHKIMSTUSUEDRTNHWPDVENFDVCKIZZLASY\
MOZLVFFEUWQLRXRBJHBNSVRFWIJIHVAKMBSUYRVMDROGVLVFFUGHKMCMMSZDUDSFGVHBNV\
CUSVJTXISHKMBSMCOQGGELGSGBGIRRGHMLIDNBHVCPEFGZPHWPRFRNUSIPSVIKPAOCXBGM\
MNAXZLYRBTZWQHSVBQWSSNTIHBGETUSKICIVRFKMZVDOSIWQINBHKQMKAFGDQKIDGVHKNQ\
PNBBVNVWVHKASSOQHKMHVPNGVIFIAARBMSWTROGQKCFROUOQIWBBWPDHWNFIIRLEJSQBNR\
MBGWWEELYPHKZYSRVHSMIWACZBGETGVHZDGOHZGJDROGIUVHRGOOFSZPLGVHXZXHFPHPHR"


### Problem 1

### define the population variance of an arbitrary string
def var(string):
    count=[0]*26
    for i in range(0,len(string)):
        count[ord(string[i].capitalize())-ord('A')]+=1
    assert sum(count)==len(string)
    s=0
    for i in range(0,26):
        s+=(float(count[i])/len(string) - float(1)/26)**2
    return s/26

p1=open("P1.txt","w")
p1.write("# Problem 1\n")


''' (a) What is the population variance of the relative letter frequencies in English text? '''
s=0
for i in range(ord('A'),ord('Z')+1):
    s+=(dictionary[chr(i)] - float(1)/26)**2
p1.write("part_a_var_english=")
p1.write(str(s/26)+"\n")


''' (b) What is the population variance of the relative letter frequencies in the given plaintext? '''
p1.write("part_b_var_plaintext=")
p1.write(str(var(plaintext))+"\n")

''' (c) For each of the following keys-yz,xyz,wxyz,vwxyz,uvwxyz-encrypt
    the plaintext with a Vigenère cipher and the given key,
    then calculate and report the population variance of the relative letter
    frequencies in the resulting ciphertext.
    Describe and briefly explain the trend in this sequence of variances.
'''
vigenere=[]
l=[]
p1.write("part_c_var_ciphertexts=[")
for key in ("yz","xyz","wxyz","vwxyz","uvwxyz"):
    s=""
    for i in range(0,len(plaintext)):
        s=s+chr((ord(plaintext[i])+ord(key[i%len(key)])-2*ord('a'))%26+ord('a'))
        # print(key[i%len(key)],plaintext[i],char)
    vigenere.append(s)
    l.append(str(var(s)))
p1.write(", ".join(l))
p1.write("]\n")
explain="The variance here evaluates how unbalanced the occurrence of letters is. " \
        "In particular, if the string is 'abcdefghijklmnopqrstuvwxyz' or any of its permutation, " \
        "the population variance will be 0, meaning that all letters occur at the same frequency. " \
        "According to the dictionary, English texts, in general, are not evenly distributed, " \
        "so the population variance should be greater than zero. " \
        "Indeed, from part (a), we get 0.001..., and so is the plaintext. " \
        "However, if the plaintext is encrypted by a Vigenère cipher, the origin distribution is also broken, " \
        "making the letters distributed more evenly. " \
        "Thus, the population variance has a trend to decrease (to zero).\n"
p1.write("part_c_explain="+explain)

''' (d) Viewing a Vigenère key of length k as a collection of k independent Caesar ciphers,
    calculate the mean of the frequency variances of the ciphertext for each one.
    (E.g., for key yz, calculate the frequency variance of the even numbered ciphertext characters
    and the frequency variance of the odd numbered ciphertext characters. Then take their mean.)
    Report the result for each key in part (c).
    Is the mean variance like those observed in part (b)? Part (c)? Briefly explain.
'''
p1.write("part_d_means=[")
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

for i in range(0,len(vigenere)):
    p1.write(str(kasiski(vigenere[i],i+2)))
    if i!=len(vigenere)-1:
        p1.write(", ")
    else:
        p1.write("]\n")
explain="Caesar cipher of length one does not change the population variance of the plaintext. " \
        "This is because each character of the plaintext is shifted by the same amount, " \
        "making the relative frequency unchanged. " \
        "Thus, the population variances remain close to the regular English texts for all the Vigenère keys in (c), " \
        "which is approximately 0.001, and is close to the result in (b) and is much higher than the results in (c).\n"
p1.write("part_d_explain="+explain)

''' (e) Consider the ciphertext that was produced with key uvwxyz.
    In part (d), you calculated the mean of six variances for this key.
    Revisit that ciphertext, and calculate the mean of the frequency variances that arise
    if you had assumed that the key had length 2, 3, 4, and 5.
    Does this suggest a variant to the Kasiski attack? (Don't say no!) Briefly explain.
'''
p1.write("part_e_means=[")
for i in range(2,6):
    p1.write(str(kasiski(vigenere[4],i)))
    if i!=5:
        p1.write(", ")
    else:
        p1.write("]\n")
explain="This method is a very efficient variant of Kasiski attack. " \
        "In Kasiski attack we need to break ciphertexts into blocks of certain lengths " \
        "and search for frequently occurring patterns. " \
        "And this method is easier to implement since we don't need to search patterns. " \
        "Most of the code is doing numerical calculation, instead of using data structure to manipulate characters. " \
        "We are quite sure that, if we guess the key length wrong, then the average of the population variances should " \
        "be much lower than the normal English texts level (approximately 0.001), " \
        "while if we guess the key length correct, then it is very likely that the average of population variances " \
        "jumps to 0.001 level."
p1.write("part_e_explain="+explain)

p1.close()











### Problem 2
p2=open("P2.txt","w")
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

finallist=selector(3,0.001)
p2.write("So the final list of candidates are the following keys:\n")

p2.write(', '.join(selector(3,0.001))+"\n")

p2.write("Print the decrypted text together with the population variance,\n")
for key in finallist:
    plain=decrypt(ciphertext, key, capital=False)
    p2.write(key+"\t"+str(var(plain))+"\n"+plain+"\n")

p2.write("It turns out that the plaintext decrypted by key 'ANODIZE' makes the most sense.")

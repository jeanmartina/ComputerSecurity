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


''' Problem 1 '''

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
    Describe and brieﬂy explain the trend in this sequence of variances. 
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
explain="The variance here evaluates how inbalanced the orrurance of letters is.\n\t\
In particular, if the string is 'abcdefghijklmnopqrstuvwxyz' or any of its permutation,\n\t\
the population variance will be 0, meaning that all letters occur at the same frequency.\n\t\
According to the dictionary, English texts, in general, are not evenly distributed,\n\t\
so the population variance should be greater than zero.\n\t\
Indeed, from part (a), we get 0.001..., and so is the plaintext.\n\t\
However, if the plaintext is encryped by a Vigenère cipher, the origin distribution is also breaked,\n\t\
making the letters distributed more evenly.\n\t\
Thus, the population variance has a trend to decrease (to zero).\n\
"
p1.write("part_c_explain="+explain)

''' (d) Viewing a Vigenère key of length k as a collection of k independent Caesar ciphers,
    calculate the mean of the frequency variances of the ciphertext for each one.
    (E.g., for key yz, calculate the frequency variance of the even numbered ciphertext characters 
    and the frequency variance of the odd numbered ciphertext characters. Then take their mean.)
    Report the result for each key in part (c).
    Is the mean variance like those observed in part (b)? Part (c)? Briefly explain.
'''
p1.write("part_d_means=[")
for i in range(0,len(vigenere)):
    # print vigenere[i]+"\n"
    l=[]
    for j in range(0,i+2):
        l.append("")
    for j in range(0,len(vigenere[i])):
        l[j%(i+2)]+=(vigenere[i][j])
    s=0
    for k in l:
        s+=var(k)
    p1.write(str(s/len(l)))
    if i!=len(vigenere)-1:
        p1.write(", ")
    else:
        p1.write("]")

p1.close()

"ANODIZE"
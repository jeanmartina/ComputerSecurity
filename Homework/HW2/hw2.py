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
p1=open("P1.txt","w")
p1.write("# Problem 1\n")

### (a) What is the population variance of the relative letter frequencies in English text?
s=0
for i in range(ord('A'),ord('Z')+1):
    s=s+dictionary[chr(i)]
print(s)
## the sum of frequency is a little larger than 1, which means there is round-off errors.

s=0
for i in range(ord('A'),ord('Z')+1):
    s=s+(dictionary[chr(i)]-1/26)**2
# print(s/26)
p1.write("part_a_var_english=")
p1.write(str(s/26)+"\n")

n=len(plaintext)
s=0
for i in range(0,n):
    char=plaintext[i].capitalize()
    s=s+dictionary[char]
# print(s/n)
p1.write("part_b_var_plaintext=")
p1.write(str(s/n)+"\n")

p1.close()
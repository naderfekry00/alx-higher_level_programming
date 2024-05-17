#!/usr/bin/python3

for i in range(122,96,-1):
        ascii_chr = chr(i)
        if i % 2 != 0:
            print(ascii_chr.upper(), end='')
        else:
            print(ascii_chr, end='')

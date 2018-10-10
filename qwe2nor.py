#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
qwe2nor - transform qwerty layout table to norman layout

Auther: Verf
Email: verf@protonmail.com
Licence: GPL v3
"""
import sys

MAP = {'q': 'q',
       'w': 'w',
       'e': 'd',
       'r': 'f',
       't': 'k',
       'y': 'j',
       'u': 'u',
       'i': 'r',
       'o': 'l',
       'p': 'h',
       'a': 'a',
       's': 's',
       'd': 'e',
       'f': 't',
       'g': 'g',
       'h': 'y',
       'j': 'n',
       'k': 'i',
       'l': 'o',
       'z': 'z',
       'x': 'x',
       'c': 'c',
       'v': 'v',
       'b': 'b',
       'n': 'p',
       'm': 'm', }


def main():
    if len(sys.argv) != 3:
        print("Error: Worry Argument!")
        return
    if sys.argv[1] == '-h':
        print("Usage: qwd2nor.py <Source File> <Destination File>")
        return
    sour = sys.argv[1]
    dest = sys.argv[2]
    new_table = ''
    with open(sour) as f:
        isData = False
        for line in f:
            if '[Data]' in line:
                isData = True
            if isData:
                new_line = ''
                for char in line[:-1]:
                    if char in MAP.keys():
                        new_line += MAP[char]
                    else:
                        new_line += char
                new_table += new_line + '\n'
            else:
                new_table += line
    with open(dest, 'w') as f:
        f.write(new_table)
    print("Done!")


if __name__ == '__main__':
    main()

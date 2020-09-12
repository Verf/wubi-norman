#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
qwe2nor - transform qwerty layout table to norman layout

Auther: Verf
Email: verf@protonmail.com
Licence: GPL v3
"""
import os
import sys
import argparse

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

def line_trans(line, isdata=True):
    new_line = ''
    if isdata:
        for char in line:
            if char in MAP.keys():
                new_line += MAP[char]
            else:
                new_line += char
    else:
        new_line = line
    return new_line

def default_transcoder(sourf, destf, spliter=None):
    if not spliter:
        spliter = ''
    isdata = False
    for line in sourf:
        new_line = line_trans(line, isdata)
        destf.write(new_line)
        if spliter in line:
            isdata = True

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="需要进行转换的源文件路径", type=str)
    parser.add_argument("-o", "--output", help="转换后的输出文件路径", type=str)
    parser.add_argument("-t", "--type", help="需要进行转换的文件类型", type=str.lower, choices=['fcitx', 'rime'])
    parser.add_argument("-s", "--spliter", help="需要进行转换的文件分隔符", type=str)
    args = parser.parse_args()

    if args.output:
        output = args.output
    else:
        _, source_name = os.path.split(args.source)
        tmp = source_name.split('.')
        output = tmp[0] + '_norman.' + '.'.join(tmp[1:])

    souf = open(args.source, 'r', encoding='utf-8')
    outf = open(output, 'w', encoding='utf-8')
    if args.type == 'fcitx':
        default_transcoder(souf, outf, spliter='[Data]')
    elif args.type == 'rime':
        default_transcoder(souf, outf, spliter='...')
    else:
        default_transcoder(souf, outf, args.spliter)
    souf.close()
    outf.close()


if __name__ == '__main__':
    main(sys.argv)

# wubi-norman
wubi(五笔) table for norman keyboard layout user
基于norman键盘布局的fcitx格式的五笔86码表

- qwe2nor.py: The Python script transform qwerty layout to norman layout
- wbn.conf: wubi-norman config file
- wbn.mb: wubi-norman table file
- wbn.txt: wubi-norman txt format file
- wbx.mb: default qwerty wubi table file
- wbx.txt: default qwerty wubi txt format file

### usage
1. copy wbn.conf and wbn.mb file to ~/.config/fcitx/table/
2. select wubin in fcitx configuration

### qwe2nor usage
Usage: qwd2nor.py <Source File> <Destination File>

The source file must in txt format.
You can transform mb format to txt format by mb2txt tool provided py fcitx.
`mb2txt <mb file> > <txt file>`
Also you can use txt2mb tool transform txt format to mb format.
`txt2mb <txt file> <mb file>`

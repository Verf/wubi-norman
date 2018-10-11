# wubi-norman
wubi(五笔) table for norman keyboard layout user  
基于norman键盘布局的fcitx格式的五笔86码表  

- qwe2nor.py: The Python script transform qwerty layout to norman layout
- wbn.conf: wubi-norman config file
- wbn.mb: wubi-norman table file
- wbn.txt: wubi-norman txt format file
- wbx.mb: default qwerty wubi table file
- wbx.txt: default qwerty wubi txt format file

### 用法
1. 复制`wbn.conf`和`wbn.mb`文件到`~/.config/fcitx/table/`路径  
2. 在fcitx的设置菜单添加wubi-norman布局  
注意：由于norman布局的变化，原来p键(之字部)被移到了norman布局h键(原；符号)的位置。  

### qwe2nor脚本用法
Usage: qwd2nor.py <Source File> <Destination File>

源文件需要是txt格式的码表文件，转换出的文件同样为txt格式，若要使用需要转为mb格式  
你可以使用fcitx提供的mb2txt工具把mb格式的码表转为txt格式  
`mb2txt <mb file> > <txt file>`  
同样，你也可以使用txt2mb工具把txt格式的码表转为mb格式  
`txt2mb <txt file> <mb file>`  

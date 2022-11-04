# Wubi - Norman

基于Norman键盘布局的五笔86码表和五笔98码表，包括Fcitx版本和Rime版本。Fcitx版本和Rime版本都使用其内置的五笔码表，如果有特殊需求也可以使用本项目提供的转换脚本对其他码表进行转换。注意，由于Norman键盘布局的变化，Qwerty布局的`P`键（之字部，Norman布局中为`;`键）被移动到了`;`键位置（Norman布局中为`H`键）的位置，可能需要适应一段时间。

## 用法

### Fcitx

1. 复制`wubi-norman.conf`和`wubi-norman.mb`文件到`~/.config/fcitx/table/`目录
2. 在Fcitx的设置菜单中添加`wubi-norman`

### Rime

1. 复制`wubi86_nn.schema.yaml`和`wubi86_nn.dict.yaml`或`wubi98_nn.schema.yaml`和`wubi98_nn.dict.yaml`到Rime用户文件夹中
2. 在Rime的输入法设定中选择`五笔86-Norman`或`五笔98nn`

## 脚本用法
将QWERTY布局的fcitx码表文件或rime码表文件转换为Norman布局：
```bash
python qwe2nor.py -t {fcitx, rime} <dict file>
```

**注意**：对于fcitx码表，其默认格式为`.mb`文件，在转换前需要使用fcitx官方的mb2txt工具将mb文件转换为txt文件，在布局转换完成后，也要使用txt2mb工具将txt文件转换为mb文件使用：
```bash
mb2txt <mb file> > <txt file>
txt2mb <txt file> <mb file>
```

除了针对Fcitx和Rime格式的码表，也可以直接将任意QWERTY布局的码表文件转换为Norman布局：
```bash
python qwe2nor.py <source file>
```

很多码表文件都在文件开头进行参数设置，然后使用一个字段作为分隔，再之后才是字词编码内容，因此可以使用`-s`参数指定分隔字段：
```bash
python qwe2nor.py -s <split token> <source file>
```

默认将在脚本的调用路径生成转换后的Norman布局码表文件，也可以使用`-o`参数指定输出路径：
```bash
python qwe2nor.py <source file> -o <output file>
```

import MeCab
m = MeCab.Tagger("-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
print(m.parse("けやき坂46がどん兵衛を食べている"))
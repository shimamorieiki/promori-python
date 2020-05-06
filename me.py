import MeCab
m = MeCab.Tagger("-u /home/tk/Documents/prog/py-promori/dic/atsumori.dic")
print(m.parse("けやき坂46がショボいつりざおを壊した"))
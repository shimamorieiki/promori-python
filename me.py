import MeCab

m = MeCab.Tagger("-Ochasen")
print(m.parse("けやき坂46が赤いきつねを食べている"))

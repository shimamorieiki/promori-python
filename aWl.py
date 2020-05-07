words = []
with open("./text/words.csv", mode='r', encoding="utf-8") as f:
    lines = f.readlines()
    # coding: UTF-8
    for line in lines:
        if line != "\n":
            index = line.split(",")
            words.append(index[0])

x = input("追加したい言葉を入力してください:")
y = input("読みを入力してください:")
check = input(x + ":" + y + "を登録しますか？")
if check == "y" or check == "ｙ":
    if x in words:
        print("すでに登録されています")
    else:
        with open("./text/words.csv", mode='a', encoding="utf-8") as f:
            # 表層形,左文脈ID,右文脈ID,コスト,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
            f.write("\n")
            f.write(x+",,,"+"1,名詞,固有名詞,一般,*,*,*," +
                    x + "," + y + ",,(用語)")
        print(x+"を登録しました")
else:
    print("登録をキャンセルしました")

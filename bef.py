
recipes = []
exists = []

with open("./text/furni20200506.html", mode='r', encoding="utf-8") as f:
    lines = f.readlines()
    # coding: UTF-8
    for line in lines:
        if line != "\n":
            recipes.append(line.replace("\n", ""))


with open("./text/recipe.csv", mode='r', encoding="utf-8") as f:
    lines = f.readlines()
    # coding: UTF-8
    for line in lines:
        item = line.split(",")
        exists.append(item[0])

with open("./text/recipe.csv", mode='a', encoding="utf-8") as f:
    for recipe in recipes:
        if recipe in exists:
            # 表層形,左文脈ID,右文脈ID,コスト,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
            f.write(recipe+",,,"+"1,名詞,固有名詞,一般,*,*,*," +
                    recipe+",yomi,hatuonn,(レシピアイテム)\n")

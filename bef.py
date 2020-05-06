
recipes = []
with open("./text/item.html", mode='r',encoding="utf-8") as f:
    # f.write(tweet.full_text.replace("\n","")+"\n")
    lines = f.readlines()
    # coding: UTF-8
    for line in lines:
        if line != "\n":
            recipes.append(line)

with open("./text/recipe.csv", mode='w',encoding="utf-8") as f:
    for recipe in recipes:
        #表層形,左文脈ID,右文脈ID,コスト,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
        f.write(recipe.replace("\n","")+",,,"+"1,名詞,固有名詞,一般,*,*,*,"+recipe.replace("\n","")+",yomi,hatuonn,(レシピアイテム)\n")

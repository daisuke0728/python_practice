#変数yearに西暦を年で入力
print("yearを入力してください。year: ")
year = input()
year = int(year)


#if文により条件分岐をしうるう年可平年かを判別する
if year%100 == 0 and year%400 != 0:
    print(str(year)+"は平年です")
elif year % 4 == 0:
    print(str(year)+"はうるう年です")
else:
    print(str(year)+"は平年です")

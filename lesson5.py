#Format 格式化
'''
[法一]
%d -> int
%f -> float
%s -> str
usage: '%s %d %f....' % (data1, data2, ..., dataN)
1.如果在前面加數字 -> 至少輸出幾個字元，如果不夠就補空格在前面，太多就不管
2.如果在%f中加入.2(N) -> 輸出到小數點後2(N)位
'''
#name: kevin
name = 'kevin'
height = 180
weight = 70
#姓名：＿＿＿ 身高： 體重： bmi:
print('姓名：%7s 身高：%d 體重：%d bmi：%.2f'%(name, height, weight, weight/(height/100)**2))
#name: kevin
name = 'Alan'
height = 180
weight = 70

#姓名：＿＿＿ 身高： 體重： bmi:
print('姓名：%7s 身高：%d 體重：%d bmi：%.2f'%(name, height, weight, weight/(height/100)**2))
'''
[法二]
.format() -> .:1.的 2.對...做...
順序 -> always starts from 0
挖洞：{順序(int):至少輸出幾個字元(int)}
如果設定至少幾N個字元:
    -> if N > 實際輸出的字元 then 在後面補空格
    -> else 超過就不管
設定輸出到小數點後第Ｎ位 -> {:.Nf}
'''
name = 'Alanaa'
height = 180
weight = 70

print('{1} {2} {0:5} {3:.2f}'.format(name, height, weight,weight/(height/100)**2))
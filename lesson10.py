'''t = (1, 2, 3)
print(t[0])

dict1 = {'John':30, 'Eddy':21, 'Mary':18} #建立一個字典
print(dict1['John'])
'''

#1.Jonh mid: 70, final: 75, casual: 80
#2.Cindy mid: 46, final :90, casual: 75
#3.Kevin mid: 66, final :60, casual: 70
#平均, 排名

def avg(s:list):
    return sum(s)/3

s = {'John':[70, 75, 80],'Cindy':[46, 90, 75],'Kevin':[66,60, 70]}
print(s.keys())
# a = {'John':avg(s['John']),'Cindy':avg(s['Cindy']),'Kevin':avg(s['Kevin'])}
# r = []
# for i in ['John', 'Cindy', 'Kevin']:
#     if not r:
#         r.append(i)
#         continue
#     if a[i] > a[r[-1]]:
#         r.append(i)
#     else:
#         r.reverse()
#         r.append(i)
#         r.reverse()
# for i in r:
#     print("%s:%d"%(i, a[i]))


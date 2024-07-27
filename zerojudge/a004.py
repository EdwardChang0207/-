'''
連續輸入：lesson 1 補充講義
'''
import sys #使用sys函式庫
for i in sys.stdin: #std -> standard
    if (int(i) % 4 == 0 and int(i) % 100 != 0) or (int(i) % 400 == 0):
        print('閏年')
    else:
        print('平年')
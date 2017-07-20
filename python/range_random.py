#!/use/bin/python
# -*- coding: utf-8 -*
#内建range函数
#range(start,end,step) 
#range(1,5) 代表从1到5 （不包含5）
#range(5) 代表从0到5 （不包含5）
#导入 random 库
import random
a=[]
for x in range(10):
   a.append(random.randrange(100))

a.sort()
print a

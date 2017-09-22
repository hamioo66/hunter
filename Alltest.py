# -*- coding=utf-8 -*-
import random
#test.login()
#s=strs.strip("'")
#print type(s)

# -*- coding=UTF-8 -*-
list=[]
strs="'[108,1873]'"
#去除字符串两边的字符
s=strs.strip("'[]'")
print s
#以逗号拆分字符串，并逐一添加到list中
a=int(s.split(',')[0])
b=int(s.split(',')[1])
list.append(a)
list.append(b)
print list
#将字符串当成表达式来求值
print eval('[596, 1627]')
#去除字符串左边的字符
#s1=strs.lstrip("'[")
#去除字符串右边的字符
#s2=s1.rstrip("']")


s="hello"
print s[:-2]



####
print random.randint(0,9)
print random.randrange(0,10)
#######
i = '13'
j = str(random.randrange(4, 10)) + ''.join(str(random.choice(range(10))) for j in range(8))
phoneNum=i+j
print phoneNum


########
import django
print django.VERSION

#迭代器及for循环
list=[1,2,3,4,5]
for x in list:
    list.pop(0)
    print(" old: ",str(x))
    x=1
    print(" new:",str(x))
    print(" new list: ",str(list))
    print()

#循环猜数字游戏
start=0
end=100
number=23
running=True
while running:
    guess=int(raw_input(u'请输入一个1-100范围内的数字'))
    if guess==number:
        print u"恭喜你，猜对了！"
        running=False
    elif guess<number:
        global guess1
        guess1=guess
        print(u"你猜小了，正确值在 %d " % guess1 + u"到 %d 之间" % end)
    elif guess>number:
        global guess2
        guess2=guess
        while guess2 < guess1:
            print(u"你输的数字太大了，正确值在%d" % guess1 + u"到 %d 之间" % guess)
        else:
            print(u"你输的数字太大了,正确值在 %d " % guess1 + u"到 %d 之间" % guess2)
    else:
        break
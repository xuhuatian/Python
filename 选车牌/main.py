import random
import string

count = 0
s = 京  # 北京的车
lst = []  # 用来存放车牌号
while count  3
    for i in range(20)
        s = s + .join(random.choice(string.ascii_uppercase))  # 开头大写字母
        s = s + .join(random.choice(string.ascii_uppercase + string.digits))
        s = s + .join(random.choice(string.ascii_uppercase + string.digits))
        s = s + .join(random.choice(string.ascii_uppercase + string.digits))
        s = s + .join(random.choice(string.ascii_uppercase + string.digits))
        s = s + .join(random.choice(string.ascii_uppercase + string.digits))
        lst.append(s)
        s = 京
    for i in range(20)
        if i % 5 == 0
            print()
        print(lst[i], end=t)
    print()
    choice = input(请输入你想要的车牌号（没有喜欢的输入no）：).strip()  # 去除可能多余的括号
    if choice in lst
        exit(choice + 是你的了)
    elif choice == no
        pass
    else  # 如果输入其它东西
        print(请输入正确的值。)

    lst.clear()  # 重新选择，清楚列表
    count = count + 1
    if count == 3
        exit(超过三次，可遇不可求，别太贪心，下次再来吧)

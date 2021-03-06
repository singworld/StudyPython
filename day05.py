# 项目实战一
# 项目描述：根据嵌套 for 循环生成九九乘法表
# 提示：
# 根据九九乘法表的规律，找到两个
# for 循环的边界值
# 使用range()函数生成数字集合

for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={j*i}',end=' ')
    print('')


# 项目实战二，打印图
# *
# ***
# *****
# *******
# *****
# ***
# *
# 使用两个 for 循环
# 找对 in 后面的边界值，使用range()
for i in range(1,8,2) :
    for j in range(i):
        print('*',end=' ')
    print('')
for i in range(5,0,-2) :
    for j in range(i):
        print('*',end=' ')
    print('')

# 项目实战三
# |---欢迎进入通讯录程序---|
# |---1、 查询联系人资料---|
# |---2、 插入新的联系人---|
# |---3、 删除已有联系人---|
# |---4、 退出通讯录程序---|
# 请输入指令代码：1
# 请输入联系人姓名: 刘德华
# 该联系人不存在！
# 请输入指令代码：2
# 请输入联系人姓名:刘德华
# 请输入联系人电话：136XXXXXXX 联系人加入成功！
# 请输入指令代码：2
# 请输入联系人姓名:杨幂
# 请输入联系人电话：177xxxxxxxxx 联系人加入成功！
# 请输入指令代码：1
# 请输入联系人姓名:杨幂
# 杨幂 : 177xxxxxxxxx
# 请输入指令代码：4
# |---感谢使用通讯录程序---|
# 使用字典构建通讯录
# 使用 while 循环一直判断是不是进行
# 使用 if 语句判断指令类型
addrBook = {}
print('|---欢迎进入通讯录程序---|')
print('|---1、 查询联系人资料---|')
print('|---2、 插入新的联系人---|')
print('|---3、 删除已有联系人---|')
print('|---4、 退出通讯录程序---|')
while True:
    i = input('请输入指令代码：')
    if '1' == i:
        name = input('请输入联系人姓名：')
        linkMan = addrBook.get(name)
        if None != linkMan:
            print(name + ':' + linkMan)
        else:
            print('该联系人不存在！')
    elif '2' == i:
        name = input('请输入联系人姓名：')
        if name in addrBook.keys():
            print("该联系人已存在")
        else:
            phone = input('请输入联系人电话：')
            addrBook.update({name: phone})
            print('联系人加入成功！')
    elif '3' == i:
        name = input('请输入联系人姓名：')
        if name in addrBook.keys():
            addrBook.pop(name)
            print('联系人删除成功！')
        else:
            print('你要删除的联系人不存在')
    elif '4' == i:
        print('|---感谢使用通讯录程序---|')
        break
    else:
        print('请输入1，2，3，4')

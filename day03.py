#定义变量并打印
my_name ="刘德华"
print (my_name)

'''''
整数运算
'''''
# 加法
add = 3 + 4
print('3+4的值是{}'.format(add))

# 减法
sub = 10 -8
print('10-8的值是{}'.format(sub))

# 乘法
multi = 23*3
print('23*3的值是{}'.format(multi))

# 除法
div = 10 / 2
print('10/2的值是{}'.format(div))

# 取模
delivery = 7%3
print('7%3的值是{}'.format(delivery))

# 取整除 返回商的整数
round_number =7//3
print('7//3的值是{}'.format(round_number))

# 幂运算
power = 7**3
print('7**3的值是{}'.format(power))

'''''
浮点数运算
'''''

# 加法
add = 0.2+0.1
print('0.2+0.1={}'.format(add))

# python3.6以上版本为了减少{},可以使用f'的方法
com = 'Complex'
comp = 'complicated'

# 3.6以下的用法
print('\n 3.6以下的用法')
print('{}is better than {}'.format(com,comp))

# 3.6以上的用法
print('\n 3.6以上用法')
print(f'{com} is better than {comp}')

# 减法
sub = 10.9-8.1
print(f'10.9-8.1的值是{sub}')

# 乘法
multi = 0.1*3
print(f'0.1*3={multi}')

# 除法
div = 10.0/2.0
print(f'10.0/2.0={div}')

# 取模
delivery = 7%4.3
print(f'7%4.3={delivery}')

# 取整除
round_number = 7//4.3
print(f'7//4.3={round_number}')

# 幂运算
power = 7**2.0
print(f'7**2.0={power}')

'''
布尔类型
'''

print(True and False)

'''
字符串
'''
# 转意字符串
command = 'Let\'s go!'
print('\n 使用转意字符串输出' ,command)

# 字符串的基本用法
# 添加空白 \n表示换行 \t表示制表符把文字空两格输出
print('\n 欢迎来到python的世界\t请留言')

# 连接字符串 +
log_1_str = 'hello'
log_2_str = 'python'
log_str = log_1_str + log_2_str
print('\n 拼接后的字符串是\t',log_str)

# 字符串运算
# 字符串大小写转换
welcome = "Hello,welcome to python"
# 将每个单词的首字母大写
print('\n 每个单词首字母大写',welcome.title())
# 段落的首字母大写
print('\n 段落的首字母大写',welcome.capitalize())
# 所有字母小写
print('\n 所有字母小写',welcome.lower())
# 所有字母大写
print('\n 所有字母大写',welcome.upper())
# 大小写互换
print('\n 大小写互换',welcome.swapcase())
# 判断字符串是否全部为数字或英文
print('\n 判断字符串是否全部为数字或英文',welcome.isalnum())
# 判断字符串是否全部为整数
print('\n 判断字符串是否全部为整数',welcome.isdigit())

# 字符串分割
string_example = 'Now is better than never'
# 分割
print('分割字符串',string_example.split())
# 按照某个字母分割
print('按照指定字母分割',string_example.split('n'))
# 去掉换行符
print('以换行符分割', '1+2\n+3+4'.splitlines())

# 删除两边空白
love_python = ' hello python '
print('去除两端空白',love_python.strip())
# 去除右侧空白
print('去除右侧空白',love_python.rstrip())
# 去除左侧空白
print('去除左侧空白',love_python.lstrip())

# 字符串切片 slice
print(love_python[3:5:1])

# 字符串编码
# encode("utf-8")

# 各种类型转换
number = 100
print('\n number的数据类型是',type(number))

# 将整数转换为浮点数
float_number = float(number)
print('\n number的数据类型是',type(number))

# 将整型转换为字符串
str_number = str(number)
print('str_number的类型是',type(str_number))
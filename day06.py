import os
# os.getcwd() # 获取当前目录
# os.listdir() #列出指定路径下文件或文件夹名字
# os.path.join() #拼接文件路径和文件名
# endswith()文件结尾
# os.rename() 重命名文件
# os.renames() 重命名文件+路径
# os.remove() 删除文件

print('目录为:',os.getcwd())
# 实战项目 删除指定文件
# 1.获取当前路径
path = os.getcwd()
# 2.创建几个文件
# file1 = os.path.join(path,'a.md')
open('a.md', 'w')
open('b.md', 'w')
open('c.md', 'w')
files = os.listdir(path)
# os.remove('a.md')
# os.remove(os.path.join(path,'b.md'))
print('执行删除前的文件')
print(files)
## 创建删除文件函数
def removeFile(*fileNames):
    for fileName in fileNames:
        if fileName in files:
            os.remove(fileName)
            print(fileName + '删除成功')
        else:
            print(fileName+'不存在')
# 调用函数删除a.md,b.md,c.md,1.txt
removeFile('a.md','b.md','c.md','1.txt')
# removeFile('a.md','b.md','c.md')
print('执行删除后的文件')
print(os.listdir(path))
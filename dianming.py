
#创建一个字典students，key是学号，value是姓名
# 学生信息在students.csv文件里，从文件中读取并保存到字典

# 打开students1.csv文件
file = open(r'C:\Users\Administrator\Desktop\students1.csv','r')
# 读取文件内容
lines = file.readlines()
# 抽取每行的学号和姓名，保存到字典
students = {}
for line in lines:
    tmp_list = line.split(',')
    xuehao = tmp_list[0]
    xingming = tmp_list[1]
    students[xuehao] = xingming

print(students)
# 从学号中随机抽取N个学号
import random
num = int(input("输入你要抽取的人数："))
#如何把字典中的key(学号)取成列表
students.keys()
xuehao_list = random.sample(students.keys(),num)
xuehao_list
# 根据随机抽取的学号，打印输出对应的姓名
for xuehao in xuehao_list:
    print(students[xuehao])
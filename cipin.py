# 整合代码，输出py文件
# 打开并读取文件
file = open(r"C:\Users\Administrator\Desktop\Walden.txt",'r')
lines = file.readlines()      #列表
# 要把每行拆成单词
words = []

for line in lines:
    tmp_list = line.split()
    for word in tmp_list:
        words.append(word.replace(',','').replace('.','').replace('"','').replace('!','').replace('?','').replace(':','') )
words
# 对words中每一个元素计算出他出现的个数
# 把统计结果保存到字典中，字典的key是单词，value是出现次数
word_count = {}
word_set = set(words)
for word in word_set:
    count_num = words.count(word)
    word_count[word] = count_num

print(word_count)
# 对word_count字典进行排序，按照出现的次数（value）进行排序
sorted(word_count.items(),key=lambda item:item[1],reverse=True)
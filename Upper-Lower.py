ifn = 'E:\\infile.txt'
ofn = 'e:\\Outfile.txt'

outfile = open(ofn,'w')
outfile.truncate()
outfile.close()

strList = []
words = input("请输入内容(单独输入'q'保存退出):\n")
while words != 'q':
    line = strList.append(words)
    words = input()


strings = "\n".join(strList)

infile = open(ifn,'w')
infile.write(strings)
infile.close()

infile = open(ifn,'r')
outfile = open(ofn,'w')
lines = []
for line in infile:
	lines = line.lower()
	for temp in lines:
		outfile.write(temp)

infile.close()
outfile.close()

print('\n\n以下是已经转换的字符串：\n\n')
for line in open('e:\\Outfile.txt'):
	print(line,end = '')

print('\n\n\n请复制已经转换的字符串后，按回车键退出')
input()
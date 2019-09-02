''' Create new file '''
'''
with open("Mytext.txt",'w+')as f:
    f.writelines('hello world')
    f.writelines('\nline2')


# print contents of file

with open("Mytext.txt" , 'r') as f:
    for line in f.readlines():
        print(line)

'''


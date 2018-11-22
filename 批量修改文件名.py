import os
print('输入需要改名的文件夹路径,如 C:\\新建文件夹')
try:
    path=input()
    nameList=os.listdir(path)
    os.chdir(path)
    print('文件名列表如下：')
    for k in range(len(nameList)):
        print(nameList[k])
except:
    print('报错，请检查输入的路径，随后重新运行')
else:
    while True:
        print('\n输入变更后的文件名,以空格区分,加上拓展名，如 AAA.txt BBB.doc CCC.xls DDDD.ppt')
        a=input()
        nameList_new=a.split(' ')
        if len(nameList)!=len(nameList_new):
            print('原文件名与新文件名数量不符，请核实')
        else:
            break
    for i in range(len(nameList)):
        os.rename(nameList[i],nameList_new[i])
    print('文件名已更新，新的文件名列表如下：')
    for n in range(len(nameList_new)):
        print(os.listdir(path)[n])

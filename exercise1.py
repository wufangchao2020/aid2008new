# 现在我们要做一个电子书的翻页功能
# 一种是:自动翻页  3s翻一页,每次的量,是3行的内容
# 另外一种是:手动翻页  当按某个键时,开始翻页
# 提示:让用户自行选择,是自动翻页,还是手动翻页

import time

with open('wjbk', 'r') as f:
    # 首先要确定有多少个字节总共
    f.seek(0, 2)
    # 把文件末尾的指针,记录下的字节量来
    end = f.tell()
    # 此时再将光标放到开始
    f.seek(0, 0)
    auto = input('是否开启自动翻页y/n:')
    if auto == 'y':
        while True:
            for item in range(3):
                print(f.readline())
            time.sleep(2)
            if f.tell() == end:
                print('电子书看完了,你真棒!!!')
                break
    else:
        con = 'n'
        while True:
            if con == 'n':
                for item in range(3):
                    print(f.readline())
            else:
                print('请输入n')
            if f.tell()== end:
                break
            con = input('请输入n翻页:')
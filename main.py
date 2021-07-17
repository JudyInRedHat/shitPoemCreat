"""
关于此作品：
生草！生草！生草!
真心不知道是哪个家伙想出来让程序写诗这作品的
所以就有这玩意了！
准备哈哈大笑吧！
"""
#导入库
from tkinter import *
from random import *
#——————————————函数区———————————————
def creatPoem():
    #初始化所有的词语内容
    name = ["你","我","他","它","她","程序员","学生","老师","校长","警察","小麻将","红帽","某人","海文","杀人魔","傻子"]
    place = ["家里","尧山里","老家","朋友家","猪窝","办公室","学校","讲台上","主席台","警察局","社区里","某人家里","某地","大庆","漫展","神经病院"]
    do = ["玩电脑","肝作品","做一个好哥哥","蹦迪","吃猪粮","敲代码","讲课","讲一堆废话","执行正义","鸽子","聊天","上课","做某事","生病","炫富","发癫"]
    #连接四句诗
    for i in range(4):
        PoemLine[i].set(name[randint(0,15)]+"在"+place[randint(0,15)]+do[randint(0,15)]+"。")
#——————————————分割线———————————————
#建立窗口
window = Tk()
#设置窗口的长宽
window.geometry("600x600")
#设置窗口标题和图标
window.title("生草诗句生成器")
window.iconbitmap("icon.ico")
#初始化var列表
PoemLine = []
for i in range(4):
    PoemLine.append(StringVar())
#初始化诗句内容为省略号，然后放置它
PoemLine[0].set("……")
poemList = []
for Line in PoemLine:
    poemList.append(Label(window,textvariable=Line))
for thing in poemList:
    thing.pack()
#设置生成诗句的按钮并显示
creat = Button(window,text="点我生成诗句",command=creatPoem)
creat.pack()
#显示窗口
window.mainloop()
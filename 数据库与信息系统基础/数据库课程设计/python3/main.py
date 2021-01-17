# -*-coding:gbk-*-

from tkinter import *
import tkinter.messagebox as message
import excuate
import jygl
import jhtj
import xstj
import yjck
import cksjb


top2 = Tk()
top2.geometry("600x400+500+300")
top2.title('销售管理信息系统 v1.0')
mainmenu = Menu(top2)
menu_jygl = Menu(mainmenu)
mainmenu.add_cascade(label="交易管理", menu=menu_jygl)
menu_jygl.add_command(label="进货登记", command=jygl._jhdj)
menu_jygl.add_command(label="销售登记", command=jygl._xsdj)
menu_jygl.add_command(label="退货登记", command=jygl._thdj)

menu_jhtj = Menu(mainmenu)
mainmenu.add_cascade(label="进货统计", menu=menu_jhtj)
menu_jhtj.add_command(label="今日进货量", command=jhtj._jrjh)
menu_jhtj.add_command(label="本月进货量", command=jhtj._byjh)
menu_jhtj.add_command(label="本季度进货量", command=jhtj._jdjh)
menu_jhtj.add_command(label="今年进货量", command=jhtj._jnjh)

menu_xstj = Menu(mainmenu)
mainmenu.add_cascade(label="销售统计", menu=menu_xstj)
menu_xstj.add_command(label="今日销售量", command=xstj._jrxs)
menu_xstj.add_command(label="本月销售量", command=xstj._byxs)
menu_xstj.add_command(label="本季度销售量", command=xstj._jdxs)
menu_xstj.add_command(label="今年销售量",command=xstj._jnxs)

menu_yjck = Menu(mainmenu)
mainmenu.add_cascade(label="业绩查看", menu=menu_yjck)
menu_yjck.add_command(label="业绩查看", command=yjck._yjck)

menu_cksjb = Menu(mainmenu)
mainmenu.add_cascade(label="查看数据表", menu=menu_cksjb)
menu_cksjb.add_command(label="现存货表", command=cksjb._xchb)
menu_cksjb.add_command(label="已售商品表", command=cksjb._scys)
menu_cksjb.add_command(label="退货表", command=cksjb._xsth)
menu_cksjb.add_command(label="员工表", command=cksjb._xsyg)
menu_cksjb.add_command(label="进货商表",command=cksjb._jhsb)

png = PhotoImage(file='0.png')
Label(image=png).pack()

top2.config(menu=mainmenu)
top2.withdraw()


def _load():
    char = "SELECT 密码 FROM userdb WHERE 用户名 = '%s'" % usertext.get()
    findp = excuate.cal_r(char)
    findu = excuate.cal_r("SELECT 用户名 FROM userdb")
    y = []
    for x in findu:
        y.append(x[0])

    if usertext.get() in y:
        if pwtext.get() == findp[0][0]:
            message.showinfo('提示', '登陆成功！')
            usertext.delete(0, END)
            pwtext.delete(0, END)
            top.destroy()
            top2.update()
            top2.deiconify()
        else:
            message.showerror('提示','用户名或密码错误！')
            usertext.delete(0, END)
            pwtext.delete(0, END)
    else:
        message.showerror('提示', '用户名或密码错误！')
        usertext.delete(0, END)
        pwtext.delete(0, END)

def _adduser():
    def _add():
        if add_pw.get() != add_pw2.get():
            message.showerror('错误', '两次密码输入不一致！')
            add_pw.delete(0, END)
            add_pw2.delete(0, END)
        else:
            char = "INSERT INTO userdb(用户名,密码) VALUES ('%s','%s')" % (add_user.get(),add_pw.get())
            excuate.cal_nr(char)
            message.showinfo('提示', '注册成功！')
            add_win.destroy()

    add_win = Toplevel(top)
    add_win.title('用户注册')
    add_win.geometry("300x150+500+300")
    Label(add_win, text="新账户名称：").place(x=12, y=20)
    Label(add_win, text="请输入密码：").place(x=12, y=50)
    Label(add_win, text="请确认密码：").place(x=12, y=80)
    Button(add_win, text="确定", width=30, command=_add).place(x=16, y=120)
    add_user = Entry(add_win)
    add_pw = Entry(add_win)
    add_pw2 = Entry(add_win)
    add_user.place(x=100, y=20)
    add_pw.place(x=100, y=50)
    add_pw2.place(x=100, y=80)

def _changepw():
    def _change():
        char = "SELECT 密码 FROM userdb WHERE 用户名 = '%s'" % change_user.get()
        findp = excuate.cal_r(char)
        findu = excuate.cal_r("SELECT 用户名 FROM userdb")
        y = []
        for x in findu:
            y.append(x[0])

        if change_user.get() in y:
            if change_pw_b.get() == findp[0][0]:
                if change_pw_n1.get() != change_pw_n2.get():
                    message.showerror('错误', '两次密码输入不一致！')
                    change_pw_n1.delete(0, END)
                    change_pw_n2.delete(0, END)
                else:
                    char = "UPDATE userdb SET 密码 = '%s' WHERE 用户名 = '%s'" % (change_pw_n1.get(),change_user.get())
                    excuate.cal_nr(char)
                    message.showinfo('提示', '修改成功！')
                    change_win.destroy()
            else:
                message.showerror('错误', '原密码输入错误！')
                change_pw_b.delete(0, END)
        else:
            message.showerror('错误', '该用户不存在！')
            change_user.delete(0, END)
            change_pw_b.delete(0, END)

    change_win = Toplevel(top)
    change_win.title('修改密码')
    change_win.geometry("300x190+500+300")
    Label(change_win, text="您的账户名称：").place(x=10, y=20)
    Label(change_win, text="输入您的密码：").place(x=10, y=50)
    Label(change_win, text="输入新的密码：").place(x=10, y=80)
    Label(change_win, text="再次输入密码：").place(x=10, y=110)
    Button(change_win, text="确定", width=30, command=_change).place(x=16, y=152)
    change_user = Entry(change_win)
    change_pw_b = Entry(change_win)
    change_pw_n1 = Entry(change_win)
    change_pw_n2 = Entry(change_win)
    change_user.place(x=100, y=20)
    change_pw_b.place(x=100, y=50)
    change_pw_n1.place(x=100, y=80)
    change_pw_n2.place(x=100, y=110)

top = Tk()
top.geometry("400x220+500+300")
top.title('销售管理信息系统登陆')

lab1 = Label(top,
             text="用户名：",
             font=("黑体", 14),
             width=10,
             height=2,
             anchor="e")
lab2 = Label(top,
             text="密  码：",
             font=("黑体", 14),
             width=10,
             anchor="e",
             height=2)
lab3 = Label(top,
             text="销售管理信息系统",
             font=("黑体", 30),
             height=3
             ).pack()
usertext = Entry(top)
pwtext = Entry(top, show='*')

load = Button(top, text="登陆", width=6, height=3, command=_load)
addu = Button(top, text="添加用户", command=_adduser)
repw = Button(top, text="修改密码", command=_changepw)

lab1.place(x=22,y=100)
lab2.place(x=22,y=130)
usertext.place(x=102, y=105)
pwtext.place(x=102, y=135)
load.place(x=299, y=108)
addu.place(x=80, y=172)
repw.place(x=255, y=172)

top.mainloop()

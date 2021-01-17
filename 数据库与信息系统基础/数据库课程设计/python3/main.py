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
top2.title('���۹�����Ϣϵͳ v1.0')
mainmenu = Menu(top2)
menu_jygl = Menu(mainmenu)
mainmenu.add_cascade(label="���׹���", menu=menu_jygl)
menu_jygl.add_command(label="�����Ǽ�", command=jygl._jhdj)
menu_jygl.add_command(label="���۵Ǽ�", command=jygl._xsdj)
menu_jygl.add_command(label="�˻��Ǽ�", command=jygl._thdj)

menu_jhtj = Menu(mainmenu)
mainmenu.add_cascade(label="����ͳ��", menu=menu_jhtj)
menu_jhtj.add_command(label="���ս�����", command=jhtj._jrjh)
menu_jhtj.add_command(label="���½�����", command=jhtj._byjh)
menu_jhtj.add_command(label="�����Ƚ�����", command=jhtj._jdjh)
menu_jhtj.add_command(label="���������", command=jhtj._jnjh)

menu_xstj = Menu(mainmenu)
mainmenu.add_cascade(label="����ͳ��", menu=menu_xstj)
menu_xstj.add_command(label="����������", command=xstj._jrxs)
menu_xstj.add_command(label="����������", command=xstj._byxs)
menu_xstj.add_command(label="������������", command=xstj._jdxs)
menu_xstj.add_command(label="����������",command=xstj._jnxs)

menu_yjck = Menu(mainmenu)
mainmenu.add_cascade(label="ҵ���鿴", menu=menu_yjck)
menu_yjck.add_command(label="ҵ���鿴", command=yjck._yjck)

menu_cksjb = Menu(mainmenu)
mainmenu.add_cascade(label="�鿴���ݱ�", menu=menu_cksjb)
menu_cksjb.add_command(label="�ִ����", command=cksjb._xchb)
menu_cksjb.add_command(label="������Ʒ��", command=cksjb._scys)
menu_cksjb.add_command(label="�˻���", command=cksjb._xsth)
menu_cksjb.add_command(label="Ա����", command=cksjb._xsyg)
menu_cksjb.add_command(label="�����̱�",command=cksjb._jhsb)

png = PhotoImage(file='0.png')
Label(image=png).pack()

top2.config(menu=mainmenu)
top2.withdraw()


def _load():
    char = "SELECT ���� FROM userdb WHERE �û��� = '%s'" % usertext.get()
    findp = excuate.cal_r(char)
    findu = excuate.cal_r("SELECT �û��� FROM userdb")
    y = []
    for x in findu:
        y.append(x[0])

    if usertext.get() in y:
        if pwtext.get() == findp[0][0]:
            message.showinfo('��ʾ', '��½�ɹ���')
            usertext.delete(0, END)
            pwtext.delete(0, END)
            top.destroy()
            top2.update()
            top2.deiconify()
        else:
            message.showerror('��ʾ','�û������������')
            usertext.delete(0, END)
            pwtext.delete(0, END)
    else:
        message.showerror('��ʾ', '�û������������')
        usertext.delete(0, END)
        pwtext.delete(0, END)

def _adduser():
    def _add():
        if add_pw.get() != add_pw2.get():
            message.showerror('����', '�����������벻һ�£�')
            add_pw.delete(0, END)
            add_pw2.delete(0, END)
        else:
            char = "INSERT INTO userdb(�û���,����) VALUES ('%s','%s')" % (add_user.get(),add_pw.get())
            excuate.cal_nr(char)
            message.showinfo('��ʾ', 'ע��ɹ���')
            add_win.destroy()

    add_win = Toplevel(top)
    add_win.title('�û�ע��')
    add_win.geometry("300x150+500+300")
    Label(add_win, text="���˻����ƣ�").place(x=12, y=20)
    Label(add_win, text="���������룺").place(x=12, y=50)
    Label(add_win, text="��ȷ�����룺").place(x=12, y=80)
    Button(add_win, text="ȷ��", width=30, command=_add).place(x=16, y=120)
    add_user = Entry(add_win)
    add_pw = Entry(add_win)
    add_pw2 = Entry(add_win)
    add_user.place(x=100, y=20)
    add_pw.place(x=100, y=50)
    add_pw2.place(x=100, y=80)

def _changepw():
    def _change():
        char = "SELECT ���� FROM userdb WHERE �û��� = '%s'" % change_user.get()
        findp = excuate.cal_r(char)
        findu = excuate.cal_r("SELECT �û��� FROM userdb")
        y = []
        for x in findu:
            y.append(x[0])

        if change_user.get() in y:
            if change_pw_b.get() == findp[0][0]:
                if change_pw_n1.get() != change_pw_n2.get():
                    message.showerror('����', '�����������벻һ�£�')
                    change_pw_n1.delete(0, END)
                    change_pw_n2.delete(0, END)
                else:
                    char = "UPDATE userdb SET ���� = '%s' WHERE �û��� = '%s'" % (change_pw_n1.get(),change_user.get())
                    excuate.cal_nr(char)
                    message.showinfo('��ʾ', '�޸ĳɹ���')
                    change_win.destroy()
            else:
                message.showerror('����', 'ԭ�����������')
                change_pw_b.delete(0, END)
        else:
            message.showerror('����', '���û������ڣ�')
            change_user.delete(0, END)
            change_pw_b.delete(0, END)

    change_win = Toplevel(top)
    change_win.title('�޸�����')
    change_win.geometry("300x190+500+300")
    Label(change_win, text="�����˻����ƣ�").place(x=10, y=20)
    Label(change_win, text="�����������룺").place(x=10, y=50)
    Label(change_win, text="�����µ����룺").place(x=10, y=80)
    Label(change_win, text="�ٴ��������룺").place(x=10, y=110)
    Button(change_win, text="ȷ��", width=30, command=_change).place(x=16, y=152)
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
top.title('���۹�����Ϣϵͳ��½')

lab1 = Label(top,
             text="�û�����",
             font=("����", 14),
             width=10,
             height=2,
             anchor="e")
lab2 = Label(top,
             text="��  �룺",
             font=("����", 14),
             width=10,
             anchor="e",
             height=2)
lab3 = Label(top,
             text="���۹�����Ϣϵͳ",
             font=("����", 30),
             height=3
             ).pack()
usertext = Entry(top)
pwtext = Entry(top, show='*')

load = Button(top, text="��½", width=6, height=3, command=_load)
addu = Button(top, text="����û�", command=_adduser)
repw = Button(top, text="�޸�����", command=_changepw)

lab1.place(x=22,y=100)
lab2.place(x=22,y=130)
usertext.place(x=102, y=105)
pwtext.place(x=102, y=135)
load.place(x=299, y=108)
addu.place(x=80, y=172)
repw.place(x=255, y=172)

top.mainloop()

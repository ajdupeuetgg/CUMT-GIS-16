# -*-coding:gbk-*-

from tkinter import *
import tkinter.messagebox as message
import tkinter.ttk as ttk
import excuate

def _jhdj():
    def _clearsp():
        text_spmc.delete(0, END)
        text_sccs.delete(0, END)
        text_xh.delete(0, END)
        text_dj.delete(0, END)
        text_sl.delete(0, END)
        text_j_n.delete(0, END)
        text_j_y.delete(0, END)
        text_j_r.delete(0, END)
        text_ywybh.delete(0, END)

    def _clearcs():
        text_csmc.delete(0, END)
        text_frdb.delete(0, END)
        text_dh.delete(0, END)
        text_csdz.delete(0, END)

    def _insertsp():
        if text_sccs.get():
            pass
        else:
            message.showerror('��ʾ','��ѡ���������̣�')
            return
        if text_spmc.get():
            pass
        else:
            message.showerror('��ʾ','��������Ʒ���ƣ�')
            return
        if text_xh.get():
            pass
        else:
            message.showerror('��ʾ','�������ͺţ�')
            return
        if text_dj.get():
            pass
        else:
            message.showerror('��ʾ','�����뵥�ۣ�')
            return
        if text_sl.get():
            pass
        else:
            message.showerror('��ʾ','������������')
            return
        if text_j_n.get():
            pass
        else:
            message.showerror('��ʾ','�����������ݣ�')
            return
        if text_j_y.get():
            pass
        else:
            message.showerror('��ʾ', '����������·ݣ�')
            return
        if text_j_r.get():
            pass
        else:
            message.showerror('��ʾ', '����������գ�')
            return
        if text_ywybh.get():
            pass
        else:
            message.showerror('��ʾ', '��ѡ��ҵ��Ա��ţ�')
            return
        char = """INSERT INTO goods(��������,��Ʒ��,�ͺ�,����,����,�ܽ��,������,������,������,ҵ��Ա���)
                  VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            text_sccs.get(),text_spmc.get(),text_xh.get(),text_dj.get(),text_sl.get(),
            int(text_dj.get())*int(text_sl.get()),text_j_n.get(),text_j_y.get(),text_j_r.get(),text_ywybh.get())
        excuate.cal_nr(char)
        message.showinfo('��ʾ', '����ɹ���')
        _clearsp()

    def _insertcs():
        char = """INSERT INTO manufacturer(��������,���˴���,���̵�ַ,�绰)
                  VALUES ('%s','%s','%s','%s')""" % (
            text_csmc.get(),text_frdb.get(),text_csdz.get(),text_dh.get())
        excuate.cal_nr(char)
        message.showinfo('��ʾ', '����ɹ���')
        _clearcs()
    
    jy_jh_win = Tk()
    jy_jh_win.geometry("450x490+600+200")
    jy_jh_win.title('�����Ʒ���')

    frame_tjsp = LabelFrame(jy_jh_win, text="�����Ʒ", labelanchor="nw")
    frame_tjsp.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.45)

    Label(frame_tjsp, text="��Ʒ��ţ�").place(relx=0.03, rely=0.03)
    text_spbh = Entry(frame_tjsp, width=8)
    text_spbh.insert(0, '�Զ����')
    text_spbh.place(relx=0.28, rely=0.03)

    Label(frame_tjsp, text="��Ʒ���ƣ�").place(relx=0.49, rely=0.03)
    text_spmc = Entry(frame_tjsp, width=8)
    text_spmc.place(relx=0.69, rely=0.03)

    Label(frame_tjsp, text="�������̣�").place(relx=0.03, rely=0.2)
    val1 = excuate.fet_list("��������","manufacturer")
    text_sccs = ttk.Combobox(frame_tjsp, width=6, values=val1)
    text_sccs.place(relx=0.28, rely=0.2)

    Label(frame_tjsp, text="�ͺţ�").place(relx=0.49, rely=0.2)
    text_xh = Entry(frame_tjsp, width=8)
    text_xh.place(relx=0.69, rely=0.2)

    Label(frame_tjsp, text="���ۣ�").place(relx=0.03, rely=0.37)
    text_dj = Entry(frame_tjsp, width=8)
    text_dj.place(relx=0.28, rely=0.37)

    Label(frame_tjsp, text="������").place(relx=0.49, rely=0.37)
    text_sl = Entry(frame_tjsp, width=8)
    text_sl.place(relx=0.69, rely=0.37)

    Label(frame_tjsp, text="�������ڣ�").place(relx=0.03, rely=0.53)
    text_j_n = Entry(frame_tjsp, width=3)
    text_j_n.place(relx=0.28, rely=0.53)
    Label(frame_tjsp, text="��").place(relx=0.38, rely=0.53)
    text_j_y = Entry(frame_tjsp, width=3)
    text_j_y.place(relx=0.46, rely=0.53)
    Label(frame_tjsp, text="��").place(relx=0.58, rely=0.53)
    text_j_r = Entry(frame_tjsp, width=3)
    text_j_r.place(relx=0.64, rely=0.53)
    Label(frame_tjsp, text="��").place(relx=0.78, rely=0.53)

    Label(frame_tjsp, text="ҵ��Ա��ţ�").place(relx=0.03, rely=0.69)
    val2 = excuate.fet_list("Ա�����","employee")
    text_ywybh = ttk.Combobox(frame_tjsp, width=4, values=val2)
    text_ywybh.place(relx=0.31, rely=0.69)

    Label(frame_tjsp, text="�ܽ�").place(relx=0.49, rely=0.69)
    text_zje = Entry(frame_tjsp, width=6)
    text_zje.place(relx=0.69, rely=0.69)
    text_zje.insert(0, '�Զ�����')

    tjrk_but = Button(frame_tjsp, text="������", width=8, command=_insertsp)
    tjrk_but.place(relx=0.2, rely=0.85)

    tjrk_but = Button(frame_tjsp, text="�������", width=8, command=_clearsp)
    tjrk_but.place(relx=0.58, rely=0.85)


    frame_tjcs = LabelFrame(jy_jh_win, text="��ӳ���", labelanchor="nw")
    frame_tjcs.place(relx=0.05, rely=0.50, relwidth=0.9, relheight=0.45)

    Label(frame_tjcs, text="�������ƣ�").place(relx=0.03, rely=0.03)
    text_csmc = Entry(frame_tjcs, width=24)
    text_csmc.place(relx=0.31, rely=0.03)

    Label(frame_tjcs, text="���˴���").place(relx=0.03, rely=0.23)
    text_frdb = Entry(frame_tjcs, width=24)
    text_frdb.place(relx=0.31, rely=0.23)

    Label(frame_tjcs, text="�绰��").place(relx=0.03, rely=0.47)
    text_dh = Entry(frame_tjcs, width=24)
    text_dh.place(relx=0.31, rely=0.47)

    Label(frame_tjcs, text="���̵�ַ��").place(relx=0.03, rely=0.68)
    text_csdz = Entry(frame_tjcs, width=24)
    text_csdz.place(relx=0.31, rely=0.68)

    tjrk_but = Button(frame_tjcs, text="������", width=8, command=_insertcs)
    tjrk_but.place(relx=0.2, rely=0.85)

    tjrk_but = Button(frame_tjcs, text="�������", width=8, command=_clearcs)
    tjrk_but.place(relx=0.58, rely=0.85)

def _xsdj():
    def _clearsp():
        text_spmc.delete(0, END)
        text_sccs.delete(0, END)
        text_xh.delete(0, END)
        text_dj.delete(0, END)
        text_sl.delete(0, END)
        text_j_n.delete(0, END)
        text_j_y.delete(0, END)
        text_j_r.delete(0, END)
        text_ywybh.delete(0, END)

    def _sellsp():
        if text_sccs.get():
            pass
        else:
            message.showerror('��ʾ','��ѡ���������̣�')
            return
        if text_spmc.get():
            pass
        else:
            message.showerror('��ʾ','��������Ʒ���ƣ�')
            return
        if text_xh.get():
            pass
        else:
            message.showerror('��ʾ','�������ͺţ�')
            return
        if text_dj.get():
            pass
        else:
            message.showerror('��ʾ','�����뵥�ۣ�')
            return
        if text_sl.get():
            pass
        else:
            message.showerror('��ʾ','������������')
            return
        if text_j_n.get():
            pass
        else:
            message.showerror('��ʾ','������������ݣ�')
            return
        if text_j_y.get():
            pass
        else:
            message.showerror('��ʾ', '�����������·ݣ�')
            return
        if text_j_r.get():
            pass
        else:
            message.showerror('��ʾ', '�����������գ�')
            return
        if text_ywybh.get():
            pass
        else:
            message.showerror('��ʾ', '��ѡ��ҵ��Ա��ţ�')
            return

        val3 = excuate.fet_list("��Ʒ��", "goods")
        if text_spmc.get() in val3:
            num_goods = excuate.cal_r("SELECT ���� FROM goods WHERE ��Ʒ�� = '%s'" % text_spmc.get())
            num = num_goods[0][0] - int(text_sl.get())
            if num >= 0:
                char1 = """INSERT INTO sell (��������,��Ʒ��,�ͺ�,����,����,�ܽ��,������,������,������,ҵ��Ա���)
                                  VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
                    text_sccs.get(), text_spmc.get(), text_xh.get(), text_dj.get(), text_sl.get(),
                    int(text_dj.get()) * int(text_sl.get()), text_j_n.get(), text_j_y.get(), text_j_r.get(),
                    text_ywybh.get())
                excuate.cal_nr(char1)

                char2 = "UPDATE goods SET ���� = '%s' WHERE ��Ʒ�� = '%s'" % (
                    num, text_spmc.get())
                excuate.cal_nr(char2)

                message.showinfo('��ʾ', '�������ۼ�¼�ɹ���')
                _clearsp()
            else:
                message.showerror('����', 'ʣ���Ʒ�������㣡')
                text_sl.delete(0, END)
        else:
            message.showerror('����', 'û�и�����Ʒ��')
            _clearsp()

    jy_xs_win = Tk()
    jy_xs_win.geometry("450x290+600+200")
    jy_xs_win.title("���۵Ǽ�")

    Label(jy_xs_win, text="��Ʒ��ţ�").place(relx=0.03, rely=0.03)
    text_spbh = Entry(jy_xs_win, width=8)
    text_spbh.insert(0, '�Զ����')
    text_spbh.place(relx=0.28, rely=0.03)

    Label(jy_xs_win, text="��Ʒ���ƣ�").place(relx=0.49, rely=0.03)
    text_spmc = Entry(jy_xs_win, width=8)
    text_spmc.place(relx=0.69, rely=0.03)

    Label(jy_xs_win, text="�������̣�").place(relx=0.03, rely=0.2)
    val1 = excuate.fet_list("��������", "manufacturer")
    text_sccs = ttk.Combobox(jy_xs_win, width=6, values=val1)
    text_sccs.place(relx=0.28, rely=0.2)

    Label(jy_xs_win, text="�ͺţ�").place(relx=0.49, rely=0.2)
    text_xh = Entry(jy_xs_win, width=8)
    text_xh.place(relx=0.69, rely=0.2)

    Label(jy_xs_win, text="���ۣ�").place(relx=0.03, rely=0.37)
    text_dj = Entry(jy_xs_win, width=8)
    text_dj.place(relx=0.28, rely=0.37)

    Label(jy_xs_win, text="������").place(relx=0.49, rely=0.37)
    text_sl = Entry(jy_xs_win, width=8)
    text_sl.place(relx=0.69, rely=0.37)

    Label(jy_xs_win, text="�������ڣ�").place(relx=0.03, rely=0.53)
    text_j_n = Entry(jy_xs_win, width=3)
    text_j_n.place(relx=0.28, rely=0.53)
    Label(jy_xs_win, text="��").place(relx=0.38, rely=0.53)
    text_j_y = Entry(jy_xs_win, width=3)
    text_j_y.place(relx=0.46, rely=0.53)
    Label(jy_xs_win, text="��").place(relx=0.58, rely=0.53)
    text_j_r = Entry(jy_xs_win, width=3)
    text_j_r.place(relx=0.64, rely=0.53)
    Label(jy_xs_win, text="��").place(relx=0.78, rely=0.53)

    Label(jy_xs_win, text="ҵ��Ա��ţ�").place(relx=0.03, rely=0.69)
    val2 = excuate.fet_list("Ա�����", "employee")
    text_ywybh = ttk.Combobox(jy_xs_win, width=4, values=val2)
    text_ywybh.place(relx=0.31, rely=0.69)

    Label(jy_xs_win, text="�ܽ�").place(relx=0.49, rely=0.69)
    text_zje = Entry(jy_xs_win, width=6)
    text_zje.place(relx=0.69, rely=0.69)
    text_zje.insert(0, '�Զ�����')

    tjrk_but = Button(jy_xs_win, text="����", width=8, command=_sellsp)
    tjrk_but.place(relx=0.2, rely=0.85)

    tjrk_but = Button(jy_xs_win, text="�������", width=8, command=_clearsp)
    tjrk_but.place(relx=0.58, rely=0.85)

def _thdj():
    def _clearsp():
        text_spmc.delete(0, END)
        text_sccs.delete(0, END)
        text_xh.delete(0, END)
        text_dj.delete(0, END)
        text_sl.delete(0, END)
        text_j_n.delete(0, END)
        text_j_y.delete(0, END)
        text_j_r.delete(0, END)
        text_ywybh.delete(0, END)

    def _retreatsp():
        if text_sccs.get():
            pass
        else:
            message.showerror('��ʾ','��ѡ���������̣�')
            return
        if text_spmc.get():
            pass
        else:
            message.showerror('��ʾ','��������Ʒ���ƣ�')
            return
        if text_xh.get():
            pass
        else:
            message.showerror('��ʾ','�������ͺţ�')
            return
        if text_dj.get():
            pass
        else:
            message.showerror('��ʾ','�����뵥�ۣ�')
            return
        if text_sl.get():
            pass
        else:
            message.showerror('��ʾ','������������')
            return
        if text_j_n.get():
            pass
        else:
            message.showerror('��ʾ','�������˻���ݣ�')
            return
        if text_j_y.get():
            pass
        else:
            message.showerror('��ʾ', '�������˻��·ݣ�')
            return
        if text_j_r.get():
            pass
        else:
            message.showerror('��ʾ', '�������˻��գ�')
            return
        if text_ywybh.get():
            pass
        else:
            message.showerror('��ʾ', '��ѡ��ҵ��Ա��ţ�')
            return

        val3 = excuate.fet_list("��Ʒ��", "sell")
        if text_spmc.get() in val3:
            val4 = excuate.fet_list("��Ʒ��", "retreat")
            if text_spmc.get() in val4:
                num_retreat = excuate.cal_r("SELECT ���� FROM retreat WHERE ��Ʒ�� = '%s'" % text_spmc.get())
                numm = num_retreat[0][0] + int(text_sl.get())
                char3 = "UPDATE retreat SET ���� = '%s' WHERE ��Ʒ�� = '%s'" % (
                    numm,text_spmc.get())
                excuate.cal_nr(char3)
            else:
                char1 = """INSERT INTO retreat (����,��Ʒ��,�ͺ�,����,����,�ܽ��,�˻���,�˻���,�˻���,ҵ��Ա���)
                                            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
                    text_sccs.get(), text_spmc.get(), text_xh.get(), text_dj.get(), text_sl.get(),
                    int(text_dj.get()) * int(text_sl.get()), text_j_n.get(), text_j_y.get(), text_j_r.get(),
                    text_ywybh.get())
                excuate.cal_nr(char1)

            num_sell = excuate.cal_r("SELECT ���� FROM sell WHERE ��Ʒ�� = '%s'" % text_spmc.get())
            num = num_sell[0][0] - int(text_sl.get())

            char2 = "UPDATE sell SET ���� = '%s' WHERE ��Ʒ�� = '%s'" % (
                num, text_spmc.get())
            excuate.cal_nr(char2)

            num_goods = excuate.cal_r("SELECT ���� FROM goods WHERE ��Ʒ�� = '%s'" % text_spmc.get())
            nummb = num_goods[0][0] + int(text_sl.get())

            char2 = "UPDATE goods SET ���� = '%s' WHERE ��Ʒ�� = '%s'" % (
                nummb, text_spmc.get())
            excuate.cal_nr(char2)

            message.showinfo('��ʾ', '�����˻���¼�ɹ���')
            _clearsp()
        else:
            message.showerror('����', 'û���۳���������Ʒ��')
            _clearsp()



    jy_th_win = Tk()
    jy_th_win.geometry("450x290+600+200")
    jy_th_win.title("�˻��Ǽ�")

    Label(jy_th_win, text="��Ʒ��ţ�").place(relx=0.03, rely=0.03)
    text_spbh = Entry(jy_th_win, width=8)
    text_spbh.insert(0, '�Զ����')
    text_spbh.place(relx=0.28, rely=0.03)

    Label(jy_th_win, text="��Ʒ���ƣ�").place(relx=0.49, rely=0.03)
    text_spmc = Entry(jy_th_win, width=8)
    text_spmc.place(relx=0.69, rely=0.03)

    Label(jy_th_win, text="�������̣�").place(relx=0.03, rely=0.2)
    val1 = excuate.fet_list("��������", "manufacturer")
    text_sccs = ttk.Combobox(jy_th_win, width=6, values=val1)
    text_sccs.place(relx=0.28, rely=0.2)

    Label(jy_th_win, text="�ͺţ�").place(relx=0.49, rely=0.2)
    text_xh = Entry(jy_th_win, width=8)
    text_xh.place(relx=0.69, rely=0.2)

    Label(jy_th_win, text="���ۣ�").place(relx=0.03, rely=0.37)
    text_dj = Entry(jy_th_win, width=8)
    text_dj.place(relx=0.28, rely=0.37)

    Label(jy_th_win, text="������").place(relx=0.49, rely=0.37)
    text_sl = Entry(jy_th_win, width=8)
    text_sl.place(relx=0.69, rely=0.37)

    Label(jy_th_win, text="�˻����ڣ�").place(relx=0.03, rely=0.53)
    text_j_n = Entry(jy_th_win, width=3)
    text_j_n.place(relx=0.28, rely=0.53)
    Label(jy_th_win, text="��").place(relx=0.38, rely=0.53)
    text_j_y = Entry(jy_th_win, width=3)
    text_j_y.place(relx=0.46, rely=0.53)
    Label(jy_th_win, text="��").place(relx=0.58, rely=0.53)
    text_j_r = Entry(jy_th_win, width=3)
    text_j_r.place(relx=0.64, rely=0.53)
    Label(jy_th_win, text="��").place(relx=0.78, rely=0.53)

    Label(jy_th_win, text="ҵ��Ա��ţ�").place(relx=0.03, rely=0.69)
    val2 = excuate.fet_list("Ա�����", "employee")
    text_ywybh = ttk.Combobox(jy_th_win, width=4, values=val2)
    text_ywybh.place(relx=0.31, rely=0.69)

    Label(jy_th_win, text="�ܽ�").place(relx=0.49, rely=0.69)
    text_zje = Entry(jy_th_win, width=6)
    text_zje.place(relx=0.69, rely=0.69)
    text_zje.insert(0, '�Զ�����')

    tjrk_but = Button(jy_th_win, text="�˻�", width=8, command=_retreatsp)
    tjrk_but.place(relx=0.2, rely=0.85)

    tjrk_but = Button(jy_th_win, text="�������", width=8, command=_clearsp)
    tjrk_but.place(relx=0.58, rely=0.85)

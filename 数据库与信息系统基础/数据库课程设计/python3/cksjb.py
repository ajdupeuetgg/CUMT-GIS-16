# -*-coding:gbk-*-

from tkinter import *
import tkinter.messagebox as message
import tkinter.ttk as ttk
import excuate

def _xchb():
    def _tjcx():
        char1 = "SELECT * FROM goods WHERE ��Ʒ�� = '%s' AND �ͺ� = '%s'" % (text_spm.get(), text_xh.get())
        find1 = excuate.cal_r(char1)
        if find1:
            char2 = "SELECT * FROM goods WHERE ��Ʒ�� = '%s' AND �ͺ� = '%s'" % (text_spm.get(), text_xh.get())
            find2 = excuate.cal_r(char2)

            char3 = """SELECT COUNT(*) FROM
                      (SELECT * FROM goods WHERE ��Ʒ�� = '%s' AND �ͺ� = '%s')a""" % (text_spm.get(), text_xh.get())
            num_c = excuate.cal_r(char3)[0][0]

            tree_h = ttk.Treeview(yjck_win, show="headings", height=15)
            tree_h.place(relx=0.02, rely=0.11)

            tree_h["columns"] = ("��Ʒ���", "��������", "��Ʒ��", "�ͺ�", "����", "����", "�ܽ��", "������", "������", "������", "ҵ��Ա���")
            tree_h.column("��Ʒ���", width=47)
            tree_h.column("��������", width=48)
            tree_h.column("��Ʒ��", width=48)
            tree_h.column("�ͺ�", width=47)
            tree_h.column("����", width=48)
            tree_h.column("����", width=47)
            tree_h.column("�ܽ��", width=48)
            tree_h.column("������", width=48)
            tree_h.column("������", width=47)
            tree_h.column("������", width=47)
            tree_h.column("ҵ��Ա���", width=47)

            tree_h.heading("��Ʒ���", text="��Ʒ���")
            tree_h.heading("��������", text="��������")
            tree_h.heading("��Ʒ��", text="��Ʒ��")
            tree_h.heading("�ͺ�", text="�ͺ�")
            tree_h.heading("����", text="����")
            tree_h.heading("����", text="����")
            tree_h.heading("�ܽ��", text="�ܽ��")
            tree_h.heading("������", text="������")
            tree_h.heading("������", text="������")
            tree_h.heading("������", text="������")
            tree_h.heading("ҵ��Ա���", text="ҵ��Ա���")

            z = {}
            for i in range(0, num_c):
                z[i] = find2[i][0:11]
                tree_h.insert("", i, values=z[i])
        else:
            message.showerror('����', '���ִ������Ϣ��')

    def _cxqb():
        char2 = "SELECT * FROM goods"
        find2 = excuate.cal_r(char2)

        char3 = """SELECT COUNT(*) FROM
                   (SELECT * FROM goods)a"""
        num_c = excuate.cal_r(char3)[0][0]

        tree_h = ttk.Treeview(yjck_win, show="headings", height=15)
        tree_h.place(relx=0.02, rely=0.11)

        tree_h["columns"] = ("��Ʒ���", "��������", "��Ʒ��","�ͺ�","����","����","�ܽ��","������","������","������","ҵ��Ա���")
        tree_h.column("��Ʒ���", width=47)
        tree_h.column("��������", width=48)
        tree_h.column("��Ʒ��", width=48)
        tree_h.column("�ͺ�", width=47)
        tree_h.column("����", width=48)
        tree_h.column("����", width=47)
        tree_h.column("�ܽ��", width=48)
        tree_h.column("������", width=48)
        tree_h.column("������", width=47)
        tree_h.column("������", width=47)
        tree_h.column("ҵ��Ա���", width=47)

        tree_h.heading("��Ʒ���", text="��Ʒ���")
        tree_h.heading("��������", text="��������")
        tree_h.heading("��Ʒ��", text="��Ʒ��")
        tree_h.heading("�ͺ�", text="�ͺ�")
        tree_h.heading("����", text="����")
        tree_h.heading("����", text="����")
        tree_h.heading("�ܽ��", text="�ܽ��")
        tree_h.heading("������", text="������")
        tree_h.heading("������", text="������")
        tree_h.heading("������", text="������")
        tree_h.heading("ҵ��Ա���", text="ҵ��Ա���")


        z = {}
        for i in range(0, num_c):
            z[i] = find2[i][0:11]
            tree_h.insert("", i, values=z[i])

    yjck_win = Tk()
    yjck_win.geometry("550x375+550+320")
    yjck_win.title('��ѯ�ִ����')

    Label(yjck_win, text="��Ʒ����").place(relx=0.019, rely=0.015)
    Label(yjck_win, text="�ͺţ�").place(relx=0.42, rely=0.015)

    text_spm = Entry(yjck_win, width=14)
    text_spm.place(relx=0.15, rely=0.01)
    text_xh = Entry(yjck_win, width=14)
    text_xh.place(relx=0.52, rely=0.01)

    yghcx_but = Button(yjck_win, text="��ѯ", width=6, command=_tjcx)
    yghcx_but.place(relx=0.85, rely=0.018)

    cxqb_but = Button(yjck_win, text="��ʾȫ���ִ���Ʒ", width=58, command=_cxqb)
    cxqb_but.place(relx=0.02, rely=0.92)

    yjck_win.mainloop()

def _scys():
    def _tjcx():
        char1 = "SELECT * FROM sell WHERE ��Ʒ�� = '%s' AND �ͺ� = '%s'" % (text_spm.get(), text_xh.get())
        find1 = excuate.cal_r(char1)
        if find1:
            char2 = "SELECT * FROM sell WHERE ��Ʒ�� = '%s' AND �ͺ� = '%s'" % (text_spm.get(), text_xh.get())
            find2 = excuate.cal_r(char2)

            char3 = """SELECT COUNT(*) FROM
                         (SELECT * FROM sell WHERE ��Ʒ�� = '%s' AND �ͺ� = '%s')a""" % (text_spm.get(), text_xh.get())
            num_c = excuate.cal_r(char3)[0][0]

            tree_h = ttk.Treeview(yjck_win, show="headings", height=15)
            tree_h.place(relx=0.02, rely=0.11)

            tree_h["columns"] = ("��Ʒ���", "��������", "��Ʒ��", "�ͺ�", "����", "����", "�ܽ��", "������", "������", "������", "ҵ��Ա���")
            tree_h.column("��Ʒ���", width=47)
            tree_h.column("��������", width=48)
            tree_h.column("��Ʒ��", width=48)
            tree_h.column("�ͺ�", width=47)
            tree_h.column("����", width=48)
            tree_h.column("����", width=47)
            tree_h.column("�ܽ��", width=48)
            tree_h.column("������", width=48)
            tree_h.column("������", width=47)
            tree_h.column("������", width=47)
            tree_h.column("ҵ��Ա���", width=47)

            tree_h.heading("��Ʒ���", text="��Ʒ���")
            tree_h.heading("��������", text="��������")
            tree_h.heading("��Ʒ��", text="��Ʒ��")
            tree_h.heading("�ͺ�", text="�ͺ�")
            tree_h.heading("����", text="����")
            tree_h.heading("����", text="����")
            tree_h.heading("�ܽ��", text="�ܽ��")
            tree_h.heading("������", text="������")
            tree_h.heading("������", text="������")
            tree_h.heading("������", text="������")
            tree_h.heading("ҵ��Ա���", text="ҵ��Ա���")

            z = {}
            for i in range(0, num_c):
                z[i] = find2[i][0:11]
                tree_h.insert("", i, values=z[i])
        else:
            message.showerror('����', '���۳�������Ϣ��')

    def _cxqb():
        char2 = "SELECT * FROM sell"
        find2 = excuate.cal_r(char2)

        char3 = """SELECT COUNT(*) FROM
                      (SELECT * FROM sell)a"""
        num_c = excuate.cal_r(char3)[0][0]

        tree_h = ttk.Treeview(yjck_win, show="headings", height=15)
        tree_h.place(relx=0.02, rely=0.11)

        tree_h["columns"] = ("��Ʒ���", "��������", "��Ʒ��", "�ͺ�", "����", "����", "�ܽ��", "������", "������", "������", "ҵ��Ա���")
        tree_h.column("��Ʒ���", width=47)
        tree_h.column("��������", width=48)
        tree_h.column("��Ʒ��", width=48)
        tree_h.column("�ͺ�", width=47)
        tree_h.column("����", width=48)
        tree_h.column("����", width=47)
        tree_h.column("�ܽ��", width=48)
        tree_h.column("������", width=48)
        tree_h.column("������", width=47)
        tree_h.column("������", width=47)
        tree_h.column("ҵ��Ա���", width=47)

        tree_h.heading("��Ʒ���", text="��Ʒ���")
        tree_h.heading("��������", text="��������")
        tree_h.heading("��Ʒ��", text="��Ʒ��")
        tree_h.heading("�ͺ�", text="�ͺ�")
        tree_h.heading("����", text="����")
        tree_h.heading("����", text="����")
        tree_h.heading("�ܽ��", text="�ܽ��")
        tree_h.heading("������", text="������")
        tree_h.heading("������", text="������")
        tree_h.heading("������", text="������")
        tree_h.heading("ҵ��Ա���", text="ҵ��Ա���")

        z = {}
        for i in range(0, num_c):
            z[i] = find2[i][0:11]
            tree_h.insert("", i, values=z[i])

    yjck_win = Tk()
    yjck_win.geometry("550x375+550+320")
    yjck_win.title('��ѯ���ۻ���')

    Label(yjck_win, text="��Ʒ����").place(relx=0.019, rely=0.015)
    Label(yjck_win, text="�ͺţ�").place(relx=0.42, rely=0.015)

    text_spm = Entry(yjck_win, width=14)
    text_spm.place(relx=0.15, rely=0.01)
    text_xh = Entry(yjck_win, width=14)
    text_xh.place(relx=0.52, rely=0.01)

    yghcx_but = Button(yjck_win, text="��ѯ", width=6, command=_tjcx)
    yghcx_but.place(relx=0.85, rely=0.018)

    cxqb_but = Button(yjck_win, text="��ʾȫ���۳���Ʒ", width=58, command=_cxqb)
    cxqb_but.place(relx=0.02, rely=0.92)

    yjck_win.mainloop()

def _xsth():
    xsth_win = Tk()
    xsth_win.geometry("550x310+525+275")
    xsth_win.title('��ʾ�˻���')

    tree_h = ttk.Treeview(xsth_win, show="headings", height=15)
    tree_h.place(relx=0.02, rely=0.01)

    tree_h["columns"] = ("��Ʒ���", "��������", "��Ʒ��", "�ͺ�", "����", "����", "�ܽ��", "�˻���", "�˻���", "�˻���", "ҵ��Ա���")
    tree_h.column("��Ʒ���", width=47)
    tree_h.column("��������", width=48)
    tree_h.column("��Ʒ��", width=48)
    tree_h.column("�ͺ�", width=47)
    tree_h.column("����", width=48)
    tree_h.column("����", width=47)
    tree_h.column("�ܽ��", width=50)
    tree_h.column("�˻���", width=48)
    tree_h.column("�˻���", width=47)
    tree_h.column("�˻���", width=47)
    tree_h.column("ҵ��Ա���", width=50)

    tree_h.heading("��Ʒ���", text="��Ʒ���")
    tree_h.heading("��������", text="��������")
    tree_h.heading("��Ʒ��", text="��Ʒ��")
    tree_h.heading("�ͺ�", text="�ͺ�")
    tree_h.heading("����", text="����")
    tree_h.heading("����", text="����")
    tree_h.heading("�ܽ��", text="�ܽ��")
    tree_h.heading("�˻���", text="�˻���")
    tree_h.heading("�˻���", text="�˻���")
    tree_h.heading("�˻���", text="�˻���")
    tree_h.heading("ҵ��Ա���", text="ҵ��Ա���")

    char2 = "SELECT * FROM retreat"
    find2 = excuate.cal_r(char2)

    char3 = """SELECT COUNT(*) FROM
              (SELECT * FROM retreat)a"""
    num_c = excuate.cal_r(char3)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:11]
        tree_h.insert("", i, values=z[i])

def _xsyg():
    xsyg_win = Tk()
    xsyg_win.title('��ʾԱ����')
    xsyg_win.geometry("300x270+300+250")

    tree_yg = ttk.Treeview(xsyg_win, height=10, show="headings")
    tree_yg.place(relx=0, rely=0)

    tree_yg["columns"] = ("Ա�����", "Ա������", "Ա���绰", "Ա����ַ")

    tree_yg.column("Ա�����", width=75, anchor='center')
    tree_yg.column("Ա������", width=75, anchor='center')
    tree_yg.column("Ա���绰", width=75, anchor='center')
    tree_yg.column("Ա����ַ", width=75, anchor='center')

    tree_yg.heading("Ա�����", text="Ա�����")
    tree_yg.heading("Ա������", text="Ա������")
    tree_yg.heading("Ա���绰", text="Ա���绰")
    tree_yg.heading("Ա����ַ", text="Ա����ַ")

    char1 = "SELECT * FROM employee"
    find1 = excuate.cal_r(char1)

    char2 = "SELECT count(*) FROM (SELECT * FROM employee)a"
    num_col = excuate.cal_r(char2)[0][0]

    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:4]
        tree_yg.insert("", i, values=z[i])


    def _change():
        def _changed():
            message.showinfo('��ʾ', '�޸ĳɹ���')
            changed_but.destroy()

        changed_but = Button(xsyg_win, text="ȷ���޸�", width=9, command=_changed)
        changed_but.place(relx=0.16, rely=0.82)

        def set_cell_value(event):
            column = tree_yg.identify_column(event.x)
            row = tree_yg.identify_row(event.y)
            cn = int(str(column).replace('#', ''))
            rn = int(str(row).replace('I', ''))
            val = z[rn - 1][cn - 1]
            c_val = tree_yg["columns"][cn - 1]

            text_change = Entry(xsyg_win, width=7)
            text_change.place(x=(cn-1)*75, y=(rn-1)*20+10)
            text_change.insert(0, val)

            def _set(event=None):
                char = "UPDATE employee SET %s = '%s' WHERE Ա����� = '%s'" % (
                    c_val, text_change.get(), rn
                )
                excuate.cal_nr(char)

                text_change.destroy()

                x = tree_yg.get_children()
                for item in x:
                    tree_yg.delete(item)
                tree_yg.selection_clear()

                char1 = "SELECT * FROM employee"
                find1 = excuate.cal_r(char1)

                char2 = "SELECT count(*) FROM (SELECT * FROM employee)a"
                num_col = excuate.cal_r(char2)[0][0]

                z = {}
                for i in range(0, num_col):
                    z[i] = find1[i][0:4]
                    tree_yg.insert("", i, values=z[i])

            text_change.bind('<Return>', _set)

        tree_yg.bind('<Double-1>', set_cell_value)

    def _del():
        char1 = "SELECT * FROM employee"
        find1 = excuate.cal_r(char1)

        global rn
        char = "DELETE FROM employee WHERE Ա����� = '%s'" % find1[rn-1][0]
        excuate.cal_nr(char)

        char2 = "SELECT * FROM employee"
        find2 = excuate.cal_r(char2)

        char3 = "SELECT count(*) FROM (SELECT * FROM employee)a"
        num_col = excuate.cal_r(char3)[0][0]

        x = tree_yg.get_children()
        for item in x:
            tree_yg.delete(item)

        z = {}
        for i in range(0, num_col):
            z[i] = find2[i][0:4]
            tree_yg.insert("", i, values=z[i])

    def _getrn(event):
        row = tree_yg.identify_row(event.y)
        global rn
        rn = int(str(row).replace('I', ''))
    tree_yg.bind('<Button-1>', _getrn)

    change_but = Button(xsyg_win, text="�޸ļ�¼", width=9, command=_change)
    change_but.place(relx=0.16, rely=0.82)
    delete_but = Button(xsyg_win, text="ɾ����¼", width=9, command=_del)
    delete_but.place(relx=0.56, rely=0.82)

def _jhsb():
    xsyg_win = Tk()
    xsyg_win.title('��ʾ�����̱�')
    xsyg_win.geometry("375x270+300+250")

    tree_yg = ttk.Treeview(xsyg_win, height=10, show="headings")
    tree_yg.place(relx=0, rely=0)

    tree_yg["columns"] = ("���̱��", "��������", "���˴���", "���̵�ַ", "�绰")

    tree_yg.column("���̱��", width=75, anchor='center')
    tree_yg.column("��������", width=75, anchor='center')
    tree_yg.column("���˴���", width=75, anchor='center')
    tree_yg.column("���̵�ַ", width=75, anchor='center')
    tree_yg.column("�绰", width=75, anchor='center')

    tree_yg.heading("���̱��", text="���̱��")
    tree_yg.heading("��������", text="��������")
    tree_yg.heading("���˴���", text="���˴���")
    tree_yg.heading("���̵�ַ", text="���̵�ַ")
    tree_yg.heading("�绰", text="�绰")

    char1 = "SELECT * FROM manufacturer"
    find1 = excuate.cal_r(char1)

    char2 = "SELECT count(*) FROM (SELECT * FROM manufacturer)a"
    num_col = excuate.cal_r(char2)[0][0]

    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:5]
        tree_yg.insert("", i, values=z[i])

    def _change():
        def _changed():
            message.showinfo('��ʾ', '�޸ĳɹ���')
            changed_but.destroy()

        changed_but = Button(xsyg_win, text="ȷ���޸�", width=9, command=_changed)
        changed_but.place(relx=0.16, rely=0.82)

        def set_cell_value(event):
            column = tree_yg.identify_column(event.x)
            row = tree_yg.identify_row(event.y)
            cn = int(str(column).replace('#', ''))
            rn = int(str(row).replace('I', ''))
            val = z[rn - 1][cn - 1]
            c_val = tree_yg["columns"][cn - 1]

            text_change = Entry(xsyg_win, width=7)
            text_change.place(x=(cn - 1) * 75, y=(rn - 1) * 20 + 10)
            text_change.insert(0, val)

            def _set(event=None):
                char = "UPDATE manufacturer SET %s = '%s' WHERE ���̱�� = '%s'" % (
                    c_val, text_change.get(), rn
                )
                excuate.cal_nr(char)

                text_change.destroy()

                x = tree_yg.get_children()
                for item in x:
                    tree_yg.delete(item)
                tree_yg.selection_clear()

                char1 = "SELECT * FROM manufacturer"
                find1 = excuate.cal_r(char1)

                char2 = "SELECT count(*) FROM (SELECT * FROM manufacturer)a"
                num_col = excuate.cal_r(char2)[0][0]

                z = {}
                for i in range(0, num_col):
                    z[i] = find1[i][0:4]
                    tree_yg.insert("", i, values=z[i])

            text_change.bind('<Return>', _set)

        tree_yg.bind('<Double-1>', set_cell_value)

    def _del():
        char1 = "SELECT * FROM manufacturer"
        find1 = excuate.cal_r(char1)

        global rn
        char = "DELETE FROM manufacturer WHERE ���̱�� = '%s'" % find1[rn - 1][0]
        excuate.cal_nr(char)

        char2 = "SELECT * FROM manufacturer"
        find2 = excuate.cal_r(char2)

        char3 = "SELECT count(*) FROM (SELECT * FROM manufacturer)a"
        num_col = excuate.cal_r(char3)[0][0]

        x = tree_yg.get_children()
        for item in x:
            tree_yg.delete(item)

        z = {}
        for i in range(0, num_col):
            z[i] = find2[i][0:4]
            tree_yg.insert("", i, values=z[i])

    def _getrn(event):
        row = tree_yg.identify_row(event.y)
        global rn
        rn = int(str(row).replace('I', ''))

    tree_yg.bind('<Button-1>', _getrn)

    change_but = Button(xsyg_win, text="�޸ļ�¼", width=9, command=_change)
    change_but.place(relx=0.16, rely=0.82)
    delete_but = Button(xsyg_win, text="ɾ����¼", width=9, command=_del)
    delete_but.place(relx=0.56, rely=0.82)

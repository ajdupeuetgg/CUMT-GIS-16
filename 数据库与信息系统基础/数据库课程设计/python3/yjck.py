# -*-coding:gbk-*-

from tkinter import *
import tkinter.ttk as ttk
import excuate
import tkinter.messagebox as message

def _yjck():
    def _yghcx():
        char1 = "SELECT Ա������ FROM employee WHERE Ա����� = '%s'" % text_ygh.get()
        find1 = excuate.cal_r(char1)

        if find1:
            tree_ygh = ttk.Treeview(yjck_win, show="headings", height=15)
            tree_ygh.place(relx=0.02, rely=0.11)

            tree_ygh["columns"] = ("ҵ��Ա���", "Ա������", "�����ܽ��")
            tree_ygh.column("ҵ��Ա���", width=102)
            tree_ygh.column("Ա������", width=102)
            tree_ygh.column("�����ܽ��", width=102)

            tree_ygh.heading("ҵ��Ա���", text="ҵ��Ա���")
            tree_ygh.heading("Ա������", text="Ա������")
            tree_ygh.heading("�����ܽ��", text="�����ܽ��")

            char4 = """SELECT Ա�����, Ա������, SUM(�ܽ��)
                       FROM employee, sell
                       WHERE Ա����� = ҵ��Ա��� AND Ա����� = '%s'
                       GROUP BY Ա�����, Ա������
                       ORDER BY Ա�����""" % text_ygh.get()
            find4 = excuate.cal_r(char4)

            char5 = """SELECT COUNT(*) FROM
                      (SELECT Ա�����, Ա������, SUM(�ܽ��)
                       FROM employee, sell
                       WHERE Ա����� = ҵ��Ա��� AND Ա����� = '%s'
                       GROUP BY Ա�����, Ա������
                       ORDER BY Ա�����)a""" % text_ygh.get()
            num_c = excuate.cal_r(char5)[0][0]

            z = {}
            for i in range(0, num_c):
                z[i] = find4[i][0:3]
                tree_ygh.insert("", i, values=z[i])

        else:
            message.showerror('����', '�޸�Ա����Ϣ��')

    def _cxqb():
        char2 = """SELECT Ա�����, Ա������, SUM(�ܽ��)
                   FROM employee, sell
                   WHERE Ա����� = ҵ��Ա���
                   GROUP BY Ա�����, Ա������
                   ORDER BY Ա�����"""
        find2 = excuate.cal_r(char2)

        char3 = """SELECT COUNT(*) FROM
                   (SELECT Ա�����, Ա������, SUM(�ܽ��)
                    FROM employee, sell
                    WHERE Ա����� = ҵ��Ա���
                    GROUP BY Ա�����, Ա������
                    ORDER BY Ա�����)a"""
        num_c = excuate.cal_r(char3)[0][0]

        tree_yg = ttk.Treeview(yjck_win, show="headings", height=15)
        tree_yg.place(relx=0.02, rely=0.11)

        tree_yg["columns"] = ("ҵ��Ա���", "Ա������", "�����ܽ��")
        tree_yg.column("ҵ��Ա���", width=102)
        tree_yg.column("Ա������", width=102)
        tree_yg.column("�����ܽ��", width=102)

        tree_yg.heading("ҵ��Ա���", text="ҵ��Ա���")
        tree_yg.heading("Ա������", text="Ա������")
        tree_yg.heading("�����ܽ��", text="�����ܽ��")

        z = {}
        for i in range(0, num_c):
            z[i] = find2[i][0:3]
            tree_yg.insert("", i, values=z[i])

    yjck_win = Tk()
    yjck_win.geometry("325x375+550+320")
    yjck_win.title('��ѯԱ�����۶�')

    Label(yjck_win, text="Ա���ţ�").place(relx=0.02, rely=0.015)

    text_ygh = Entry(yjck_win)
    text_ygh.place(relx=0.2, rely=0.01)

    yghcx_but = Button(yjck_win, text="��ѯ", width=5, command=_yghcx)
    yghcx_but.place(relx=0.8, rely=0.018)

    cxqb_but = Button(yjck_win, text="��ʾȫ��Ա�����۶�", width=34, command=_cxqb)
    cxqb_but.place(relx=0.02, rely=0.92)

    yjck_win.mainloop()
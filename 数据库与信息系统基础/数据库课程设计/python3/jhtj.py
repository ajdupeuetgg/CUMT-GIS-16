# -*-coding:gbk-*-

from tkinter import *
import tkinter.ttk as ttk
import excuate
import time

def _jrjh():
    jh_jr_win = Tk()
    jh_jr_win.title("���ս���")
    jh_jr_win.geometry("600x340+300+250")

    # ��ѯ�������
    tree_jr = ttk.Treeview(jh_jr_win, show="headings")
    tree_jr.place(relx=0.01, rely=0.01)

    tree_jr["columns"] = ("��Ʒ���", "��������", "��Ʒ��", "�ͺ�", "����", "����", "�ܽ��", "ҵ��Ա���")

    tree_jr.column("��Ʒ���", width=62)
    tree_jr.column("��������", width=75)
    tree_jr.column("��Ʒ��", width=75)
    tree_jr.column("�ͺ�", width=75)
    tree_jr.column("����", width=75)
    tree_jr.column("����", width=75)
    tree_jr.column("�ܽ��", width=75)
    tree_jr.column("ҵ��Ա���", width=75)

    tree_jr.heading("��Ʒ���", text="��Ʒ���")
    tree_jr.heading("��������", text="��������")
    tree_jr.heading("��Ʒ��", text="��Ʒ��")
    tree_jr.heading("�ͺ�", text="�ͺ�")
    tree_jr.heading("����", text="����")
    tree_jr.heading("����", text="����")
    tree_jr.heading("�ܽ��", text="�ܽ��")
    tree_jr.heading("ҵ��Ա���", text="ҵ��Ա���")

    char1 = """SELECT ��Ʒ���, ��������, ��Ʒ��, �ͺ�, ����, ����, �ܽ��, ҵ��Ա���
               FROM goods
               WHERE ������ = '%s' AND ������ = '%s' AND ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(��Ʒ���) FROM goods
               WHERE ������ = '%s' AND ������ = '%s' AND ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:8]
        tree_jr.insert("", i, values=z[i])

    # �����ѯ�������
    tree_cs = ttk.Treeview(jh_jr_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.62)

    tree_cs["columns"] = ("��������", "�����̽����ܽ��")

    tree_cs.column("��������", width=100)
    tree_cs.column("�����̽����ܽ��", width=130)

    tree_cs.heading("��������", text="��������")
    tree_cs.heading("�����̽����ܽ��", text="�����̽����ܽ��")


    char3  = """SELECT ��������, SUM(�ܽ��)
                FROM goods
                WHERE ������ = '%s' AND ������ = '%s' AND ������ = '%s'
                GROUP BY ��������""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT ��������)
            FROM goods
            WHERE ������ = '%s' AND ������ = '%s' AND ������ = '%s'
            GROUP BY ��������)a""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # �������ı���
    Label(jh_jr_win, text="�����ܽ�").place(relx=0.45, rely=0.76)
    text_jhzje = Entry(jh_jr_win)
    text_jhzje.place(relx=0.6, rely=0.75)

    char5 = """SELECT SUM(�ܽ��)
               FROM goods
               WHERE ������ = '%s' AND ������ = '%s' AND ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    sum_gcszje = excuate.cal_r(char5)[0][0]
    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    jh_jr_win.mainloop()

def _byjh():
    jh_by_win = Tk()
    jh_by_win.title("���½���")
    jh_by_win.geometry("600x340+300+250")

    # ��ѯ�������
    tree_by = ttk.Treeview(jh_by_win, show="headings")
    tree_by.place(relx=0.01, rely=0.01)

    tree_by["columns"] = ("��Ʒ���", "��������", "��Ʒ��", "�ͺ�", "����", "����", "�ܽ��", "ҵ��Ա���")

    tree_by.column("��Ʒ���", width=62)
    tree_by.column("��������", width=75)
    tree_by.column("��Ʒ��", width=75)
    tree_by.column("�ͺ�", width=75)
    tree_by.column("����", width=75)
    tree_by.column("����", width=75)
    tree_by.column("�ܽ��", width=75)
    tree_by.column("ҵ��Ա���", width=75)

    tree_by.heading("��Ʒ���", text="��Ʒ���")
    tree_by.heading("��������", text="��������")
    tree_by.heading("��Ʒ��", text="��Ʒ��")
    tree_by.heading("�ͺ�", text="�ͺ�")
    tree_by.heading("����", text="����")
    tree_by.heading("����", text="����")
    tree_by.heading("�ܽ��", text="�ܽ��")
    tree_by.heading("ҵ��Ա���", text="ҵ��Ա���")

    char1 = """SELECT ��Ʒ���, ��������, ��Ʒ��, �ͺ�, ����, ����, �ܽ��, ҵ��Ա���
               FROM goods
               WHERE ������ = '%s' AND ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(��Ʒ���) FROM goods
               WHERE ������ = '%s' AND ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime())
    )
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:8]
        tree_by.insert("", i, values=z[i])

    # �����ѯ�������
    tree_cs = ttk.Treeview(jh_by_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.62)

    tree_cs["columns"] = ("��������", "�����̽����ܽ��")

    tree_cs.column("��������", width=100)
    tree_cs.column("�����̽����ܽ��", width=130)

    tree_cs.heading("��������", text="��������")
    tree_cs.heading("�����̽����ܽ��", text="�����̽����ܽ��")


    char3  = """SELECT ��������, SUM(�ܽ��)
                FROM goods
                WHERE ������ = '%s' AND ������ = '%s'
                GROUP BY ��������""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
              (SELECT COUNT(DISTINCT ��������)
               FROM goods
               WHERE ������ = '%s' AND ������ = '%s'
               GROUP BY ��������)a""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # �������ı���
    Label(jh_by_win, text="�����ܽ�").place(relx=0.45, rely=0.76)
    text_jhzje = Entry(jh_by_win)
    text_jhzje.place(relx=0.6, rely=0.75)

    char5 = """SELECT SUM(�ܽ��)
               FROM goods
               WHERE ������ = '%s' AND ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    sum_gcszje = excuate.cal_r(char5)[0][0]

    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    jh_by_win.mainloop()

def _jdjh():
    jh_jd_win = Tk()
    jh_jd_win.title("�����Ƚ���")
    jh_jd_win.geometry("600x340+300+250")

    # ��ѯ�������
    tree_by = ttk.Treeview(jh_jd_win, show="headings")
    tree_by.place(relx=0.01, rely=0.01)

    tree_by["columns"] = ("��Ʒ���", "��������", "��Ʒ��", "�ͺ�", "����", "����", "�ܽ��", "ҵ��Ա���")

    tree_by.column("��Ʒ���", width=62)
    tree_by.column("��������", width=75)
    tree_by.column("��Ʒ��", width=75)
    tree_by.column("�ͺ�", width=75)
    tree_by.column("����", width=75)
    tree_by.column("����", width=75)
    tree_by.column("�ܽ��", width=75)
    tree_by.column("ҵ��Ա���", width=75)

    tree_by.heading("��Ʒ���", text="��Ʒ���")
    tree_by.heading("��������", text="��������")
    tree_by.heading("��Ʒ��", text="��Ʒ��")
    tree_by.heading("�ͺ�", text="�ͺ�")
    tree_by.heading("����", text="����")
    tree_by.heading("����", text="����")
    tree_by.heading("�ܽ��", text="�ܽ��")
    tree_by.heading("ҵ��Ա���", text="ҵ��Ա���")

    A = 0
    B = 0
    C = int(time.strftime("%m", time.localtime()))
    if C in range(1, 4):
        A = 1
        B = 3
    elif C in range(4, 7):
        A = 4
        B = 6
    elif C in range(7, 10):
        A = 7
        B = 9
    elif C in range(10, 13):
        A = 10
        B = 12

    char1 = """SELECT ��Ʒ���, ��������, ��Ʒ��, �ͺ�, ����, ����, �ܽ��, ҵ��Ա���
               FROM goods
               WHERE ������ = '%s' AND ������ >= '%s' AND ������ <= '%s'""" % (
        time.strftime("%Y", time.localtime()), A, B)
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(��Ʒ���) FROM goods
               WHERE ������ = '%s' AND ������ >= '%s' AND ������ <= '%s'""" % (
        time.strftime("%Y", time.localtime()), A, B)
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:8]
        tree_by.insert("", i, values=z[i])

    # �����ѯ�������
    tree_cs = ttk.Treeview(jh_jd_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.62)

    tree_cs["columns"] = ("��������", "�����̽����ܽ��")

    tree_cs.column("��������", width=100)
    tree_cs.column("�����̽����ܽ��", width=130)

    tree_cs.heading("��������", text="��������")
    tree_cs.heading("�����̽����ܽ��", text="�����̽����ܽ��")


    char3  = """SELECT ��������, SUM(�ܽ��)
                FROM goods
                WHERE ������ = '%s' AND ������ >= '%s' AND ������ <= '%s'
                GROUP BY ��������""" % (
        time.strftime("%Y", time.localtime()), A, B)
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT ��������)
            FROM goods
            WHERE ������ = '%s' AND ������ >= '%s' AND ������ <= '%s'
            GROUP BY ��������)a""" % (
        time.strftime("%Y", time.localtime()), A, B)
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # �������ı���
    Label(jh_jd_win, text="�����ܽ�").place(relx=0.45, rely=0.76)
    text_jhzje = Entry(jh_jd_win)
    text_jhzje.place(relx=0.6, rely=0.75)

    char5 = """SELECT SUM(�ܽ��)
               FROM goods
               WHERE ������ = '%s' AND ������ >= '%s' AND ������ <= '%s'""" % (
        time.strftime("%Y", time.localtime()), A, B)
    sum_gcszje = excuate.cal_r(char5)[0][0]

    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    jh_jd_win.mainloop()

def _jnjh():
    jh_jn_win = Tk()
    jh_jn_win.title("�������")
    jh_jn_win.geometry("600x340+300+250")

    # ��ѯ�������
    tree_by = ttk.Treeview(jh_jn_win, show="headings")
    tree_by.place(relx=0.01, rely=0.01)

    tree_by["columns"] = ("��Ʒ���", "��������", "��Ʒ��", "�ͺ�", "����", "����", "�ܽ��", "ҵ��Ա���")

    tree_by.column("��Ʒ���", width=62)
    tree_by.column("��������", width=75)
    tree_by.column("��Ʒ��", width=75)
    tree_by.column("�ͺ�", width=75)
    tree_by.column("����", width=75)
    tree_by.column("����", width=75)
    tree_by.column("�ܽ��", width=75)
    tree_by.column("ҵ��Ա���", width=75)

    tree_by.heading("��Ʒ���", text="��Ʒ���")
    tree_by.heading("��������", text="��������")
    tree_by.heading("��Ʒ��", text="��Ʒ��")
    tree_by.heading("�ͺ�", text="�ͺ�")
    tree_by.heading("����", text="����")
    tree_by.heading("����", text="����")
    tree_by.heading("�ܽ��", text="�ܽ��")
    tree_by.heading("ҵ��Ա���", text="ҵ��Ա���")

    char1 = """SELECT ��Ʒ���, ��������, ��Ʒ��, �ͺ�, ����, ����, �ܽ��, ҵ��Ա���
               FROM goods
               WHERE ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(��Ʒ���) FROM goods
               WHERE ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:8]
        tree_by.insert("", i, values=z[i])

    # �����ѯ�������
    tree_cs = ttk.Treeview(jh_jn_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.62)

    tree_cs["columns"] = ("��������", "�����̽����ܽ��")

    tree_cs.column("��������", width=100)
    tree_cs.column("�����̽����ܽ��", width=130)

    tree_cs.heading("��������", text="��������")
    tree_cs.heading("�����̽����ܽ��", text="�����̽����ܽ��")


    char3  = """SELECT ��������, SUM(�ܽ��)
                FROM goods
                WHERE ������ = '%s'
                GROUP BY ��������""" % (
        time.strftime("%Y", time.localtime()))
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT ��������)
            FROM goods
            WHERE ������ = '%s'
            GROUP BY ��������)a""" % (
        time.strftime("%Y", time.localtime()))
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # �������ı���
    Label(jh_jn_win, text="�����ܽ�").place(relx=0.45, rely=0.76)
    text_jhzje = Entry(jh_jn_win)
    text_jhzje.place(relx=0.6, rely=0.75)

    char5 = """SELECT SUM(�ܽ��)
               FROM goods
               WHERE ������ = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    sum_gcszje = excuate.cal_r(char5)[0][0]

    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    jh_jn_win.mainloop()

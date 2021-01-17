# -*-coding:gbk-*-

from tkinter import *
import tkinter.ttk as ttk
import excuate
import time

def _jrjh():
    jh_jr_win = Tk()
    jh_jr_win.title("今日进货")
    jh_jr_win.geometry("600x340+300+250")

    # 查询结果窗口
    tree_jr = ttk.Treeview(jh_jr_win, show="headings")
    tree_jr.place(relx=0.01, rely=0.01)

    tree_jr["columns"] = ("商品编号", "生产厂商", "商品名", "型号", "单价", "数量", "总金额", "业务员编号")

    tree_jr.column("商品编号", width=62)
    tree_jr.column("生产厂商", width=75)
    tree_jr.column("商品名", width=75)
    tree_jr.column("型号", width=75)
    tree_jr.column("单价", width=75)
    tree_jr.column("数量", width=75)
    tree_jr.column("总金额", width=75)
    tree_jr.column("业务员编号", width=75)

    tree_jr.heading("商品编号", text="商品编号")
    tree_jr.heading("生产厂商", text="生产厂商")
    tree_jr.heading("商品名", text="商品名")
    tree_jr.heading("型号", text="型号")
    tree_jr.heading("单价", text="单价")
    tree_jr.heading("数量", text="数量")
    tree_jr.heading("总金额", text="总金额")
    tree_jr.heading("业务员编号", text="业务员编号")

    char1 = """SELECT 商品编号, 生产厂商, 商品名, 型号, 单价, 数量, 总金额, 业务员编号
               FROM goods
               WHERE 进货年 = '%s' AND 进货月 = '%s' AND 进货日 = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(商品编号) FROM goods
               WHERE 进货年 = '%s' AND 进货月 = '%s' AND 进货日 = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:8]
        tree_jr.insert("", i, values=z[i])

    # 分类查询结果窗口
    tree_cs = ttk.Treeview(jh_jr_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.62)

    tree_cs["columns"] = ("生产厂商", "各厂商进货总金额")

    tree_cs.column("生产厂商", width=100)
    tree_cs.column("各厂商进货总金额", width=130)

    tree_cs.heading("生产厂商", text="生产厂商")
    tree_cs.heading("各厂商进货总金额", text="各厂商进货总金额")


    char3  = """SELECT 生产厂商, SUM(总金额)
                FROM goods
                WHERE 进货年 = '%s' AND 进货月 = '%s' AND 进货日 = '%s'
                GROUP BY 生产厂商""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT 生产厂商)
            FROM goods
            WHERE 进货年 = '%s' AND 进货月 = '%s' AND 进货日 = '%s'
            GROUP BY 生产厂商)a""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # 计算结果文本框
    Label(jh_jr_win, text="进货总金额：").place(relx=0.45, rely=0.76)
    text_jhzje = Entry(jh_jr_win)
    text_jhzje.place(relx=0.6, rely=0.75)

    char5 = """SELECT SUM(总金额)
               FROM goods
               WHERE 进货年 = '%s' AND 进货月 = '%s' AND 进货日 = '%s'""" % (
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
    jh_by_win.title("本月进货")
    jh_by_win.geometry("600x340+300+250")

    # 查询结果窗口
    tree_by = ttk.Treeview(jh_by_win, show="headings")
    tree_by.place(relx=0.01, rely=0.01)

    tree_by["columns"] = ("商品编号", "生产厂商", "商品名", "型号", "单价", "数量", "总金额", "业务员编号")

    tree_by.column("商品编号", width=62)
    tree_by.column("生产厂商", width=75)
    tree_by.column("商品名", width=75)
    tree_by.column("型号", width=75)
    tree_by.column("单价", width=75)
    tree_by.column("数量", width=75)
    tree_by.column("总金额", width=75)
    tree_by.column("业务员编号", width=75)

    tree_by.heading("商品编号", text="商品编号")
    tree_by.heading("生产厂商", text="生产厂商")
    tree_by.heading("商品名", text="商品名")
    tree_by.heading("型号", text="型号")
    tree_by.heading("单价", text="单价")
    tree_by.heading("数量", text="数量")
    tree_by.heading("总金额", text="总金额")
    tree_by.heading("业务员编号", text="业务员编号")

    char1 = """SELECT 商品编号, 生产厂商, 商品名, 型号, 单价, 数量, 总金额, 业务员编号
               FROM goods
               WHERE 进货年 = '%s' AND 进货月 = '%s'""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(商品编号) FROM goods
               WHERE 进货年 = '%s' AND 进货月 = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime())
    )
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:8]
        tree_by.insert("", i, values=z[i])

    # 分类查询结果窗口
    tree_cs = ttk.Treeview(jh_by_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.62)

    tree_cs["columns"] = ("生产厂商", "各厂商进货总金额")

    tree_cs.column("生产厂商", width=100)
    tree_cs.column("各厂商进货总金额", width=130)

    tree_cs.heading("生产厂商", text="生产厂商")
    tree_cs.heading("各厂商进货总金额", text="各厂商进货总金额")


    char3  = """SELECT 生产厂商, SUM(总金额)
                FROM goods
                WHERE 进货年 = '%s' AND 进货月 = '%s'
                GROUP BY 生产厂商""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
              (SELECT COUNT(DISTINCT 生产厂商)
               FROM goods
               WHERE 进货年 = '%s' AND 进货月 = '%s'
               GROUP BY 生产厂商)a""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # 计算结果文本框
    Label(jh_by_win, text="进货总金额：").place(relx=0.45, rely=0.76)
    text_jhzje = Entry(jh_by_win)
    text_jhzje.place(relx=0.6, rely=0.75)

    char5 = """SELECT SUM(总金额)
               FROM goods
               WHERE 进货年 = '%s' AND 进货月 = '%s'""" % (
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
    jh_jd_win.title("本季度进货")
    jh_jd_win.geometry("600x340+300+250")

    # 查询结果窗口
    tree_by = ttk.Treeview(jh_jd_win, show="headings")
    tree_by.place(relx=0.01, rely=0.01)

    tree_by["columns"] = ("商品编号", "生产厂商", "商品名", "型号", "单价", "数量", "总金额", "业务员编号")

    tree_by.column("商品编号", width=62)
    tree_by.column("生产厂商", width=75)
    tree_by.column("商品名", width=75)
    tree_by.column("型号", width=75)
    tree_by.column("单价", width=75)
    tree_by.column("数量", width=75)
    tree_by.column("总金额", width=75)
    tree_by.column("业务员编号", width=75)

    tree_by.heading("商品编号", text="商品编号")
    tree_by.heading("生产厂商", text="生产厂商")
    tree_by.heading("商品名", text="商品名")
    tree_by.heading("型号", text="型号")
    tree_by.heading("单价", text="单价")
    tree_by.heading("数量", text="数量")
    tree_by.heading("总金额", text="总金额")
    tree_by.heading("业务员编号", text="业务员编号")

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

    char1 = """SELECT 商品编号, 生产厂商, 商品名, 型号, 单价, 数量, 总金额, 业务员编号
               FROM goods
               WHERE 进货年 = '%s' AND 进货月 >= '%s' AND 进货月 <= '%s'""" % (
        time.strftime("%Y", time.localtime()), A, B)
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(商品编号) FROM goods
               WHERE 进货年 = '%s' AND 进货月 >= '%s' AND 进货月 <= '%s'""" % (
        time.strftime("%Y", time.localtime()), A, B)
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:8]
        tree_by.insert("", i, values=z[i])

    # 分类查询结果窗口
    tree_cs = ttk.Treeview(jh_jd_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.62)

    tree_cs["columns"] = ("生产厂商", "各厂商进货总金额")

    tree_cs.column("生产厂商", width=100)
    tree_cs.column("各厂商进货总金额", width=130)

    tree_cs.heading("生产厂商", text="生产厂商")
    tree_cs.heading("各厂商进货总金额", text="各厂商进货总金额")


    char3  = """SELECT 生产厂商, SUM(总金额)
                FROM goods
                WHERE 进货年 = '%s' AND 进货月 >= '%s' AND 进货月 <= '%s'
                GROUP BY 生产厂商""" % (
        time.strftime("%Y", time.localtime()), A, B)
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT 生产厂商)
            FROM goods
            WHERE 进货年 = '%s' AND 进货月 >= '%s' AND 进货月 <= '%s'
            GROUP BY 生产厂商)a""" % (
        time.strftime("%Y", time.localtime()), A, B)
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # 计算结果文本框
    Label(jh_jd_win, text="进货总金额：").place(relx=0.45, rely=0.76)
    text_jhzje = Entry(jh_jd_win)
    text_jhzje.place(relx=0.6, rely=0.75)

    char5 = """SELECT SUM(总金额)
               FROM goods
               WHERE 进货年 = '%s' AND 进货月 >= '%s' AND 进货月 <= '%s'""" % (
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
    jh_jn_win.title("今年进货")
    jh_jn_win.geometry("600x340+300+250")

    # 查询结果窗口
    tree_by = ttk.Treeview(jh_jn_win, show="headings")
    tree_by.place(relx=0.01, rely=0.01)

    tree_by["columns"] = ("商品编号", "生产厂商", "商品名", "型号", "单价", "数量", "总金额", "业务员编号")

    tree_by.column("商品编号", width=62)
    tree_by.column("生产厂商", width=75)
    tree_by.column("商品名", width=75)
    tree_by.column("型号", width=75)
    tree_by.column("单价", width=75)
    tree_by.column("数量", width=75)
    tree_by.column("总金额", width=75)
    tree_by.column("业务员编号", width=75)

    tree_by.heading("商品编号", text="商品编号")
    tree_by.heading("生产厂商", text="生产厂商")
    tree_by.heading("商品名", text="商品名")
    tree_by.heading("型号", text="型号")
    tree_by.heading("单价", text="单价")
    tree_by.heading("数量", text="数量")
    tree_by.heading("总金额", text="总金额")
    tree_by.heading("业务员编号", text="业务员编号")

    char1 = """SELECT 商品编号, 生产厂商, 商品名, 型号, 单价, 数量, 总金额, 业务员编号
               FROM goods
               WHERE 进货年 = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(商品编号) FROM goods
               WHERE 进货年 = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:8]
        tree_by.insert("", i, values=z[i])

    # 分类查询结果窗口
    tree_cs = ttk.Treeview(jh_jn_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.62)

    tree_cs["columns"] = ("生产厂商", "各厂商进货总金额")

    tree_cs.column("生产厂商", width=100)
    tree_cs.column("各厂商进货总金额", width=130)

    tree_cs.heading("生产厂商", text="生产厂商")
    tree_cs.heading("各厂商进货总金额", text="各厂商进货总金额")


    char3  = """SELECT 生产厂商, SUM(总金额)
                FROM goods
                WHERE 进货年 = '%s'
                GROUP BY 生产厂商""" % (
        time.strftime("%Y", time.localtime()))
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT 生产厂商)
            FROM goods
            WHERE 进货年 = '%s'
            GROUP BY 生产厂商)a""" % (
        time.strftime("%Y", time.localtime()))
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # 计算结果文本框
    Label(jh_jn_win, text="进货总金额：").place(relx=0.45, rely=0.76)
    text_jhzje = Entry(jh_jn_win)
    text_jhzje.place(relx=0.6, rely=0.75)

    char5 = """SELECT SUM(总金额)
               FROM goods
               WHERE 进货年 = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    sum_gcszje = excuate.cal_r(char5)[0][0]

    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    jh_jn_win.mainloop()

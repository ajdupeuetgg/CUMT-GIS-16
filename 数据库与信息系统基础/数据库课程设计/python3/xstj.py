# -*-coding:gbk-*-

from tkinter import *
import tkinter.ttk as ttk
import excuate
import time

def _jrxs():
    xs_jr_win = Tk()
    xs_jr_win.title("今日销售")
    xs_jr_win.geometry("300x380+300+250")

    # 查询结果窗口
    tree_jr = ttk.Treeview(xs_jr_win, show="headings")
    tree_jr.place(relx=0.01, rely=0.01)

    tree_jr["columns"] = ("商品编号", "生产厂商", "商品名", "型号")

    tree_jr.column("商品编号", width=62)
    tree_jr.column("生产厂商", width=75)
    tree_jr.column("商品名", width=75)
    tree_jr.column("型号", width=75)

    tree_jr.heading("商品编号", text="商品编号")
    tree_jr.heading("生产厂商", text="生产厂商")
    tree_jr.heading("商品名", text="商品名")
    tree_jr.heading("型号", text="型号")

    char1 = """SELECT 商品编号, 生产厂商, 商品名, 型号
               FROM sell
               WHERE 销售年 = '%s' AND 销售月 = '%s' AND 销售日 = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(商品编号) FROM sell
               WHERE 销售年 = '%s' AND 销售月 = '%s' AND 销售日 = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:4]
        tree_jr.insert("", i, values=z[i])

    # 分类查询结果窗口
    tree_cs = ttk.Treeview(xs_jr_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.56)

    tree_cs["columns"] = ("生产厂商", "各厂商销售总金额")

    tree_cs.column("生产厂商", width=143)
    tree_cs.column("各厂商销售总金额", width=144)

    tree_cs.heading("生产厂商", text="生产厂商")
    tree_cs.heading("各厂商销售总金额", text="各厂商销售总金额")


    char3  = """SELECT 生产厂商, SUM(总金额)
                FROM sell
                WHERE 销售年 = '%s' AND 销售月 = '%s' AND 销售日 = '%s'
                GROUP BY 生产厂商""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT 生产厂商)
            FROM sell
            WHERE 销售年 = '%s' AND 销售月 = '%s' AND 销售日 = '%s'
            GROUP BY 生产厂商)a""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # 计算结果文本框
    Label(xs_jr_win, text="销售总金额：").place(relx=0.02, rely=0.89)
    text_jhzje = Entry(xs_jr_win)
    text_jhzje.place(relx=0.31, rely=0.88)

    char5 = """SELECT SUM(总金额)
               FROM sell
               WHERE 销售年 = '%s' AND 销售月 = '%s' AND 销售日 = '%s'""" % (
        time.strftime("%Y", time.localtime()),time.strftime("%m", time.localtime()),time.strftime("%d", time.localtime())
    )
    sum_gcszje = excuate.cal_r(char5)[0][0]

    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    xs_jr_win.mainloop()

def _byxs():
    xs_by_win = Tk()
    xs_by_win.title("本月销售")
    xs_by_win.geometry("300x380+300+250")

    # 查询结果窗口
    tree_jr = ttk.Treeview(xs_by_win, show="headings")
    tree_jr.place(relx=0.01, rely=0.01)

    tree_jr["columns"] = ("商品编号", "生产厂商", "商品名", "型号")

    tree_jr.column("商品编号", width=62)
    tree_jr.column("生产厂商", width=75)
    tree_jr.column("商品名", width=75)
    tree_jr.column("型号", width=75)

    tree_jr.heading("商品编号", text="商品编号")
    tree_jr.heading("生产厂商", text="生产厂商")
    tree_jr.heading("商品名", text="商品名")
    tree_jr.heading("型号", text="型号")

    char1 = """SELECT 商品编号, 生产厂商, 商品名, 型号
               FROM sell
               WHERE 销售年 = '%s' AND 销售月 = '%s'""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(商品编号) FROM sell
               WHERE 销售年 = '%s' AND 销售月 = '%s'""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:4]
        tree_jr.insert("", i, values=z[i])

    # 分类查询结果窗口
    tree_cs = ttk.Treeview(xs_by_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.56)

    tree_cs["columns"] = ("生产厂商", "各厂商销售总金额")

    tree_cs.column("生产厂商", width=143)
    tree_cs.column("各厂商销售总金额", width=144)

    tree_cs.heading("生产厂商", text="生产厂商")
    tree_cs.heading("各厂商销售总金额", text="各厂商销售总金额")

    char3 = """SELECT 生产厂商, SUM(总金额)
                FROM sell
                WHERE 销售年 = '%s' AND 销售月 = '%s'
                GROUP BY 生产厂商""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT 生产厂商)
            FROM sell
            WHERE 销售年 = '%s' AND 销售月 = '%s'
            GROUP BY 生产厂商)a""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # 计算结果文本框
    Label(xs_by_win, text="销售总金额：").place(relx=0.02, rely=0.89)
    text_jhzje = Entry(xs_by_win)
    text_jhzje.place(relx=0.31, rely=0.88)

    char5 = """SELECT SUM(总金额)
               FROM sell
               WHERE 销售年 = '%s' AND 销售月 = '%s'""" % (
        time.strftime("%Y", time.localtime()), time.strftime("%m", time.localtime())
    )
    sum_gcszje = excuate.cal_r(char5)[0][0]

    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    xs_by_win.mainloop()

def _jdxs():
    xs_jd_win = Tk()
    xs_jd_win.title("本季度销售")
    xs_jd_win.geometry("300x380+300+250")

    # 查询结果窗口
    tree_by = ttk.Treeview(xs_jd_win, show="headings")
    tree_by.place(relx=0.01, rely=0.01)

    tree_by["columns"] = ("商品编号", "生产厂商", "商品名", "型号")

    tree_by.column("商品编号", width=62)
    tree_by.column("生产厂商", width=75)
    tree_by.column("商品名", width=75)
    tree_by.column("型号", width=75)

    tree_by.heading("商品编号", text="商品编号")
    tree_by.heading("生产厂商", text="生产厂商")
    tree_by.heading("商品名", text="商品名")
    tree_by.heading("型号", text="型号")

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

    char1 = """SELECT 商品编号, 生产厂商, 商品名, 型号
               FROM sell
               WHERE 销售年 = '%s' AND 销售月 >= '%s' AND 销售月 <= '%s'""" % (
        time.strftime("%Y", time.localtime()), A, B)
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(商品编号) FROM sell
               WHERE 销售年 = '%s' AND 销售月 >= '%s' AND 销售月 <= '%s'""" % (
        time.strftime("%Y", time.localtime()), A, B)
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:4]
        tree_by.insert("", i, values=z[i])

    # 分类查询结果窗口
    tree_cs = ttk.Treeview(xs_jd_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.56)

    tree_cs["columns"] = ("生产厂商", "各厂商销售总金额")

    tree_cs.column("生产厂商", width=143)
    tree_cs.column("各厂商销售总金额", width=143)

    tree_cs.heading("生产厂商", text="生产厂商")
    tree_cs.heading("各厂商销售总金额", text="各厂商销售总金额")


    char3  = """SELECT 生产厂商, SUM(总金额)
                FROM sell
                WHERE 销售年 = '%s' AND 销售月 >= '%s' AND 销售月 <= '%s'
                GROUP BY 生产厂商""" % (
        time.strftime("%Y", time.localtime()), A, B)
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
            (SELECT COUNT(DISTINCT 生产厂商)
            FROM sell
            WHERE 销售年 = '%s' AND 销售月 >= '%s' AND 销售月 <= '%s'
            GROUP BY 生产厂商)a""" % (
        time.strftime("%Y", time.localtime()), A, B)
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # 计算结果文本框
    Label(xs_jd_win, text="销售总金额：").place(relx=0.02, rely=0.89)
    text_jhzje = Entry(xs_jd_win)
    text_jhzje.place(relx=0.31, rely=0.88)

    char5 = """SELECT SUM(总金额)
               FROM sell
               WHERE 销售年 = '%s' AND 销售月 >= '%s' AND 销售月 <= '%s'""" % (
        time.strftime("%Y", time.localtime()), A, B)
    sum_gcszje = excuate.cal_r(char5)[0][0]

    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    xs_jd_win.mainloop()

def _jnxs():
    xs_jn_win = Tk()
    xs_jn_win.title("今年销售")
    xs_jn_win.geometry("300x380+300+250")

    # 查询结果窗口
    tree_jr = ttk.Treeview(xs_jn_win, show="headings")
    tree_jr.place(relx=0.01, rely=0.01)

    tree_jr["columns"] = ("商品编号", "生产厂商", "商品名", "型号")

    tree_jr.column("商品编号", width=62)
    tree_jr.column("生产厂商", width=75)
    tree_jr.column("商品名", width=75)
    tree_jr.column("型号", width=75)

    tree_jr.heading("商品编号", text="商品编号")
    tree_jr.heading("生产厂商", text="生产厂商")
    tree_jr.heading("商品名", text="商品名")
    tree_jr.heading("型号", text="型号")

    char1 = """SELECT 商品编号, 生产厂商, 商品名, 型号
                   FROM sell
                   WHERE 销售年 = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    find1 = excuate.cal_r(char1)

    char2 = """SELECT count(商品编号) FROM sell
                   WHERE 销售年 = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    num_col = excuate.cal_r(char2)[0][0]
    z = {}
    for i in range(0, num_col):
        z[i] = find1[i][0:4]
        tree_jr.insert("", i, values=z[i])

    # 分类查询结果窗口
    tree_cs = ttk.Treeview(xs_jn_win, show="headings", height=5)
    tree_cs.place(relx=0.01, rely=0.56)

    tree_cs["columns"] = ("生产厂商", "各厂商销售总金额")

    tree_cs.column("生产厂商", width=143)
    tree_cs.column("各厂商销售总金额", width=144)

    tree_cs.heading("生产厂商", text="生产厂商")
    tree_cs.heading("各厂商销售总金额", text="各厂商销售总金额")

    char3 = """SELECT 生产厂商, SUM(总金额)
                    FROM sell
                    WHERE 销售年 = '%s'
                    GROUP BY 生产厂商""" % (
        time.strftime("%Y", time.localtime()))
    find2 = excuate.cal_r(char3)

    char4 = """SELECT COUNT(*) FROM
                (SELECT COUNT(DISTINCT 生产厂商)
                FROM sell
                WHERE 销售年 = '%s'
                GROUP BY 生产厂商)a""" % (
        time.strftime("%Y", time.localtime()))
    num_c = excuate.cal_r(char4)[0][0]

    z = {}
    for i in range(0, num_c):
        z[i] = find2[i][0:2]
        tree_cs.insert("", i, values=z[i])

    # 计算结果文本框
    Label(xs_jn_win, text="销售总金额：").place(relx=0.02, rely=0.89)
    text_jhzje = Entry(xs_jn_win)
    text_jhzje.place(relx=0.31, rely=0.88)

    char5 = """SELECT SUM(总金额)
                   FROM sell
                   WHERE 销售年 = '%s'""" % (
        time.strftime("%Y", time.localtime()))
    sum_gcszje = excuate.cal_r(char5)[0][0]

    if num_col:
        text_jhzje.insert(0, sum_gcszje)
        text_jhzje.config(state=DISABLED)
    else:
        text_jhzje.insert(0, 0)
        text_jhzje.config(state=DISABLED)

    xs_jn_win.mainloop()
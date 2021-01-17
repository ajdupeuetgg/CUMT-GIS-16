# -*-coding:gbk-*-

from tkinter import *
import tkinter.ttk as ttk
import excuate
import tkinter.messagebox as message

def _yjck():
    def _yghcx():
        char1 = "SELECT 员工姓名 FROM employee WHERE 员工编号 = '%s'" % text_ygh.get()
        find1 = excuate.cal_r(char1)

        if find1:
            tree_ygh = ttk.Treeview(yjck_win, show="headings", height=15)
            tree_ygh.place(relx=0.02, rely=0.11)

            tree_ygh["columns"] = ("业务员编号", "员工姓名", "销售总金额")
            tree_ygh.column("业务员编号", width=102)
            tree_ygh.column("员工姓名", width=102)
            tree_ygh.column("销售总金额", width=102)

            tree_ygh.heading("业务员编号", text="业务员编号")
            tree_ygh.heading("员工姓名", text="员工姓名")
            tree_ygh.heading("销售总金额", text="销售总金额")

            char4 = """SELECT 员工编号, 员工姓名, SUM(总金额)
                       FROM employee, sell
                       WHERE 员工编号 = 业务员编号 AND 员工编号 = '%s'
                       GROUP BY 员工编号, 员工姓名
                       ORDER BY 员工编号""" % text_ygh.get()
            find4 = excuate.cal_r(char4)

            char5 = """SELECT COUNT(*) FROM
                      (SELECT 员工编号, 员工姓名, SUM(总金额)
                       FROM employee, sell
                       WHERE 员工编号 = 业务员编号 AND 员工编号 = '%s'
                       GROUP BY 员工编号, 员工姓名
                       ORDER BY 员工编号)a""" % text_ygh.get()
            num_c = excuate.cal_r(char5)[0][0]

            z = {}
            for i in range(0, num_c):
                z[i] = find4[i][0:3]
                tree_ygh.insert("", i, values=z[i])

        else:
            message.showerror('错误', '无该员工信息！')

    def _cxqb():
        char2 = """SELECT 员工编号, 员工姓名, SUM(总金额)
                   FROM employee, sell
                   WHERE 员工编号 = 业务员编号
                   GROUP BY 员工编号, 员工姓名
                   ORDER BY 员工编号"""
        find2 = excuate.cal_r(char2)

        char3 = """SELECT COUNT(*) FROM
                   (SELECT 员工编号, 员工姓名, SUM(总金额)
                    FROM employee, sell
                    WHERE 员工编号 = 业务员编号
                    GROUP BY 员工编号, 员工姓名
                    ORDER BY 员工编号)a"""
        num_c = excuate.cal_r(char3)[0][0]

        tree_yg = ttk.Treeview(yjck_win, show="headings", height=15)
        tree_yg.place(relx=0.02, rely=0.11)

        tree_yg["columns"] = ("业务员编号", "员工姓名", "销售总金额")
        tree_yg.column("业务员编号", width=102)
        tree_yg.column("员工姓名", width=102)
        tree_yg.column("销售总金额", width=102)

        tree_yg.heading("业务员编号", text="业务员编号")
        tree_yg.heading("员工姓名", text="员工姓名")
        tree_yg.heading("销售总金额", text="销售总金额")

        z = {}
        for i in range(0, num_c):
            z[i] = find2[i][0:3]
            tree_yg.insert("", i, values=z[i])

    yjck_win = Tk()
    yjck_win.geometry("325x375+550+320")
    yjck_win.title('查询员工销售额')

    Label(yjck_win, text="员工号：").place(relx=0.02, rely=0.015)

    text_ygh = Entry(yjck_win)
    text_ygh.place(relx=0.2, rely=0.01)

    yghcx_but = Button(yjck_win, text="查询", width=5, command=_yghcx)
    yghcx_but.place(relx=0.8, rely=0.018)

    cxqb_but = Button(yjck_win, text="显示全部员工销售额", width=34, command=_cxqb)
    cxqb_but.place(relx=0.02, rely=0.92)

    yjck_win.mainloop()
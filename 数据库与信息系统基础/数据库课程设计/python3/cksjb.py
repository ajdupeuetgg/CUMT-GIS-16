# -*-coding:gbk-*-

from tkinter import *
import tkinter.messagebox as message
import tkinter.ttk as ttk
import excuate

def _xchb():
    def _tjcx():
        char1 = "SELECT * FROM goods WHERE 商品名 = '%s' AND 型号 = '%s'" % (text_spm.get(), text_xh.get())
        find1 = excuate.cal_r(char1)
        if find1:
            char2 = "SELECT * FROM goods WHERE 商品名 = '%s' AND 型号 = '%s'" % (text_spm.get(), text_xh.get())
            find2 = excuate.cal_r(char2)

            char3 = """SELECT COUNT(*) FROM
                      (SELECT * FROM goods WHERE 商品名 = '%s' AND 型号 = '%s')a""" % (text_spm.get(), text_xh.get())
            num_c = excuate.cal_r(char3)[0][0]

            tree_h = ttk.Treeview(yjck_win, show="headings", height=15)
            tree_h.place(relx=0.02, rely=0.11)

            tree_h["columns"] = ("商品编号", "生产厂商", "商品名", "型号", "单价", "数量", "总金额", "进货年", "进货月", "进货日", "业务员编号")
            tree_h.column("商品编号", width=47)
            tree_h.column("生产厂商", width=48)
            tree_h.column("商品名", width=48)
            tree_h.column("型号", width=47)
            tree_h.column("单价", width=48)
            tree_h.column("数量", width=47)
            tree_h.column("总金额", width=48)
            tree_h.column("进货年", width=48)
            tree_h.column("进货月", width=47)
            tree_h.column("进货日", width=47)
            tree_h.column("业务员编号", width=47)

            tree_h.heading("商品编号", text="商品编号")
            tree_h.heading("生产厂商", text="生产厂商")
            tree_h.heading("商品名", text="商品名")
            tree_h.heading("型号", text="型号")
            tree_h.heading("单价", text="单价")
            tree_h.heading("数量", text="数量")
            tree_h.heading("总金额", text="总金额")
            tree_h.heading("进货年", text="进货年")
            tree_h.heading("进货月", text="进货月")
            tree_h.heading("进货日", text="进货日")
            tree_h.heading("业务员编号", text="业务员编号")

            z = {}
            for i in range(0, num_c):
                z[i] = find2[i][0:11]
                tree_h.insert("", i, values=z[i])
        else:
            message.showerror('错误', '无现存货物信息！')

    def _cxqb():
        char2 = "SELECT * FROM goods"
        find2 = excuate.cal_r(char2)

        char3 = """SELECT COUNT(*) FROM
                   (SELECT * FROM goods)a"""
        num_c = excuate.cal_r(char3)[0][0]

        tree_h = ttk.Treeview(yjck_win, show="headings", height=15)
        tree_h.place(relx=0.02, rely=0.11)

        tree_h["columns"] = ("商品编号", "生产厂商", "商品名","型号","单价","数量","总金额","进货年","进货月","进货日","业务员编号")
        tree_h.column("商品编号", width=47)
        tree_h.column("生产厂商", width=48)
        tree_h.column("商品名", width=48)
        tree_h.column("型号", width=47)
        tree_h.column("单价", width=48)
        tree_h.column("数量", width=47)
        tree_h.column("总金额", width=48)
        tree_h.column("进货年", width=48)
        tree_h.column("进货月", width=47)
        tree_h.column("进货日", width=47)
        tree_h.column("业务员编号", width=47)

        tree_h.heading("商品编号", text="商品编号")
        tree_h.heading("生产厂商", text="生产厂商")
        tree_h.heading("商品名", text="商品名")
        tree_h.heading("型号", text="型号")
        tree_h.heading("单价", text="单价")
        tree_h.heading("数量", text="数量")
        tree_h.heading("总金额", text="总金额")
        tree_h.heading("进货年", text="进货年")
        tree_h.heading("进货月", text="进货月")
        tree_h.heading("进货日", text="进货日")
        tree_h.heading("业务员编号", text="业务员编号")


        z = {}
        for i in range(0, num_c):
            z[i] = find2[i][0:11]
            tree_h.insert("", i, values=z[i])

    yjck_win = Tk()
    yjck_win.geometry("550x375+550+320")
    yjck_win.title('查询现存货物')

    Label(yjck_win, text="商品名：").place(relx=0.019, rely=0.015)
    Label(yjck_win, text="型号：").place(relx=0.42, rely=0.015)

    text_spm = Entry(yjck_win, width=14)
    text_spm.place(relx=0.15, rely=0.01)
    text_xh = Entry(yjck_win, width=14)
    text_xh.place(relx=0.52, rely=0.01)

    yghcx_but = Button(yjck_win, text="查询", width=6, command=_tjcx)
    yghcx_but.place(relx=0.85, rely=0.018)

    cxqb_but = Button(yjck_win, text="显示全部现存商品", width=58, command=_cxqb)
    cxqb_but.place(relx=0.02, rely=0.92)

    yjck_win.mainloop()

def _scys():
    def _tjcx():
        char1 = "SELECT * FROM sell WHERE 商品名 = '%s' AND 型号 = '%s'" % (text_spm.get(), text_xh.get())
        find1 = excuate.cal_r(char1)
        if find1:
            char2 = "SELECT * FROM sell WHERE 商品名 = '%s' AND 型号 = '%s'" % (text_spm.get(), text_xh.get())
            find2 = excuate.cal_r(char2)

            char3 = """SELECT COUNT(*) FROM
                         (SELECT * FROM sell WHERE 商品名 = '%s' AND 型号 = '%s')a""" % (text_spm.get(), text_xh.get())
            num_c = excuate.cal_r(char3)[0][0]

            tree_h = ttk.Treeview(yjck_win, show="headings", height=15)
            tree_h.place(relx=0.02, rely=0.11)

            tree_h["columns"] = ("商品编号", "生产厂商", "商品名", "型号", "单价", "数量", "总金额", "销售年", "销售月", "销售日", "业务员编号")
            tree_h.column("商品编号", width=47)
            tree_h.column("生产厂商", width=48)
            tree_h.column("商品名", width=48)
            tree_h.column("型号", width=47)
            tree_h.column("单价", width=48)
            tree_h.column("数量", width=47)
            tree_h.column("总金额", width=48)
            tree_h.column("销售年", width=48)
            tree_h.column("销售月", width=47)
            tree_h.column("销售日", width=47)
            tree_h.column("业务员编号", width=47)

            tree_h.heading("商品编号", text="商品编号")
            tree_h.heading("生产厂商", text="生产厂商")
            tree_h.heading("商品名", text="商品名")
            tree_h.heading("型号", text="型号")
            tree_h.heading("单价", text="单价")
            tree_h.heading("数量", text="数量")
            tree_h.heading("总金额", text="总金额")
            tree_h.heading("销售年", text="销售年")
            tree_h.heading("销售月", text="销售月")
            tree_h.heading("销售日", text="销售日")
            tree_h.heading("业务员编号", text="业务员编号")

            z = {}
            for i in range(0, num_c):
                z[i] = find2[i][0:11]
                tree_h.insert("", i, values=z[i])
        else:
            message.showerror('错误', '无售出货物信息！')

    def _cxqb():
        char2 = "SELECT * FROM sell"
        find2 = excuate.cal_r(char2)

        char3 = """SELECT COUNT(*) FROM
                      (SELECT * FROM sell)a"""
        num_c = excuate.cal_r(char3)[0][0]

        tree_h = ttk.Treeview(yjck_win, show="headings", height=15)
        tree_h.place(relx=0.02, rely=0.11)

        tree_h["columns"] = ("商品编号", "生产厂商", "商品名", "型号", "单价", "数量", "总金额", "销售年", "销售月", "销售日", "业务员编号")
        tree_h.column("商品编号", width=47)
        tree_h.column("生产厂商", width=48)
        tree_h.column("商品名", width=48)
        tree_h.column("型号", width=47)
        tree_h.column("单价", width=48)
        tree_h.column("数量", width=47)
        tree_h.column("总金额", width=48)
        tree_h.column("销售年", width=48)
        tree_h.column("销售月", width=47)
        tree_h.column("销售日", width=47)
        tree_h.column("业务员编号", width=47)

        tree_h.heading("商品编号", text="商品编号")
        tree_h.heading("生产厂商", text="生产厂商")
        tree_h.heading("商品名", text="商品名")
        tree_h.heading("型号", text="型号")
        tree_h.heading("单价", text="单价")
        tree_h.heading("数量", text="数量")
        tree_h.heading("总金额", text="总金额")
        tree_h.heading("销售年", text="销售年")
        tree_h.heading("销售月", text="销售月")
        tree_h.heading("销售日", text="销售日")
        tree_h.heading("业务员编号", text="业务员编号")

        z = {}
        for i in range(0, num_c):
            z[i] = find2[i][0:11]
            tree_h.insert("", i, values=z[i])

    yjck_win = Tk()
    yjck_win.geometry("550x375+550+320")
    yjck_win.title('查询销售货物')

    Label(yjck_win, text="商品名：").place(relx=0.019, rely=0.015)
    Label(yjck_win, text="型号：").place(relx=0.42, rely=0.015)

    text_spm = Entry(yjck_win, width=14)
    text_spm.place(relx=0.15, rely=0.01)
    text_xh = Entry(yjck_win, width=14)
    text_xh.place(relx=0.52, rely=0.01)

    yghcx_but = Button(yjck_win, text="查询", width=6, command=_tjcx)
    yghcx_but.place(relx=0.85, rely=0.018)

    cxqb_but = Button(yjck_win, text="显示全部售出商品", width=58, command=_cxqb)
    cxqb_but.place(relx=0.02, rely=0.92)

    yjck_win.mainloop()

def _xsth():
    xsth_win = Tk()
    xsth_win.geometry("550x310+525+275")
    xsth_win.title('显示退货表')

    tree_h = ttk.Treeview(xsth_win, show="headings", height=15)
    tree_h.place(relx=0.02, rely=0.01)

    tree_h["columns"] = ("商品编号", "生产厂商", "商品名", "型号", "单价", "数量", "总金额", "退货年", "退货月", "退货日", "业务员编号")
    tree_h.column("商品编号", width=47)
    tree_h.column("生产厂商", width=48)
    tree_h.column("商品名", width=48)
    tree_h.column("型号", width=47)
    tree_h.column("单价", width=48)
    tree_h.column("数量", width=47)
    tree_h.column("总金额", width=50)
    tree_h.column("退货年", width=48)
    tree_h.column("退货月", width=47)
    tree_h.column("退货日", width=47)
    tree_h.column("业务员编号", width=50)

    tree_h.heading("商品编号", text="商品编号")
    tree_h.heading("生产厂商", text="生产厂商")
    tree_h.heading("商品名", text="商品名")
    tree_h.heading("型号", text="型号")
    tree_h.heading("单价", text="单价")
    tree_h.heading("数量", text="数量")
    tree_h.heading("总金额", text="总金额")
    tree_h.heading("退货年", text="退货年")
    tree_h.heading("退货月", text="退货月")
    tree_h.heading("退货日", text="退货日")
    tree_h.heading("业务员编号", text="业务员编号")

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
    xsyg_win.title('显示员工表')
    xsyg_win.geometry("300x270+300+250")

    tree_yg = ttk.Treeview(xsyg_win, height=10, show="headings")
    tree_yg.place(relx=0, rely=0)

    tree_yg["columns"] = ("员工编号", "员工姓名", "员工电话", "员工地址")

    tree_yg.column("员工编号", width=75, anchor='center')
    tree_yg.column("员工姓名", width=75, anchor='center')
    tree_yg.column("员工电话", width=75, anchor='center')
    tree_yg.column("员工地址", width=75, anchor='center')

    tree_yg.heading("员工编号", text="员工编号")
    tree_yg.heading("员工姓名", text="员工姓名")
    tree_yg.heading("员工电话", text="员工电话")
    tree_yg.heading("员工地址", text="员工地址")

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
            message.showinfo('提示', '修改成功！')
            changed_but.destroy()

        changed_but = Button(xsyg_win, text="确认修改", width=9, command=_changed)
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
                char = "UPDATE employee SET %s = '%s' WHERE 员工编号 = '%s'" % (
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
        char = "DELETE FROM employee WHERE 员工编号 = '%s'" % find1[rn-1][0]
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

    change_but = Button(xsyg_win, text="修改记录", width=9, command=_change)
    change_but.place(relx=0.16, rely=0.82)
    delete_but = Button(xsyg_win, text="删除记录", width=9, command=_del)
    delete_but.place(relx=0.56, rely=0.82)

def _jhsb():
    xsyg_win = Tk()
    xsyg_win.title('显示进货商表')
    xsyg_win.geometry("375x270+300+250")

    tree_yg = ttk.Treeview(xsyg_win, height=10, show="headings")
    tree_yg.place(relx=0, rely=0)

    tree_yg["columns"] = ("厂商编号", "厂商名称", "法人代表", "厂商地址", "电话")

    tree_yg.column("厂商编号", width=75, anchor='center')
    tree_yg.column("厂商名称", width=75, anchor='center')
    tree_yg.column("法人代表", width=75, anchor='center')
    tree_yg.column("厂商地址", width=75, anchor='center')
    tree_yg.column("电话", width=75, anchor='center')

    tree_yg.heading("厂商编号", text="厂商编号")
    tree_yg.heading("厂商名称", text="厂商名称")
    tree_yg.heading("法人代表", text="法人代表")
    tree_yg.heading("厂商地址", text="厂商地址")
    tree_yg.heading("电话", text="电话")

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
            message.showinfo('提示', '修改成功！')
            changed_but.destroy()

        changed_but = Button(xsyg_win, text="确认修改", width=9, command=_changed)
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
                char = "UPDATE manufacturer SET %s = '%s' WHERE 厂商编号 = '%s'" % (
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
        char = "DELETE FROM manufacturer WHERE 厂商编号 = '%s'" % find1[rn - 1][0]
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

    change_but = Button(xsyg_win, text="修改记录", width=9, command=_change)
    change_but.place(relx=0.16, rely=0.82)
    delete_but = Button(xsyg_win, text="删除记录", width=9, command=_del)
    delete_but.place(relx=0.56, rely=0.82)

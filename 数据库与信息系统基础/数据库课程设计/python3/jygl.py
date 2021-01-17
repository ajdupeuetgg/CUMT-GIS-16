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
            message.showerror('提示','请选择生产厂商！')
            return
        if text_spmc.get():
            pass
        else:
            message.showerror('提示','请输入商品名称！')
            return
        if text_xh.get():
            pass
        else:
            message.showerror('提示','请输入型号！')
            return
        if text_dj.get():
            pass
        else:
            message.showerror('提示','请输入单价！')
            return
        if text_sl.get():
            pass
        else:
            message.showerror('提示','请输入数量！')
            return
        if text_j_n.get():
            pass
        else:
            message.showerror('提示','请输入进货年份！')
            return
        if text_j_y.get():
            pass
        else:
            message.showerror('提示', '请输入进货月份！')
            return
        if text_j_r.get():
            pass
        else:
            message.showerror('提示', '请输入进货日！')
            return
        if text_ywybh.get():
            pass
        else:
            message.showerror('提示', '请选择业务员编号！')
            return
        char = """INSERT INTO goods(生产厂商,商品名,型号,单价,数量,总金额,进货年,进货月,进货日,业务员编号)
                  VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            text_sccs.get(),text_spmc.get(),text_xh.get(),text_dj.get(),text_sl.get(),
            int(text_dj.get())*int(text_sl.get()),text_j_n.get(),text_j_y.get(),text_j_r.get(),text_ywybh.get())
        excuate.cal_nr(char)
        message.showinfo('提示', '插入成功！')
        _clearsp()

    def _insertcs():
        char = """INSERT INTO manufacturer(厂商名称,法人代表,厂商地址,电话)
                  VALUES ('%s','%s','%s','%s')""" % (
            text_csmc.get(),text_frdb.get(),text_csdz.get(),text_dh.get())
        excuate.cal_nr(char)
        message.showinfo('提示', '插入成功！')
        _clearcs()
    
    jy_jh_win = Tk()
    jy_jh_win.geometry("450x490+600+200")
    jy_jh_win.title('添加商品入库')

    frame_tjsp = LabelFrame(jy_jh_win, text="添加商品", labelanchor="nw")
    frame_tjsp.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.45)

    Label(frame_tjsp, text="商品编号：").place(relx=0.03, rely=0.03)
    text_spbh = Entry(frame_tjsp, width=8)
    text_spbh.insert(0, '自动添加')
    text_spbh.place(relx=0.28, rely=0.03)

    Label(frame_tjsp, text="商品名称：").place(relx=0.49, rely=0.03)
    text_spmc = Entry(frame_tjsp, width=8)
    text_spmc.place(relx=0.69, rely=0.03)

    Label(frame_tjsp, text="生产厂商：").place(relx=0.03, rely=0.2)
    val1 = excuate.fet_list("厂商名称","manufacturer")
    text_sccs = ttk.Combobox(frame_tjsp, width=6, values=val1)
    text_sccs.place(relx=0.28, rely=0.2)

    Label(frame_tjsp, text="型号：").place(relx=0.49, rely=0.2)
    text_xh = Entry(frame_tjsp, width=8)
    text_xh.place(relx=0.69, rely=0.2)

    Label(frame_tjsp, text="单价：").place(relx=0.03, rely=0.37)
    text_dj = Entry(frame_tjsp, width=8)
    text_dj.place(relx=0.28, rely=0.37)

    Label(frame_tjsp, text="数量：").place(relx=0.49, rely=0.37)
    text_sl = Entry(frame_tjsp, width=8)
    text_sl.place(relx=0.69, rely=0.37)

    Label(frame_tjsp, text="进货日期：").place(relx=0.03, rely=0.53)
    text_j_n = Entry(frame_tjsp, width=3)
    text_j_n.place(relx=0.28, rely=0.53)
    Label(frame_tjsp, text="年").place(relx=0.38, rely=0.53)
    text_j_y = Entry(frame_tjsp, width=3)
    text_j_y.place(relx=0.46, rely=0.53)
    Label(frame_tjsp, text="月").place(relx=0.58, rely=0.53)
    text_j_r = Entry(frame_tjsp, width=3)
    text_j_r.place(relx=0.64, rely=0.53)
    Label(frame_tjsp, text="日").place(relx=0.78, rely=0.53)

    Label(frame_tjsp, text="业务员编号：").place(relx=0.03, rely=0.69)
    val2 = excuate.fet_list("员工编号","employee")
    text_ywybh = ttk.Combobox(frame_tjsp, width=4, values=val2)
    text_ywybh.place(relx=0.31, rely=0.69)

    Label(frame_tjsp, text="总金额：").place(relx=0.49, rely=0.69)
    text_zje = Entry(frame_tjsp, width=6)
    text_zje.place(relx=0.69, rely=0.69)
    text_zje.insert(0, '自动计算')

    tjrk_but = Button(frame_tjsp, text="添加入库", width=8, command=_insertsp)
    tjrk_but.place(relx=0.2, rely=0.85)

    tjrk_but = Button(frame_tjsp, text="清空重填", width=8, command=_clearsp)
    tjrk_but.place(relx=0.58, rely=0.85)


    frame_tjcs = LabelFrame(jy_jh_win, text="添加厂商", labelanchor="nw")
    frame_tjcs.place(relx=0.05, rely=0.50, relwidth=0.9, relheight=0.45)

    Label(frame_tjcs, text="厂商名称：").place(relx=0.03, rely=0.03)
    text_csmc = Entry(frame_tjcs, width=24)
    text_csmc.place(relx=0.31, rely=0.03)

    Label(frame_tjcs, text="法人代表：").place(relx=0.03, rely=0.23)
    text_frdb = Entry(frame_tjcs, width=24)
    text_frdb.place(relx=0.31, rely=0.23)

    Label(frame_tjcs, text="电话：").place(relx=0.03, rely=0.47)
    text_dh = Entry(frame_tjcs, width=24)
    text_dh.place(relx=0.31, rely=0.47)

    Label(frame_tjcs, text="厂商地址：").place(relx=0.03, rely=0.68)
    text_csdz = Entry(frame_tjcs, width=24)
    text_csdz.place(relx=0.31, rely=0.68)

    tjrk_but = Button(frame_tjcs, text="添加入库", width=8, command=_insertcs)
    tjrk_but.place(relx=0.2, rely=0.85)

    tjrk_but = Button(frame_tjcs, text="清空重填", width=8, command=_clearcs)
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
            message.showerror('提示','请选择生产厂商！')
            return
        if text_spmc.get():
            pass
        else:
            message.showerror('提示','请输入商品名称！')
            return
        if text_xh.get():
            pass
        else:
            message.showerror('提示','请输入型号！')
            return
        if text_dj.get():
            pass
        else:
            message.showerror('提示','请输入单价！')
            return
        if text_sl.get():
            pass
        else:
            message.showerror('提示','请输入数量！')
            return
        if text_j_n.get():
            pass
        else:
            message.showerror('提示','请输入销售年份！')
            return
        if text_j_y.get():
            pass
        else:
            message.showerror('提示', '请输入销售月份！')
            return
        if text_j_r.get():
            pass
        else:
            message.showerror('提示', '请输入销售日！')
            return
        if text_ywybh.get():
            pass
        else:
            message.showerror('提示', '请选择业务员编号！')
            return

        val3 = excuate.fet_list("商品名", "goods")
        if text_spmc.get() in val3:
            num_goods = excuate.cal_r("SELECT 数量 FROM goods WHERE 商品名 = '%s'" % text_spmc.get())
            num = num_goods[0][0] - int(text_sl.get())
            if num >= 0:
                char1 = """INSERT INTO sell (生产厂商,商品名,型号,单价,数量,总金额,销售年,销售月,销售日,业务员编号)
                                  VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
                    text_sccs.get(), text_spmc.get(), text_xh.get(), text_dj.get(), text_sl.get(),
                    int(text_dj.get()) * int(text_sl.get()), text_j_n.get(), text_j_y.get(), text_j_r.get(),
                    text_ywybh.get())
                excuate.cal_nr(char1)

                char2 = "UPDATE goods SET 数量 = '%s' WHERE 商品名 = '%s'" % (
                    num, text_spmc.get())
                excuate.cal_nr(char2)

                message.showinfo('提示', '插入销售记录成功！')
                _clearsp()
            else:
                message.showerror('错误', '剩余货品数量不足！')
                text_sl.delete(0, END)
        else:
            message.showerror('错误', '没有该种商品！')
            _clearsp()

    jy_xs_win = Tk()
    jy_xs_win.geometry("450x290+600+200")
    jy_xs_win.title("销售登记")

    Label(jy_xs_win, text="商品编号：").place(relx=0.03, rely=0.03)
    text_spbh = Entry(jy_xs_win, width=8)
    text_spbh.insert(0, '自动添加')
    text_spbh.place(relx=0.28, rely=0.03)

    Label(jy_xs_win, text="商品名称：").place(relx=0.49, rely=0.03)
    text_spmc = Entry(jy_xs_win, width=8)
    text_spmc.place(relx=0.69, rely=0.03)

    Label(jy_xs_win, text="生产厂商：").place(relx=0.03, rely=0.2)
    val1 = excuate.fet_list("厂商名称", "manufacturer")
    text_sccs = ttk.Combobox(jy_xs_win, width=6, values=val1)
    text_sccs.place(relx=0.28, rely=0.2)

    Label(jy_xs_win, text="型号：").place(relx=0.49, rely=0.2)
    text_xh = Entry(jy_xs_win, width=8)
    text_xh.place(relx=0.69, rely=0.2)

    Label(jy_xs_win, text="单价：").place(relx=0.03, rely=0.37)
    text_dj = Entry(jy_xs_win, width=8)
    text_dj.place(relx=0.28, rely=0.37)

    Label(jy_xs_win, text="数量：").place(relx=0.49, rely=0.37)
    text_sl = Entry(jy_xs_win, width=8)
    text_sl.place(relx=0.69, rely=0.37)

    Label(jy_xs_win, text="销售日期：").place(relx=0.03, rely=0.53)
    text_j_n = Entry(jy_xs_win, width=3)
    text_j_n.place(relx=0.28, rely=0.53)
    Label(jy_xs_win, text="年").place(relx=0.38, rely=0.53)
    text_j_y = Entry(jy_xs_win, width=3)
    text_j_y.place(relx=0.46, rely=0.53)
    Label(jy_xs_win, text="月").place(relx=0.58, rely=0.53)
    text_j_r = Entry(jy_xs_win, width=3)
    text_j_r.place(relx=0.64, rely=0.53)
    Label(jy_xs_win, text="日").place(relx=0.78, rely=0.53)

    Label(jy_xs_win, text="业务员编号：").place(relx=0.03, rely=0.69)
    val2 = excuate.fet_list("员工编号", "employee")
    text_ywybh = ttk.Combobox(jy_xs_win, width=4, values=val2)
    text_ywybh.place(relx=0.31, rely=0.69)

    Label(jy_xs_win, text="总金额：").place(relx=0.49, rely=0.69)
    text_zje = Entry(jy_xs_win, width=6)
    text_zje.place(relx=0.69, rely=0.69)
    text_zje.insert(0, '自动计算')

    tjrk_but = Button(jy_xs_win, text="销售", width=8, command=_sellsp)
    tjrk_but.place(relx=0.2, rely=0.85)

    tjrk_but = Button(jy_xs_win, text="清空重填", width=8, command=_clearsp)
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
            message.showerror('提示','请选择生产厂商！')
            return
        if text_spmc.get():
            pass
        else:
            message.showerror('提示','请输入商品名称！')
            return
        if text_xh.get():
            pass
        else:
            message.showerror('提示','请输入型号！')
            return
        if text_dj.get():
            pass
        else:
            message.showerror('提示','请输入单价！')
            return
        if text_sl.get():
            pass
        else:
            message.showerror('提示','请输入数量！')
            return
        if text_j_n.get():
            pass
        else:
            message.showerror('提示','请输入退货年份！')
            return
        if text_j_y.get():
            pass
        else:
            message.showerror('提示', '请输入退货月份！')
            return
        if text_j_r.get():
            pass
        else:
            message.showerror('提示', '请输入退货日！')
            return
        if text_ywybh.get():
            pass
        else:
            message.showerror('提示', '请选择业务员编号！')
            return

        val3 = excuate.fet_list("商品名", "sell")
        if text_spmc.get() in val3:
            val4 = excuate.fet_list("商品名", "retreat")
            if text_spmc.get() in val4:
                num_retreat = excuate.cal_r("SELECT 数量 FROM retreat WHERE 商品名 = '%s'" % text_spmc.get())
                numm = num_retreat[0][0] + int(text_sl.get())
                char3 = "UPDATE retreat SET 数量 = '%s' WHERE 商品名 = '%s'" % (
                    numm,text_spmc.get())
                excuate.cal_nr(char3)
            else:
                char1 = """INSERT INTO retreat (厂商,商品名,型号,单价,数量,总金额,退货年,退货月,退货日,业务员编号)
                                            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
                    text_sccs.get(), text_spmc.get(), text_xh.get(), text_dj.get(), text_sl.get(),
                    int(text_dj.get()) * int(text_sl.get()), text_j_n.get(), text_j_y.get(), text_j_r.get(),
                    text_ywybh.get())
                excuate.cal_nr(char1)

            num_sell = excuate.cal_r("SELECT 数量 FROM sell WHERE 商品名 = '%s'" % text_spmc.get())
            num = num_sell[0][0] - int(text_sl.get())

            char2 = "UPDATE sell SET 数量 = '%s' WHERE 商品名 = '%s'" % (
                num, text_spmc.get())
            excuate.cal_nr(char2)

            num_goods = excuate.cal_r("SELECT 数量 FROM goods WHERE 商品名 = '%s'" % text_spmc.get())
            nummb = num_goods[0][0] + int(text_sl.get())

            char2 = "UPDATE goods SET 数量 = '%s' WHERE 商品名 = '%s'" % (
                nummb, text_spmc.get())
            excuate.cal_nr(char2)

            message.showinfo('提示', '插入退货记录成功！')
            _clearsp()
        else:
            message.showerror('错误', '没有售出过该种商品！')
            _clearsp()



    jy_th_win = Tk()
    jy_th_win.geometry("450x290+600+200")
    jy_th_win.title("退货登记")

    Label(jy_th_win, text="商品编号：").place(relx=0.03, rely=0.03)
    text_spbh = Entry(jy_th_win, width=8)
    text_spbh.insert(0, '自动添加')
    text_spbh.place(relx=0.28, rely=0.03)

    Label(jy_th_win, text="商品名称：").place(relx=0.49, rely=0.03)
    text_spmc = Entry(jy_th_win, width=8)
    text_spmc.place(relx=0.69, rely=0.03)

    Label(jy_th_win, text="生产厂商：").place(relx=0.03, rely=0.2)
    val1 = excuate.fet_list("厂商名称", "manufacturer")
    text_sccs = ttk.Combobox(jy_th_win, width=6, values=val1)
    text_sccs.place(relx=0.28, rely=0.2)

    Label(jy_th_win, text="型号：").place(relx=0.49, rely=0.2)
    text_xh = Entry(jy_th_win, width=8)
    text_xh.place(relx=0.69, rely=0.2)

    Label(jy_th_win, text="单价：").place(relx=0.03, rely=0.37)
    text_dj = Entry(jy_th_win, width=8)
    text_dj.place(relx=0.28, rely=0.37)

    Label(jy_th_win, text="数量：").place(relx=0.49, rely=0.37)
    text_sl = Entry(jy_th_win, width=8)
    text_sl.place(relx=0.69, rely=0.37)

    Label(jy_th_win, text="退货日期：").place(relx=0.03, rely=0.53)
    text_j_n = Entry(jy_th_win, width=3)
    text_j_n.place(relx=0.28, rely=0.53)
    Label(jy_th_win, text="年").place(relx=0.38, rely=0.53)
    text_j_y = Entry(jy_th_win, width=3)
    text_j_y.place(relx=0.46, rely=0.53)
    Label(jy_th_win, text="月").place(relx=0.58, rely=0.53)
    text_j_r = Entry(jy_th_win, width=3)
    text_j_r.place(relx=0.64, rely=0.53)
    Label(jy_th_win, text="日").place(relx=0.78, rely=0.53)

    Label(jy_th_win, text="业务员编号：").place(relx=0.03, rely=0.69)
    val2 = excuate.fet_list("员工编号", "employee")
    text_ywybh = ttk.Combobox(jy_th_win, width=4, values=val2)
    text_ywybh.place(relx=0.31, rely=0.69)

    Label(jy_th_win, text="总金额：").place(relx=0.49, rely=0.69)
    text_zje = Entry(jy_th_win, width=6)
    text_zje.place(relx=0.69, rely=0.69)
    text_zje.insert(0, '自动计算')

    tjrk_but = Button(jy_th_win, text="退货", width=8, command=_retreatsp)
    tjrk_but.place(relx=0.2, rely=0.85)

    tjrk_but = Button(jy_th_win, text="清空重填", width=8, command=_clearsp)
    tjrk_but.place(relx=0.58, rely=0.85)

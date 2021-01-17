# -*- coding:utf-8 -*-

import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from osgeo import gdal
from osgeo import gdal_array
import turtle
import time

root = tk.Tk()
FILEWAY = ""
labelImage = tk.Label()
initWin = '500x100+750+400'
w_box, h_box = 800, 800
default_dir = "/Users/apple/Documents/GDAL"


def resize(w, h, wbox, hbox, pil_image):
    f1 = 1.0 * wbox / w
    f2 = 1.0 * hbox / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


def refreshImage(fway):
    global labelImage
    labelImage.place_forget()
    pil_image = Image.open(fway)
    # 获取图像的原始大小
    w, h = pil_image.size
    # 缩放图像让它保持比例，同时限制在一个矩形框范围内
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    # 把PIL图像对象转变为Tkinter的PhotoImage对象
    tk_image = ImageTk.PhotoImage(pil_image_resized)

    root.geometry('{}x{}+600+150'.format(w_box, h_box))
    labelImage = tk.Label(root, image=tk_image, width=w_box, height=h_box)
    labelImage.image = tk_image
    labelImage.place(relx=0, rely=0)
    global FILEWAY
    FILEWAY = fway


def _clear():
    global labelImage
    labelImage.place_forget()
    root.geometry(initWin)
    global FILEWAY
    FILEWAY = ""


def _open():
    global FILEWAY
    FILEWAY = filedialog.askopenfilename(title="选择遥感影像", initialdir=(os.path.expanduser(default_dir)))
    if FILEWAY:
        refreshImage(FILEWAY)


def _showInfo():
    if FILEWAY:
        dataset = gdal.Open(FILEWAY)
        im_width = dataset.RasterXSize
        im_height = dataset.RasterYSize
        im_proj = dataset.GetProjection()
        rootInfo = tk.Toplevel()
        rootInfo.geometry('450x320+750+300')
        rootInfo.title('基本信息')
        labelInfo_size = tk.Label(rootInfo, text="影像尺寸：{} * {}".format(im_width, im_height), font=("黑体", 18), height=2)
        labelInfo_size.pack()
        labelInfo_proj = tk.Label(rootInfo, text="投影信息：" + im_proj, font=("黑体", 18), height=10, wraplength=320)
        labelInfo_proj.pack()
    else:
        messagebox.showerror("提示", "未打开任何图像！")


def _swapBand():
    def change(band1, band2, band3):
        arr = gdal_array.LoadFile(FILEWAY)
        gdal_array.SaveArray(arr[[band1, band2, band3], :], "swap.tif", format="GTiff", prototype=FILEWAY)
        resWay = FILEWAY[:FILEWAY.rfind('/') + 1] + "swap.tif"
        time.sleep(2)
        refreshImage(resWay)
        rootBand.destroy()

    if FILEWAY:
        rootBand = tk.Toplevel()
        rootBand.geometry('150x100+750+300')
        rootBand.title('波段选择')
        tk.Label(rootBand, text="波段1：  ").grid(row=0)
        tk.Label(rootBand, text="波段2：  ").grid(row=1)
        tk.Label(rootBand, text="波段3：  ").grid(row=2)

        number1 = tk.StringVar()
        band1Chosen = ttk.Combobox(rootBand, width=6, textvariable=number1, state='readonly')
        band1Chosen['values'] = (1, 2, 3)
        band1Chosen.grid(row=0, column=1)
        band1Chosen.current(0)

        number2 = tk.StringVar()
        band2Chosen = ttk.Combobox(rootBand, width=6, textvariable=number2, state='readonly')
        band2Chosen['values'] = (1, 2, 3)
        band2Chosen.grid(row=1, column=1)
        band2Chosen.current(1)

        number3 = tk.StringVar()
        band3Chosen = ttk.Combobox(rootBand, width=6, textvariable=number3, state='readonly')
        band3Chosen['values'] = (1, 2, 3)
        band3Chosen.grid(row=2, column=1)
        band3Chosen.current(2)

        confirm = tk.Button(rootBand, text="确认", width=8, command=lambda: change(int(band1Chosen.get()) - 1,
                                                                                 int(band2Chosen.get()) - 1,
                                                                                 int(band3Chosen.get()) - 1))
        confirm.grid(row=3, columnspan=2)
    else:
        messagebox.showerror("提示", "未打开任何图像！")


def _gram():
    def histogram(a):
        fa = a.flat
        n = gdal_array.numpy.searchsorted(gdal_array.numpy.sort(fa), list(range(0, 256)))
        n = gdal_array.numpy.concatenate([n, [len(fa)]])
        hist = n[1:] - n[:-1]
        return hist

    def draw_histogram(hist, scale=True):
        turtle.color("black")
        axes = ((-355, -200), (355, -200), (-355, -200), (-355, 250))
        turtle.up()
        for p in axes:
            turtle.goto(p)
            turtle.down()
        turtle.up()
        turtle.goto(0, -250)
        turtle.write("值", font=("SimHei, ", 18, "bold"))
        turtle.up()
        turtle.goto(-400, 280)
        turtle.write("频率", font=("SimHei, ", 18, "bold"))
        x = -355
        y = -200
        turtle.up()
        for i in range(1, 11):
            x = x + 65
            turtle.goto(x, y)
            turtle.down()
            turtle.goto(x, y - 10)
            turtle.up()
            turtle.goto(x, y - 25)
            turtle.write("{}".format((i * 25)), align="center")
        x = -355
        y = -200
        turtle.up()
        pixels = sum(hist[0])
        if scale:
            maxValue = 0
            for h in hist:
                hmax = h.max()
                if hmax > maxValue:
                    maxValue = hmax
            pixels = maxValue
        label = int(pixels / 10)
        for i in range(1, 11):
            y = y + 45
            turtle.goto(x, y)
            turtle.down()
            turtle.goto(x - 10, y)
            turtle.up()
            turtle.goto(x - 15, y - 6)
            turtle.write("{}".format((i * label)), align="right")
        x_ratio = 709.0 / 256
        y_ratio = 450.0 / pixels
        colors = ["red", "green", "blue"]
        for j in range(len(hist)):
            h = hist[j]
            x = -354
            y = -199
            turtle.up()
            turtle.goto(x, y)
            turtle.down()
            turtle.color(colors[j])
            for i in range(256):
                x = i * x_ratio
                y = h[i] * y_ratio
                x = x - (709 / 2)
                y = y + -199
                turtle.goto((x, y))

    if FILEWAY:
        turtle.tracer(False)
        histograms = []
        arr = gdal_array.LoadFile(FILEWAY)
        for b in arr:
            histograms.append(histogram(b))
        draw_histogram(histograms)
        turtle.pen(shown=False)
        turtle.done()
    else:
        messagebox.showerror("提示", "未打开任何图像！")


def _save():
    if FILEWAY:
        image = Image.open(FILEWAY)
        saveWay = filedialog.askdirectory(title="选择保存路径", initialdir=(os.path.expanduser(default_dir)))
        image.save(saveWay + '/result.tif')
    else:
        messagebox.showerror("提示", "未打开任何图像！")


root.title('OpenSource GDAL大作业')
root.geometry(initWin)
labelNotice = tk.Label(root, text="请选择文件->打开，打开遥感影像", font=("黑体", 30), height=3).pack()

# 创建菜单栏
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)

filemenu.add_command(label='清空', command=_clear)
filemenu.add_command(label='打开', command=_open)
filemenu.add_command(label='保存', command=_save)
filemenu.add_separator()  # 分隔线
filemenu.add_command(label='退出', command=root.quit)

# 继续编辑菜单栏
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='操作', menu=editmenu)

editmenu.add_command(label='信息', command=_showInfo)
editmenu.add_command(label='变换波段', command=_swapBand)
editmenu.add_command(label='显示直方图', command=_gram)

root.config(menu=menubar)

root.mainloop()

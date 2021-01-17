# -*-coding:gbk-*-

import mysql.connector

def cal_r(char):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1qw23e00",
        database="sellSystem")

    mycursor = mydb.cursor()
    mycursor.autocommit = True
    mycursor.execute(char)

    return mycursor.fetchall()


def cal_nr(char):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1qw23e00",
        database="sellSystem")

    mycursor = mydb.cursor()
    mycursor.autocommit = True
    mycursor.execute(char)
    mydb.commit()

def fet_list(column, db):
    find = cal_r("SELECT %s FROM %s" % (column, db))
    y = []
    for x in find:
        y.append(x[0])
    return y

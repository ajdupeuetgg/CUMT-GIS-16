//
//  main.cpp
//  list
//
//  Created by GENKi on 2019/6/3.
//  Copyright © 2019 GENKi. All rights reserved.
//

#include <iostream>
#include <stdlib.h>
#include "seqList.h"
using namespace std;

template <class T>
SeqList<T>::SeqList(int sz){     //构造函数，通过sz定义数组的长度
    if(sz > 0)
    {
        maxSize = sz;last = -1;
        data = new T[maxSize];
        cout << "初始化完成，该顺序表空间大小为：" << sz << endl;
        if (data == NULL)
        {
            cerr << "存储分配错误！" << endl;exit(1);
        }
    }
}

template <class T>
SeqList<T>::SeqList(SeqList<T>&L){      //复制构造函数，用参数表中给出的已有顺序表初始化新建的顺序表
    maxSize = L.Size();
    last = L.Length() - 1;
    T value;
    data = new T[maxSize];
    if(data == NULL)
    {
        cerr << "存储分配错误！" << endl;exit(1);
    }
    for(int i = 1;i<=last+1;i++)
    {
        L.getData(i, value);data[i-1]=value;
    }
}

template <class T>
void SeqList<T>::reSize(int newSize){       //私有函数：扩充顺序表的存储数组空间为newSize个
    if(newSize<=0)
    {
        cerr << "无效的数组大小！" << endl;return;
    }
    if(newSize != maxSize){
        T * newarray = new T[newSize];
        if(newarray == NULL)
        {
            cerr << "存储分配错误！" << endl;exit(1);
        }
        int n = last+1;
        T * srcptr = data;
        T * desptr = newarray;
        while(n--) *desptr++=*srcptr++;
        delete []data;
        data = newarray;maxSize = newSize;
    }
}

template <class T>
int SeqList<T>::Search(T& x)const{
    for (int i = 0; i<=last; i++)
        if(data[i] == x)
            return i+1;
    return 0;
}

template <class T>
int SeqList<T>::Locate(int i)const{
    if(i >= 1 && i <= last+1)
        return data[i-1];
    else
        return 0;
}

template <class T>
bool SeqList<T>::getData(int i, T& x)const{
    if(i > 0 && i <= last+1)
    {
        x = data[i-1];
        return true;
    }
    else
        return false;
}

template <class T>
void SeqList<T>::setData(int i, T& x){
    if(i > 0 && i <= last+1)
        data[i-1] = x;
}

template <class T>
bool SeqList<T>::Insert(int i, T& x){
    if(last == maxSize)
    {
        cout << "插入失败！顺序表已满！" << endl;
        return false;
    }
    if(i < 0||i > last+1)
    {
        cout << "插入失败！指定位置不存在！" << endl;
        return false;
    }
    for(int j = last;j >= i-1;j--)
        data[j+1] = data[j];
    data[i-1] = x;
    last++;
    return true;
}

template <class T>
bool SeqList<T>::Remove(int i, T& x){
    if(last == -1)
    {
        cout << "删除失败！顺序表为空！" << endl;
        return false;
    }
    if(i < 1||i > last+1)
    {
        cout << "删除失败！指定位置不存在！" << endl;
        return false;
    }
    x = data[i-1];
    for(int j = i;j <= last;j++)
        data[j-1] = data[j];
    last--;
    return true;
}

template <class T>
void SeqList<T>::Expand(){
    if ((double)maxSize/(double)last >= 0.5)
    {
        reSize(2 * maxSize);
        cout << "顺序表内空间占用过半，已自动扩展顺序表空间至原来的两倍" << endl;
    }
}

template <class T>
void SeqList<T>::input(){
    cout << "开始对顺序表进行插入操作，请输入表中想要插入的元素个数：";
    while (1) {
        cin >> last;
        if(last <= maxSize) break;
        cout << "表元素个数输入有误，范围不能超过" << maxSize << "，请重新输入：";
    }
    for (int i = 0; i < last; i++)
    {cin >> data[i];cout << "//已输入顺序为" << i+1 << "的元素" << endl;}
}

template <class T>
void SeqList<T>::output(){
    cout << "顺序表当前元素最后位置为：" << last << endl;
    for(int i = 0; i < last; i++)
        cout << "#" << i+1 << " " << data[i] << endl;
}

template <class T>
SeqList<T> SeqList<T>::operator=(SeqList<T> &L){
    maxSize = L.Size();
    last = L.Length() - 1;
    T value;
    data = new T[maxSize];
    if(data == NULL)
    {
        cerr << "存储分配错误！" << endl;
        exit(1);
    }
    for(int i = 1;i<=last+1;i++)
    {
        L.getData(i, value);
        data[i-1]=value;
    }
    return *this;
}

int main()
{
    
    int sz;
    cout << "准备建立顺序表，请输入顺序表初始最大容量：";
    cin >> sz;
    SeqList<int> L1(sz);
    if (L1.IsEmpty())
        cout << "该顺序表暂空" << endl;
    L1.input();
    L1.output();
    if (L1.IsFull())
        cout << "该顺序表已满" << endl;
    else
        cout << "该顺序表未满，剩余" << L1.getBlank() << "个空位" << endl;
    int b,a,c,d;  //b此处存放顺序表的某个位置，a用来存放想要插入/删除顺序表的数值，c用来存放Remove函数弹出的删除的数据
    cout << "请输入插入数字的位置：";
    cin >> b;
    cout << "请输入插入数字的数值：";
    cin >> a;
    if(L1.Insert(b, a))
        cout << "插入成功" << endl;
    L1.output();
    cout << "请输入想要查询位置的数值：";
    cin >> d;
    cout << d << "所在的位置为：" << L1.Search(d) << endl;
    cout << "请输入想要确认数值的位置：";
    cin >> d;
    cout << d << "位置处所存储的数字为：" << L1.Locate(d) << endl;
    cout << "请输入想要删除的数字的位置：";
    cin >> b;
    if(L1.Remove(b, c))
        cout << "删除成功，删除的数字为："<< c << endl;
    L1.output();
    L1.Expand();
    if (L1.IsFull())
        cout << "该顺序表已满" << endl;
    else
        cout << "该顺序表未满，剩余" << L1.getBlank() << "个空位" << endl;
    SeqList<int> L2;
    L2 = L1;
    L2.output();
    return 0;
    
}

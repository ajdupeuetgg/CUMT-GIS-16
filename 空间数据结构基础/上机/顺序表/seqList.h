//
//  seqList.h
//  list
//
//  Created by GENKi on 2019/6/3.
//  Copyright © 2019 GENKi. All rights reserved.
//

#ifndef seqList_h
#define seqList_h

#include <iostream>
#include <stdlib.h>
using namespace std;
const int defaultSize = 100;

template <class T>
class SeqList{
protected:
    T *data;
    int maxSize;
    int last;
    void reSize(int newSize);
public:
    SeqList(int sz = defaultSize);
    SeqList(SeqList<T>& L);
    ~SeqList(){delete[] data;}
    int Size()const{return maxSize;}
    int Length()const{return last+1;}
    int Search(T& x)const;
    int Locate(int i)const;
    bool getData(int i, T& x)const;
    void setData(int i, T& x);  //int& x == int &x
    bool Insert(int i, T& x);
    bool Remove(int i, T& x);
    bool IsEmpty(){return (last == -1)?true:false;}
    bool IsFull(){return (last == maxSize)?true:false;}
    void Expand();
    int getBlank(){return maxSize-last;}
    void input();
    void output();
    SeqList<T> operator=(SeqList<T>&L);
};

#endif /* seqList_h */

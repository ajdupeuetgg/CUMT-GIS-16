#ifndef seqList_h
#define seqList_h

#include <iostream>
#include <stdlib.h>
using namespace std;

template<class T>
struct address
{
    int no;
    string nam;
    int relation;
    long number;
};

template<class T>
class SeqList
{
protected:
    address<T> *data;
public:
    SeqList();
    SeqList(T &x);
    address<T> *getdata();
    void Search(string tag);
    void Change(string tag);
    void Remove(string tag);
    void input();
    void output(int t);
};

#endif /* seqList_h */

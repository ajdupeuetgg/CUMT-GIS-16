#include<iostream>
using namespace std;

template <class T>
struct LinkNode
{
    T data;
    LinkNode<T> *link;
    LinkNode(LinkNode<T> *ptr = NULL)
    {
        link = ptr;
    }
    LinkNode(const T& item, LinkNode<T> *ptr = NULL)
    {
        data = item;
        link = ptr;
    }
};

template <class T>
class List
{
protected:
    LinkNode<T> *first;
public:
    List() {first = new LinkNode<T>;}
    List(const T& x) {first = new LinkNode<T>(x);}
    List(List<T>& L);
    ~List(){ makeEmpty(); }
    void makeEmpty();
    int Length()const;
    LinkNode<T> *getHead()const {return first;}
    LinkNode<T> *Search(T x);
    LinkNode<T> *Locate(int i);
    bool getData(int i, T&x);
    void setData(int i, T&x);
    bool Insert(int i, T&x);
    bool Remove(int i, T&x);
    bool IsEmpty()const{return first->link==NULL ? true : false;}
    bool IsFull()const{return false;}
    void Sort();
    void inputFront(T endTag);
    void inputRear(T endTag);
    void output();
    List<T>& operator=(List<T>& L);
};

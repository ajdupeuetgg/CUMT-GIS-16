#include<iostream>
#include<stdlib.h>
#include"List.h"
using namespace std;
template<class T>
List<T>::List(List<T>& L)
{
    T value;
    LinkNode<T> *srcptr = L.getHead();
    LinkNode<T> *destptr = first = new LinkNode<T>;
    while (srcptr->link != NULL)
    {
        value = srcptr->link->data;
        destptr->link = new LinkNode<T>(value);
        destptr = destptr->link;
        srcptr = srcptr->link;
    }
    destptr->link = NULL;
}

template <class T>
void List<T>::makeEmpty()
{
    LinkNode<T> *q;
    while (first->link != NULL)
    {
        q = first->link;
        first->link = q->link;
        delete q;
    }
}

template<class T>
int List<T>::Length()const
{
    LinkNode<T> *p = first->link;
    int count = 0;
    while(p != NULL)
    {
        p = p->link;
        count++;
    }
    return count;
}

template <class T>
LinkNode<T> *List<T>::Search(T x)
{
    LinkNode<T> *current = first->link;
    while (current != NULL && current->data != x)
        current = current->link;
    return current;
}

template <class T>
LinkNode<T> *List<T>::Locate(int i)
{
    if (i < 0)
        return NULL;
    LinkNode<T> *current = first;
    int k = 0;
    while (current != NULL && k < i)
    {
        current = current->link;
        k++;
    }
    return current;
}

template <class T>
bool List<T>::getData(int i, T& x)
{
    if (i <= 0)
        return NULL;
    LinkNode<T>  *current = Locate(i);
    if (current == NULL)
        return  false;
    else
    {
        x = current->data;
        return true;
    }
}

template <class T>
void List <T>::setData(int i, T& x)
{
    if (i <= 0)
        return;
    LinkNode<T>  *current = Locate(i);
    if (current == NULL)
        return;
    else  current->data = x;
}

template <class T>
bool List<T>::Insert(int i, T& x)
{
    LinkNode<T> *current = Locate(i-1);
    if (current == NULL) return false;
    LinkNode<T> *newNode = new LinkNode<T>(x);
    if (newNode == NULL)
    {
        cerr << "内存分配错误！" << endl;
        exit(1);
    }
    newNode->link = current->link;
    current->link = newNode;
    return true;
}

template <class T>
bool List<T>::Remove(int i, T& x)
{
    LinkNode<T> *current = Locate(i-1);
    if (current == NULL || current->link == NULL)
        return false;
    LinkNode<T> *del = current->link;
    current->link = del->link;
    x = del->data;
    delete del;
    return true;
}

template <class T>
void List<T>::output()
{
    LinkNode<T>  *current = first->link;
    while (current != NULL)
    {
        cout << current->data << endl;
        current = current->link;
    }
}

template <class T>
void List<T>::inputFront(T endTag)
{
    LinkNode<T> *newNode;
    T val;
    makeEmpty();
    cin>>val;
    while (val != endTag)
    {
        newNode = new LinkNode<T>(val);
        if (newNode == NULL)
        {
            cerr << "内存分配错误！" << endl;
            exit(1);
        }
        newNode->link = first->link;      //插在表前端
        first->link = newNode;
        cin >> val;
    }
}

template <class T>
void List<T>::inputRear(T endTag)
{
    LinkNode<T> *newNode, *last;
    T val;
    makeEmpty();
    cin >> val;
    last = first;
    while (val != endTag)
    {
        newNode = new LinkNode<T>(val);
        if (newNode == NULL)
        {
            cerr<<"内存分配错误！"<<endl;
            exit(1);
        }
        last->link = newNode;      //插在表尾
        last = newNode;
        cin >> val;
    }
}

template<class T>
void List<T>::Sort()
{
    LinkNode<T> *head, *pre, *cur, *next, *end, *temp;
    head = first;
    end = NULL;
    while(head -> link != end)
    {
        for(pre = head, cur = pre -> link, next = cur -> link;
            next != end;
            pre = pre -> link, cur = cur -> link, next = next -> link)
        {
            if(cur -> data > next -> data)
            {
                cur -> link = next -> link;
                pre ->link = next;
                next -> link = cur;
                temp = next;
                next = cur;
                cur = temp;
            }
        }
        end = cur;
    }
    cout << "升序排序成功！" << endl;
}

template<class T>
List<T>&List<T>::operator = (List<T> &L)
{
    T value;
    LinkNode<T> *srcptr = L.getHead();
    LinkNode<T> *destptr = first = new LinkNode<T>;
    while (srcptr->link != NULL)
    {
        value = srcptr->link->data;
        destptr->link = new LinkNode<T>(value);
        destptr = destptr->link;
        srcptr = srcptr->link;
    }
    destptr->link = NULL;
    return *this;
}


int main()
{
    List<int> A, B, C;
    cout << "初始化链表A开始（使用后插法），输入0时结束插入" << endl;
    A.inputRear(0);
    cout << "初始化A成功，结果如下：" << endl;
    A.output();
    cout << "初始化链表B开始（使用后插法），输入0时结束插入" << endl;
    B.inputRear(0);
    cout << "初始化B成功，结果如下：" << endl;
    B.output();
}

#include<iostream>
using namespace std;

template<class T>
struct car
{
    int ID = 0;
    char Ctype = 0;
    int Cstate = 0;
    string Cname = "";
    int dateMonth = 0;
    int dateDay = 0;
    int costDaily = 0;
    int costDestory = 500;
};

template <class T>
struct LinkNode
{
    car<T> data;
    LinkNode<T> *link;
    LinkNode(LinkNode<T> *ptr = NULL)
    {
        link = ptr;
    }
    LinkNode(car<T> value)
    {
        
        data.ID = value.ID;
        data.Ctype = value.Ctype;
        data.Cstate = value.Cstate;
        data.Cname = value.Cname;
        data.dateMonth = value.dateMonth;
        data.dateDay = value.dateDay;
        data.costDaily = value.costDaily;
        data.costDestory = value.costDestory;
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
    LinkNode<T> *search_Type(char type);
    bool search_Type2(char type);
    bool search_Name2(string name);
    LinkNode<T> *search_Name(string name);
    void collectDestory(List<T> &L);
    void Repair();
    int searchType(car<T> &x);
    int searchName(car<T> &x);
    bool Insert(int i, car<T> x);
    bool Pick(int i, car<T> &x);
    bool IsEmpty()const{return first->link==NULL ? true : false;}
    void inputRear_rented();
    void inputRear_lend();
    void Rent(List<T> &lend, List<T> &rented);
    void ReturnBack(List<T> &lend, List<T> &rented);
    void output();
};

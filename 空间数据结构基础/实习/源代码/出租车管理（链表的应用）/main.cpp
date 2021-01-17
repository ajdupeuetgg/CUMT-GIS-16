#include <stdlib.h>
#include "list.h"
static int day[12] = {31,28,31,30,31,30,31,31,30,31,30,31};

template<class T>
List<T>::List(List<T>& L)
{
    car<T> value;
    LinkNode<T> *srcptr = L.getHead();
    LinkNode<T> *destptr = first = new LinkNode<T>;
    while (srcptr->link != NULL)
    {
        value.ID = srcptr->link->data.ID;
        value.Ctype = srcptr->link->data.Ctype;
        value.Cstate = srcptr->link->data.Cstate;
        value.Cname = srcptr->link->data.Cname;
        value.dateMonth = srcptr->link->data.dateMonth;
        value.dateDay = srcptr->link->data.dateDay;
        value.costDaily = srcptr->link->data.costDaily;
        value.costDestory = srcptr->link->data.costDestory;
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
    while (first->link != NULL) {
        q = first->link;
        first->link = q->link;
        delete q;
    }
}

template<class T>
int List<T>::Length()const
{
    LinkNode<T> *p = first->link;
    int count=0;
    while(p != NULL)
    {
        p = p->link;
        count++;
    }
    return count;
}

template <class T>
int List<T>::searchType(car<T> &x)
{
    int k = 0;
    LinkNode<T> *current = first->link;
    while (current != NULL)
    {
        k++;
        if(current->data.Ctype == x.Ctype)
            return k;
        current = current->link;
    }
    return -1;
}

template <class T>
bool List<T>::search_Type2(char type)
{
    LinkNode<T> *current = first->link;
    while (current != NULL)
    {
        if(current->data.Ctype == type)
            return true;
        current = current->link;
    }
    return false;
}

template <class T>
LinkNode<T> *List<T>::search_Type(char type)
{
    LinkNode<T> *current = first->link;
    while (current != NULL && current->data.Ctype != type)
        current = current->link;
    return current;
}

template <class T>
int List<T>::searchName(car<T> &x)
{
    int k = 0;
    LinkNode<T> *current = first->link;
    while (current != NULL)
    {
        k++;
        if(current->data.Cname == x.Cname)
            return k;
        else
            current = current->link;
    }
    return -1;
}

template <class T>
LinkNode<T> *List<T>::search_Name(string name)
{
    LinkNode<T> *current = first->link;
    while (current != NULL && current->data.Cname != name)
        current = current->link;
    return current;
}

template <class T>
bool List<T>::search_Name2(string name)
{
    LinkNode<T> *current = first->link;
    while (current != NULL)
    {
        if(current->data.Cname == name)
            return true;
        current = current->link;
    }
    return false;
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
bool List<T>::Insert(int i, car<T> x)
{
    LinkNode<T> *current = Locate(i-1);
    if (current == NULL)
        return false;
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
bool List<T>::Pick(int i, car<T> &x) //i主管大局，最后x的输出都是以i为准
{
    LinkNode<T> *current = Locate(i-1);
    if (current == NULL || current->link == NULL)
        return false;
    LinkNode<T> *del = current->link;
    current->link = del->link;
    x.ID = del->data.ID;
    x.Ctype = del->data.Ctype;
    x.Cstate = del->data.Cstate;
    x.dateDay = del->data.dateDay;
    x.dateMonth = del->data.dateMonth;
    x.costDaily = del->data.costDaily;
    delete del;
    return true;
}

template <class T>
void List<T>::output()
{
    LinkNode<T>  *current = first->link;
    while (current != NULL)
    {
        cout << "-------------------------" << endl;
        cout << "车辆ID为：" << current->data.ID << endl;
        cout << "该车型号为：" << current->data.Ctype << endl;
        if(current->data.Cstate == 0)
            cout << "该车目前完好" << endl;
        else
            cout << "该车目前已损坏" << endl;
        if(current->data.Cname == "")
            cout << "该车目前没有租者" << endl;
        else
            cout << "顾客姓名为：" << current->data.Cname << endl;
        cout << "-------------------------" << endl;
        current = current->link;
    }
}

template <class T>
void List<T>::inputRear_lend()
{
    LinkNode<T> *newNode, *last;
    car<T> val;
    makeEmpty();
    int flag = 0;
    last = first;
    while (flag == 0)
    {
        cout << "请输入车辆ID号：";
        cin >> val.ID;
        cout << "请输入车辆车型：";
        cin >> val.Ctype;
        cout << "请输入车辆状态（1表示已损坏，0表示完好）";
        cin >> val.Cstate;
        cout << "请输入该车日租金额：";
        cin >> val.costDaily;
        newNode = new LinkNode<T>(val);
        last->link = newNode;
        last = newNode;
        cout << "是否继续输入下一待租车辆的信息：(继续0/结束1)";
        cin >> flag;
    }
    last->link = NULL;
}

template <class T>
void List<T>::inputRear_rented()
{
    LinkNode<T> *newNode, *last;
    car<T> val;
    makeEmpty();
    int flag = 0;
    last = first;
    while (flag == 0)
    {
        cout << "请输入车辆ID号：";
        cin >> val.ID;
        cout << "请输入车辆车型：";
        cin >> val.Ctype;
        cout << "请输入车辆状态（1表示已损坏，0表示完好）";
        cin >> val.Cstate;
        cout << "请输入该车顾客姓名：";
        cin >> val.Cname;
        cout << "请输入车辆的租用日期：（示例格式6 26）";
        cin >> val.dateMonth >> val.dateDay;
        cout << "请输入该车日租金额：";
        cin >> val.costDaily;
        cout << "请输入该车的损坏罚金：";
        cin >> val.costDestory;
        newNode = new LinkNode<T>(val);
        last->link = newNode;
        last = newNode;
        cout << "是否继续输入下一客户租车的信息：(继续0/结束1)";
        cin >> flag;
    }
    last->link = NULL;
}

template <class T>
void List<T>::Rent(List<T> &lend, List<T> &rented)
{
    car<T> x;
    char ty;
    cout << "请输入您想租用的车型：";
    cin >> ty;
    if(lend.search_Type2(ty))
    {
        x = lend.search_Type(ty)->data;
        cout << "请输入您的姓名：";
        cin >> x.Cname;
        x.Ctype = ty;
        cout << "请输入当天日期：";
        cin >> x.dateMonth >> x.dateDay;
        lend.search_Type(ty)->data = x;
    
        int k = lend.searchType(x);
        if (lend.first->link)
        {
            if (k >= 0)
            {
                lend.Pick(k, x);
                rented.Insert(1, x);
                cout << "已成功租车！" << endl;
            }
            
        }else
        {
            cout << "抱歉，所有的车都在出租中" << endl;
        }
    }else
    {
        cout << "抱歉，没有您需求的车型" << endl;
    }
}

template<class T>
void List<T>::ReturnBack(List<T> &lend, List<T> &rented)
{
    time_t now = time(0);
    tm *ltm = localtime(&now);
    int M = 1 + ltm->tm_mon;
    int D = ltm->tm_mday;
    car<T> x;
    string na;
    cout << "请输入顾客姓名：";
    cin >> na;
    
    if(rented.search_Name2(na))
    {
        x = rented.search_Name(na)->data;
        x.Cname = "";
        rented.search_Name(na)->data = x;
        int s;
        int k = rented.searchName(x);
        if (k >= 0)
        {
            cout << "请输入该车目前的状态：(0完好/1损坏)";
            cin >> s;
        
            rented.Pick(k, x);
            x.Cstate = s;
            lend.Insert(1, x);
        
            int m_di = M - x.dateMonth;
            int d_di,d_co;
            int day1 = 0, day2 = 0;
            day1 += D;
            day2 += x.dateDay;
        
            if(m_di == 0)
                d_di = D - x.dateDay;
            else
            {
                for(int i = 0; i < M; i++)
                    day1 = day1 + day[i];
                for(int i = 0; i < x.dateMonth; i++)
                    day2 = day2 + day[i];
                d_di = day1 - day2;
            }
            d_co = d_di * x.costDaily;
            if(s == 1)
            {
                d_co += x.costDestory;
                cout << "该车共租出" << d_di << "天时间，" << endl;
                cout << "需要支付费用" << d_co << "元（其中包含损坏罚金500元）" << endl;
            }else
            {
                cout << "该车共租出" << d_di << "天时间，" << endl;
                cout << "需要支付费用" << d_co << "元" << endl;
            }
        }
    }
    else
    {
        cout << "抱歉，您似乎并没有租车" << endl;
    }
}

template<class T>
void List<T>::collectDestory(List<T> &L)
{
    LinkNode<T> *p = first->link;
    int i = 0;
    while(p != NULL)
    {
        if (p->data.Cstate == 1)
        {
            i++;
            L.Insert(i, p->data);
        }
        p = p->link;
    }
}

template<class T>
void List<T>::Repair()
{
    LinkNode<T> *p = first->link;
    int i = 0;
    while(p != NULL)
    {
        if (p->data.Cstate == 1)
        {
            i++;
            p->data.Cstate = 0;
        }
        p = p->link;
    }
    if(i != 0)
        cout << "维修成功！本次共维修" << i << "辆汽车" << endl;
    else
        cout << "没有车辆需要维修！" << endl;
}

int main()
{
    cout << "开始初始化待租车辆表" << endl;
    List<int> lend_list, rented_list, o;
    List<int> destory_list;
    lend_list.inputRear_lend();
    cout << "初始化待租车辆表成功" << endl;
    rented_list.makeEmpty();
    cout << "已租车辆表置空完成" << endl << endl;
    
    cout << "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"<< endl;
    cout << " |    如果你感觉界面熟悉没错还是我写的   |"<< endl;
    cout << "  |     出～租～车～管～理～系～统     |"<< endl;
    cout << "  |                               |"<< endl;
    cout << " |      如果你选‘1’ - 进行租车操作     |"<< endl;
    cout << " |      如果你选‘2’ - 进行还车操作     |"<< endl;
    cout << " |      如果你选‘3’ - 打印待租信息     |"<< endl;
    cout << " |      如果你选‘4’ - 打印已租信息     |"<< endl;
    cout << " |      如果你选‘5’ - 打印坏车信息     |"<< endl;
    cout << " |      如果你选‘6’ - 进行车辆维修     |"<< endl;
    cout << " |      如果你选‘7’ - 我们下次再见     |"<< endl;
    cout << " |                                 |"<< endl;
    cout << " |             Copyright © 2019 ZQY.|" << endl;
    cout << " |              All rights reserved.|" << endl;
    cout << "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"<< endl;
    int f = 0;
    while (1)
    {
        cout << "选择：";
        int x;
        cin >> x;
        switch (x)
        {
            case 1:
                o.Rent(lend_list, rented_list);
                break;
            case 2:
                o.ReturnBack(lend_list, rented_list);
                break;
            case 3:
                if(lend_list.IsEmpty())
                    cout << "目前没有可租车辆！ " << endl;
                else
                {
                    lend_list.output();
                    cout << "共" << lend_list.Length() << "条待租车辆信息" << endl;
                    cout << "-------------------------" << endl;
                }
                break;
            case 4:
                if(rented_list.IsEmpty())
                    cout << "目前没有租出车辆！" << endl;
                else
                {
                    rented_list.output();
                    cout << "共" << rented_list.Length() << "条租出车辆信息" << endl;
                    cout << "-------------------------" << endl;
                }
                break;
            case 5:
                destory_list.makeEmpty();
                lend_list.collectDestory(destory_list);
                rented_list.collectDestory(destory_list);
                if(destory_list.IsEmpty())
                    cout << "目前没有损坏的车辆！" << endl;
                else
                {
                    destory_list.output();
                    cout << "共" << destory_list.Length() << "条损坏车辆信息" << endl;
                    cout << "-------------------------" << endl;
                }
                break;
            case 6:
                lend_list.Repair();
                break;
            case 7:
                cout << endl << "" << endl;
                f = 1;
                break;
            default:
                break;
        }
        if(f)
            break;
    }
}

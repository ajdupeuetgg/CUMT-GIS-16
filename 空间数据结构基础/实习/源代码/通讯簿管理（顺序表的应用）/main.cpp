#include "seqList.h"

static int n = 0;
static int m = 0;

template<class T>
SeqList<T>::SeqList()
{
    data = new address<T>;
}

template<class T>
SeqList<T>::SeqList(T &x)
{
    data = new address<T>(x);
}

template<class T>
address<T> *SeqList<T>::getdata()
{
    return data;
}

template<class T>
void SeqList<T>::Search(string tag)
{
    bool c = false;
    for(int i = 0; i < n; i++)
        if(strcmp(tag.c_str(), data[i].nam.c_str()) == 0)
        {
            c = true;
            cout << "您查询的联系人电话号码为：" << data[i].number << endl;
            break;
        }
    if (c)
        return ;
    else
        cout << "查无此人！" << endl;
}

template<class T>
void SeqList<T>::Change(string tag)
{
    int x,No;
    string Nam;
    long Nu;
    for(int i = 0; i < n; i++)
        if(strcmp(tag.c_str(), data[i].nam.c_str()) == 0)
        {
            cout << "请输入想要修改的信息：[序号(1)/姓名(2)/与本人关系(3)/电话号码(4)]";
            cin >> x;
            switch (x) {
                case 1:
                    cout << "请输入新的序号：";
                    cin >> No;
                    data[i].no = No;
                    break;
                case 2:
                    cout << "请输入新的姓名：";
                    cin >> Nam;
                    data[i].nam = Nam;
                    break;
                case 3:
                    cout << "请输入新的关系：";
                    cin >> No;
                    data[i].relation = No;
                    break;
                case 4:
                    cout << "请输入新的电话号码：";
                    cin >> Nu;
                    data[i].number = Nu;
                    break;
                default:
                    break;
            }
            break;
        }else
        {
            cout << "查无此人，修改失败！" << endl;
            break;
        }
}

template<class T>
void SeqList<T>::Remove(string tag)
{
    for(int i = 0; i < n; i++)
        if(strcmp(tag.c_str(), data[i].nam.c_str()) == 0)
        {
            if(i == 0)
            {
                data[i].no = NULL;
                data[i].nam = "";
                data[i].relation = NULL;
                data[i].number = NULL;
            }else
            {
                data[i].no = data[m-1].no;
                data[i].nam = data[m-1].nam;
                data[i].relation = data[m-1].relation;
                data[i].number = data[m-1].number;
            }
            m--;
            cout << "已成功删除信息" << endl;
            break;
        }else
        {
            cout << "查无此人，删除失败！" << endl;
            break;
        }
}

template<class T>
void SeqList<T>::input()
{
    cout << "请输入您想要添加的人的序号：";
    cin >> data[n].no;
    cout << "请输入您想要添加的人的姓名：";
    cin >> data[n].nam;
    cout << "请输入您想要添加的人与本人的关系：(亲人1、朋友2或是同事3)";
    cin >> data[n].relation;
    cout << "请输入您想要添加的人的电话号码：";
    cin >> data[n].number;
    n++;
    m++;
}

template<class T>
void SeqList<T>::output(int t)
{
    bool c = false;
    if(t == 1)
    {
        cout<<"我的亲人有："<<endl;
        for(int i = 0; i < n; i++)
        {
            if(data[i].relation == 1)
            {
                c = true;
                cout << data[i].no << "号的姓名是" << data[i].nam << "，电话号码："<< data[i].number << endl;
            }
        }
        if (c)
            return ;
        else
            cout << "无亲人记录！" << endl;
    }
    else if (t == 2)
    {
        cout<<"我的朋友有："<<endl;
        for(int i = 0; i < n; i++)
        {
            if(data[i].relation == 2)
            {
                c = true;
                cout << data[i].no << "号的姓名是" << data[i].nam << "，电话号码："<< data[i].number << endl;
            }
        }
        if (c)
            return ;
        else
            cout << "无朋友记录！" << endl;
    }
    else if (t == 3)
    {
        cout<<"我的同事有："<<endl;
        for(int i = 0; i < n; i++)
        {
            if(data[i].relation == 3)
            {
                c = true;
                cout << data[i].no << "号的姓名是" << data[i].nam << "，电话号码："<< data[i].number << endl;
            }
        }
        if (c)
            return ;
        else
            cout << "无同事记录！" << endl;
    }
}

int main()
{
    cout << "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"<< endl;
    cout << " |       用了不知道多长时间才写出来的    |"<< endl;
    cout << "  |            通～讯～簿            |"<< endl;
    cout << "  |                ☎              |"<< endl;
    cout << " |      如果你选‘1’ - 查找电话号码     |"<< endl;
    cout << " |      如果你选‘2’ - 可添加新记录     |"<< endl;
    cout << " |      如果你选‘3’ - 可以修改记录     |"<< endl;
    cout << " |      如果你选‘4’ - 可以删除记录     |"<< endl;
    cout << " |      如果你选‘5’ - 打印亲人清单     |"<< endl;
    cout << " |      如果你选‘6’ - 打印朋友清单     |"<< endl;
    cout << " |      如果你选‘7’ - 打印同事清单     |"<< endl;
    cout << " |      如果你选‘8’ - 我们下次再见     |"<< endl;
    cout << " |                                  |"<< endl;
    cout << " |             Copyright © 2019 ZQY.|" << endl;
    cout << " |              All rights reserved.|" << endl;
    cout << "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"<< endl;
    SeqList<string> L;
    string Tag;
    int f = 0;
    while (1)
    {
        cout << "选择：";
        int x;
        cin >> x;
        switch (x)
        {
            case 1:
                cout << "请输入你想查找哪个姓名对应的电话号码：";
                cin >> Tag;
                L.Search(Tag);
                break;
            case 2:
                L.input();
                break;
            case 3:
                cout << "请输入你想修改哪个姓名对应的信息：";
                cin >> Tag;
                L.Change(Tag);
                break;
            case 4:
                cout << "请输入你想删除哪个姓名对应的信息：";
                cin >> Tag;
                L.Remove(Tag);
                break;
            case 5:
                L.output(1);
                break;
            case 6:
                L.output(2);
                break;
            case 7:
                L.output(3);
                break;
            case 8:
                cout << endl << "" << endl <<endl;
                f = 1;
                break;
            default:
                break;
        }
        if(f)
            break;
    }
    return 0;
}

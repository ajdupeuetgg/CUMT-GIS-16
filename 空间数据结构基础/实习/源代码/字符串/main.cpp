#include "str.h"

String::String (const String &sb)    //复制构造函数：从已有串sb复制
{
    ch = new char[maxLen+1];  //字符串存储空间
    f = new int[maxLen+1];    //串的失效函数值存储空间
    if ( !ch ) {
        cerr << "存储分配错 \n";
        exit(1);
    }
    slen = sb.slen;
    strcpy (ch, sb.ch);
}

String::String (const char *ch_arr)
{
    //复制构造函数: 从已有字符数组*ch_arr复制
    ch = new char[maxLen+1];
    f = new int[maxLen+1];
    if ( !ch ){
        cerr << "存储分配错 \n";
        exit(1);
    }
    slen = (int)strlen (ch_arr);
    strcpy ( ch, ch_arr );
}

String::String()
{
    //构造函数：创建一个空串
    ch = new char[maxLen+1];
    f = new int[maxLen+1];
    if ( !ch ) {
        cerr << "存储分配错\n";
        exit(1);
    }
    slen = 0;
    ch[0] = '\0';
}

String &String:: operator () (int pos, int len)
{
    //从串中第 pos 个位置起连续提取 len 个字符作为子串返回
    String *temp = new String;   //动态分配
    if ( pos < 0 || pos+len-1 >= maxLen || len < 0 )
    {
        temp->slen = 0;           //子串长度为0，返回空串
        temp->ch[0] = '\0';        //添加串结束符
    }
    else
    {                    //提取子串
        if (pos+len -1 >= slen)
            len = slen - pos;
        temp->slen = len;//子串长度
        for (int i = 0, j = pos; i <len; i++, j++)
            temp->ch[i] = ch[j];      //传送串数组
        temp->ch[len] = '\0';//子串结束，添加串结束符
    }
    return *temp;
}

String &String::operator = (const String &sb)
{
    //串赋值：从已有串sb复制
    if ( &sb != this ) {
        delete [ ] ch;
        ch = new char [maxLen+1];  //重新分配
        if ( ! ch ) {
            cerr << "内存不足!\n ";  exit (1);
        }
        slen = sb.slen;              //串复制
        strcpy ( ch, sb.ch );
    }
    else  cout << "字符串自身赋值出错! \n";
    return *this;
}

String &String::operator += (const String &sb)
{
    //串连接
    char * temp =ch;               //暂存原串数组
    slen += sb.slen;       //串长度累加
    ch = new char [maxLen+1];
    if ( ! ch ) {
        cerr << "字符串下标超界!\n";  exit (1) ;
    }
    strcpy (ch, temp);          //拷贝原串数组
    strcat (ch, sb.ch);          //连接sb串数组
    delete []temp;
    return *this;
}

int String::Search(String Target, String pattern)
{
    for(int pos = 0; pos <= Target.Length(); pos++)
        if(pattern == Target(pos,pattern.Length()))
            return pos;
    return -1;
}

ostream &operator << (ostream &out,String &P){ //打印字符串
    for(int i=0;i<P.slen;i++)
        cout<<P.ch[i];
    return out;
}

void String::Calculate()
{
    char c[maxLen];
    int num[maxLen] = {0};
    int i, j;
    int n = 0;
    for(i = 0; ch[i] != '\0'; i++)
    {
        for(j = 0; j < n; j++)
            if(ch[i] == c[j])
                break;
        if(j < n)
            num[j]++;
        else
        {
            c[j] = ch[i];
            num[j]++;
            n++;
        }
    }
    for(i = 0; i < n; i++)
        cout << c[i] << "出现了" << num[i] << "次" << endl;
}

int main()
{
    char a[50] = "aaaaabcLetabcaabcdde___#$##33";
    char b[6] = "aabcd";
    char c[10] = "abcLetabc";
    String A(a);
    String B(b);
    String C(c);
    cout << "A串：" << A << endl;
    cout << "B串：" << B << endl;
    A += B;
    cout << A << endl;
    C = B;
    cout << C << "的长度是" << C.Length() << endl;
    cout << C.Search(A, B) << endl;
    A.Calculate();
    return 0;
}

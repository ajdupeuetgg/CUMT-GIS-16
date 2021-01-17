#ifndef str_h
#define str_h
#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;
const int maxLen = 128;        //字符串存储空间的最大长度

class String
{
public:
    String ( const String & sb );  //构造函数，复制已有的串对象sb来创建一个新串
    String ( const char *ch_arr );
    //构造函数，从已有的字符数组*ch_arr复制字符来创建一个新串
    String ();                    //构造函数，创建一个空串
    ~String () { delete []ch; }  //析构函数，释放动态分配的串空间
    int Length () const { return slen; } //返回字符串的长度
    String &operator () (int pos, int len);  //重载()运算符，从串中pos位置起连续提取 len 个字符形成子串返回
    int operator == ( const String &sb )
    const { return strcmp (ch, sb.ch) == 0; } //重载==运算符，判断串是否相等
    int operator != ( const String &sb )
    const { return strcmp (ch, sb.ch) != 0; } //重载!=运算符，判断串是否不相等
    int operator !() const { return slen == 0; }  //重载!( )运算符，判断是否为空串
    String &operator = ( const String &sb );    //串赋值，从另一串sb复制而得
    String &operator += ( const String &sb );  //串连接，将串sb接到*this串后面
    char &operator [] ( int i );               //取串中第i个字符
    friend ostream &operator << (ostream &out,String &P); //输出字符串
    int Search(String Target, String pattern);
    void Calculate();
private:
    char *ch;           //串的存储数组
    int slen;           //串的字符个数(串长度)
    int *f;             //串的失效函数值
};
#endif /* str_h */

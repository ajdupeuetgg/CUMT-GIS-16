#ifndef DATALIST_H
#define DATALIST_H

#include <iostream>
#include <stdlib.h>
using namespace std;

template <class Type>
class dataList{
private:
    Type *Element;
    int ArraySize;
    void Swap (int m1, int m2);
    int MaxKey (int low, int high);
public:
    dataList(int size=10):ArraySize(size),
    Element(new Type[size]){}
    ~dataList () {delete []Element;}
    void Sort ();
    friend ostream& operator << (ostream&outStream, dataList<Type>& outList)
    {
        outStream << "数组内容: \n";
        for (int i = 0; i < outList.ArraySize; i++)
            outStream << outList.Element[i] << " ";
        outStream << endl;
        outStream << "数组当前大小: " << outList.ArraySize << endl;
        return outStream;
    }
    friend istream& operator >> (istream&inStream, dataList<Type>& inList){
        cout << "录入数组当前大小: ";
        inStream >> inList.ArraySize;
        cout << "录入数组元素值: \n";
        for (int i = 0; i < inList.ArraySize; i++)
        {
            cout << "元素" << i << ":";
            inStream >> inList.Element[i];
        }
        return inStream;
    }
};
#endif

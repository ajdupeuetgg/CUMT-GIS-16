#include <iostream>
#include "datalist.h"
#include "selecttm.h"
using namespace std;
const int SIZE=10;


int main()
{
    dataList<int>TestList(SIZE);
    cin>>TestList;
    cout<<TestList<<endl;
    TestList.Sort();
    cout<<TestList<<endl;
    return 0;
}
